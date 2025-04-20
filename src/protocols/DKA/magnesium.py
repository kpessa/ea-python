"""DKA magnesium replacement protocol."""

from typing import List

from ...orders import lab_orders as Labs
from ...types import ProtocolData, SectionGroup, InitialLabConfig
from ...utils import naming as Naming
from ... import text as Text

_electrolyte = 'Magnesium'
_unit = 'mg/dL'

_section_groups: List[SectionGroup] = [
    # Group for 1.4 - 1.5 mg/dL
    {
        'rangeInfo': {'type': 'between', 'electrolyte': _electrolyte, 'lower': 1.4, 'upper': 1.5, 'unit': _unit},
        'replacementSection': {
            'sectionName': '',
            'conceptName': Naming.create_between_concept(_electrolyte, 1.4, 1.5),
            'singleSelect': 1,
            'orders': [
                {
                    'predefinedMedKey': 'MAG_OX_TAB_400MG_Q12H_2DOSES',
                    'associatedRouteType': 'Oral'                
                },
                {
                    'predefinedMedKey': 'MAG_SULF_IV_2G_ONCE_2HR',
                    'associatedRouteType': 'Intravenous'
                },
            ]
        },
        'labSections': [
            {
                'conceptName': Naming.create_between_concept(_electrolyte, 1.4, 1.5),
                'associatedRouteType': 'Oral',
                'sectionDescription': 'Monitoring: Recheck magnesium level with next AM labs',
                'orders': [
                    Labs.mag_level_tomorrow_am,
                ]
            },
            {
                'conceptName': Naming.create_between_concept(_electrolyte, 1.4, 1.5),
                'associatedRouteType': 'IV',
                'sectionDescription': 'Monitoring: Recheck magnesium level 4 hrs after infusion complete',
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
            'conceptName': Naming.create_less_than_concept(_electrolyte, 1.4),
            'singleSelect': 1,
            'orders': [
                {
                    'predefinedMedKey': 'MAG_SULF_IV_2G_Q2H_2DOSES_2HR',
                    'associatedRouteType': 'Peripheral / Central IV'
                },
            ]
        },
        'labSections': [
            {
                'conceptName': Naming.create_less_than_concept(_electrolyte, 1.4),
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