"""DKA potassium replacement protocol."""

from typing import List

from ...orders import lab_orders as Labs
from ...types import ProtocolData, SectionGroup, InitialLabConfig
from ...utils import naming as Naming
from ... import text as Text

_electrolyte = 'Potassium'
_unit = 'mEq/L'

_section_groups: List[SectionGroup] = [
    # Group for 3.6-3.9 mEq/L
    {
        'rangeInfo': {'type': 'between', 'electrolyte': _electrolyte, 'lower': 3.6, 'upper': 3.9, 'unit': _unit},
        'replacementSection': {
            'sectionName': '',
            'conceptName': Naming.create_between_concept(_electrolyte, 3.6, 3.9),
            'singleSelect': 1,
            'orders': [
                {
                    'predefinedMedKey': 'KCL_IVPERIPH_10MEQ_Q1H_2DOSES_1HR',
                },
                {
                    'predefinedMedKey': 'KCL_IVCENT_20MEQ_ONCE_1HR',
                }
            ]
        },
        'labSections': [
            {
                'conceptName': Naming.create_between_concept(_electrolyte, 3.6, 3.9),
                'sectionDescription': 'Monitoring: Recheck BMP with next AM labs.',
                'orders': [
                    Labs.bmp_tomorrow_am
                ]
            }
        ]
    },
    # Group for 3.2-3.5 mEq/L
    {
        'rangeInfo': {'type': 'between', 'electrolyte': _electrolyte, 'lower': 3.2, 'upper': 3.5, 'unit': _unit},
        'replacementSection': {
            'sectionName': '',
            'conceptName': Naming.create_between_concept(_electrolyte, 3.2, 3.5),
            'singleSelect': 1,
            'orders': [
                {
                    'predefinedMedKey': 'KCL_IVPERIPH_10MEQ_Q1H_4DOSES_1HR',
                },
                {
                    'predefinedMedKey': 'KCL_IVCENT_20MEQ_Q1H_2DOSES_1HR',
                }
            ]
        },
        'labSections': [
            {
                'conceptName': Naming.create_between_concept(_electrolyte, 3.2, 3.5),
                'associatedRouteType': 'Peripheral IV',
                'sectionDescription': 'Monitoring: Recheck potassium level 1 hr after infusion complete.',
                'orders': [
                    {'type': 'timed_lab', 'base_name': 'k_level', 'minutes': 300, 
                     'comment_base': 'Recheck potassium level 1 hr after infusion complete'},
                ]
            },
            {
                'conceptName': Naming.create_between_concept(_electrolyte, 3.2, 3.5),
                'sectionDescription': 'Monitoring: Recheck potassium level 1 hr after infusion complete.',
                'associatedRouteType': 'Central IV',
                'orders': [
                    {'type': 'timed_lab', 'base_name': 'k_level', 'minutes': 180, 
                     'comment_base': 'Recheck potassium level 1 hr after infusion complete',
                     'criticalCare': True}
                ]
            }
        ]
    },
    # Group for 2.8-3.1 mEq/L
    {
        'rangeInfo': {'type': 'between', 'electrolyte': _electrolyte, 'lower': 2.8, 'upper': 3.1, 'unit': _unit},
        'replacementSection': {
            'sectionName': '',
            'conceptName': Naming.create_between_concept(_electrolyte, 2.8, 3.1),
            'singleSelect': 1,
            'orders': [
                {
                    'predefinedMedKey': 'KCL_IVPERIPH_10MEQ_Q1H_6DOSES_1HR',
                },
                {
                    'predefinedMedKey': 'KCL_IVCENT_20MEQ_Q1H_3DOSES_1HR',
                }
            ]
        },
        'labSections': [
            {
                'conceptName': Naming.create_between_concept(_electrolyte, 2.8, 3.1),
                'sectionDescription': 'Monitoring: Recheck potassium level 1 hr after infusion complete.',
                'orders': [
                    {'type': 'timed_lab', 'base_name': 'k_level', 'minutes': 420, 
                     'comment_base': 'Recheck potassium level 1 hr after infusion complete'},
                    {'type': 'timed_lab', 'base_name': 'k_level', 'minutes': 240, 
                     'comment_base': 'Recheck potassium level 1 hr after infusion complete',
                     'criticalCare': True}
                ]
            }
        ]
    },
    # Group for < 2.8 mEq/L
    {
        'rangeInfo': {'type': 'lessThan', 'electrolyte': _electrolyte, 'level': 2.8, 'unit': _unit},
        'replacementSection': {
            'criticalAlertText': Text.create_notify_provider_text(2.8, 'mEq/L'),
            'sectionName': '',
            'conceptName': Naming.create_less_than_concept(_electrolyte, 2.8),
            'singleSelect': 1,
            'orders': [
                {
                    'predefinedMedKey': 'KCL_IVPERIPH_10MEQ_Q1H_8DOSES_1HR',
                },
                {
                    'predefinedMedKey': 'KCL_IVCENT_20MEQ_Q1H_4DOSES_1HR',
                }
            ]
        },
        'labSections': [
            {
                'conceptName': Naming.create_less_than_concept(_electrolyte, 2.8),
                'sectionDescription': 'Monitoring: Add-on mag + phos levels STAT. Recheck potassium level 1 hr after infusion complete.',
                'orders': [
                    Labs.mag_level_asap,
                    Labs.phos_level_stat,
                    {'type': 'timed_lab', 'base_name': 'k_level', 'minutes': 540, 
                     'comment_base': 'Recheck potassium level 1 hr after infusion complete'},
                    {'type': 'timed_lab', 'base_name': 'k_level', 'minutes': 300, 
                     'comment_base': 'Recheck potassium level 1 hr after infusion complete',
                     'criticalCare': True},
                    Labs.bmp_tomorrow_am,
                    Labs.mag_level_tomorrow_am,
                    Labs.phos_level_tomorrow_am
                ]
            }
        ]
    }
]

_initial_labs: List[InitialLabConfig] = [
    {
        'sectionName': 'Potassium Lab Orders',
        'conceptName': '[%{EALABPOTTODO}.COUNT = 0%]',
        'orders': [
            Labs.k_level_stat,
            Labs.bmp_tomorrow_am,
            {'type': 'timed_lab', 'base_name': 'k_level', 'minutes': 180, 
             'comment_base': 'Recheck potassium level in 3 hours'}
        ]
    }
]

data: ProtocolData = {
    'sectionGroups': _section_groups,
    'initialLabs': _initial_labs,
} 