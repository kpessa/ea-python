import os
import math
from typing import List, Dict, Optional, cast, Union

# Import types and other helper modules
from .types import (
    BaseOrder, # MedicationOrderParams removed
    BaseMedicationDefinition, LabOrderDefinition,
    OrderSection, SectionGroup, InitialLabConfig, ProtocolData, Mnemonic,
    GraphedResult, TabConfig, GenerationContext, Protocol, # RouteStyle removed
    RangeInfo
)
from . import text as Text
from . import components as Components
from .predefined_med_orders import PREDEFINED_MED_ORDERS # Import the new definitions
from . import lab_orders as Labs 

# --- Environment Variable Handling ---

def get_generation_context() -> GenerationContext:
    """Reads environment variables to determine build context."""
    # Default values mimic compile.sh
    raw_protocol = os.environ.get('EA_PROTOCOL', 'REGULAR')
    # route_style = cast(RouteStyle, os.environ.get('ROUTE_STYLE', 'bold_underline')) # Removed
    # show_total_dose_env = os.environ.get('SHOW_TOTAL_DOSE', 'false').lower() # Removed
    # show_total_dose = show_total_dose_env == 'true' # Removed

    # Basic validation
    protocol = cast(Protocol, raw_protocol)
    if protocol not in ['REGULAR', 'CARDIAC', 'DKA']:
        raise ValueError(f"Invalid EA_PROTOCOL: {protocol}")
    # if route_style not in ['badge', 'bold_underline']: # Removed
    #     raise ValueError(f"Invalid ROUTE_STYLE: {route_style}") # Removed

    return {
        'protocol': protocol,
        # 'routeStyle': route_style, # Removed
        # 'showTotalDose': show_total_dose # Removed
    }

# --- Formatting Helpers ---

def format_level_for_display(level: float) -> str:
    """Formats a float to one decimal place."""
    return f"{level:.1f}"

def format_level_for_concept(level: float) -> str:
    """Removes decimal by multiplying by 10 and flooring."""
    return str(math.floor(level * 10))

# --- Concept Name Helpers ---

_CONCEPT_NAME_MAPPING: Dict[str, str] = {
    'Potassium': 'POT',
    'Magnesium': 'MAG',
    'Phosphorous': 'PHOS',
    'Phosphorus': 'PHOS',
    'Calcium': 'CALCIUM',
    'Ionized Calcium': 'CALCIUM',
}

def get_concept_name(tab_name: str) -> str:
    """Gets the short concept name for an electrolyte."""
    return _CONCEPT_NAME_MAPPING.get(tab_name, tab_name.replace(' ', '').upper())

def create_between_concept(electrolyte: str, lower: float, upper: float) -> str:
    """Creates the concept string for a value between lower and upper."""
    concept = get_concept_name(electrolyte)
    lower_str = format_level_for_concept(lower)
    upper_str = format_level_for_concept(upper)
    return f"[%{{EALAB{concept}TODO}}.COUNT > 0 AND {{EALAB{concept}BTW{lower_str}AND{upper_str}}}%]"

def create_less_than_concept(electrolyte: str, level: float) -> str:
    """Creates the concept string for a value less than level."""
    concept = get_concept_name(electrolyte)
    level_str = format_level_for_concept(level)
    return f"[%{{EALAB{concept}TODO}}.COUNT > 0 AND {{EALAB{concept}LT{level_str}}}%]"

# --- Section Name Helpers ---

def create_between_section_name(electrolyte: str, lower: float, upper: float, unit: str, is_replacement: bool = False) -> str:
    """Creates the section name for a between range."""
    prefix = '' if is_replacement else f"{electrolyte} - "
    return f"{prefix}{format_level_for_display(lower)} - {format_level_for_display(upper)} {unit}"

