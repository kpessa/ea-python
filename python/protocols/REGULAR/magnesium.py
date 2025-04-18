from ...types import ProtocolData, SectionGroup, InitialLabConfig
from typing import List # Import List
from ... import naming as Naming # NEW IMPORT
from ... import text as Text # For alert text
from ... import medication_orders as Meds
from ... import lab_orders as Labs

# Define the electrolyte name for clarity
_electrolyte = 'Magnesium'
_unit = 'mg/dL'

_section_groups: List[SectionGroup] = [
    # Group for 1.4 - 1.5 mg/dL
    {
        'rangeInfo': {'type': 'between', 'electrolyte': _electrolyte, 'lower': 1.4, 'upper': 1.5, 'unit': _unit},
        'replacementSection': {
            'sectionName': '', # Built dynamically in helpers
            'conceptName': Naming.create_between_concept(_electrolyte, 1.4, 1.5),
            'singleSelect': 1,
            'orders': [
                {
                    'predefinedMedKey': 'MAG_OX_TAB_400MG_Q12H_2DOSES'
                },
                {
                    'predefinedMedKey': 'MAG_SULF_IV_2G_ONCE_2HR'
                },
            ]
        },
        'labSections': [
            { # Single lab section for all routes in this group
                'conceptName': Naming.create_between_concept(_electrolyte, 1.4, 1.5),
                'sectionDescription': 'Monitoring: Recheck BMP and magnesium level with next AM labs.',
                'orders': [
                    Labs.bmp_tomorrow_am,
                    Labs.mag_level_tomorrow_am,
                ]
            }
        ]
    },
    # Group for < 1.4 mg/dL
    {
        'rangeInfo': {'type': 'lessThan', 'electrolyte': _electrolyte, 'level': 1.4, 'unit': _unit},
        'recommendOral': False, # Explicitly set to False
        'replacementSection': {
            'criticalAlertText': Text.create_notify_provider_text(1.2, 'mg/dL'),
            'sectionName': '', 
            'conceptName': Naming.create_less_than_concept(_electrolyte, 1.4),
            'singleSelect': 1,
            'orders': [
                {
                    'predefinedMedKey': 'MAG_SULF_IV_2G_Q2H_2DOSES_2HR'
                },
            ]
        },
        'labSections': [
            {
                'conceptName': Naming.create_less_than_concept(_electrolyte, 1.4),
                'sectionDescription': 'Monitoring: Recheck magnesium level 4 hrs after infusion complete.',
                'orders': [
                    Labs.create_specific_timed_lab('mag_level', 480, 'Recheck magnesium level 4 hrs after infusion complete.'),
                ]
            }
        ]
    }
]

_initial_labs: List[InitialLabConfig] = [
    {
        'sectionName': 'Magnesium Lab Orders',
        'conceptName': '[%{EALABMAGTODO}.COUNT = 0%]', # Hardcoded concept
        'orders': [
            Labs.mag_level_asap,
            Labs.mag_level_tomorrow_am,
            Labs.bmp_tomorrow_am,
            Labs.mag_level_tomorrow_am,
        ]
    },
]

# Export the final data structure
data: ProtocolData = {
    'sectionGroups': _section_groups,
    'initialLabs': _initial_labs,
} 