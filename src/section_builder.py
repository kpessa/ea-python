from typing import List, Dict, Optional

# Import types and other helper modules
from .types import (
    BaseOrder, SectionGroup, OrderSection, InitialLabConfig, GenerationContext
)
from . import text as Text
from .orders import lab_orders as Labs
from .orders import order_builder as Orders
from .utils import formatting as Format
from . import constants as C

# --- Section Creation Helpers ---

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
    # --- Build ORDERS (Now uses predefinedMedKey) ---
    orders_list: List[BaseOrder] = []
    for item in repl_section_config.get('orders', []):
        med_key = item.get('predefinedMedKey')
        extra_comment = item.get('extraComment') 
        if not med_key:
             raise ValueError("Missing 'predefinedMedKey' in replacementSection order item")
        med_order = Orders.create_medication_order(
            predefined_med_key=med_key, 
            recommend_oral=recommend_oral_flag, 
            context=context,
            extra_comment_override=extra_comment # Pass the specific comment
        )
        orders_list.append(med_order)
    replacement_section['ORDERS'] = orders_list

    return replacement_section

def _get_lab_section_prefix(associated_route: Optional[str], protocol: str) -> str:
    """Determines the display prefix for a lab section based on route and protocol."""
    if not associated_route:
        return ''

    temp_prefix = ''
    route_lower = associated_route.lower()
    is_combined_route = '/' in associated_route

    if 'oral' in route_lower:
        temp_prefix = 'ORAL / FEEDING TUBE - Labs' if is_combined_route else 'ORAL - Labs'
    elif 'peripheral' in route_lower or 'central' in route_lower:
        if protocol == 'CARDIAC':
            if is_combined_route:
                temp_prefix = 'PERIPHERAL / CENTRAL IV - Labs'
            elif 'peripheral' in route_lower:
                 temp_prefix = 'PERIPHERAL IV - Labs'
            else:
                 temp_prefix = 'CENTRAL IV - Labs'
        else: # REGULAR or DKA protocol
            temp_prefix = 'IV - Labs'
    elif associated_route == 'IV': # Catch generic 'IV'
        temp_prefix = 'IV - Labs'

    return f"{temp_prefix}:" if temp_prefix else ''

def _build_lab_section(
    lab_section_config: Dict, # Using Dict temporarily, refine if needed
    index: int,
    context: GenerationContext
) -> OrderSection:
    """Builds a lab order section."""
    protocol = context['protocol']
    # Apply step prefix ONLY to the first lab section within the group (index 0)
    step_prefix = Text.step2_text if index == 0 else ''

    # Determine prefix using the helper function
    associated_route = lab_section_config.get('associatedRouteType')
    display_prefix = _get_lab_section_prefix(associated_route, protocol)

    # Construct section name
    monitoring_instructions = lab_section_config.get('sectionDescription', 'Missing Description')
    separator = C.HTML_LINE_BREAK if display_prefix and monitoring_instructions else ''
    formatted_instructions = C.HTML_SMALL_NORMAL_FONT.format(instructions=monitoring_instructions) if monitoring_instructions else ''
    
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
            # Call the function from lab_orders to get the LabOrderDefinition
            timed_lab_def = Labs.create_specific_timed_lab(base_name, minutes, comment_base, suffix)
            # Process it like a standard lab order to get the BaseOrder format
            orders_list.append(Orders.create_lab_order(timed_lab_def)) 
        else:
            # Assume it's a standard LabOrderDefinition (like Labs.bmp_tomorrow_am)
            orders_list.append(Orders.create_lab_order(order_config))

    final_lab_section: OrderSection = {
        'SECTION_NAME': final_section_name,
        'CONCEPT_NAME': lab_section_config['conceptName'],
        'SINGLE_SELECT': 0, # Labs usually multi-select
        'SHOW_INACTIVE_DUPLICATES': 0,
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
            range_header_text = f"{range_info['electrolyte']}: {Format.format_level_for_display(range_info['lower'])} - {Format.format_level_for_display(range_info['upper'])} {range_info['unit']}{C.HTML_LINE_BREAK}"
        elif range_info['type'] == 'lessThan':
            range_header_text = f"{range_info['electrolyte']}: < {Format.format_level_for_display(range_info['level'])} {range_info['unit']}{C.HTML_LINE_BREAK}"
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
                processed_orders.append(Orders.create_lab_order(timed_lab_definition))
            else:
                # Assume it's a standard LabOrderDefinition
                processed_orders.append(Orders.create_lab_order(order_def))
        
        order_sections.append({
            'SECTION_NAME': lab_config['sectionName'],
            'CONCEPT_NAME': lab_config['conceptName'],
            'SINGLE_SELECT': 0, # Allow multiple initial labs
            'SHOW_INACTIVE_DUPLICATES': 0,
            'ORDERS': processed_orders, # Use the processed list
        })
    return order_sections 