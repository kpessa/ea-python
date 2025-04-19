import importlib
import copy # For deep copying base tab structures
from typing import List, Optional, Dict, cast

from .types import (
    ProtocolData, TabConfig, RConfig, FullConfig, ResourceUrl, GenerationContext, Protocol
)
from . import section_builder as Sections
from . import tab_builder as Tabs
from .protocols import PROTOCOLS

# --- Protocol Specific Overrides ---

_cardiac_resource_urls: List[ResourceUrl] = [
    {
        'LABEL': 'Cardiac Electrolyte Replacement Guide',
        'URL': 'https://baycare1.sharepoint.com/sites/NUR/Shared%20Documents/Cardiac%20Electrolyte%20Replacement%20Guide.pdf',
    },
]
_cardiac_mnemonic_suffix = ' Replacement CARD'

# --- Helper Function to Get Protocol Data ---

def _get_protocol_data(protocol: Protocol, electrolyte: str) -> Optional[ProtocolData]:
    """Gets protocol data from the PROTOCOLS dictionary."""
    try:
        return cast(ProtocolData, PROTOCOLS[protocol][electrolyte])
    except KeyError:
        # This is expected for combinations like REGULAR/Calcium
        return None
    except Exception as e:
        print(f"Error getting protocol data for {protocol}/{electrolyte}: {e}")
        return None

# --- Main Configuration Generation Logic ---

def generate_config(context: GenerationContext) -> FullConfig:
    """Generates the full RCONFIG structure for a given protocol."""
    protocol = context['protocol']

    # Protocol specific overrides
    resource_urls_override = _cardiac_resource_urls if protocol == 'CARDIAC' else None
    mnemonic_suffix_override = _cardiac_mnemonic_suffix if protocol == 'CARDIAC' else ''

    # Function to build ORDER_SECTIONS for a specific electrolyte
    def build_order_sections(protocol_data: Optional[ProtocolData]) -> List[Dict]: # Return list of dicts for JSON
        if not protocol_data:
            return []
        grouped_sections = Sections.create_grouped_order_sections(protocol_data['sectionGroups'], context)
        initial_lab_sections = Sections.create_initial_lab_sections(protocol_data['initialLabs'])
        # Combine and ensure they are dicts for JSON serialization

        # return [dict(s) for s in grouped_sections + initial_lab_sections] # Original shallow copy
        return [copy.deepcopy(s) for s in grouped_sections + initial_lab_sections] # Use deepcopy

    # Function to create a complete TabConfig dictionary
    def create_protocol_tab(tab_name: str, electrolyte: str) -> Optional[Dict]:
        protocol_data = _get_protocol_data(protocol, electrolyte)

        # Skip Calcium tab if protocol is not CARDIAC
        if electrolyte == 'Calcium' and protocol != 'CARDIAC':
            return None
        # Skip any tab if data is missing (should only be Calcium for REGULAR)
        if not protocol_data and not (electrolyte == 'Calcium' and protocol != 'CARDIAC'):
             print(f"Warning: Missing expected protocol data for {protocol}/{electrolyte}. Skipping tab.")
             return None

        base_tab = Tabs.create_tab(tab_name)
        order_sections = build_order_sections(protocol_data)

        # --- Construct final tab with explicit key order --- 
        
        # Determine final values for keys affected by overrides
        final_mnemonics = ([{'MNEMONIC': tab_name + mnemonic_suffix_override}]
                           if mnemonic_suffix_override
                           else base_tab.get('MNEMONICS', []))
        
        # Handle Resource URLs merge/override
        final_resource_urls = list(base_tab.get('RESOURCE_URLS', []))
        if resource_urls_override:
            existing_labels = {url['LABEL'] for url in final_resource_urls}
            for url in resource_urls_override:
                if url['LABEL'] not in existing_labels:
                    final_resource_urls.append(url)

        # Determine final TAB_KEY
        final_tab_key = base_tab.get('TAB_KEY', '') # Start with base
        if tab_name == 'Phosphorus':
            final_tab_key = 'PHOSPHATE'
        elif tab_name == 'Calcium':
            final_tab_key = 'CALCIUM'

        # Build the dictionary in the order defined by the template
        final_tab = {
            'TAB_NAME': tab_name, # From parameter
            'TAB_KEY': final_tab_key,
            'FLAG_ON_CONCEPT': base_tab.get('FLAG_ON_CONCEPT', ''),
            'CONCEPT_FOR_DISMISS': base_tab.get('CONCEPT_FOR_DISMISS', ''),
            'MNEMONICS': final_mnemonics,
            'CONCEPTS': base_tab.get('CONCEPTS', []),
            'CRITERIA': base_tab.get('CRITERIA', []),
            'GRAPHED_RESULTS': base_tab.get('GRAPHED_RESULTS', []),
            'ORDER_SECTIONS': order_sections, # Use calculated value
            # RESOURCE_URLS is added conditionally below
            'SUBMIT_BUTTON': base_tab.get('SUBMIT_BUTTON', {}),
            'CANCEL_BUTTON': base_tab.get('CANCEL_BUTTON', {}),
        }

        # Conditionally add RESOURCE_URLS only if it's not empty
        if final_resource_urls:
             final_tab['RESOURCE_URLS'] = final_resource_urls
        
        # Re-insert RESOURCE_URLS at the correct position if it was added
        # This is slightly awkward but ensures order if it exists
        if 'RESOURCE_URLS' in final_tab:
            resource_urls = final_tab.pop('RESOURCE_URLS')
            # Insert it before SUBMIT_BUTTON by rebuilding the end of the dict
            submit_button = final_tab.pop('SUBMIT_BUTTON')
            cancel_button = final_tab.pop('CANCEL_BUTTON')
            final_tab['RESOURCE_URLS'] = resource_urls
            final_tab['SUBMIT_BUTTON'] = submit_button
            final_tab['CANCEL_BUTTON'] = cancel_button

        return final_tab # Return as dictionary

    # Build Tabs
    tabs_maybe: List[Optional[Dict]] = [
        create_protocol_tab('Magnesium', 'Magnesium'),
        create_protocol_tab('Potassium', 'Potassium'),
        create_protocol_tab('Phosphorus', 'Phosphorus'),
        create_protocol_tab('Calcium', 'Calcium'),
    ]

    # Filter out None tabs
    valid_tabs = [tab for tab in tabs_maybe if tab is not None]

    # Cast to list of TabConfig dictionaries for the final structure
    # This assumes the dictionaries created match the TypedDict structure
    tabs_final: List[TabConfig] = cast(List[TabConfig], valid_tabs)

    rconfig: RConfig = {
        'TABS': tabs_final,
        'CCL_POSTPROCESS': 'UHS_MPG_GET_TABBED_ADVISOR',
        'JSON_RETURN': '',
    }

    full_config: FullConfig = {'RCONFIG': rconfig}
    return full_config 