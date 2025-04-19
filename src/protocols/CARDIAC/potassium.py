from typing import List
from ...types import ProtocolData, SectionGroup, InitialLabConfig
from ... import naming as Naming
from ... import text as Text
from ... import medication_orders as Meds
from ... import lab_orders as Labs

_electrolyte = 'Potassium'
_unit = 'mmol/L'

_section_groups: List[SectionGroup] = [
    # Group for 3.6 - 3.9 mmol/L
    {
        'rangeInfo': {'type': 'between', 'electrolyte': _electrolyte, 'lower': 3.6, 'upper': 3.9, 'unit': _unit},
        'replacementSection': {
            'sectionName': '',
            'conceptName': Naming.create_between_concept(_electrolyte, 3.6, 3.9),
            'singleSelect': 1,
            'orders': [
                {
                    'predefinedMedKey': 'KCL_ERTAB_20MEQ_ONCE'
                },
                {
                    'predefinedMedKey': 'KCL_LIQ_20MEQ_ONCE'
                },
                {
                    'predefinedMedKey': 'KCL_IVPERIPH_10MEQ_Q1H_2DOSES_1HR'
                },
                {
                    'predefinedMedKey': 'KCL_IVCENT_20MEQ_ONCE_1HR'
                },
            ]
        },
        'labSections': [
            {
                'conceptName': Naming.create_between_concept(_electrolyte, 3.6, 3.9),
                'associatedRouteType': 'IV',
                'sectionDescription': 'Monitoring: Recheck BMP with next AM labs.',
                'orders': [
                    Labs.bmp_tomorrow_am,
                ]
            }
        ]
    },
    # Group for 3.2 - 3.5 mmol/L
    {
        'rangeInfo': {'type': 'between', 'electrolyte': _electrolyte, 'lower': 3.2, 'upper': 3.5, 'unit': _unit},
        'replacementSection': {
            'sectionName': '',
            'conceptName': Naming.create_between_concept(_electrolyte, 3.2, 3.4),
            'singleSelect': 1,
            'orders': [
                {
                    'predefinedMedKey': 'KCL_ERTAB_20MEQ_Q2H_2DOSES'
                },
                {
                    'predefinedMedKey': 'KCL_LIQ_20MEQ_Q2H_2DOSES'
                },
                {
                    'predefinedMedKey': 'KCL_IVPERIPH_10MEQ_Q1H_4DOSES_1HR'
                },
                {
                    'predefinedMedKey': 'KCL_IVCENT_20MEQ_Q1H_2DOSES_1HR'
                },
            ]
        },
        'labSections': [
            {
                'conceptName': Naming.create_between_concept(_electrolyte, 3.2, 3.4),
                'associatedRouteType': 'Oral',
                'sectionDescription': 'Monitoring: Recheck potassium level 4 hours after last dose.',
                'orders': [
                    {'type': 'timed_lab', 'base_name': 'k_level', 'minutes': 480, 
                     'comment_base': Text.timed_lab_comment_k_oral},
                ]
            },
            {
                'conceptName': Naming.create_between_concept(_electrolyte, 3.2, 3.4),
                'associatedRouteType': 'Peripheral',
                'sectionDescription': 'Monitoring: Recheck potassium level 1 hr after infusion complete.',
                'orders': [
                    {'type': 'timed_lab', 'base_name': 'k_level', 'minutes': 300, 
                     'comment_base': Text.timed_lab_comment_k_iv},
                ]
            },
            {
                'conceptName': Naming.create_between_concept(_electrolyte, 3.2, 3.4),
                'associatedRouteType': 'Central',
                'sectionDescription': 'Monitoring: Recheck potassium level 1 hr after infusion complete.',
                'orders': [
                    {'type': 'timed_lab', 'base_name': 'k_level', 'minutes': 180, 
                     'comment_base': Text.timed_lab_comment_k_iv},
                ]
            }
        ]
    },
    # Group for 2.8 - 3.1 mmol/L
    {
        'rangeInfo': {'type': 'between', 'electrolyte': _electrolyte, 'lower': 2.8, 'upper': 3.1, 'unit': _unit},
        'recommendOral': False,
        'replacementSection': {
            'sectionName': '',
            'conceptName': Naming.create_between_concept(_electrolyte, 2.8, 3.1),
            'singleSelect': 1,
            'orders': [
                {
                    'predefinedMedKey': 'KCL_ERTAB_20MEQ_Q2H_3DOSES'
                },
                {
                    'predefinedMedKey': 'KCL_LIQ_20MEQ_Q2H_3DOSES'
                },
                {
                    'predefinedMedKey': 'KCL_IVPERIPH_10MEQ_Q1H_6DOSES_1HR'
                },
                {
                    'predefinedMedKey': 'KCL_IVCENT_20MEQ_Q1H_3DOSES_1HR'
                },
            ]
        },
        'labSections': [
            {
                'conceptName': Naming.create_between_concept(_electrolyte, 2.8, 3.1),
                'associatedRouteType': 'Oral',
                'sectionDescription': 'Monitoring: Recheck potassium level 4 hrs after last dose.',
                'orders': [
                    {'type': 'timed_lab', 'base_name': 'k_level', 'minutes': 600, 'suffix': '_oral',
                     'comment_base': Text.timed_lab_comment_k_oral},
                ]
            },
            {
                'conceptName': Naming.create_between_concept(_electrolyte, 2.8, 3.1),
                'associatedRouteType': 'Peripheral',
                'sectionDescription': 'Monitoring: Recheck potassium level 1 hr after infusion complete.',
                'orders': [
                    {'type': 'timed_lab', 'base_name': 'k_level', 'minutes': 420, 
                     'comment_base': Text.timed_lab_comment_k_iv},
                ]
            },
            {
                'conceptName': Naming.create_between_concept(_electrolyte, 2.8, 3.1),
                'associatedRouteType': 'Central',
                'sectionDescription': 'Monitoring: Recheck potassium level 1 hr after infusion complete.',
                'orders': [
                    {'type': 'timed_lab', 'base_name': 'k_level', 'minutes': 240, 
                     'comment_base': Text.timed_lab_comment_k_iv},
                ]
            }
        ]
    },
    # Group for < 2.8 mmol/L
    {
        'rangeInfo': {'type': 'lessThan', 'electrolyte': _electrolyte, 'level': 2.8, 'unit': _unit},
        'recommendOral': False,
        'replacementSection': {
            'criticalAlertText': Text.notify_provider_simple_text,
            'sectionName': '',
            'conceptName': Naming.create_less_than_concept(_electrolyte, 2.8),
            'singleSelect': 1,
            'orders': [
                {
                    'predefinedMedKey': 'KCL_IVPERIPH_10MEQ_Q1H_8DOSES_1HR'
                },
                {
                    'predefinedMedKey': 'KCL_IVCENT_20MEQ_Q1H_4DOSES_1HR'
                },
            ]
        },
        'labSections': [
            {
                'conceptName': Naming.create_less_than_concept(_electrolyte, 2.8),
                'sectionDescription': 'Monitoring: <br>1. Add-on mag & phos levels STAT, if not recently obtained.<br>2. Recheck potassium level 1 hr after infusion complete.<br>3. Repeat BMP, mag and phos levels with next AM labs.<hr>1. Add-on mag & phos levels STAT, if not recently obtained.',
                'orders': [
                    Labs.phos_level_add_on,
                    Labs.mag_level_add_on,
                ]
            },
            {
                'conceptName': Naming.create_less_than_concept(_electrolyte, 2.8),
                'associatedRouteType': 'Peripheral',
                'sectionDescription': 'Monitoring: Recheck potassium level 1 hr after infusion complete.',
                'orders': [
                    {'type': 'timed_lab', 'base_name': 'k_level', 'minutes': 540, 
                     'comment_base': Text.timed_lab_comment_k_iv},
                ]
            },
            {
                'conceptName': Naming.create_less_than_concept(_electrolyte, 2.8),
                'associatedRouteType': 'Central',
                'sectionDescription': 'Monitoring: Recheck potassium level 1 hr after infusion complete.',
                'orders': [
                    {'type': 'timed_lab', 'base_name': 'k_level', 'minutes': 300, 
                     'comment_base': Text.timed_lab_comment_k_iv},
                ]
            },
            {
                'conceptName': Naming.create_less_than_concept(_electrolyte, 2.8),
                'sectionDescription': 'Monitoring: Repeat BMP, mag and phos levels with next AM labs.',
                'orders': [
                    Labs.bmp_tomorrow_am,
                    Labs.mag_level_tomorrow_am,
                    Labs.phos_level_tomorrow_am,
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
            {'type': 'timed_lab', 'base_name': 'bmp', 'minutes': 240, 
             'comment_base': 'Collect BMP 4 hours after event'},
            {'type': 'timed_lab', 'base_name': 'mag_level', 'minutes': 240, 
             'comment_base': 'Collect mag level 4 hours after event'},
            {'type': 'timed_lab', 'base_name': 'phos_level', 'minutes': 240, 
             'comment_base': 'Collect phos level 4 hours after event'},
        ]
    },
]

data: ProtocolData = {
    'sectionGroups': _section_groups,
    'initialLabs': _initial_labs,
} 