import pytest
import json
import os
import glob
import re
import csv # Import csv module
from functools import cache
from pathlib import Path
from thefuzz import process, fuzz # Keep for potential future fuzzy matching?
from collections import defaultdict
from typing import Dict, Set, Tuple

# --- Define paths relative to this test file ---
PROJECT_ROOT = Path(__file__).parent.parent
GENERATED_CONFIG_DIR = PROJECT_ROOT / 'generated_configs'
EXPECTED_SENTENCES_DIR = PROJECT_ROOT / 'expected_sentences'
EXPECTED_EXTRACT_FILE = EXPECTED_SENTENCES_DIR / 'extract.csv' # Path to the single CSV

# --- Constants ---
# FUZZY_MATCH_THRESHOLD = 85 # Keep commented out, using exact match

# --- Helper to get file list for parametrization ---
def get_generated_config_paths():
    """Returns a list of paths to generated JSON config files for parametrization."""
    if not GENERATED_CONFIG_DIR.is_dir():
        pytest.fail(f"GENERATED_CONFIG_DIR is not defined or not a directory: {GENERATED_CONFIG_DIR}")
    json_files = glob.glob(str(GENERATED_CONFIG_DIR / '*.json'))
    if not json_files:
        pytest.fail(f"No generated JSON config files found in {GENERATED_CONFIG_DIR}")
    return json_files

# --- Fixtures --- (None needed)

# --- Helper Functions ---

# Removed sanitize_filename as it's no longer needed

@cache
def load_all_expected_from_csv() -> Dict[str, Set[str]]:
    """Loads all expected sentences from extract.csv into a dictionary.

    Reads the CSV file and groups sentences by MNEMONIC.
    Returns a dictionary mapping mnemonic strings to sets of sentence strings.
    Caches the result for performance.
    """
    expected_data: Dict[str, Set[str]] = defaultdict(set)
    if not EXPECTED_EXTRACT_FILE.is_file():
        pytest.fail(f"Expected sentences file not found: {EXPECTED_EXTRACT_FILE}")

    try:
        with open(EXPECTED_EXTRACT_FILE, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter='\t') # Use DictReader assuming header row, specify tab delimiter
            # Verify expected column names (adjust if different)
            if reader.fieldnames is None: # Check if fieldnames were read
                 pytest.fail(f"Could not read headers from CSV {EXPECTED_EXTRACT_FILE}")
                 
            required_columns = ['MNEMONIC', 'ORDER_SENTENCE_DISPLAY_LINE']
            if not all(col in reader.fieldnames for col in required_columns):
                missing = [col for col in required_columns if col not in reader.fieldnames]
                pytest.fail(
                    f"CSV {EXPECTED_EXTRACT_FILE.name} missing required columns: {missing}"
                )

            for row in reader:
                mnemonic = row.get('MNEMONIC')
                sentence = row.get('ORDER_SENTENCE_DISPLAY_LINE')
                # Add non-empty sentences to the set for the mnemonic
                if mnemonic and sentence:
                    expected_data[mnemonic].add(sentence.strip())
    except Exception as e:
        pytest.fail(f"Failed to read or parse {EXPECTED_EXTRACT_FILE}: {e}")

    if not expected_data:
        pytest.fail(f"No data loaded from {EXPECTED_EXTRACT_FILE}")

    return dict(expected_data) # Return a regular dict from defaultdict

# Simple wrapper to get sentences for a specific mnemonic from the cached dict
def get_expected_sentences_for_mnemonic(mnemonic: str) -> Set[str]:
    """Retrieves the set of expected sentences for a given mnemonic from the cached CSV data."""
    all_expected = load_all_expected_from_csv()
    return all_expected.get(mnemonic, set()) # Return empty set if mnemonic not found


def get_protocol_from_filename(filepath):
    """Extracts the protocol name (e.g., Regular, Cardiac) from filename."""
    filename = os.path.basename(filepath)
    if filename.startswith('output_') and filename.endswith('.json'):
        protocol_part = filename[len('output_'):-len('.json')]
        return protocol_part.capitalize()
    return None

# --- Test Function --- (Will modify this next)

