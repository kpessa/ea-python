import json
import os
import glob
import pytest
from typing import List, Dict, Set, Any
from collections import defaultdict
from pathlib import Path

# --- Define paths relative to this test file --- 
TEST_FILE_PATH = Path(__file__).resolve()
PROJECT_ROOT = TEST_FILE_PATH.parents[2]  # Go up two levels from tests/integration to project root

GENERATED_CONFIG_DIR = PROJECT_ROOT / 'generated_configs'
EXPECTED_SENTENCES_DIR = PROJECT_ROOT / 'tests' / 'fixtures' / 'expected_sentences'
EXPECTED_EXTRACT_FILE = EXPECTED_SENTENCES_DIR / 'extract.csv'

# --- Debug path definitions ---
print(f"DEBUG (test_config_sentences): Using PROJECT_ROOT = {PROJECT_ROOT}")
print(f"DEBUG (test_config_sentences): EXPECTED_EXTRACT_FILE = {EXPECTED_EXTRACT_FILE}")
print(f"DEBUG (test_config_sentences): EXPECTED_EXTRACT_FILE exists = {EXPECTED_EXTRACT_FILE.is_file()}")
# --- End Debug --- 

# --- Helper Functions ---

def sanitize_filename(mnemonic: str) -> str:
    """Replaces characters invalid in filenames."""
    return mnemonic.replace('/', '#')

def desanitize_filename(filename: str) -> str:
    """Reverses filename sanitization."""
    base = os.path.splitext(filename)[0]
    return base.replace('#', '/')

def find_orders(data: Any) -> List[Dict[str, Any]]:
    """Recursively find all order dictionaries (labs or meds) within the config structure."""
    found_orders = []
    if isinstance(data, dict):
        if 'MNEMONIC' in data and 'ORDER_SENTENCE' in data:
            found_orders.append(data)
        for value in data.values():
            found_orders.extend(find_orders(value))
    elif isinstance(data, list):
        for item in data:
            found_orders.extend(find_orders(item))
    return found_orders

# --- Helper to load domain sentences --- 
# Using the same robust parser as test_expected_sentences
# Note: No @cache here as pytest fixtures handle caching scope
def load_domain_sentences_from_extract(filepath: Path) -> Dict[str, Set[str]]:
    """Parses the domain extract CSV (tab-separated) into a dictionary."""
    domain_sentences = defaultdict(set)
    if not filepath.is_file():
        print(f"Error: Domain extract file not found: {filepath}")
        # Fail immediately if the source of truth is missing
        pytest.fail(f"Domain extract file not found: {filepath}", pytrace=False)
        return domain_sentences # Should not be reached

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            is_header = True
            for line_num, line in enumerate(f):
                if is_header:
                    is_header = False
                    continue
                line = line.strip()
                if not line:
                    continue
                parts = line.split('\t', 1) 
                if len(parts) == 2:
                    mnemonic, sentence = parts[0].strip(), parts[1].strip()
                    if mnemonic and sentence:
                        domain_sentences[mnemonic].add(sentence)
    except Exception as e:
        pytest.fail(f"Error reading or parsing domain extract file {filepath}: {e}", pytrace=False)
        
    print(f"(test_config_sentences) Loaded domain sentences for {len(domain_sentences)} mnemonics from {filepath}")
    return domain_sentences

# --- Fixtures ---

@pytest.fixture(scope="session")
def generated_config_files():
    """Returns a list of paths to the generated JSON config files."""
    json_files = glob.glob(str(GENERATED_CONFIG_DIR / '*.json'))
    if not json_files:
        pytest.fail(f"No generated JSON config files found in {GENERATED_CONFIG_DIR}", pytrace=False)
    return json_files

@pytest.fixture(scope="session")
def expected_sentences():
    """Loads the expected sentences from the extract.csv file."""
    return load_domain_sentences_from_extract(EXPECTED_EXTRACT_FILE)

@pytest.fixture(scope="session")
def actual_orders_by_mnemonic(generated_config_files):
    """Extracts all unique generated {mnemonic: {sentence}} pairs from JSON files."""
    all_orders = defaultdict(set)
    for file_path in generated_config_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                tabs = data.get('RCONFIG', {}).get('TABS', [])
                for tab in tabs:
                    sections = tab.get('ORDER_SECTIONS', [])
                    for section in sections:
                        orders = section.get('ORDERS', [])
                        for order in orders:
                            mnemonic = order.get('MNEMONIC')
                            sentence = order.get('ORDER_SENTENCE')
                            if mnemonic and sentence:
                                all_orders[mnemonic].add(sentence)
        except Exception as e:
            pytest.fail(f"Failed to load/parse {file_path}: {e}", pytrace=False)
    return all_orders

# --- Test Functions ---

def test_all_expected_mnemonics_found(expected_sentences, actual_orders_by_mnemonic):
    """Check if all mnemonics defined in the domain extract are found in generated JSON."""
    missing_mnemonics = expected_sentences.keys() - actual_orders_by_mnemonic.keys()
    assert not missing_mnemonics, \
        f"Mnemonics defined in {EXPECTED_EXTRACT_FILE} but not found in any generated JSON: {sorted(list(missing_mnemonics))}"

def test_no_unexpected_mnemonics_without_expectations(expected_sentences, actual_orders_by_mnemonic):
    """Check if generated JSON contains mnemonics not present in the domain extract."""
    unexpected_mnemonics = actual_orders_by_mnemonic.keys() - expected_sentences.keys()
    # Filter out any mnemonics that might be intentionally generated but not have specific sentence expectations
    # (Requires a list of such allowed mnemonics if applicable)
    truly_unexpected = {m for m in unexpected_mnemonics if m} # Basic check for non-empty
    assert not truly_unexpected, \
        f"Mnemonics found in generated JSON but NOT defined in {EXPECTED_EXTRACT_FILE}: {sorted(list(truly_unexpected))}"

def test_sentence_verification(expected_sentences, actual_orders_by_mnemonic):
    """Verify that generated sentences for each mnemonic exist in the expected extract.csv pool."""
    mnemonics_to_test = actual_orders_by_mnemonic.keys() # Test all generated mnemonics
    
    failures = [] # Store sentence mismatch errors

    for mnemonic in mnemonics_to_test:
        expected_set = expected_sentences.get(mnemonic, set()) # Sentences for this mnemonic in extract.csv
        found_set = actual_orders_by_mnemonic.get(mnemonic, set()) # Sentences generated in JSON

        # missing_expected = expected_set - found_set # Domain sentences not generated - IGNORE THIS CASE
        extra_generated = found_set - expected_set  # Generated sentences not in domain extract

        # Report generated sentences not matching the domain expectation for this mnemonic
        if extra_generated:
            error_detail = [f"Sentences generated for MNEMONIC '{mnemonic}' that DO NOT match any entry in {EXPECTED_EXTRACT_FILE}:"]
            for sentence in sorted(list(extra_generated)):
                error_detail.append(f"    - {repr(sentence)}") # Use repr to show quotes clearly
            failures.append("\n".join(error_detail))

        # # Report domain sentences that were expected but not generated for this mnemonic - REMOVED
        # if missing_expected:
        #     error_detail = [f"Sentences defined for MNEMONIC '{mnemonic}' in {EXPECTED_EXTRACT_FILE} but NOT generated:"]
        #     for sentence in sorted(list(missing_expected)):
        #         error_detail.append(f"    - {sentence}")
        #     failures.append("\n".join(error_detail))
            
    assert not failures, "\n\n" + "\n\n".join(failures) 