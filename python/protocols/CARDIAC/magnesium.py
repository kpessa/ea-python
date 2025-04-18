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
                    'baseMed': Meds.mag_sulfate_iv,
                    'params': {
                        'dose': 1, 'doseUnit': 'g', 'route': 'IVPB', 'form': 'Premix',
                        'frequency': 'Once', 'duration': None, 'numberOfDoses': 1,
                        'infuseOver': '1 hr'
                    },
                },
            ]
        },
        'labSections': [
            {
                'conceptName': H.create_between_concept(_electrolyte, 1.8, 2.0),
                'associatedRouteType': 'IV', # Jsonnet had 'Peripheral', using 'IV' as per TS translation logic
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
                    'baseMed': Meds.mag_sulfate_iv,
                    'params': {
                        'dose': 2, 'doseUnit': 'g', 'route': 'IVPB', 'form': 'Premix',
                        'frequency': 'Once', 'duration': None, 'numberOfDoses': 1,
                        'infuseOver': '2 hr'
                    },
                },
            ]
        },
        'labSections': [
            {
                'conceptName': H.create_between_concept(_electrolyte, 1.4, 1.7),
                'associatedRouteType': 'IV',
                'sectionDescription': 'Monitoring: Recheck magnesium level 4 hrs after infusion complete.',
                'orders': [
                    Labs.get_timed_lab('mag_level', 360),
                ]
            }
        ]
    },
    # Group for < 1.4 mg/dL
    {
        'rangeInfo': {'type': 'lessThan', 'electrolyte': _electrolyte, 'level': 1.4, 'unit': _unit},
        'recommendOral': False,
        'replacementSection': {
            'criticalAlertText': Text.create_critically_low_notify_physician_text(1.2, 'mg/dL'),
            'sectionName': '',
            'conceptName': H.create_less_than_concept(_electrolyte, 1.4),
            'singleSelect': 1,
            'orders': [
                {
                    'baseMed': Meds.mag_sulfate_iv,
                    'params': {
                        'dose': 2, 'doseUnit': 'g', 'route': 'IVPB', 'form': 'Premix',
                        'frequency': 'q2hr (interval)', 'duration': '2 dose(s)', 'numberOfDoses': 2,
                        'infuseOver': '2 hr'
                    },
                },
            ]
        },
        'labSections': [
            {
                'conceptName': H.create_less_than_concept(_electrolyte, 1.4),
                'associatedRouteType': 'IV',
                'sectionDescription': 'Monitoring: Recheck magnesium level 4 hrs after infusion complete.',
                'orders': [
                    Labs.get_timed_lab('mag_level', 480),
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
            Labs.get_timed_lab('mag_level', 240),
        ]
    }
]

data: ProtocolData = {
    'sectionGroups': _section_groups,
    'initialLabs': _initial_labs,
} 