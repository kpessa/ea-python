from typing import List

from ...orders import lab_orders as Labs
from ...types import ProtocolData, SectionGroup, InitialLabConfig
from ...utils import naming as Naming
from ... import text as Text

_electrolyte = 'Phosphorus' # Use consistent spelling
_unit = 'mg/dL'

_section_groups: List[SectionGroup] = [
    # Group for 1.6 - 2.0 mg/dL
    {
        'rangeInfo': {'type': 'between', 'electrolyte': _electrolyte, 'lower': 1.6, 'upper': 2.0, 'unit': _unit},
        'replacementSection': {
            'sectionName': '',
            'conceptName': Naming.create_between_concept(_electrolyte, 1.6, 2.0),
            'singleSelect': 1,
            'orders': [
                {
                    'predefinedMedKey': 'KPHOSNEUT_TAB_2TABS_Q2H_2DOSES'
                },
                {
                    'predefinedMedKey': 'NAPHOS_IV_15MMOL_ONCE'
                },
            ]
        },
        'labSections': [
            {
                'conceptName': Naming.create_between_concept(_electrolyte, 1.6, 2.0),
                'sectionDescription': 'Monitoring: Recheck phosphorous & calcium levels with next AM labs.',
                'orders': [
                    Labs.phos_level_tomorrow_am,
                    Labs.calcium_ion_serum_tomorrow_am,
                    Labs.calcium_ion_wb_tomorrow_am,
                ]
            }
        ]
    },
    # Group for 1.0 - 1.5 mg/dL
    {
        'rangeInfo': {'type': 'between', 'electrolyte': _electrolyte, 'lower': 1.0, 'upper': 1.5, 'unit': _unit},
        'replacementSection': {
            'criticalAlertText': Text.create_notify_provider_text(1.1, 'mg/dL'),
            'sectionName': '',
            'conceptName': Naming.create_between_concept(_electrolyte, 1.0, 1.5),
            'singleSelect': 1,
            'orders': [
                {
                    'predefinedMedKey': 'KPHOSNEUT_TAB_2TABS_Q2H_3DOSES'
                },
                {
                    'predefinedMedKey': 'NAPHOS_IV_15MMOL_Q4H_2DOSES'
                },
            ]
        },
        'labSections': [
            {
                'conceptName': Naming.create_between_concept(_electrolyte, 1.0, 1.5),
                'associatedRouteType': 'Oral',
                'sectionDescription': 'Monitoring: Recheck phosphorous & calcium levels with next AM labs.',
                'orders': [
                    Labs.phos_level_tomorrow_am,
                    Labs.calcium_ion_serum_tomorrow_am,
                    Labs.calcium_ion_wb_tomorrow_am,
                ]
            },
            {
                'conceptName': Naming.create_between_concept(_electrolyte, 1.0, 1.5),
                'associatedRouteType': 'IV',
                'sectionDescription': 'Monitoring: Recheck phosphorous & calcium levels 2 hrs after infusion.',
                'orders': [
                    {'type': 'timed_lab', 'base_name': 'phos_level', 'minutes': 600, 
                     'comment_base': 'Recheck phosphorous level 2 hrs after infusion.'},
                    {'type': 'timed_lab', 'base_name': 'calcium_ion_serum', 'minutes': 600, 
                     'comment_base': 'Recheck calcium level 2 hrs after infusion.'},
                    {'type': 'timed_lab', 'base_name': 'calcium_ion_wb', 'minutes': 600, 
                     'comment_base': 'Recheck calcium level 2 hrs after infusion.'},
                ]
            }
        ]
    },
    # Group for < 1.0 mg/dL
    {
        'rangeInfo': {'type': 'lessThan', 'electrolyte': _electrolyte, 'level': 1.0, 'unit': _unit},
        'recommendOral': False,
        'replacementSection': {
            'criticalAlertText': Text.create_notify_provider_text(1.1, 'mg/dL'),
            'sectionName': '',
            'conceptName': Naming.create_less_than_concept(_electrolyte, 1.0),
            'singleSelect': 1,
            'orders': [
                {
                    'predefinedMedKey': 'NAPHOS_IV_15MMOL_Q4H_2DOSES'
                },
            ]
        },
        'labSections': [
            {
                'conceptName': Naming.create_less_than_concept(_electrolyte, 1.0),
                'associatedRouteType': 'IV',
                'sectionDescription': 'Monitoring: Recheck phosphorous & calcium levels 2 hrs after infusion.',
                'orders': [
                    {'type': 'timed_lab', 'base_name': 'phos_level', 'minutes': 600, 
                     'comment_base': 'Recheck phosphorous level 2 hrs after infusion.'},
                    {'type': 'timed_lab', 'base_name': 'calcium_ion_serum', 'minutes': 600, 
                     'comment_base': 'Recheck calcium level 2 hrs after infusion.'},
                    {'type': 'timed_lab', 'base_name': 'calcium_ion_wb', 'minutes': 600, 
                     'comment_base': 'Recheck calcium level 2 hrs after infusion.'},
                ]
            }
        ]
    }
]

_initial_labs: List[InitialLabConfig] = [
    {
        'sectionName': 'Phosphorous Lab Orders',
        'conceptName': '[%{EALABPHOSTODO}.COUNT = 0%]',
        'orders': [
            Labs.phos_level_stat,
            Labs.calcium_ion_serum_stat,
            Labs.calcium_ion_wb_stat,
            Labs.phos_level_tomorrow_am,
            Labs.calcium_ion_serum_tomorrow_am,
            Labs.calcium_ion_wb_tomorrow_am,
            {'type': 'timed_lab', 'base_name': 'phos_level', 'minutes': 120, 
             'comment_base': 'Collect phos level 2 hours after event'},
            {'type': 'timed_lab', 'base_name': 'calcium_ion_serum', 'minutes': 120, 
             'comment_base': 'Collect calcium level 2 hours after event'},
            {'type': 'timed_lab', 'base_name': 'calcium_ion_wb', 'minutes': 120, 
             'comment_base': 'Collect calcium level 2 hours after event'},
        ]
    },
]

data: ProtocolData = {
    'sectionGroups': _section_groups,
    'initialLabs': _initial_labs,
} 