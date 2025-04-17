from typing import List
from ...types import ProtocolData, SectionGroup, InitialLabConfig
from ... import helpers as H
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
            'conceptName': H.create_between_concept(_electrolyte, 3.6, 3.9),
            'singleSelect': 1,
            'orders': [
                {
                    'baseMed': Meds.kcl_er_tab,
                    'params': {'dose': 20, 'doseUnit': 'mEq', 'route': 'PO', 'form': 'ER tab', 'frequency': 'Once', 'numberOfDoses': 1},
                },
                {
                    'baseMed': Meds.kcl_liquid,
                    'params': {'dose': 20, 'doseUnit': 'mEq', 'route': 'Feeding Tube', 'form': 'Liq', 'frequency': 'Once', 'numberOfDoses': 1},
                },
                {
                    'baseMed': Meds.kcl_iv_peripheral,
                    'params': {'dose': 10, 'doseUnit': 'mEq', 'route': 'IV', 'frequency': 'q1hr', 'duration': '2 dose(s)', 'numberOfDoses': 2, 'infuseOver': '1 hr'},
                },
                {
                    'baseMed': Meds.kcl_iv_central,
                    'params': {'dose': 20, 'doseUnit': 'mEq', 'route': 'IV', 'frequency': 'Once', 'numberOfDoses': 1, 'infuseOver': '1 hr'},
                },
            ]
        },
        'labSections': [
            {
                'conceptName': H.create_between_concept(_electrolyte, 3.6, 3.9),
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
            'conceptName': H.create_between_concept(_electrolyte, 3.2, 3.5),
            'singleSelect': 1,
            'orders': [
                {
                    'baseMed': Meds.kcl_er_tab,
                    'params': {'dose': 20, 'doseUnit': 'mEq', 'route': 'PO', 'form': 'ER tab', 'frequency': 'q2hr (interval)', 'duration': '2 dose(s)', 'numberOfDoses': 2},
                },
                {
                    'baseMed': Meds.kcl_liquid,
                    'params': {'dose': 20, 'doseUnit': 'mEq', 'route': 'Feeding Tube', 'form': 'Liq', 'frequency': 'q2hr (interval)', 'duration': '2 dose(s)', 'numberOfDoses': 2},
                },
                {
                    'baseMed': Meds.kcl_iv_peripheral,
                    'params': {'dose': 10, 'doseUnit': 'mEq', 'route': 'IV', 'frequency': 'q1hr', 'duration': '4 dose(s)', 'numberOfDoses': 4, 'infuseOver': '1 hr'},
                },
                {
                    'baseMed': Meds.kcl_iv_central,
                    'params': {'dose': 20, 'doseUnit': 'mEq', 'route': 'IV', 'frequency': 'q1hr', 'duration': '2 dose(s)', 'numberOfDoses': 2, 'infuseOver': '1 hr'},
                },
            ]
        },
        'labSections': [
            {
                'conceptName': H.create_between_concept(_electrolyte, 3.2, 3.5),
                'associatedRouteType': 'Oral',
                'sectionDescription': 'Monitoring: Recheck potassium level 4 hours after last dose.',
                'orders': [
                    Labs.k_level_timed_n480,
                ]
            },
            {
                'conceptName': H.create_between_concept(_electrolyte, 3.2, 3.5),
                'associatedRouteType': 'Peripheral',
                'sectionDescription': 'Monitoring: Recheck potassium level 1 hr after infusion complete.',
                'orders': [
                    Labs.k_level_timed_n300,
                ]
            },
            {
                'conceptName': H.create_between_concept(_electrolyte, 3.2, 3.5),
                'associatedRouteType': 'Central',
                'sectionDescription': 'Monitoring: Recheck potassium level 1 hr after infusion complete.',
                'orders': [
                    Labs.k_level_timed_n180,
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
            'conceptName': H.create_between_concept(_electrolyte, 2.8, 3.1),
            'singleSelect': 1,
            'orders': [
                {
                    'baseMed': Meds.kcl_er_tab,
                    'params': {'dose': 20, 'doseUnit': 'mEq', 'route': 'PO', 'form': 'ER tab', 'frequency': 'q2hr (interval)', 'duration': '3 dose(s)', 'numberOfDoses': 3},
                },
                {
                    'baseMed': Meds.kcl_liquid,
                    'params': {'dose': 20, 'doseUnit': 'mEq', 'route': 'Feeding Tube', 'form': 'Liq', 'frequency': 'q2hr (interval)', 'duration': '3 dose(s)', 'numberOfDoses': 3},
                },
                {
                    'baseMed': Meds.kcl_iv_peripheral,
                    'params': {'dose': 10, 'doseUnit': 'mEq', 'route': 'IV', 'frequency': 'q1hr', 'duration': '6 dose(s)', 'numberOfDoses': 6, 'infuseOver': '1 hr'},
                },
                {
                    'baseMed': Meds.kcl_iv_central,
                    'params': {'dose': 20, 'doseUnit': 'mEq', 'route': 'IV', 'frequency': 'q1hr', 'duration': '3 dose(s)', 'numberOfDoses': 3, 'infuseOver': '1 hr'},
                },
            ]
        },
        'labSections': [
            {
                'conceptName': H.create_between_concept(_electrolyte, 2.8, 3.1),
                'associatedRouteType': 'Oral',
                'sectionDescription': 'Monitoring: Recheck potassium level 4 hrs after last dose.',
                'orders': [
                    Labs.k_level_timed_n600_oral,
                ]
            },
            {
                'conceptName': H.create_between_concept(_electrolyte, 2.8, 3.1),
                'associatedRouteType': 'Peripheral',
                'sectionDescription': 'Monitoring: Recheck potassium level 1 hr after infusion complete.',
                'orders': [
                    Labs.k_level_timed_n420,
                ]
            },
            {
                'conceptName': H.create_between_concept(_electrolyte, 2.8, 3.1),
                'associatedRouteType': 'Central',
                'sectionDescription': 'Monitoring: Recheck potassium level 1 hr after infusion complete.',
                'orders': [
                    Labs.k_level_timed_n240,
                ]
            }
        ]
    },
    # Group for < 2.8 mmol/L
    {
        'rangeInfo': {'type': 'lessThan', 'electrolyte': _electrolyte, 'level': 2.8, 'unit': _unit},
        'replacementSection': {
            'criticalAlertText': Text.critically_low_notify_physician_simple_text,
            'sectionName': '',
            'conceptName': H.create_less_than_concept(_electrolyte, 2.8),
            'singleSelect': 1,
            'orders': [
                {
                    'baseMed': Meds.kcl_iv_peripheral,
                    'params': {'dose': 10, 'doseUnit': 'mEq', 'route': 'IV', 'form': None, 'frequency': 'q1hr', 'duration': '8 dose(s)', 'numberOfDoses': 8, 'infuseOver': '1 hr'},
                },
                {
                    'baseMed': Meds.kcl_iv_central,
                    'params': {'dose': 20, 'doseUnit': 'mEq', 'route': 'IV', 'frequency': 'q1hr', 'duration': '4 dose(s)', 'numberOfDoses': 4, 'infuseOver': '1 hr'},
                },
            ]
        },
        'labSections': [
            {
                'conceptName': H.create_less_than_concept(_electrolyte, 2.8),
                'associatedRouteType': 'Peripheral',
                'sectionDescription': 'Monitoring: Add-on mag & phos levels STAT, if not recently obtained.',
                'orders': [
                    Labs.phos_level_add_on,
                    Labs.mag_level_add_on,
                ]
            },
            {
                'conceptName': H.create_less_than_concept(_electrolyte, 2.8),
                'associatedRouteType': 'Peripheral',
                'sectionDescription': 'Monitoring: Recheck potassium level 1 hr after infusion complete.',
                'orders': [
                    Labs.k_level_timed_n540,
                ]
            },
            {
                'conceptName': H.create_less_than_concept(_electrolyte, 2.8),
                'associatedRouteType': 'Central',
                'sectionDescription': 'Monitoring: Recheck potassium level 1 hr after infusion complete.',
                'orders': [
                    Labs.k_level_timed_n300,
                ]
            },
            {
                'conceptName': H.create_less_than_concept(_electrolyte, 2.8),
                'associatedRouteType': 'IV', # Generic for AM labs
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
            Labs.bmp_timed_n240,
            Labs.mag_level_timed_n240,
            Labs.phos_level_timed_n240,
        ]
    },
]

data: ProtocolData = {
    'sectionGroups': _section_groups,
    'initialLabs': _initial_labs,
} 