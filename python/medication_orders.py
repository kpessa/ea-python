from .types import BaseMedicationDefinition
from typing import Dict

# Base Medication Definitions (matching common/medication_orders.jsonnet)

# --- Magnesium ---
mag_oxide_tab: BaseMedicationDefinition = {
    'MNEMONIC': 'magnesium oxide',
    'routeInfo': {'pillText': 'Oral', 'isOralOrTube': True},
}

mag_sulfate_iv: BaseMedicationDefinition = {
    'MNEMONIC': 'magnesium sulfate',
    'routeInfo': {'pillText': 'Intravenous', 'isOralOrTube': False},
}

# --- Potassium ---
kcl_er_tab: BaseMedicationDefinition = {
    'MNEMONIC': 'potassium chloride extended release',
    'routeInfo': {'pillText': 'Oral', 'isOralOrTube': True},
}

kcl_liquid: BaseMedicationDefinition = {
    'MNEMONIC': 'potassium chloride', # Base mnemonic for liquid/tube
    'routeInfo': {'pillText': 'Feeding Tube', 'isOralOrTube': True},
}

kcl_iv_peripheral: BaseMedicationDefinition = {
    'MNEMONIC': 'potassium chloride 10 mEq/100 mL intravenous solution',
    'routeInfo': {'pillText': 'Peripheral IV', 'isOralOrTube': False},
}

kcl_iv_central: BaseMedicationDefinition = {
    'MNEMONIC': 'potassium chloride 20 mEq/100 mL intravenous solution',
    'routeInfo': {'pillText': 'Central IV Preferred', 'isOralOrTube': False},
}

# --- Phosphate ---
k_phos_neutral_tab: BaseMedicationDefinition = {
    'MNEMONIC': 'K-Phos Neutral',
    'routeInfo': {'pillText': 'Oral', 'isOralOrTube': True},
}

na_phosphate_iv: BaseMedicationDefinition = {
    'MNEMONIC': 'sodium phosphate',
    'routeInfo': {'pillText': 'Intravenous', 'isOralOrTube': False},
}

# --- Calcium ---
calcium_chloride_iv: BaseMedicationDefinition = {
    'MNEMONIC': 'calcium chloride',
    'routeInfo': {'pillText': 'Intravenous', 'isOralOrTube': False},
}

# Optional: Create a dictionary for easier lookup if needed later
all_med_orders: Dict[str, BaseMedicationDefinition] = {
    "magOxideTab": mag_oxide_tab,
    "magSulfateIv": mag_sulfate_iv,
    "kclErTab": kcl_er_tab,
    "kclLiquid": kcl_liquid,
    "kclIvPeripheral": kcl_iv_peripheral,
    "kclIvCentral": kcl_iv_central,
    "kPhosNeutralTab": k_phos_neutral_tab,
    "naPhosphateIv": na_phosphate_iv,
    "calciumChlorideIv": calcium_chloride_iv,
} 