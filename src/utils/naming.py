from typing import Dict
# Import specific formatting functions needed
from .formatting import format_level_for_concept, format_level_for_display

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
    """Gets the short concept name for an electrolyte.

    Uses a mapping for known names, otherwise uppercases and removes spaces.

    >>> get_concept_name('Potassium')
    'POT'
    >>> get_concept_name('Ionized Calcium')
    'CALCIUM'
    >>> get_concept_name('Blood Glucose')
    'BLOODGLUCOSE'
    """
    return _CONCEPT_NAME_MAPPING.get(tab_name, tab_name.replace(' ', '').upper())

def create_between_concept(electrolyte: str, lower: float, upper: float) -> str:
    """Creates the concept string for a value between lower and upper.

    >>> create_between_concept('Potassium', 3.0, 3.4)
    '[%{EALABPOTTODO}.COUNT > 0 AND {EALABPOTBTW30AND34}%]'
    >>> create_between_concept('Magnesium', 1.2, 1.6)
    '[%{EALABMAGTODO}.COUNT > 0 AND {EALABMAGBTW12AND16}%]'
    """
    concept = get_concept_name(electrolyte)
    lower_str = format_level_for_concept(lower)
    upper_str = format_level_for_concept(upper)
    return f"[%{{EALAB{concept}TODO}}.COUNT > 0 AND {{EALAB{concept}BTW{lower_str}AND{upper_str}}}%]"

def create_less_than_concept(electrolyte: str, level: float) -> str:
    """Creates the concept string for a value less than level.

    >>> create_less_than_concept('Potassium', 2.8)
    '[%{EALABPOTTODO}.COUNT > 0 AND {EALABPOTLT28}%]'
    >>> create_less_than_concept('Ionized Calcium', 1.1)
    '[%{EALABCALCIUMTODO}.COUNT > 0 AND {EALABCALCIUMLT11}%]'
    """
    concept = get_concept_name(electrolyte)
    level_str = format_level_for_concept(level)
    return f"[%{{EALAB{concept}TODO}}.COUNT > 0 AND {{EALAB{concept}LT{level_str}}}%]"

# --- Section Name Helpers ---

def create_between_section_name(electrolyte: str, lower: float, upper: float, unit: str, is_replacement: bool = False) -> str:
    """Creates the section name for a between range.

    >>> create_between_section_name('Potassium', 3.0, 3.4, 'mmol/L')
    'Potassium - 3.0 - 3.4 mmol/L'
    >>> create_between_section_name('Magnesium', 1.2, 1.6, 'mg/dL', is_replacement=True)
    '1.2 - 1.6 mg/dL'
    """
    prefix = '' if is_replacement else f"{electrolyte} - "
    return f"{prefix}{format_level_for_display(lower)} - {format_level_for_display(upper)} {unit}"

def create_less_than_section_name(electrolyte: str, level: float, unit: str, is_replacement: bool = False) -> str:
    """Creates the section name for a less than range.

    >>> create_less_than_section_name('Potassium', 2.8, 'mmol/L')
    'Potassium - < 2.8 mmol/L'
    >>> create_less_than_section_name('Magnesium', 1.2, 'mg/dL', is_replacement=True)
    '< 1.2 mg/dL'
    """
    prefix = '' if is_replacement else f"{electrolyte} - "
    return f"{prefix}< {format_level_for_display(level)} {unit}" 