@pytest.mark.parametrize("config_file_path", get_generated_config_paths())
def test_expected_sentences_match_generated(config_file_path):
    """
    Verifies that order sentences in the generated JSON match EXACTLY those defined
    in the expected_sentences/extract.csv file.
    """
    # --- Clear cache (optional, but good practice if data might change between runs) ---
    load_all_expected_from_csv.cache_clear()
    # --- End Clear Cache ---

    # Load JSON inside the test
    try:
        with open(config_file_path, 'r', encoding='utf-8') as f:
            loaded_json_config = json.load(f)
    except Exception as e:
        pytest.fail(f"Failed to load or parse JSON from {config_file_path}: {e}")

    protocol = get_protocol_from_filename(config_file_path)
    assert protocol, f"Could not determine protocol from filename: {config_file_path}"

    errors = []
    processed_json_orders = set()

    # Iterate through the generated JSON structure
    try:
        tabs = loaded_json_config.get('RCONFIG', {}).get('TABS', [])
        for tab in tabs:
            tab_key = tab.get('TAB_KEY') # Still useful for context in errors
            if not tab_key:
                continue

            order_sections = tab.get('ORDER_SECTIONS', [])
            for section_index, section in enumerate(order_sections):
                orders_in_section = section.get('ORDERS', [])
                for order_index, order in enumerate(orders_in_section):
                    json_mnemonic = order.get('MNEMONIC')
                    json_sentence = order.get('ORDER_SENTENCE')
                    json_order_id = f"{tab_key}-S{section_index}-O{order_index}-{json_mnemonic}"

                    if not json_mnemonic or not json_sentence:
                        continue
                    if json_order_id in processed_json_orders:
                        continue

                    # --- Debug: Print mnemonic being checked ---
                    # print(f"DEBUG: Checking Mnemonic='{json_mnemonic}', Tab='{tab_key}'")
                    # --- End Debug ---

                    # Get expected sentences for this mnemonic from the single CSV
                    expected_sentences = get_expected_sentences_for_mnemonic(json_mnemonic)

                    if not expected_sentences:
                        # Mnemonic in JSON does not exist in extract.csv or has no sentences!
                        errors.append(
                            f"  - Unexpected/Missing Entry: Mnemonic '{json_mnemonic}' in Tab '{tab_key}'\
                             not found or has no sentences in {EXPECTED_EXTRACT_FILE.name}\n"
                            f"    JSON Sentence: {repr(json_sentence)}"
                        )
                        processed_json_orders.add(json_order_id)
                        continue

                    # --- Exact Comparison Logic --- (Remains the same)
                    if json_sentence in expected_sentences:
                        # Exact match found - good!
                        processed_json_orders.add(json_order_id)
                    else:
                        # Exact match NOT found - this is an error
                        # Format expected sentences for error message
                        expected_list_str = f"\n      Expected Sentences for Mnemonic '{json_mnemonic}' in {EXPECTED_EXTRACT_FILE.name}:\n"
                        preview_count = 5 # Show a few more maybe
                        expected_list_str += "\n".join([f"        - {repr(s)}" for s in list(expected_sentences)[:preview_count]])
                        if len(expected_sentences) > preview_count:
                            expected_list_str += f"\n        - ... ({len(expected_sentences) - preview_count} more)"

                        errors.append(
                            f"  - Sentence Mismatch: Mnemonic '{json_mnemonic}' in Tab '{tab_key}'\n"
                            f"    JSON    : {repr(json_sentence)}\n"
                            f"    Expected: Not found exactly in the set of sentences for this mnemonic.{expected_list_str}"
                        )
                        processed_json_orders.add(json_order_id)

    except Exception as e:
        pytest.fail(f"Error processing JSON structure in {config_file_path}: {e}")

    # --- Final Assertion --- (Remains the same, message updated slightly)
    if errors:
        final_error_message = f"\nFound Discrepancies (JSON vs {EXPECTED_EXTRACT_FILE.name}) in {os.path.basename(config_file_path)}:\n"
        final_error_message += "\n".join(errors)
        assert not final_error_message, final_error_message 