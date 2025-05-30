from ..types import LabOrderDefinition
from typing import Dict

# Definitions for Lab Orders (matching common/lab_orders.jsonnet)

# --- Base Lab Mnemonics (for dynamic lookup) ---
# Derived from existing definitions
_base_lab_mnemonics = {
    'bmp': 'BMP',
    'mag_level': 'Magnesium Level',
    'k_level': 'Potassium Level',
    'phos_level': 'Phosphate Level',
    'calcium_ion_serum': 'Calcium Level Ionized, Serum',
    'calcium_ion_wb': 'Calcium Level Ionized, Whole Blood',
}

# --- Predefined Lab Orders ---

# --- BMP ---
bmp_tomorrow_am: LabOrderDefinition = {
    'MNEMONIC': 'BMP',
    'ORDER_SENTENCE': 'Requested Draw Date and T T+1;0400, Blood, Tomorrow AM collect, Once',
    'COMMENT': 'Order a BMP with next AM labs.',
}

# --- Magnesium ---
mag_level_tomorrow_am: LabOrderDefinition = {
    'MNEMONIC': 'Magnesium Level',
    'ORDER_SENTENCE': 'Requested Draw Date and T T+1;0400, Blood, Tomorrow AM collect, Once',
    'COMMENT': 'Order a Magnesium Level with next AM labs.',
}

mag_level_asap: LabOrderDefinition = {
    'MNEMONIC': 'Magnesium Level',
    'ORDER_SENTENCE': 'Blood, ASAP (Now) collect, Once',
    'COMMENT': 'Order a STAT Magnesium Level.',
}

mag_level_add_on: LabOrderDefinition = {
    'MNEMONIC': 'Magnesium Level',
    'ORDER_SENTENCE': 'Requested Draw Date and T T;N, Blood, Routine Today collect, Once, add to specimen in lab',
    'COMMENT': 'Order an add-on Magnesium Level.',
}

# --- Potassium ---
k_level_tomorrow_am: LabOrderDefinition = {
    'MNEMONIC': 'Potassium Level',
    'ORDER_SENTENCE': 'Requested Draw Date and T T+1;0400, Blood, Tomorrow AM collect, Once',
    'COMMENT': 'Order a Potassium Level with next AM labs.',
}

k_level_stat: LabOrderDefinition = {
    'MNEMONIC': 'Potassium Level',
    'ORDER_SENTENCE': 'Blood, ASAP (Now) collect, Once',
    'COMMENT': 'Order a STAT Potassium Level.',
}

# --- Phosphate ---
phos_level_tomorrow_am: LabOrderDefinition = {
    'MNEMONIC': 'Phosphate Level',
    'ORDER_SENTENCE': 'Requested Draw Date and T T+1;0400, Blood, Tomorrow AM collect, Once',
    'COMMENT': 'Order a Phosphate Level with next AM labs.',
}

phos_level_stat: LabOrderDefinition = {
    'MNEMONIC': 'Phosphate Level',
    'ORDER_SENTENCE': 'Blood, ASAP (Now) collect, Once',
    'COMMENT': 'Order a STAT Phosphate Level.',
}

phos_level_add_on: LabOrderDefinition = {
    'MNEMONIC': 'Phosphate Level',
    'ORDER_SENTENCE': 'Requested Draw Date and T T;N, Blood, Routine Today collect, Once, add to specimen in lab',
    'COMMENT': 'Order an add-on Phosphate Level.',
}

# --- Calcium ---
calcium_ion_serum_tomorrow_am: LabOrderDefinition = {
    'MNEMONIC': 'Calcium Level Ionized, Serum',
    'ORDER_SENTENCE': 'Requested Draw Date and T T+1;0400, Blood, Tomorrow AM collect, Once',
    'COMMENT': 'Order a Calcium Level with next AM labs.',
}

calcium_ion_wb_tomorrow_am: LabOrderDefinition = {
    'MNEMONIC': 'Calcium Level Ionized, Whole Blood',
    'ORDER_SENTENCE': 'Requested Draw Date and T T+1;0400, Blood, Tomorrow AM collect, Once',
    'COMMENT': 'Order a Calcium Level with next AM labs.',
}

# Uncommenting serum stat and setting sentence to match whole blood stat
calcium_ion_serum_stat: LabOrderDefinition = {
    'MNEMONIC': 'Calcium Level Ionized, Serum',
    'ORDER_SENTENCE': 'Requested Draw Date and T T;N, Blood, ASAP collect, Once', # Reverted to domain sentence
    'COMMENT': 'Order a STAT Calcium Level.',
}

calcium_ion_wb_stat: LabOrderDefinition = {
    'MNEMONIC': 'Calcium Level Ionized, Whole Blood',
    'ORDER_SENTENCE': 'Blood, ASAP (Now) collect, Once', # Keep this as ASAP (Now) for now
    'COMMENT': 'Order a STAT Calcium Level.',
}

