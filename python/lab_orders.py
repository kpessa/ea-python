import re # Import regex module
from .types import LabOrderDefinition
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
    'COMMENT': 'Order an add-on Magnesium Level. Repeat with next AM labs.',
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
    'COMMENT': 'Order an add-on Phosphate Level. Repeat with next AM labs.',
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

def __getattr__(name: str) -> LabOrderDefinition:
    """Dynamically generates LabOrderDefinitions for timed labs."""
    # Pattern: base_name_timed_n<minutes>(_optional_suffix)
    match = re.match(r"^(.*?)_timed_n(\d+)(_.*)?$", name)
    
    if match:
        base_name = match.group(1)
        minutes = int(match.group(2))
        # optional_suffix = match.group(3) # Store if needed later

        # Find the base mnemonic
        mnemonic = _base_lab_mnemonics.get(base_name)
        
        if mnemonic:
            # Generate the specific timed order sentence format
            # TODO: Potentially refine COMMENT later based on medication context
            hours = round(minutes / 60, 1)
            return {
                'MNEMONIC': mnemonic,
                'ORDER_SENTENCE': f'Requested Draw Date and T T;N+{minutes}, Blood, Timed Study collect, Once',
                'COMMENT': f'Collect {hours} hours after event. [Dynamic: {name}]',
            }
        else:
            # Base name didn't match known labs
             raise AttributeError(f"Module '{__name__}' has no attribute '{name}' (Unknown base lab for dynamic timed order)")

    # If the name doesn't match the pattern, raise AttributeError
    # This allows Python to continue searching for normally defined attributes
    raise AttributeError(f"Module '{__name__}' has no attribute '{name}'")

# --- Ensure existing definitions are accessible ---
# This helps avoid conflicts with __getattr__ if the names were identical
# (though they aren't in this case)
bmp_tomorrow_am = all_lab_orders["bmpTomorrowAm"]
mag_level_tomorrow_am = all_lab_orders["magLevelTomorrowAm"]
mag_level_asap = all_lab_orders["magLevelAsap"]
mag_level_add_on = all_lab_orders["magLevelAddOn"]
k_level_tomorrow_am = all_lab_orders["kLevelTomorrowAm"]
k_level_stat = all_lab_orders["kLevelStat"]
phos_level_tomorrow_am = all_lab_orders["phosLevelTomorrowAm"]
phos_level_stat = all_lab_orders["phosLevelStat"]
phos_level_add_on = all_lab_orders["phosLevelAddOn"]
calcium_ion_serum_tomorrow_am = all_lab_orders["calciumIonSerumTomorrowAm"]
calcium_ion_wb_tomorrow_am = all_lab_orders["calciumIonWbTomorrowAm"]
calcium_ion_serum_stat = all_lab_orders["calciumIonSerumStat"] # Uncommented
calcium_ion_wb_stat = all_lab_orders["calciumIonWbStat"]