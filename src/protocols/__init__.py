# Empty file to make 'protocols' a package 

from . import REGULAR, CARDIAC, DKA

# Export all protocol data
PROTOCOLS = {
    'REGULAR': {
        'Magnesium': REGULAR.magnesium_data,
        'Potassium': REGULAR.potassium_data,
        'Phosphorus': REGULAR.phosphate_data,
    },
    'CARDIAC': {
        'Magnesium': CARDIAC.magnesium_data,
        'Potassium': CARDIAC.potassium_data,
        'Phosphorus': CARDIAC.phosphate_data,
        'Calcium': CARDIAC.calcium_data,
    },
    'DKA': {
        'Magnesium': DKA.magnesium_data,
        'Potassium': DKA.potassium_data,
        'Phosphorus': DKA.phosphate_data,
    }
} 