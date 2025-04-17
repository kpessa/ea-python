import pytest
import json
import os
import glob
from functools import lru_cache, cache
import re # Add import for regex
from pathlib import Path # Added Path
from thefuzz import process, fuzz # Added thefuzz

# Assuming parse_dcw.py is now in python/utils
# Need to ensure python utils path is discoverable if running pytest directly
import sys
TEST_DIR = Path(__file__).parent
PROJECT_ROOT = TEST_DIR.parent
PYTHON_DIR = PROJECT_ROOT / 'python'
if str(PYTHON_DIR) not in sys.path:
    sys.path.insert(1, str(PYTHON_DIR))
try:
    from utils.parse_dcw import parse_dcw_file # Relative import within python package
except ImportError as e:
    print(f"ERROR importing parse_dcw: {e}")
    # Fallback or error handling if needed
    sys.exit(1)

# --- Define paths relative to this test file ---
# Project root is one level up from the tests directory
# PROJECT_ROOT defined above
GENERATED_CONFIG_DIR = PROJECT_ROOT / 'generated_configs'
EXPECTED_SENTENCES_DIR = PROJECT_ROOT / 'expected_sentences' # For domain comparison
DCW_ORDER_SENTENCES_FILE = PROJECT_ROOT / 'dcw_order_sentences' / 'dcw.txt'

# --- Constants ---
EXPECTED_SENTENCES_DIR = os.path.join(Path(GENERATED_CONFIG_DIR).parent, 'expected_sentences')
FUZZY_MATCH_THRESHOLD = 85 # Score out of 100 - for comparing JSON vs Domain

# --- Helper to get file list for parametrization ---
def get_generated_config_paths():
    """Returns a list of paths to generated JSON config files for parametrization."""
    if not GENERATED_CONFIG_DIR.is_dir():
        pytest.fail(f"GENERATED_CONFIG_DIR is not defined or not a directory: {GENERATED_CONFIG_DIR}")
    json_files = glob.glob(str(GENERATED_CONFIG_DIR / '*.json'))
    if not json_files:
        pytest.fail(f"No generated JSON config files found in {GENERATED_CONFIG_DIR}")
    return json_files


# --- Fixtures ---

@pytest.fixture(scope="session")
@lru_cache(maxsize=None)
def dcw_data():
    """Parses and caches the DCW order sentence data."""
    if not DCW_ORDER_SENTENCES_FILE.is_file():
         pytest.fail(f"DCW_ORDER_SENTENCES_FILE is not defined or not a file: {DCW_ORDER_SENTENCES_FILE}")
    data = parse_dcw_file(str(DCW_ORDER_SENTENCES_FILE)) # Pass path as string
    assert data, f"Failed to parse DCW data from {DCW_ORDER_SENTENCES_FILE}"
    return data


# --- Helper Functions ---

def get_protocol_from_filename(filepath):
    """Extracts the protocol name (e.g., Regular, Cardiac) from filename."""
    filename = os.path.basename(filepath)
    if filename.startswith('output_') and filename.endswith('.json'):
        protocol_part = filename[len('output_'):-len('.json')]
        return protocol_part.capitalize()
    return None

def ranges_match(dcw_range_str: str, json_range_group: dict) -> bool:
    """Checks if the DCW lab range string matches the JSON range group dict.
    Parses DCW string and compares with JSON keys 'LAB_VALUE_LOW'/'HIGH'.
    """
    if not dcw_range_str or not json_range_group:
        return False
    dcw_cleaned = dcw_range_str.lower().replace("current serum level", "").replace("ical", "").strip()
    json_low = json_range_group.get('LAB_VALUE_LOW')
    json_high = json_range_group.get('LAB_VALUE_HIGH')
    print(f"\nDEBUG ranges_match: Comparing DCW='{dcw_range_str}' with JSON={json_range_group}")
    try:
        json_low_float = float(json_low) if json_low is not None else None
        json_high_float = float(json_high) if json_high is not None else None
    except (ValueError, TypeError):
        print(f"DEBUG ranges_match: Invalid JSON range values: low={json_low}, high={json_high}")
        return False
    dcw_low_float, dcw_high_float, match_found = None, None, False
    match = re.fullmatch(r"\s*([\d.]+)\s*-\s*([\d.]+)\s*", dcw_cleaned)
    if match:
        try:
            dcw_low_float = float(match.group(1))
            dcw_high_float = float(match.group(2))
            match_found = True
        except ValueError: pass
    if not match_found:
        match = re.fullmatch(r"\s*<\s*([\d.]+)\s*", dcw_cleaned)
        if match:
            try:
                dcw_high_float = float(match.group(1))
                match_found = True
            except ValueError: pass
    if not match_found:
        print(f"DEBUG ranges_match: Failed to parse DCW range: '{dcw_cleaned}'")
        return False
    print(f"DEBUG ranges_match: Parsed DCW floats: low={dcw_low_float}, high={dcw_high_float}")
    print(f"DEBUG ranges_match: JSON floats      : low={json_low_float}, high={json_high_float}")
    TOLERANCE = 1e-9
    low_match = (dcw_low_float is None and json_low_float is None) or \
                (dcw_low_float is not None and json_low_float is not None and abs(dcw_low_float - json_low_float) < TOLERANCE)
    high_match = (dcw_high_float is None and json_high_float is None) or \
                 (dcw_high_float is not None and json_high_float is not None and abs(dcw_high_float - json_high_float) < TOLERANCE)
    result = low_match and high_match
    print(f"DEBUG ranges_match: Comparison result = {result}")
    return result