def create_less_than_section_name(electrolyte: str, level: float, unit: str, is_replacement: bool = False) -> str:
    """Creates the section name for a less than range."""
    prefix = '' if is_replacement else f"{electrolyte} - "
    return f"{prefix}< {format_level_for_display(level)} {unit}"

# --- Basic Order Creation Helpers ---

def create_lab_order(order_definition: LabOrderDefinition) -> BaseOrder:
    """Creates a BaseOrder structure from a LabOrderDefinition."""
    return {
        'MNEMONIC': order_definition['MNEMONIC'],
        'ORDER_SENTENCE': order_definition['ORDER_SENTENCE'],
        'ASC_SHORT_DESCRIPTION': '', # Assumed empty
        'COMMENT': order_definition.get('COMMENT', '') # Use COMMENT if present
    }

def _create_order_sentence(
    dose: Union[int, float],
    dose_unit: str,
    route: str,
    form: Optional[str] = None,
    frequency: Optional[str] = None,
    duration: Optional[str] = None,
    infuse_over: Optional[str] = None
) -> str:
    """Constructs the ORDER_SENTENCE string matching DCW format."""
    parts = [f"{dose} {dose_unit}", route]

    # Standardize form capitalization
    if form:
        if form.lower() == 'inj': parts.append('Inj')
        elif form.lower() == 'liq': parts.append('Liq')
        elif form.lower() == 'er tab': parts.append('ER tab') # Keep space
        elif form.lower() == 'tab': parts.append('Tab')
        else: parts.append(form.capitalize()) # Default capitalize

    # Standardize frequency
    if frequency:
        freq_lower = frequency.lower()
        if 'interval' in freq_lower:
             parts.append(freq_lower.replace('(interval)', 'interval').replace('hr', 'h')) # qXh interval
        elif freq_lower == 'once':
             parts.append('Once')
        elif 'hr' in freq_lower:
             parts.append(freq_lower.replace('hr', 'h')) # qXh
        else:
             parts.append(frequency) # Keep original if unsure

    # Standardize duration
    if duration:
        dur_lower = duration.lower()
        num_str = ''.join(filter(str.isdigit, dur_lower))
        if num_str:
            num = int(num_str)
            dose_str = 'dose' if num == 1 else 'doses'
            parts.append(f"Duration: {num} {dose_str}")
        # else: # Don't append duration if number not found? Or keep original?
            # parts.append(f"Duration: {duration}") # Keep original for now if parse fails

    # Standardize infuse over
    if infuse_over:
        # Expects format like "X hr"
        parts.append(f"infuse over {infuse_over.lower()}") # lowercase 'i', no colon

    final_sentence = ', '.join(filter(None, parts)) # Filter out potential None parts if logic changes
    return final_sentence

# --- Medication Order Creation (Refactored & Simplified) ---

