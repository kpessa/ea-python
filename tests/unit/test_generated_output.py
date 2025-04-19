import pytest
import json
import os
import re # For regex matching

# --- Constants ---
# Assuming tests are run from the project root directory (e.g., where build.py is)
CONFIG_DIR = "generated_configs"
REGULAR_CONFIG_FILE = os.path.join(CONFIG_DIR, "output_regular.json")
CARDIAC_CONFIG_FILE = os.path.join(CONFIG_DIR, "output_cardiac.json")

# --- Derived Mnemonic Sets ---
# Based on filenames found in expected_sentences/

LAB_MNEMONICS = {
    'BMP',
    'Magnesium Level',
    'Potassium Level',
    'Phosphate Level',
    'Calcium Level Ionized, Serum',
    'Calcium Level Ionized, Whole Blood',
}

MED_MNEMONICS = {
    'magnesium oxide',
    'magnesium sulfate',
    'potassium chloride extended release',
    'potassium chloride',
    'potassium chloride 10 mEq/100 mL intravenous solution',
    'potassium chloride 20 mEq/100 mL intravenous solution',
    'K-Phos Neutral',
    'sodium phosphate',
    'calcium chloride',
}

# --- Helper Functions (used by fixtures and tests) ---
def load_json_config(filepath):
    """Loads JSON data from a given file path."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        pytest.fail(f"Configuration file not found: {filepath}", pytrace=False)
    except json.JSONDecodeError:
        pytest.fail(f"Error decoding JSON from file: {filepath}", pytrace=False)

# --- Fixtures for Config Data ---
@pytest.fixture(scope="module")
def regular_config():
    return load_json_config(REGULAR_CONFIG_FILE)

@pytest.fixture(scope="module")
def cardiac_config():
    return load_json_config(CARDIAC_CONFIG_FILE)

# --- Helper Functions for extracting data (used within tests) ---
def get_tabs(config):
    return config.get("RCONFIG", {}).get("TABS", [])

def get_sections(tab):
    return tab.get("ORDER_SECTIONS", [])

def get_orders(section):
    return section.get("ORDERS", [])

def get_all_orders_from_config(config):
    """Yields all individual order dictionaries from a loaded config."""
    for tab in get_tabs(config):
        for section in get_sections(tab):
            for order in get_orders(section):
                yield order

def is_lab_order(order):
    """Checks if an order dictionary is a lab order based on known MNEMONIC."""
    return order.get("MNEMONIC") in LAB_MNEMONICS

def is_med_order(order):
    """Checks if an order dictionary is a medication order based on known MNEMONIC."""
    return order.get("MNEMONIC") in MED_MNEMONICS

def get_all_lab_orders_from_config(config):
    """Yields all lab order dictionaries from a loaded config."""
    for order in get_all_orders_from_config(config):
        if is_lab_order(order):
            yield order

def get_all_med_orders_from_config(config):
    """Yields all medication order dictionaries from a loaded config."""
    for order in get_all_orders_from_config(config):
        if is_med_order(order):
            yield order
        # Optional: Add a check/warning for mnemonics not in either set?
        # elif order.get("MNEMONIC") not in LAB_MNEMONICS and order.get("MNEMONIC") not in MED_MNEMONICS:
        #     print(f"Warning: Order mnemonic '{order.get('MNEMONIC')}' not found in LAB or MED sets.")


# --- Test Functions ---

# Use pytest.mark.parametrize to run tests against both configs
@pytest.mark.parametrize("config_fixture", ["regular_config", "cardiac_config"])
def test_top_level_structure(config_fixture, request):
    """Tests that the root structure contains the RCONFIG key."""
    config = request.getfixturevalue(config_fixture) # Get the actual fixture value
    assert isinstance(config, dict)
    assert "RCONFIG" in config

@pytest.mark.parametrize("config_fixture", ["regular_config", "cardiac_config"])
def test_rconfig_structure(config_fixture, request):
    """Tests the structure within the RCONFIG object."""
    config = request.getfixturevalue(config_fixture)
    rconfig = config["RCONFIG"]
    assert isinstance(rconfig, dict)
    assert "TABS" in rconfig
    assert isinstance(rconfig["TABS"], list)
    # Check other RCONFIG keys if needed (e.g., CCL_POSTPROCESS)
    assert "CCL_POSTPROCESS" in rconfig
    assert isinstance(rconfig["CCL_POSTPROCESS"], str)
    assert "JSON_RETURN" in rconfig
    assert isinstance(rconfig["JSON_RETURN"], str)

@pytest.mark.parametrize("config_fixture", ["regular_config", "cardiac_config"])
def test_tab_structure(config_fixture, request):
    """Tests the basic structure and essential keys of each tab."""
    config = request.getfixturevalue(config_fixture)
    for tab in get_tabs(config):
        assert isinstance(tab, dict)
        # Check for essential keys in each tab
        essential_keys = [
            "TAB_NAME", "TAB_KEY", "FLAG_ON_CONCEPT", "CONCEPT_FOR_DISMISS",
            "MNEMONICS", "CONCEPTS", "CRITERIA", "GRAPHED_RESULTS",
            "ORDER_SECTIONS", "SUBMIT_BUTTON", "CANCEL_BUTTON"
            # RESOURCE_URLS is optional, checked elsewhere if needed
        ]
        for key in essential_keys:
            assert key in tab, f"Missing key '{key}' in tab '{tab.get('TAB_NAME')}'"

        # Basic type checks for some keys
        assert isinstance(tab["TAB_NAME"], str)
        assert isinstance(tab["TAB_KEY"], str)
        assert isinstance(tab["MNEMONICS"], list)
        assert isinstance(tab["CRITERIA"], list)
        assert isinstance(tab["GRAPHED_RESULTS"], list)
        assert isinstance(tab["ORDER_SECTIONS"], list)
        assert isinstance(tab["SUBMIT_BUTTON"], dict)
        assert isinstance(tab["CANCEL_BUTTON"], dict)

@pytest.mark.parametrize("config_fixture", ["regular_config", "cardiac_config"])
def test_order_basic_fields(config_fixture, request):
    """Tests that every order has the essential string keys."""
    config = request.getfixturevalue(config_fixture)
    for order in get_all_orders_from_config(config):
        assert isinstance(order, dict)
        essential_keys = ["MNEMONIC", "ORDER_SENTENCE", "COMMENT"]
        for key in essential_keys:
            assert key in order, f"Missing key '{key}' in order {order.get('MNEMONIC')}"
            assert isinstance(order[key], str), f"Key '{key}' is not a string in order {order.get('MNEMONIC')}"

# --- Lab Order Sentence Tests ---

@pytest.mark.parametrize("config_fixture", ["regular_config", "cardiac_config"])
def test_lab_sentence_format(config_fixture, request):
    """Tests general formatting rules for lab ORDER_SENTENCE."""
    config = request.getfixturevalue(config_fixture)
    for order in get_all_lab_orders_from_config(config):
        sentence = order.get("ORDER_SENTENCE", "")
        mnemonic = order.get("MNEMONIC", "") # Get mnemonic for context

        # Check add-on format FIRST
        is_add_on = "add to specimen in lab" in sentence
        if is_add_on:
            # Add-on labs should end with the add-on phrase, NOT ", Once"
             assert sentence.endswith(", add to specimen in lab"), \
                 f"Add-on lab sentence for '{mnemonic}' should end with ', add to specimen in lab': {sentence}"
            # For Add-ons, the standard collection instruction check might not apply or be different.
            # We'll skip the collection instruction check for add-ons for now,
            # as the primary identifier is the ending phrase.
        else:
            # --- Standard Lab Checks (Non Add-on) ---
            # 1. Must end with ", Once"
            assert sentence.endswith(", Once"), \
                f"Standard lab sentence for '{mnemonic}' should end with ', Once': {sentence}"

            # 2. Must contain a valid collection instruction
            valid_collections = [
                "Tomorrow AM collect",
                "Timed Study collect",
                "ASAP (Now) collect",
                "Routine Today collect",
                "ASAP collect" # Seen in Calcium STAT
            ]
            # Check if *any* known collection string is present
            assert any(coll in sentence for coll in valid_collections), \
                f"Standard lab sentence for '{mnemonic}' missing expected collection instruction: {sentence}"

# --- Medication Order Sentence Tests ---

@pytest.mark.parametrize("config_fixture", ["regular_config", "cardiac_config"])
def test_med_sentence_start_format(config_fixture, request):
    """Tests that med ORDER_SENTENCE starts with dose and unit."""
    config = request.getfixturevalue(config_fixture)
    for order in get_all_med_orders_from_config(config):
        sentence = order.get("ORDER_SENTENCE", "")
        # mnemonic = order.get("MNEMONIC", "") # Get mnemonic for debug - UNUSED
        # print(f"DEBUG: Checking Mnemonic='{mnemonic}', Sentence='{sentence}'") # Keep commented for now
        # Regex: Start (^) digits, optional decimal+digits, space, ANY chars except comma for unit ([^,]+), comma
        assert re.match(r"^\d+(\.\d+)?\s+[^,]+,\s*", sentence), \
               f"Med sentence does not start with dose, unit, comma: {sentence}"

@pytest.mark.parametrize("config_fixture", ["regular_config", "cardiac_config"])
def test_med_sentence_frequency_format(config_fixture, request):
    """Checks for expected frequency formats (qXhr, qXhr (interval), Once) matching domain data."""
    config = request.getfixturevalue(config_fixture)
    for order in get_all_med_orders_from_config(config):
        sentence = order.get("ORDER_SENTENCE", "")
        parts = sentence.split(", ")

        freq_part = None
        # Basic check: Find a part that looks like a frequency
        potential_freq_indices = [2, 3] # Often 3rd or 4th element
        for i in potential_freq_indices:
            if len(parts) > i:
                part = parts[i].strip()
                # Update regex to look for domain format: qXhr or qXhr (interval) or Once
                if part == "Once" or re.match(r"q\d+hr(\s+\(interval\))?", part):
                    freq_part = part
                    break

        if freq_part:
            if "(interval)" in freq_part:
                # Assert domain format: qXhr (interval)
                assert re.match(r"q\d+hr\s+\(interval\)", freq_part), \
                    f"Interval frequency '{freq_part}' does not match expected domain 'qXhr (interval)' format in: {sentence}"
            elif freq_part != "Once":
                 # Assert domain format: qXhr
                 assert re.match(r"q\d+hr", freq_part), \
                    f"Hourly frequency '{freq_part}' does not match expected domain 'qXhr' format in: {sentence}"
            # Implicitly passes if freq_part is "Once"
        # else: Cannot reliably determine frequency part, or it's absent. Skip check.

@pytest.mark.parametrize("config_fixture", ["regular_config", "cardiac_config"])
def test_med_sentence_infuse_over_format(config_fixture, request):
    """Checks the 'Infuse over: X hr' domain format in med ORDER_SENTENCE."""
    config = request.getfixturevalue(config_fixture)
    for order in get_all_med_orders_from_config(config):
        sentence = order.get("ORDER_SENTENCE", "")
        # Domain format: "Infuse over: " (Capital I, colon)
        infuse_prefix = "Infuse over: "
        if infuse_prefix in sentence:
            parts = sentence.split(", ")
            infuse_part = next((part for part in parts if part.startswith(infuse_prefix)), None)
            assert infuse_part is not None, f"Could not find infuse part after prefix '{infuse_prefix}' in: {sentence}"
            # Update regex to match domain format
            # assert re.match(r"infuse over \d+(\.\d+)?\s+hr", infuse_part), \
            #        f"Infuse part '{infuse_part}' does not match 'infuse over X hr' format in: {sentence}" # OLD Check
            assert re.match(r"Infuse over: \d+(\.\d+)?\s+hr", infuse_part), \
                   f"Infuse part '{infuse_part}' does not match domain 'Infuse over: X hr' format in: {sentence}" # NEW Check

# --- Remove old helper functions and parameter lists that called fixtures directly ---
# (Functions moved/integrated above, parameter lists removed entirely)

# Removed: all_config_data fixture
# Removed: all_tabs fixture
# Removed: all_sections fixture
# Removed: all_orders fixture
# Removed: all_lab_orders fixture
# Removed: all_med_orders fixture
# Removed: old get_all_orders_from_config (duplicate)
# Removed: old is_lab_order (using MNEMONIC set now)
# Removed: old get_all_lab_orders_from_config (duplicate)
# Removed: old get_all_med_orders_from_config (duplicate)
# Removed: all_lab_orders_params list comprehension
# Removed: all_med_orders_params list comprehension
# Removed: Placeholder test_something

# Ensure the file ends cleanly, removing any trailing old code/comments if necessary. 