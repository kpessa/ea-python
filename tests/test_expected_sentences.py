import pytest
import json
import os
import glob
import re
from functools import cache # lru_cache not needed now
from pathlib import Path
from thefuzz import process, fuzz
from collections import defaultdict
from typing import Dict, Set

# --- Define paths relative to this test file --- 
# Project root is one level up from the tests directory
PROJECT_ROOT = Path(__file__).parent.parent
GENERATED_CONFIG_DIR = PROJECT_ROOT / 'generated_configs'
EXPECTED_SENTENCES_DIR = PROJECT_ROOT / 'expected_sentences'
EXPECTED_EXTRACT_FILE = EXPECTED_SENTENCES_DIR / 'extract.csv'

# Removed imports from build.py
# try:
#     from build import GENERATED_CONFIG_DIR 
# except ImportError:
#    ...

# --- Constants ---
# EXPECTED_SENTENCES_DIR defined above
# EXPECTED_EXTRACT_FILE defined above
FUZZY_MATCH_THRESHOLD = 85

# --- Helper to get file list for parametrization ---
def get_generated_config_paths():
    """Returns a list of paths to generated JSON config files for parametrization."""
    # Ensure the directory constant is valid
    if not GENERATED_CONFIG_DIR.is_dir(): # Use Path object check
        pytest.fail(f"GENERATED_CONFIG_DIR is not defined or not a directory: {GENERATED_CONFIG_DIR}")
    json_files = glob.glob(str(GENERATED_CONFIG_DIR / '*.json')) # Use Path object for glob
    if not json_files:
        pytest.fail(f"No generated JSON config files found in {GENERATED_CONFIG_DIR}")
    return json_files

# --- Fixtures ---
# (No fixtures needed here anymore)

# --- Helper Functions ---

def sanitize_filename(mnemonic: str) -> str:
    """Replaces characters invalid in filenames (like /, ,)."""
    # Add other replacements if needed (e.g., :, ?, etc.)
    sanitized = mnemonic.replace('/', '#')
    sanitized = sanitized.replace(',', '') # Remove commas
    return sanitized

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
    
    # Sanitize the mnemonic for use in filename
    sanitized_mnemonic = sanitize_filename(mnemonic)
    
    expected_file_path = None # Initialize path variable
    
    if is_lab:
        # Use joinpath for robustness - This is the ONLY path for labs
        expected_file_path = expected_dir_path.joinpath('labs', f"{sanitized_mnemonic}.csv")
    elif electrolyte: # Only proceed for non-labs if electrolyte (tab key) is provided
        electrolyte_dir = electrolyte.lower()
        # Use joinpath for robustness
        expected_file_path = expected_dir_path.joinpath('meds', electrolyte_dir, f"{sanitized_mnemonic}.csv")
    # else: # If not a lab and no electrolyte provided, expected_file_path remains None

    # Check the determined path
    if expected_file_path and os.path.isfile(str(expected_file_path)):
        try:
            with open(expected_file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    sentence = line.strip()
                    if sentence:
                        expected_sentences.add(sentence)
        except Exception as e:
            print(f"Warning: Failed to read expected sentences from {expected_file_path}: {e}")
    elif expected_file_path: # Path was constructed but file not found
        # Print the path we tried to find
        print(f"DEBUG (test_expected_sentences): Expected file path check failed (os.path.isfile) for: {expected_file_path}") 
        pass 
    # else: # Path wasn't constructed (e.g., non-lab mnemonic with no electrolyte) - implicitly return empty set

    return expected_sentences

def get_protocol_from_filename(filepath):
    """Extracts the protocol name (e.g., Regular, Cardiac) from filename."""
    filename = os.path.basename(filepath)
    # Example: output_regular.json -> Regular
    if filename.startswith('output_') and filename.endswith('.json'):
        protocol_part = filename[len('output_'):-len('.json')]
        # Simple capitalization, might need adjustment if names differ
        return protocol_part.capitalize() 
    return None # Or raise error if format is unexpected

# --- Test Function ---

@pytest.mark.parametrize("config_file_path", get_generated_config_paths())
def test_expected_sentences_match_generated(config_file_path):
    """
    Verifies that order sentences in the generated JSON match EXACTLY those defined
    in the individual files within expected_sentences/.
    """
    # --- Clear cache before each test run ---
    load_expected_sentences.cache_clear()
    # --- End Clear Cache ---
    
    # Load JSON inside the test now
    try:
        with open(config_file_path, 'r', encoding='utf-8') as f:
            loaded_json_config = json.load(f)
    except Exception as e:
        pytest.fail(f"Failed to load or parse JSON from {config_file_path}: {e}")

    protocol = get_protocol_from_filename(config_file_path)
    assert protocol, f"Could not determine protocol from filename: {config_file_path}"

    errors = []
    processed_json_orders = set() 
    # No longer need unmatched_domain_sentences tracking based on extract.csv

    # Iterate through the generated JSON structure first
    try:
        tabs = loaded_json_config.get('RCONFIG', {}).get('TABS', [])
        for tab in tabs:
            tab_key = tab.get('TAB_KEY')
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

                    # --- Debug: Print mnemonic being loaded ---
                    print(f"DEBUG: Loading expected for Mnemonic='{json_mnemonic}', Tab='{tab_key}'")
                    # --- End Debug ---

                    # Load expected sentences from individual file for this mnemonic
                    expected_sentences = load_expected_sentences(json_mnemonic, tab_key)

                    if not expected_sentences:
                        # Mnemonic in JSON does not have a corresponding expected file or file is empty!
                        errors.append(
                            f"  - Unexpected/Missing File: Mnemonic '{json_mnemonic}' in Tab '{tab_key}'\n"
                            f"    JSON Sentence: {repr(json_sentence)}\n"
                            f"    (No corresponding file found or file empty in expected_sentences/)"
                        )
                        processed_json_orders.add(json_order_id)
                        continue

                    # --- Exact Comparison Logic ---
                    if json_sentence in expected_sentences:
                        # Exact match found - good!
                        processed_json_orders.add(json_order_id)
                    else:
                        # Exact match NOT found - this is an error
                        # Format expected sentences for error message
                        expected_list_str = "\n      Expected Sentences in File:\n"
                        preview_count = 3
                        expected_list_str += "\n".join([f"        - {repr(s)}" for s in list(expected_sentences)[:preview_count]])
                        if len(expected_sentences) > preview_count:
                            expected_list_str += f"\n        - ... ({len(expected_sentences) - preview_count} more)"
                            
                        errors.append(
                            f"  - Sentence Mismatch: Mnemonic '{json_mnemonic}' in Tab '{tab_key}'\n" 
                            f"    JSON    : {repr(json_sentence)}\n" 
                            f"    Expected: Not found exactly in its expected file.{expected_list_str}"
                        )
                        processed_json_orders.add(json_order_id)
                            
    except Exception as e:
        pytest.fail(f"Error processing JSON structure in {config_file_path}: {e}")

    # --- Final Assertion --- 
    if errors:
        final_error_message = f"\nFound Discrepancies (JSON vs Expected Files) in {os.path.basename(config_file_path)}:\n"
        final_error_message += "\n".join(errors)
        assert not final_error_message, final_error_message 