def create_medication_order(
    predefined_med_key: str, # Use the key instead of baseMed + params
    recommend_oral: bool,
    context: GenerationContext, # Context no longer contains style/dose info
    extra_comment_override: Optional[str] = None # Allow overriding extra comment if needed
) -> BaseOrder:
    """Creates a BaseOrder structure using a predefined medication key."""
    # route_style = context['routeStyle'] # Removed
    # show_total_dose = context['showTotalDose'] # Removed

    # Look up the predefined order details
    predefined_order = PREDEFINED_MED_ORDERS.get(predefined_med_key)
    if not predefined_order:
        raise ValueError(f"Predefined medication key not found: {predefined_med_key}")

    # Extract details from the predefined order
    mnemonic = predefined_order['mnemonic']
    order_sentence = predefined_order['order_sentence']
    base_med_ref = predefined_order['base_med_ref']
    # parse_info = predefined_order['parse_info'] # Removed

    # total_dose_comment = _format_total_dose_comment(parse_info, show_total_dose) # Removed

    # Determine route display text based on style using base_med_ref
    route_display_text = ''
    route_info = base_med_ref['routeInfo']
    show_asterisk = route_info['isOralOrTube'] and recommend_oral # Keep asterisk logic

    # Simplified logic - only bold_underline style remains
    pill_text = route_info['pillText']
    asterisk_str = ' *' if show_asterisk else ''

    if pill_text in ['Peripheral IV', 'Central IV Preferred']:
        # Underline style for specific IV routes
        route_display_text = f'<span style="font-weight: 900; text-decoration: underline;">{pill_text}</span>'
    elif route_info['isOralOrTube']:
         # Plain text for Oral/Tube, add asterisk if needed
         route_display_text = f'{pill_text}{asterisk_str}'
    elif pill_text == 'Intravenous': # Condition for generic IV
         # Plain text for generic Intravenous
         route_display_text = 'Intravenous'
    # else: No text for other routes

    # Construct final comment (using optional override if provided)
    extra_comment = extra_comment_override # Use override if present

    # Simplified comment construction
    comment_parts = []
    # No Total Dose comment anymore
    if route_display_text:
        comment_parts.append(route_display_text)
    if extra_comment:
        # Add space before extra comment only if other parts exist
        prefix = ' ' if comment_parts else ''
        comment_parts.append(prefix + extra_comment)

    final_comment = ''.join(comment_parts)

    return {
        'MNEMONIC': mnemonic,
        'ORDER_SENTENCE': order_sentence,
        'ASC_SHORT_DESCRIPTION': '', # Assuming always empty
        'COMMENT': final_comment.strip(),
    }

# --- Section Creation Helpers (Adjusted Call) ---

def _build_replacement_section(
    group: SectionGroup,
    range_header_text: str,
    recommend_oral_flag: bool,
    context: GenerationContext
) -> OrderSection:
    """Builds the replacement (medication) order section for a group."""
    repl_section_config = group['replacementSection']
    alert_text = repl_section_config.get('criticalAlertText', '')
    recommendation_text = Text.recommended_oral_text if recommend_oral_flag else ''
    replacement_section_name = (
        range_header_text +
        alert_text +
        Text.step1_text +
        recommendation_text +
        repl_section_config.get('sectionName', '') # Original sectionName often empty
    )

    replacement_section: OrderSection = {
        'SECTION_NAME': replacement_section_name,
        'CONCEPT_NAME': repl_section_config['conceptName'],
        'SINGLE_SELECT': repl_section_config['singleSelect'],
        'SHOW_INACTIVE_DUPLICATES': 0,
    }
    # --- Build ORDERS with explicit loop for debugging --- (Now uses predefinedMedKey)
    orders_list: List[BaseOrder] = []
    for item in repl_section_config.get('orders', []):
        # item should now be like {'predefinedMedKey': 'KEY_NAME', 'extraComment': 'optional comment'}
        med_key = item.get('predefinedMedKey')
        extra_comment = item.get('extraComment') # Pass extra comment if present
        if not med_key:
             raise ValueError("Missing 'predefinedMedKey' in replacementSection order item")
        med_order = create_medication_order(
            predefined_med_key=med_key, 
            recommend_oral=recommend_oral_flag, 
            context=context,
            extra_comment_override=extra_comment # Pass the specific comment
        )
        orders_list.append(med_order)
    replacement_section['ORDERS'] = orders_list
    # --- End build ORDERS with loop ---

    return replacement_section