# Optional: Create a dictionary for easier lookup if needed later
all_lab_orders: Dict[str, LabOrderDefinition] = {
    "bmpTomorrowAm": bmp_tomorrow_am,
    "magLevelTomorrowAm": mag_level_tomorrow_am,
    "magLevelAsap": mag_level_asap,
    "magLevelAddOn": mag_level_add_on,
    "kLevelTomorrowAm": k_level_tomorrow_am,
    "kLevelStat": k_level_stat,
    "phosLevelTomorrowAm": phos_level_tomorrow_am,
    "phosLevelStat": phos_level_stat,
    "phosLevelAddOn": phos_level_add_on,
    "calciumIonSerumTomorrowAm": calcium_ion_serum_tomorrow_am,
    "calciumIonWbTomorrowAm": calcium_ion_wb_tomorrow_am,
    "calciumIonSerumStat": calcium_ion_serum_stat, # Uncommented
    "calciumIonWbStat": calcium_ion_wb_stat,
}

# --- Dynamic Lab Order Generation ---

def get_timed_lab(base_name: str, minutes: int, suffix: str = '') -> LabOrderDefinition:
    """Generates LabOrderDefinitions for timed labs based on base name, minutes, and optional suffix.

    >>> get_timed_lab('k_level', 240)
    {'MNEMONIC': 'Potassium Level', 'ORDER_SENTENCE': 'Requested Draw Date and T T;N+240, Blood, Timed Study collect, Once', 'COMMENT': 'Collect 4.0 hours after event. [Dynamic: k_level_timed_n240]'}
    >>> get_timed_lab('mag_level', 360, suffix='_cardiac')
    {'MNEMONIC': 'Magnesium Level', 'ORDER_SENTENCE': 'Requested Draw Date and T T;N+360, Blood, Timed Study collect, Once', 'COMMENT': 'Collect 6.0 hours after event. [Dynamic: mag_level_timed_n360_cardiac]'}
    >>> get_timed_lab('invalid_lab', 60)
    Traceback (most recent call last):
        ...
    ValueError: Unknown base lab name 'invalid_lab' for timed order
    """
    # Find the base mnemonic
    mnemonic = _base_lab_mnemonics.get(base_name)
    
    if mnemonic:
        # Generate the specific timed order sentence format
        hours = round(minutes / 60, 1)
        name = f"{base_name}_timed_n{minutes}{suffix}" # Include suffix in dynamic name
        return {
            'MNEMONIC': mnemonic,
            'ORDER_SENTENCE': f'Requested Draw Date and T T;N+{minutes}, Blood, Timed Study collect, Once',
            'COMMENT': f'Collect {hours} hours after event. [Dynamic: {name}]', # Keep dynamic name in comment
        }
    else:
        # Base name didn't match known labs
            raise ValueError(f"Unknown base lab name '{base_name}' for timed order")

# --- New function for specific timed lab comments ---
def create_specific_timed_lab(base_name: str, minutes: int, comment_base: str, suffix: str = '') -> LabOrderDefinition:
    """Generates LabOrderDefinitions for timed labs with a specific base comment.

    Note: suffix parameter is currently unused in the output but kept for interface consistency.

    >>> create_specific_timed_lab('phos_level', 120, 'Collect 2 hours after something.')
    {'MNEMONIC': 'Phosphate Level', 'ORDER_SENTENCE': 'Requested Draw Date and T T;N+120, Blood, Timed Study collect, Once', 'COMMENT': 'Collect 2 hours after something.'}
    >>> create_specific_timed_lab('bmp', 480, 'Recheck BMP later.')
    {'MNEMONIC': 'BMP', 'ORDER_SENTENCE': 'Requested Draw Date and T T;N+480, Blood, Timed Study collect, Once', 'COMMENT': 'Recheck BMP later.'}
    >>> create_specific_timed_lab('no_such_lab', 60, 'Test')
    Traceback (most recent call last):
        ...
    ValueError: Unknown base lab name 'no_such_lab' for specific timed order
    """
    mnemonic = _base_lab_mnemonics.get(base_name)
    if not mnemonic:
        raise ValueError(f"Unknown base lab name '{base_name}' for specific timed order")

    # Generate the dynamic name part - Not needed for comment anymore
    # name = f"{base_name}_timed_n{minutes}{suffix}"
    # Construct the final comment using ONLY the base comment provided
    final_comment = comment_base # Remove the dynamic suffix

    return {
        'MNEMONIC': mnemonic,
        'ORDER_SENTENCE': f'Requested Draw Date and T T;N+{minutes}, Blood, Timed Study collect, Once',
        'COMMENT': final_comment,
        # 'ASC_SHORT_DESCRIPTION': '', # Assuming empty for labs, handled by create_lab_order
    }