# --- Helper Function from test_expected_sentences.py ---

@cache # Cache results for performance
def load_expected_sentences(mnemonic: str, electrolyte: str | None = None) -> set[str]:
    """Loads expected sentences from the corresponding CSV file in expected_sentences/.
    
    Determines path based on mnemonic (meds vs labs).
    Returns a set of non-empty sentences.
    """
    # Ensure EXPECTED_SENTENCES_DIR is treated as a Path object
    expected_dir_path = Path(EXPECTED_SENTENCES_DIR) 
    
    expected_sentences = set()
    # Basic check for lab names
    is_lab = "level" in mnemonic.lower() or mnemonic.lower() == "bmp"
    
    if is_lab:
        # Use joinpath for robustness
        expected_file_path = expected_dir_path.joinpath('labs', f"{mnemonic}.csv")
    else:
        if not electrolyte:
            return set()
        electrolyte_dir = electrolyte.lower()
        # Use joinpath for robustness
        expected_file_path = expected_dir_path.joinpath('meds', electrolyte_dir, f"{mnemonic}.csv")

    if expected_file_path.is_file():
        try:
            with open(expected_file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    sentence = line.strip()
                    if sentence:
                        expected_sentences.add(sentence)
        except Exception as e:
            print(f"Warning: Failed to read expected sentences from {expected_file_path}: {e}")
    # else: # Don't warn here if file not found, expected set will be empty
        # print(f"Warning: Expected sentences file not found: {expected_file_path}")
        pass 

    return expected_sentences

# --- Test Function ---

@pytest.mark.parametrize("config_file_path", get_generated_config_paths())
def test_dcw_sentences_match_generated(config_file_path, dcw_data):
    """
    Compares sentences from DCW against generated JSON using fuzzy matching.
    Generates a report showing the comparison and score for each DCW entry.
    """
    try:
        with open(config_file_path, 'r', encoding='utf-8') as f:
            loaded_json_config = json.load(f)
    except Exception as e:
        pytest.fail(f"Failed to load or parse JSON from {config_file_path}: {e}")

    protocol = get_protocol_from_filename(config_file_path)
    assert protocol, f"Could not determine protocol from filename: {config_file_path}"

    protocol_dcw_entries = [e for e in dcw_data if e.get('Protocol') == protocol]
    if not protocol_dcw_entries:
        print(f"Warning: No DCW entries found for protocol: {protocol}. Skipping verification.")
        return

    comparison_report_lines = []
    processing_errors = []

    for index, dcw_entry in enumerate(protocol_dcw_entries):
        dcw_electrolyte = dcw_entry.get('Electrolyte')
        dcw_mnemonic = dcw_entry.get('Mnemonic')
        dcw_range = dcw_entry.get('Lab Value Range') # Keep for context
        dcw_sentence = dcw_entry.get('Order_Sentence')

        if not all([protocol, dcw_electrolyte, dcw_mnemonic, dcw_sentence]):
            continue

        # --- Find JSON Counterpart (by mnemonic within the correct tab) ---
        json_sentence_found = None
        try:
            tabs = loaded_json_config.get('RCONFIG', {}).get('TABS', [])
            target_tab = next((
                t for t in tabs 
                if t.get('TAB_KEY') and dcw_electrolyte and t.get('TAB_KEY').upper() == dcw_electrolyte.upper()
            ), None)

            if target_tab:
                order_sections = target_tab.get('ORDER_SECTIONS', [])
                for section in order_sections:
                    orders_in_section = section.get('ORDERS', [])
                    for order in orders_in_section:
                        if order.get('MNEMONIC') == dcw_mnemonic:
                            json_sentence_found = order.get('ORDER_SENTENCE')
                            if json_sentence_found: # Found the first match
                                break
                    if json_sentence_found:
                        break
                
        except Exception as e:
            processing_errors.append(f"Error finding JSON counterpart for DCW entry {index}: {e}")
            continue 

        # --- Fuzzy Compare DCW vs JSON --- 
        comparison_score = 0
        if json_sentence_found:
            comparison_score = fuzz.token_sort_ratio(dcw_sentence, json_sentence_found)
        # else: json_sentence_found remains None

        # --- Compile Report Line --- 
        report_line = f'''
--- DCW Entry #{index} (Mnem: '{dcw_mnemonic}', Range: '{dcw_range}') ---
  DCW Spec : {repr(dcw_sentence)}
  JSON Gen : {repr(json_sentence_found) if json_sentence_found else '*** NOT FOUND in JSON Tab ***'}
  (Score DCW vs JSON: {comparison_score}%)'''
        comparison_report_lines.append(report_line)

    # --- Final Assertion --- 
    final_output_message = ""
    if comparison_report_lines:
        final_output_message += f"\nDCW vs JSON Sentence Comparison Report for {os.path.basename(config_file_path)}:\n"
        final_output_message += "\n".join(comparison_report_lines)
    if processing_errors:
         final_output_message += f"\n\nErrors encountered during processing for {os.path.basename(config_file_path)}:\n"
         final_output_message += "\n".join(processing_errors)

    # Fail if there's anything in the report to ensure it's always printed
    assert not final_output_message, final_output_message 