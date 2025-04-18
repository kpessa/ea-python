from typing import List
from ...types import ProtocolData, SectionGroup, InitialLabConfig
from ... import helpers as H
from ... import text as Text
from ... import medication_orders as Meds
from ... import lab_orders as Labs

_electrolyte = 'Phosphorus' # Use consistent spelling
_unit = 'mg/dL'

_section_groups: List[SectionGroup] = [
    # Group for 1.6 - 2.0 mg/dL
    {
        'rangeInfo': {'type': 'between', 'electrolyte': _electrolyte, 'lower': 1.6, 'upper': 2.0, 'unit': _unit},
        'replacementSection': {
            'sectionName': '',
            'conceptName': H.create_between_concept(_electrolyte, 1.6, 2.0),
            'singleSelect': 1,
            'orders': [
                {
                    'baseMed': Meds.k_phos_neutral_tab,
                    'params': {'dose': 2, 'doseUnit': 'tab(s)', 'route': 'PO', 'form': 'Tab', 'frequency': 'q2hr (interval)', 'duration': '2 dose(s)', 'numberOfDoses': 2},
                },
                {
                    'baseMed': Meds.na_phosphate_iv,
                    'params': {'dose': 15, 'doseUnit': 'mmol', 'route': 'IVPB', 'form': 'Inj', 'frequency': 'Once', 'numberOfDoses': 1},
                },
            ]
        },
        'labSections': [
            {
                'conceptName': H.create_between_concept(_electrolyte, 1.6, 2.0),
                'associatedRouteType': 'IV',
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
            'criticalAlertText': Text.create_critically_low_notify_physician_text(1.1, 'mg/dL'),
            'sectionName': '',
            'conceptName': H.create_between_concept(_electrolyte, 1.0, 1.5),
            'singleSelect': 1,
            'orders': [
                {
                    'baseMed': Meds.k_phos_neutral_tab,
                    'params': {'dose': 2, 'doseUnit': 'tab(s)', 'route': 'PO', 'form': 'Tab', 'frequency': 'q2hr (interval)', 'duration': '3 dose(s)', 'numberOfDoses': 3},
                },
                {
                    'baseMed': Meds.na_phosphate_iv,
                    'params': {'dose': 15, 'doseUnit': 'mmol', 'route': 'IVPB', 'form': 'Inj', 'frequency': 'q4hr (interval)', 'duration': '2 dose(s)', 'numberOfDoses': 2},
                },
            ]
        },
        'labSections': [
            {
                'conceptName': H.create_between_concept(_electrolyte, 1.0, 1.5),
                'associatedRouteType': 'Oral',
                'sectionDescription': 'Monitoring: Recheck phosphorous & calcium levels with next AM labs.',
                'orders': [
                    Labs.phos_level_tomorrow_am,
                    Labs.calcium_ion_serum_tomorrow_am,
                    Labs.calcium_ion_wb_tomorrow_am,
                ]
            },
            {
                'conceptName': H.create_between_concept(_electrolyte, 1.0, 1.5),
                'associatedRouteType': 'IV',
                'sectionDescription': 'Monitoring: Recheck phosphorous & calcium levels 2 hrs after infusion.',
                'orders': [
                    Labs.get_timed_lab('phos_level', 600),
                    Labs.get_timed_lab('calcium_ion_serum', 600),
                    Labs.get_timed_lab('calcium_ion_wb', 600),
                ]
            }
        ]
    },
    # Group for < 1.0 mg/dL
    {
        'rangeInfo': {'type': 'lessThan', 'electrolyte': _electrolyte, 'level': 1.0, 'unit': _unit},
        'replacementSection': {
            'criticalAlertText': Text.create_critically_low_notify_physician_text(1.1, 'mg/dL'),
            'sectionName': '',
            'conceptName': H.create_less_than_concept(_electrolyte, 1.0),
            'singleSelect': 1,
            'orders': [
                {
                    'baseMed': Meds.na_phosphate_iv,
                    'params': {'dose': 15, 'doseUnit': 'mmol', 'route': 'IVPB', 'form': 'Inj', 'frequency': 'q4hr (interval)', 'duration': '2 dose(s)', 'numberOfDoses': 2},
                },
            ]
        },
        'labSections': [
            {
                'conceptName': H.create_less_than_concept(_electrolyte, 1.0),
                'associatedRouteType': 'IV',
                'sectionDescription': 'Monitoring: Recheck phosphorous & calcium levels 2 hrs after infusion.',
                'orders': [
                    Labs.get_timed_lab('phos_level', 600),
                    Labs.get_timed_lab('calcium_ion_serum', 600),
                    Labs.get_timed_lab('calcium_ion_wb', 600),
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
            Labs.get_timed_lab('phos_level', 120),
            Labs.get_timed_lab('calcium_ion_serum', 120),
            Labs.get_timed_lab('calcium_ion_wb', 120),
        ]
    },
]

data: ProtocolData = {
    'sectionGroups': _section_groups,
    'initialLabs': _initial_labs,
} 