def _build_lab_section(
    lab_section_config: Dict, # Using Dict temporarily, refine if needed
    index: int,
    context: GenerationContext
) -> OrderSection:
    """Builds a lab order section."""
    # route_style = context['routeStyle'] # Removed
    protocol = context['protocol']
    # Apply step prefix ONLY to the first lab section within the group (index 0)
    step_prefix = Text.step2_text if index == 0 else ''

    # Determine prefix based on associatedRouteType
    associated_route = lab_section_config.get('associatedRouteType')
    display_prefix = ''
    if associated_route:
        temp_prefix = ''
        route_lower = associated_route.lower() # Convert to lowercase for easier comparison
        
        # Handle combined and specific routes
        if 'oral' in route_lower: # Catches 'Oral' and 'Oral / Feeding Tube'
            temp_prefix = 'ORAL / FEEDING TUBE - Labs' if '/' in associated_route else 'ORAL - Labs'
        elif 'peripheral' in route_lower or 'central' in route_lower: # Catches IV types
            if protocol == 'CARDIAC':
                temp_prefix = 'PERIPHERAL / CENTRAL IV - Labs' if '/' in associated_route else \
                                ('PERIPHERAL IV - Labs' if 'peripheral' in route_lower else 'CENTRAL IV - Labs')
            else: # REGULAR protocol
                temp_prefix = 'IV - Labs' # Simpler for REGULAR
        elif associated_route == 'IV': # Catch generic 'IV'
            temp_prefix = 'IV - Labs'
        # Add more mappings here if other associatedRouteTypes appear
        
        if temp_prefix:
            display_prefix = f"{temp_prefix}:" # Just the text prefix, no extra styling needed now

    # Construct section name
    monitoring_instructions = lab_section_config.get('sectionDescription', 'Missing Description')
    # --- REMOVE TEMPORARY DEBUGGING --- 
    # if index == 0 and 'Add-on mag & phos levels STAT' in monitoring_instructions: 
    #     print(f"---> DEBUG: Lab Section index={index}, monitoring_instructions = {repr(monitoring_instructions)}")
    # --- END TEMPORARY DEBUGGING ---
    # Add separator ONLY if both prefix and instructions exist
    separator = '<br>' if display_prefix and monitoring_instructions else ''
    formatted_instructions = f'<small style="font-weight: normal;">{monitoring_instructions}</small>' if monitoring_instructions else ''
    
    # Combine parts, ensuring step_prefix comes first if present
    parts = [step_prefix, display_prefix, separator, formatted_instructions]
    final_section_name = ''.join(filter(None, parts)) # Join non-empty parts

    # Build orders list based on type
    orders_list: List[BaseOrder] = []
    for order_config in lab_section_config.get('orders', []):
        if isinstance(order_config, dict) and order_config.get('type') == 'timed_lab':
            # Handle new timed lab structure
            base_name = order_config.get('base_name')
            minutes = order_config.get('minutes')
            comment_base = order_config.get('comment_base')
            suffix = order_config.get('suffix', '')
            if not all([base_name, minutes is not None, comment_base]):
                raise ValueError(f"Missing required fields for timed_lab: {order_config}")
            # Call the new function from lab_orders to get the LabOrderDefinition
            timed_lab_def = Labs.create_specific_timed_lab(base_name, minutes, comment_base, suffix)
            # Process it like a standard lab order to get the BaseOrder format
            orders_list.append(create_lab_order(timed_lab_def)) 
        else:
            # Assume it's a standard LabOrderDefinition (like Labs.bmp_tomorrow_am)
            orders_list.append(create_lab_order(order_config))

    final_lab_section: OrderSection = {
        'SECTION_NAME': final_section_name,
        'CONCEPT_NAME': lab_section_config['conceptName'],
        'SINGLE_SELECT': 0, # Labs usually multi-select
        'SHOW_INACTIVE_DUPLICATES': 0,
        # 'ORDERS': [create_lab_order(order_def) for order_def in lab_section_config['orders']], # Old way
        'ORDERS': orders_list, # Use the newly built list
    }
    return final_lab_section

