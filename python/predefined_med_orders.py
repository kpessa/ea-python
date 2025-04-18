# Centralized definitions for predefined medication orders
# Each key maps to a dictionary containing:
#   - 'mnemonic': The base medication mnemonic (e.g., 'magnesium oxide')
#   - 'order_sentence': The exact, pre-formatted order sentence string.
#   - 'base_med_ref': A reference to the original BaseMedicationDefinition 
#                     (needed for routeInfo lookup in helpers.py).
#   - 'parse_info': A dictionary containing parameters needed for comment generation 
#                   or other logic, which helpers.py might need. This avoids 
#                   complex parsing of the order_sentence string itself.

from . import medication_orders as Meds # To reference base med definitions

PREDEFINED_MED_ORDERS = {
    # Magnesium Orders
    'MAG_OX_TAB_400MG_Q12H_2DOSES': {
        'mnemonic': Meds.mag_oxide_tab['MNEMONIC'],
        'order_sentence': '400 mg, PO, Tab, q12hr (interval), Duration: 2 dose(s)',
        'base_med_ref': Meds.mag_oxide_tab,
    },
    'MAG_SULF_IV_2G_ONCE_2HR': {
        'mnemonic': Meds.mag_sulfate_iv['MNEMONIC'],
        'order_sentence': '2 g, IVPB, Premix, Once, Infuse over: 2 hr',
        'base_med_ref': Meds.mag_sulfate_iv,
    },
    'MAG_SULF_IV_2G_Q2H_2DOSES_2HR': {
        'mnemonic': Meds.mag_sulfate_iv['MNEMONIC'],
        'order_sentence': '2 g, IVPB, Premix, q2hr (interval), Duration: 2 dose(s), Infuse over: 2 hr',
        'base_med_ref': Meds.mag_sulfate_iv,
    },
    'MAG_SULF_IV_1G_ONCE_1HR': { # Cardiac Only
        'mnemonic': Meds.mag_sulfate_iv['MNEMONIC'],
        'order_sentence': '1 g, IVPB, Premix, Once, Infuse over: 1 hr',
        'base_med_ref': Meds.mag_sulfate_iv,
    },

    # Potassium Orders (Regular & Cardiac unless noted)
    'KCL_ERTAB_20MEQ_Q2H_2DOSES': {
        'mnemonic': Meds.kcl_er_tab['MNEMONIC'],
        'order_sentence': '20 mEq, PO, ER tab, q2hr (interval), Duration: 2 dose(s)',
        'base_med_ref': Meds.kcl_er_tab,
    },
    'KCL_LIQ_20MEQ_Q2H_2DOSES': {
        'mnemonic': Meds.kcl_liquid['MNEMONIC'],
        'order_sentence': '20 mEq, Feeding Tube, Liq, q2hr (interval), Duration: 2 dose(s)',
        'base_med_ref': Meds.kcl_liquid,
    },
    'KCL_IVPERIPH_10MEQ_Q1H_4DOSES_1HR': {
        'mnemonic': Meds.kcl_iv_peripheral['MNEMONIC'],
        'order_sentence': '10 mEq, IV, q1h, Duration: 4 dose(s), Infuse over: 1 hr',
        'base_med_ref': Meds.kcl_iv_peripheral,
    },
    'KCL_IVCENT_20MEQ_Q2H_2DOSES_2HR': {
        'mnemonic': Meds.kcl_iv_central['MNEMONIC'],
        'order_sentence': '20 mEq, IV, q2h, Duration: 2 dose(s), Infuse over: 2 hr',
        'base_med_ref': Meds.kcl_iv_central,
    },
    'KCL_ERTAB_20MEQ_Q2H_3DOSES': {
        'mnemonic': Meds.kcl_er_tab['MNEMONIC'],
        'order_sentence': '20 mEq, PO, ER tab, q2hr (interval), Duration: 3 dose(s)',
        'base_med_ref': Meds.kcl_er_tab,
    },
    'KCL_LIQ_20MEQ_Q2H_3DOSES': {
        'mnemonic': Meds.kcl_liquid['MNEMONIC'],
        'order_sentence': '20 mEq, Feeding Tube, Liq, q2hr (interval), Duration: 3 dose(s)',
        'base_med_ref': Meds.kcl_liquid,
    },
    'KCL_IVPERIPH_10MEQ_Q1H_6DOSES_1HR': {
        'mnemonic': Meds.kcl_iv_peripheral['MNEMONIC'],
        'order_sentence': '10 mEq, IV, q1h, Duration: 6 dose(s), Infuse over: 1 hr',
        'base_med_ref': Meds.kcl_iv_peripheral,
    },
    'KCL_IVCENT_20MEQ_Q2H_3DOSES_2HR': {
        'mnemonic': Meds.kcl_iv_central['MNEMONIC'],
        'order_sentence': '20 mEq, IV, q2h, Duration: 3 dose(s), Infuse over: 2 hr',
        'base_med_ref': Meds.kcl_iv_central,
    },
     'KCL_IVPERIPH_10MEQ_Q1H_8DOSES_1HR': {
        'mnemonic': Meds.kcl_iv_peripheral['MNEMONIC'],
        'order_sentence': '10 mEq, IV, q1h, Duration: 8 dose(s), Infuse over: 1 hr',
        'base_med_ref': Meds.kcl_iv_peripheral,
    },
    'KCL_IVCENT_20MEQ_Q2H_4DOSES_2HR': {
        'mnemonic': Meds.kcl_iv_central['MNEMONIC'],
        'order_sentence': '20 mEq, IV, q2h, Duration: 4 dose(s), Infuse over: 2 hr',
        'base_med_ref': Meds.kcl_iv_central,
    },
    'KCL_ERTAB_20MEQ_ONCE': { # Cardiac Only
        'mnemonic': Meds.kcl_er_tab['MNEMONIC'],
        'order_sentence': '20 mEq, PO, ER tab, Once',
        'base_med_ref': Meds.kcl_er_tab,
    },
    'KCL_LIQ_20MEQ_ONCE': { # Cardiac Only
        'mnemonic': Meds.kcl_liquid['MNEMONIC'],
        'order_sentence': '20 mEq, Feeding Tube, Liq, Once',
        'base_med_ref': Meds.kcl_liquid,
    },
    'KCL_IVPERIPH_10MEQ_Q1H_2DOSES_1HR': { # Cardiac Only
        'mnemonic': Meds.kcl_iv_peripheral['MNEMONIC'],
        'order_sentence': '10 mEq, IV, q1h, Duration: 2 dose(s), Infuse over: 1 hr',
        'base_med_ref': Meds.kcl_iv_peripheral,
    },
    'KCL_IVCENT_20MEQ_ONCE_1HR': { # Cardiac Only
        'mnemonic': Meds.kcl_iv_central['MNEMONIC'],
        'order_sentence': '20 mEq, IV, Once, Infuse over: 1 hr',
        'base_med_ref': Meds.kcl_iv_central,
    },
    'KCL_IVCENT_20MEQ_Q1H_2DOSES_1HR': { # Cardiac Only
        'mnemonic': Meds.kcl_iv_central['MNEMONIC'],
        'order_sentence': '20 mEq, IV, q1h, Duration: 2 dose(s), Infuse over: 1 hr',
        'base_med_ref': Meds.kcl_iv_central,
    },
    'KCL_IVCENT_20MEQ_Q1H_3DOSES_1HR': { # Cardiac Only
        'mnemonic': Meds.kcl_iv_central['MNEMONIC'],
        'order_sentence': '20 mEq, IV, q1h, Duration: 3 dose(s), Infuse over: 1 hr',
        'base_med_ref': Meds.kcl_iv_central,
    },
    'KCL_IVCENT_20MEQ_Q1H_4DOSES_1HR': { # Cardiac Only
        'mnemonic': Meds.kcl_iv_central['MNEMONIC'],
        'order_sentence': '20 mEq, IV, q1h, Duration: 4 dose(s), Infuse over: 1 hr',
        'base_med_ref': Meds.kcl_iv_central,
    },

    # Phosphate Orders
    'KPHOSNEUT_TAB_2TABS_Q2H_2DOSES': {
        'mnemonic': Meds.k_phos_neutral_tab['MNEMONIC'],
        'order_sentence': '2 tab(s), PO, Tab, q2hr (interval), Duration: 2 dose(s)',
        'base_med_ref': Meds.k_phos_neutral_tab,
    },
    'NAPHOS_IV_15MMOL_ONCE': {
        'mnemonic': Meds.na_phosphate_iv['MNEMONIC'],
        'order_sentence': '15 mmol, IVPB, Inj, Once',
        'base_med_ref': Meds.na_phosphate_iv,
    },
    'KPHOSNEUT_TAB_2TABS_Q2H_3DOSES': {
        'mnemonic': Meds.k_phos_neutral_tab['MNEMONIC'],
        'order_sentence': '2 tab(s), PO, Tab, q2hr (interval), Duration: 3 dose(s)',
        'base_med_ref': Meds.k_phos_neutral_tab,
    },
    'NAPHOS_IV_15MMOL_Q4H_2DOSES': {
        'mnemonic': Meds.na_phosphate_iv['MNEMONIC'],
        'order_sentence': '15 mmol, IVPB, Inj, q4hr (interval), Duration: 2 dose(s)',
        'base_med_ref': Meds.na_phosphate_iv,
    },

    # Calcium Orders (Cardiac Only)
    'CALCIUMCHL_IV_1G_ONCE_1HR': {
        'mnemonic': Meds.calcium_chloride_iv['MNEMONIC'],
        'order_sentence': '1 g, IVPB, Inj, Once, Infuse over: 1 hr',
        'base_med_ref': Meds.calcium_chloride_iv,
    },
} 