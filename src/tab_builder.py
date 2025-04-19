from typing import List, Dict

from .types import Mnemonic, GraphedResult
from . import components as Components
from .utils import naming as Naming


def _create_mnemonic(tab_name: str) -> Mnemonic:
    """Creates a default mnemonic dictionary.

    >>> _create_mnemonic('Potassium')
    {'MNEMONIC': 'Potassium Replacement'}
    >>> _create_mnemonic('Ionized Calcium')
    {'MNEMONIC': 'Ionized Calcium Replacement'}
    """
    return {'MNEMONIC': f'{tab_name} Replacement'}

def _create_graphed_results(tab_name: str) -> List[GraphedResult]:
    """Creates the graphed results structure for a tab.

    >>> _create_graphed_results('Magnesium')
    [{'LABEL': 'Magnesium Level', 'EVENT_SET': 'TPN Magnesium Serum Magnesium', 'LOOKBACK': '144,H', 'MAX_RESULT_COUNT': '6', 'RESULTS_VIEW': {'LOOKBEHIND_LABEL': ''}}]
    >>> _create_graphed_results('Phosphorus') # Note: Special case for event set
    [{'LABEL': 'Phosphorus Level', 'EVENT_SET': 'TPN Phosphate Serum Phosphate', 'LOOKBACK': '144,H', 'MAX_RESULT_COUNT': '6', 'RESULTS_VIEW': {'LOOKBEHIND_LABEL': ''}}]
    """
    # concept_base = Naming.get_concept_name(tab_name) # Unused variable
    event_set_electrolyte = tab_name
    if tab_name == 'Phosphorus':
        event_set_electrolyte = 'Phosphate'
    
    return [
        {
            'LABEL': f'{tab_name} Level',
            'EVENT_SET': f'TPN {event_set_electrolyte} Serum {event_set_electrolyte}',
            'LOOKBACK': '144,H',
            'MAX_RESULT_COUNT': '6',
            'RESULTS_VIEW': {
                'LOOKBEHIND_LABEL': ''
            }
        }
    ]

# Using partial type hint as ORDER_SECTIONS is added later
def create_tab(tab_name: str) -> Dict:
    """Creates the base structure for a Tab, excluding ORDER_SECTIONS."""
    concept = Naming.get_concept_name(tab_name)
    # Use common components data directly
    common_data = Components.common_components_data
    
    # Construct the dictionary directly, easier than merging partial TypedDicts
    tab_base = {
        'TAB_NAME': tab_name,
        'TAB_KEY': tab_name.upper().replace(' ', ''),
        'FLAG_ON_CONCEPT': f'[%{{EALAB{concept}TODO}}.COUNT > 0%]', 
        'CONCEPT_FOR_DISMISS': f'EALAB{concept}TODO',
        'MNEMONICS': [_create_mnemonic(tab_name)],
        'CONCEPTS': [], # Usually empty
        'CRITERIA': common_data['commonCriteria'],
        'GRAPHED_RESULTS': _create_graphed_results(tab_name),
        'RESOURCE_URLS': common_data['commonResourceUrls'], # Default common resources
        'SUBMIT_BUTTON': common_data['commonSubmitButton'],
        'CANCEL_BUTTON': common_data['commonCancelButton'],
    }
    return tab_base 