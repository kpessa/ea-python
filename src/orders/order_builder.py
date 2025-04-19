from typing import Optional

# Import types and other helper modules
from ..types import (
    BaseOrder, LabOrderDefinition, GenerationContext
)
from .predefined_med_orders import PREDEFINED_MED_ORDERS # Import the predefined definitions
from .. import constants as C # Fixed import path

# --- Basic Order Creation Helpers ---

def create_lab_order(order_definition: LabOrderDefinition) -> BaseOrder:
    """Creates a BaseOrder structure from a LabOrderDefinition.

    >>> lab_def = {'MNEMONIC': 'BMP', 'ORDER_SENTENCE': 'T+1;0400', 'COMMENT': 'Test comment'}
    >>> create_lab_order(lab_def)
    {'MNEMONIC': 'BMP', 'ORDER_SENTENCE': 'T+1;0400', 'ASC_SHORT_DESCRIPTION': '', 'COMMENT': 'Test comment'}
    >>> lab_def_no_comment = {'MNEMONIC': 'K Level', 'ORDER_SENTENCE': 'ASAP'}
    >>> create_lab_order(lab_def_no_comment)
    {'MNEMONIC': 'K Level', 'ORDER_SENTENCE': 'ASAP', 'ASC_SHORT_DESCRIPTION': '', 'COMMENT': ''}
    """
    return {
        'MNEMONIC': order_definition['MNEMONIC'],
        'ORDER_SENTENCE': order_definition['ORDER_SENTENCE'],
        'ASC_SHORT_DESCRIPTION': '', # Assumed empty
        'COMMENT': order_definition.get('COMMENT', '') # Use COMMENT if present
    }



# --- Medication Order Creation (Refactored & Simplified) ---

def create_medication_order(
    predefined_med_key: str, # Use the key instead of baseMed + params
    recommend_oral: bool,
    context: GenerationContext, # Context no longer contains style/dose info
    extra_comment_override: Optional[str] = None # Allow overriding extra comment if needed
) -> BaseOrder:
    """Creates a BaseOrder structure using a predefined medication key."""
    # Look up the predefined order details
    predefined_order = PREDEFINED_MED_ORDERS.get(predefined_med_key)
    if not predefined_order:
        raise ValueError(f"Predefined medication key not found: {predefined_med_key}")

    # Extract details from the predefined order
    mnemonic = predefined_order['mnemonic']
    order_sentence = predefined_order['order_sentence']
    base_med_ref = predefined_order['base_med_ref']

    # Determine route display text based on style using base_med_ref
    route_display_text = ''
    route_info = base_med_ref['routeInfo']
    show_asterisk = route_info['isOralOrTube'] and recommend_oral # Keep asterisk logic

    # Simplified logic - only bold_underline style remains
    pill_text = route_info['pillText']
    asterisk_str = ' *' if show_asterisk else ''

    if pill_text in ['Peripheral IV', 'Central IV Preferred']:
        # Underline style for specific IV routes
        route_display_text = C.ROUTE_STYLE_IV_BOLD_UNDERLINE.format(pill_text=pill_text)
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


# --- Timed Lab Order Helper --- -> Moved to lab_orders.py as it produces LabOrderDefinition
# Kept the medication order builder here as it directly produces BaseOrder 