def create_grouped_order_sections(
    groups: List[SectionGroup],
    context: GenerationContext
) -> List[OrderSection]:
    """Creates order sections from SectionGroup data using helper functions."""
    order_sections: List[OrderSection] = []

    for group in groups:
        recommend_oral_flag = group.get('recommendOral', True)
        range_info = group['rangeInfo']
        
        # Create header text based on range type
        if range_info['type'] == 'between':
            range_header_text = f"{range_info['electrolyte']}: {format_level_for_display(range_info['lower'])} - {format_level_for_display(range_info['upper'])} {range_info['unit']}<br>"
        elif range_info['type'] == 'lessThan':
            range_header_text = f"{range_info['electrolyte']}: < {format_level_for_display(range_info['level'])} {range_info['unit']}<br>"
        else:
             raise ValueError(f"Unknown rangeInfo type: {range_info['type']}")

        # --- Replacement Section ---
        replacement_section = _build_replacement_section(
            group=group,
            range_header_text=range_header_text,
            recommend_oral_flag=recommend_oral_flag,
            context=context
        )
        order_sections.append(replacement_section)

        # --- Lab Sections ---
        for index, lab_section_config in enumerate(group['labSections']):
            lab_section = _build_lab_section(
                lab_section_config=lab_section_config,
                index=index,
                context=context
            )
            order_sections.append(lab_section)

    return order_sections

def create_initial_lab_sections(
    initial_labs: List[InitialLabConfig]
) -> List[OrderSection]:
    """Creates order sections for initial labs."""
    order_sections: List[OrderSection] = []
    for lab_config in initial_labs:
        # Process orders within the initial lab config
        processed_orders: List[BaseOrder] = []
        for order_def in lab_config.get('orders', []):
            if isinstance(order_def, dict) and order_def.get('type') == 'timed_lab':
                # Handle new timed lab structure
                base_name = order_def.get('base_name')
                minutes = order_def.get('minutes')
                comment_base = order_def.get('comment_base')
                suffix = order_def.get('suffix', '')
                if not all([base_name, minutes is not None, comment_base]):
                    raise ValueError(f"Missing required fields for initial timed_lab: {order_def}")
                # Generate the LabOrderDefinition using the specific function
                timed_lab_definition = Labs.create_specific_timed_lab(base_name, minutes, comment_base, suffix)
                # Convert to BaseOrder format
                processed_orders.append(create_lab_order(timed_lab_definition))
            else:
                # Assume it's a standard LabOrderDefinition
                processed_orders.append(create_lab_order(order_def))
        
        order_sections.append({
            'SECTION_NAME': lab_config['sectionName'],
            'CONCEPT_NAME': lab_config['conceptName'],
            'SINGLE_SELECT': 0, # Allow multiple initial labs
            'SHOW_INACTIVE_DUPLICATES': 0,
            # 'ORDERS': [create_lab_order(order_def) for order_def in lab_config['orders']], # Old way
            'ORDERS': processed_orders, # Use the processed list
        })
    return order_sections

# --- Tab Creation Helpers ---

def _create_mnemonic(tab_name: str) -> Mnemonic:
    """Creates a default mnemonic dictionary."""
    return {'MNEMONIC': f'{tab_name} Replacement'}

def _create_graphed_results(tab_name: str) -> List[GraphedResult]:
    """Creates the graphed results structure for a tab."""
    concept_base = get_concept_name(tab_name)
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
    concept = get_concept_name(tab_name)
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

# --- Timed Lab Order Helper ---

def create_timed_lab_order(mnemonic: str, offset_minutes: int, comment: str) -> LabOrderDefinition:
    """
    Creates a LabOrderDefinition for a timed lab draw.

    Args:
        mnemonic: The base mnemonic for the lab (e.g., 'Potassium Level').
        offset_minutes: The time offset in minutes (e.g., 180 for N+180).
        comment: The specific comment to include for this timed order.

    Returns:
        A LabOrderDefinition dictionary.
    """
    order_sentence = f'Requested Draw Date and T T;N+{offset_minutes}, Blood, Timed Study collect, Once'
    return {
        'MNEMONIC': mnemonic,
        'ORDER_SENTENCE': order_sentence,
        'ASC_SHORT_DESCRIPTION': '', # Assume empty for labs
        'COMMENT': comment,
    } 