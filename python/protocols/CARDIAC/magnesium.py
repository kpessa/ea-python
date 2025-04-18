from typing import List
from ...types import ProtocolData, SectionGroup, InitialLabConfig
from ... import helpers as H
from ... import text as Text
from ... import medication_orders as Meds
from ... import lab_orders as Labs

_electrolyte = 'Magnesium'
_unit = 'mg/dL'

_section_groups: List[SectionGroup] = [
    # Group for 1.8 - 2.0 mg/dL
    {
        'rangeInfo': {'type': 'between', 'electrolyte': _electrolyte, 'lower': 1.8, 'upper': 2.0, 'unit': _unit},
        'recommendOral': False,
        'replacementSection': {
            'sectionName': '', # Built dynamically
            'conceptName': H.create_between_concept(_electrolyte, 1.8, 2.0),
            'singleSelect': 1,
            'orders': [
                {
                    'predefinedMedKey': 'MAG_SULF_IV_1G_ONCE_1HR'
                },
            ]
        },
        'labSections': [
            {
                'conceptName': H.create_between_concept(_electrolyte, 1.8, 2.0),
                'sectionDescription': 'Monitoring: Recheck BMP and magnesium level with next AM labs.',
                'orders': [
                    Labs.mag_level_tomorrow_am,
                ]
            }
        ]
    },
    # Group for 1.4 - 1.7 mg/dL
    {
        'rangeInfo': {'type': 'between', 'electrolyte': _electrolyte, 'lower': 1.4, 'upper': 1.7, 'unit': _unit},
        'recommendOral': False,
        'replacementSection': {
            'sectionName': '',
            'conceptName': H.create_between_concept(_electrolyte, 1.4, 1.7),
            'singleSelect': 1,
            'orders': [
                {
                    'predefinedMedKey': 'MAG_SULF_IV_2G_ONCE_2HR'
                },
            ]
        },
        'labSections': [
            {
                'conceptName': H.create_between_concept(_electrolyte, 1.4, 1.7),
                'sectionDescription': 'Monitoring: Recheck magnesium level 4 hrs after infusion complete.',
                'orders': [
                    {'type': 'timed_lab', 'base_name': 'mag_level', 'minutes': 360, 
                     'comment_base': 'Recheck magnesium level 4 hrs after infusion complete.'},
                ]
            }
        ]
    },
    # Group for < 1.4 mg/dL
    {
        'rangeInfo': {'type': 'lessThan', 'electrolyte': _electrolyte, 'level': 1.4, 'unit': _unit},
        'recommendOral': False,
        'replacementSection': {
            'criticalAlertText': Text.create_notify_provider_text(1.2, 'mg/dL'),
            'sectionName': '',
            'conceptName': H.create_less_than_concept(_electrolyte, 1.4),
            'singleSelect': 1,
            'orders': [
                {
                    'predefinedMedKey': 'MAG_SULF_IV_2G_Q2H_2DOSES_2HR'
                },
            ]
        },
        'labSections': [
            {
                'conceptName': H.create_less_than_concept(_electrolyte, 1.4),      'associatedRouteType': 'IV',
                'sectionDescription': 'Monitoring: Recheck magnesium level 4 hrs after infusion complete.',
                'orders': [
                    {'type': 'timed_lab', 'base_name': 'mag_level', 'minutes': 480, 
                     'comment_base': 'Recheck magnesium level 4 hrs after infusion complete.'},
                ]
            }
        ]
    }
]

# Initial labs same as REGULAR
_initial_labs: List[InitialLabConfig] = [
    {
        'sectionName': 'Magnesium Lab Orders',
        'conceptName': '[%{EALABMAGTODO}.COUNT = 0%]',
        'orders': [
            Labs.mag_level_asap,
            Labs.mag_level_tomorrow_am,
            Labs.bmp_tomorrow_am,
            {'type': 'timed_lab', 'base_name': 'mag_level', 'minutes': 240, 
             'comment_base': 'Collect mag level 4 hours after event'},
        ]
    }
]

data: ProtocolData = {
    'sectionGroups': _section_groups,
    'initialLabs': _initial_labs,
} 