import json
import os
import pytest
from typing import Any, List

# --- Constants ---
CONFIG_DIR = 'generated_configs'
TEMPLATE_FILE = 'config-template.json'
GENERATED_FILES = ['output_regular.json', 'output_cardiac.json']

# --- Recursive Helper Function ---

def _assert_dict_key_order(template: Any, actual: Any, path: str):
    """Recursively asserts that dictionary key order matches the template."""
    if isinstance(template, dict) and isinstance(actual, dict):
        template_keys = list(template.keys())
        actual_keys = list(actual.keys())
        assert template_keys == actual_keys, \
            f"Dict key order mismatch at path '{path}'\nTemplate: {template_keys}\nActual:   {actual_keys}"
        
        # Recursively check values for nested dicts/lists
        for key in template_keys:
            # Check if key exists in actual; should be true if keys matched above, but good practice
            if key in actual:
                 _assert_dict_key_order(template[key], actual[key], path=f'{path}.{key}' if path else key)

    elif isinstance(template, list) and isinstance(actual, list):
        # Only check list items if template list has items (avoids index errors)
        # We are not strictly comparing list contents, only recursing into dicts within them
        if template:
            # Check items up to the length of the *shorter* list to avoid index errors
            # Or assert len(template) == len(actual) if list lengths must match
            min_len = min(len(template), len(actual))
            for i in range(min_len):
                 _assert_dict_key_order(template[i], actual[i], path=f'{path}[{i}]')
    
    # Ignore other types (scalars, etc.) for key order comparison
    

# --- Pytest Fixtures ---

@pytest.fixture(scope='session') # Load template only once per session
def template_config() -> Any:
    """Loads the template JSON data."""
    if not os.path.exists(TEMPLATE_FILE):
        pytest.fail(f"Template file not found: {TEMPLATE_FILE}")
    try:
        with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        pytest.fail(f"Failed to load or parse template file {TEMPLATE_FILE}: {e}")

# Parametrize the generated config loading
@pytest.fixture(params=GENERATED_FILES, scope='session')
def generated_config_data(request) -> dict:
    """Loads a generated JSON config file specified by pytest parameters."""
    filename = request.param
    filepath = os.path.join(CONFIG_DIR, filename)
    if not os.path.exists(filepath):
         pytest.fail(f"Generated config file not found: {filepath}")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return {'filename': filename, 'data': data}
    except Exception as e:
        pytest.fail(f"Failed to load or parse generated file {filepath}: {e}")

# --- Test Function ---

def test_generated_config_key_order(template_config, generated_config_data):
    """Tests if the key order in a generated config matches the template recursively."""
    print(f"\nTesting key order for: {generated_config_data['filename']}")
    _assert_dict_key_order(template_config, generated_config_data['data'], path='root') 