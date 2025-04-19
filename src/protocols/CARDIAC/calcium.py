from typing import List

from ...orders import lab_orders as Labs
from ...types import ProtocolData, SectionGroup, InitialLabConfig
from ...utils import naming as Naming

_electrolyte = 'Ionized Calcium'
_unit = 'mg/dL' # Assuming mg/dL based on Jsonnet comments

_section_groups: List[SectionGroup] = [
    # Group for iCal < 1.1
    {
        'rangeInfo': {'type': 'lessThan', 'electrolyte': _electrolyte, 'level': 1.1, 'unit': _unit},
        'recommendOral': False,
        'replacementSection': {
            'sectionName': '',
            'conceptName': Naming.create_less_than_concept(_electrolyte, 1.1),
            'singleSelect': 1,
            'orders': [
                {
                    # 'baseMed': Meds.calcium_chloride_iv,
                    # 'params': {
                    #     'dose': 1,
                    #     'doseUnit': 'g',
                    #     'route': 'IVPB',
                    #     'form': 'Inj',
                    #     'frequency': 'Once',
                    #     'numberOfDoses': 1,
                    #     'infuseOver': '1 hr',
                    # },
                    'predefinedMedKey': 'CALCIUMCHL_IV_1G_ONCE_1HR'
                },
            ]
        },
        'labSections': [
            {
                'conceptName': Naming.create_less_than_concept(_electrolyte, 1.1),
                'associatedRouteType': 'IV',
                'sectionDescription': f'Monitoring: Recheck {_electrolyte} with next AM labs.',
                'orders': [
                    Labs.calcium_ion_serum_tomorrow_am,
                    Labs.calcium_ion_wb_tomorrow_am,
                ]
            }
        ]
    }
]

_initial_labs: List[InitialLabConfig] = [
    {
        'sectionName': 'Calcium Lab Orders',
        'conceptName': '[%{EALABCALCIUMTODO}.COUNT = 0%]', # Use CALCIUM concept
        'orders': [
            Labs.calcium_ion_serum_stat,
            Labs.calcium_ion_wb_stat,
            Labs.calcium_ion_serum_tomorrow_am,
            Labs.calcium_ion_wb_tomorrow_am,
        ]
    },
]

data: ProtocolData = {
    'sectionGroups': _section_groups,
    'initialLabs': _initial_labs,
} 