[1m============================= test session starts ==============================[0m
platform linux -- Python 3.12.3, pytest-8.3.5, pluggy-1.5.0 -- /home/pessk/code/ea-python/.venv/bin/python
cachedir: .pytest_cache
rootdir: /home/pessk/code/ea-python
plugins: sugar-1.0.0
[1mcollecting ... [0mcollected 33 items

tests/test_dcw_sentences.py::test_dcw_sentences_match_generated[/home/pessk/code/ea-python/generated_configs/output_cardiac.json] [31mFAILED[0m[31m [  3%][0m
tests/test_dcw_sentences.py::test_dcw_sentences_match_generated[/home/pessk/code/ea-python/generated_configs/output_regular.json] [31mFAILED[0m[31m [  6%][0m
tests/test_expected_sentences.py::test_expected_sentences_match_generated[/home/pessk/code/ea-python/generated_configs/output_cardiac.json] [31mFAILED[0m[31m [  9%][0m
tests/test_expected_sentences.py::test_expected_sentences_match_generated[/home/pessk/code/ea-python/generated_configs/output_regular.json] [31mFAILED[0m[31m [ 12%][0m
tests/test_generated_output.py::test_top_level_structure[regular_config] [32mPASSED[0m[31m [ 15%][0m
tests/test_generated_output.py::test_top_level_structure[cardiac_config] [32mPASSED[0m[31m [ 18%][0m
tests/test_generated_output.py::test_rconfig_structure[regular_config] [32mPASSED[0m[31m [ 21%][0m
tests/test_generated_output.py::test_rconfig_structure[cardiac_config] [32mPASSED[0m[31m [ 24%][0m
tests/test_generated_output.py::test_tab_structure[regular_config] [32mPASSED[0m[31m [ 27%][0m
tests/test_generated_output.py::test_tab_structure[cardiac_config] [32mPASSED[0m[31m [ 30%][0m
tests/test_generated_output.py::test_order_basic_fields[regular_config] [32mPASSED[0m[31m [ 33%][0m
tests/test_generated_output.py::test_order_basic_fields[cardiac_config] [32mPASSED[0m[31m [ 36%][0m
tests/test_generated_output.py::test_lab_sentence_format[regular_config] [32mPASSED[0m[31m [ 39%][0m
tests/test_generated_output.py::test_lab_sentence_format[cardiac_config] [32mPASSED[0m[31m [ 42%][0m
tests/test_generated_output.py::test_med_sentence_start_format[regular_config] [32mPASSED[0m[31m [ 45%][0m
tests/test_generated_output.py::test_med_sentence_start_format[cardiac_config] [32mPASSED[0m[31m [ 48%][0m
tests/test_generated_output.py::test_med_sentence_frequency_format[regular_config] [32mPASSED[0m[31m [ 51%][0m
tests/test_generated_output.py::test_med_sentence_frequency_format[cardiac_config] [32mPASSED[0m[31m [ 54%][0m
tests/test_generated_output.py::test_med_sentence_infuse_over_format[regular_config] [32mPASSED[0m[31m [ 57%][0m
tests/test_generated_output.py::test_med_sentence_infuse_over_format[cardiac_config] [32mPASSED[0m[31m [ 60%][0m
python/formatting.py::python.formatting.format_level_for_concept [32mPASSED[0m[31m  [ 63%][0m
python/formatting.py::python.formatting.format_level_for_display [32mPASSED[0m[31m  [ 66%][0m
python/lab_orders.py::python.lab_orders.create_specific_timed_lab [32mPASSED[0m[31m [ 69%][0m
python/lab_orders.py::python.lab_orders.get_timed_lab [32mPASSED[0m[31m             [ 72%][0m
python/naming.py::python.naming.create_between_concept [32mPASSED[0m[31m            [ 75%][0m
python/naming.py::python.naming.create_between_section_name [32mPASSED[0m[31m       [ 78%][0m
python/naming.py::python.naming.create_less_than_concept [32mPASSED[0m[31m          [ 81%][0m
python/naming.py::python.naming.create_less_than_section_name [32mPASSED[0m[31m     [ 84%][0m
python/naming.py::python.naming.get_concept_name [32mPASSED[0m[31m                  [ 87%][0m
python/order_builder.py::python.order_builder.create_lab_order [32mPASSED[0m[31m    [ 90%][0m
python/tab_builder.py::python.tab_builder._create_graphed_results [32mPASSED[0m[31m [ 93%][0m
python/tab_builder.py::python.tab_builder._create_mnemonic [32mPASSED[0m[31m        [ 96%][0m
python/text.py::python.text.create_notify_provider_text [32mPASSED[0m[31m           [100%][0m

=================================== FAILURES ===================================
[31m[1m_ test_dcw_sentences_match_generated[/home/pessk/code/ea-python/generated_configs/output_cardiac.json] _[0m

config_file_path = '/home/pessk/code/ea-python/generated_configs/output_cardiac.json'
dcw_data = [{'Electrolyte': 'Magnesium', 'Instructions/Note': 'Recheck BMP and magnesium level with next AM labs.', 'Lab Value Ra... Range': 'Current serum level 3.2-3.4', 'Mnemonic': 'potassium chloride 10 mEq/100 mL intravenous solution', ...}, ...]

    @pytest.mark.parametrize("config_file_path", get_generated_config_paths())
    def test_dcw_sentences_match_generated(config_file_path, dcw_data):
        """
        Compares sentences from DCW against generated JSON using fuzzy matching.
        Generates a report showing the comparison and score for each DCW entry.
        """
        try:
            with open(config_file_path, 'r', encoding='utf-8') as f:
                loaded_json_config = json.load(f)
        except Exception as e:
            pytest.fail(f"Failed to load or parse JSON from {config_file_path}: {e}")
    
        protocol = get_protocol_from_filename(config_file_path)
        assert protocol, f"Could not determine protocol from filename: {config_file_path}"
    
        protocol_dcw_entries = [e for e in dcw_data if e.get('Protocol') == protocol]
        if not protocol_dcw_entries:
            print(f"Warning: No DCW entries found for protocol: {protocol}. Skipping verification.")
            return
    
        comparison_report_lines = []
        processing_errors = []
    
        for index, dcw_entry in enumerate(protocol_dcw_entries):
            dcw_electrolyte = dcw_entry.get('Electrolyte')
            dcw_mnemonic_raw = dcw_entry.get('Mnemonic') # Get raw mnemonic
            dcw_range = dcw_entry.get('Lab Value Range') # Keep for context
            dcw_sentence = dcw_entry.get('Order_Sentence')
    
            # Clean the DCW mnemonic - remove parentheses and content within
            dcw_mnemonic_cleaned = re.sub(r'\s*\(.*?\)\s*$', '', dcw_mnemonic_raw).strip() if dcw_mnemonic_raw else None
    
            if not all([protocol, dcw_electrolyte, dcw_mnemonic_cleaned, dcw_sentence]): # Use cleaned mnemonic for check
                # Optionally log skipping due to missing cleaned mnemonic
                # print(f"Skipping DCW entry {index}: Missing required data after cleaning mnemonic.")
                continue
    
            # --- Find JSON Counterpart (by cleaned mnemonic within the correct tab) ---
            json_sentence_found = None
            try:
                tabs = loaded_json_config.get('RCONFIG', {}).get('TABS', [])
                target_tab = next((
                    t for t in tabs
                    if t.get('TAB_KEY') and dcw_electrolyte and (
                        # Standard check
                        (t.get('TAB_KEY').upper() == dcw_electrolyte.upper()) or
                        # Specific mapping for Phosphorus -> PHOSPHATE
                        (dcw_electrolyte.upper() == 'PHOSPHORUS' and t.get('TAB_KEY').upper() == 'PHOSPHATE')
                       )
                ), None)
    
                if target_tab:
                    order_sections = target_tab.get('ORDER_SECTIONS', [])
                    found_match_for_dcw_entry = False # Flag to ensure we find a matching section/order
                    for section in order_sections:
                        section_name = section.get('SECTION_NAME', '')
    
                        # Use the refactored ranges_match function
                        is_range_match = ranges_match(dcw_range, section_name)
    
                        if is_range_match:
                             orders_in_section = section.get('ORDERS', [])
                             for order in orders_in_section:
                                 # Compare JSON mnemonic with the CLEANED DCW mnemonic
                                 if order.get('MNEMONIC') == dcw_mnemonic_cleaned:
                                     json_sentence_found = order.get('ORDER_SENTENCE')
                                     found_match_for_dcw_entry = True # Mark as found
                                     break # Found the correct order in the matching section
                             if found_match_for_dcw_entry:
                                 break # Exit section loop once match is found
    
                    # If no match was found after checking all sections, json_sentence_found remains None
                    if not found_match_for_dcw_entry:
                        json_sentence_found = None # Ensure it's None if no suitable section/order found
    
            except Exception as e:
                processing_errors.append(f"Error finding JSON counterpart for DCW entry {index}: {e}")
                continue
    
            # --- Fuzzy Compare DCW vs JSON --- (Uses json_sentence_found)
            comparison_score = 0
            if json_sentence_found:
                # Compare the original DCW sentence with the found JSON sentence
                comparison_score = fuzz.token_sort_ratio(dcw_sentence, json_sentence_found)
            # else: json_sentence_found remains None
    
            # --- Compile Report Line --- (Show original DCW mnemonic for context)
            report_line = f'''
    --- DCW Entry #{index} (Mnem: '{dcw_mnemonic_raw}', Range: '{dcw_range}') ---
      DCW Spec : {repr(dcw_sentence)}
      JSON Gen : {repr(json_sentence_found) if json_sentence_found else '*** NOT FOUND in JSON Tab ***'}
      (Score DCW vs JSON: {comparison_score}%)'''
            comparison_report_lines.append(report_line)
    
        # --- Final Assertion ---
        final_output_message = ""
        if comparison_report_lines:
            final_output_message += f"\nDCW vs JSON Sentence Comparison Report for {os.path.basename(config_file_path)}:\n"
            final_output_message += "\n".join(comparison_report_lines)
        if processing_errors:
             final_output_message += f"\n\nErrors encountered during processing for {os.path.basename(config_file_path)}:\n"
             final_output_message += "\n".join(processing_errors)
    
        # Fail if there's anything in the report to ensure it's always printed
>       assert not final_output_message, final_output_message
[1m[31mE       AssertionError: [0m
[1m[31mE         DCW vs JSON Sentence Comparison Report for output_cardiac.json:[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #0 (Mnem: 'magnesium sulfate', Range: 'Current serum level 1.8-2') ---[0m
[1m[31mE           DCW Spec : '1 g, IVPB, Premix, Once, Infuse over: 1 hr'[0m
[1m[31mE           JSON Gen : '1 g, IVPB, Premix, Once, Infuse over: 1 hr'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #1 (Mnem: 'magnesium sulfate', Range: 'Current serum level 1.4-1.7') ---[0m
[1m[31mE           DCW Spec : '2 g, IVPB, Premix, Once, Infuse over: 2 hr'[0m
[1m[31mE           JSON Gen : '2 g, IVPB, Premix, Once, Infuse over: 2 hr'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #2 (Mnem: 'magnesium sulfate', Range: 'Current serum level < 1.4') ---[0m
[1m[31mE           DCW Spec : '2 g, IVPB, Premix, q2hr (interval), Duration: 2 dose(s), Infuse over: 2 hr'[0m
[1m[31mE           JSON Gen : '2 g, IVPB, Premix, q2hr (interval), Duration: 2 dose(s), Infuse over: 2 hr'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #3 (Mnem: 'potassium chloride extended release', Range: 'Current serum level 3.6-3.9') ---[0m
[1m[31mE           DCW Spec : '20 mEq, PO, ER tab, Once'[0m
[1m[31mE           JSON Gen : '20 mEq, PO, ER tab, Once'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #4 (Mnem: 'potassium chloride', Range: 'Current serum level 3.6-3.9') ---[0m
[1m[31mE           DCW Spec : '20 mEq, Feeding Tube, Liq, Once'[0m
[1m[31mE           JSON Gen : '20 mEq, Feeding Tube, Liq, Once'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #5 (Mnem: 'potassium chloride 10 mEq/100 mL intravenous solution', Range: 'Current serum level 3.6-3.9') ---[0m
[1m[31mE           DCW Spec : '10 mEq, IV, q1hr, Duration: 2 dose(s), Infuse over: 1 hr'[0m
[1m[31mE           JSON Gen : '10 mEq, IV, q1hr, Duration: 2 dose(s), Infuse over: 1 hr'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #6 (Mnem: 'potassium chloride 20 mEq/100 mL intravenous solution', Range: 'Current serum level 3.6-3.9') ---[0m
[1m[31mE           DCW Spec : '20 mEq, IV, Once, Infuse over: 1 hr'[0m
[1m[31mE           JSON Gen : '20 mEq, IV, Once, Infuse over: 1 hr'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #7 (Mnem: 'potassium chloride extended release', Range: 'Current serum level 3.2-3.5') ---[0m
[1m[31mE           DCW Spec : '20 mEq, PO, ER tab, q2hr (interval), Duration: 2 dose(s)'[0m
[1m[31mE           JSON Gen : '20 mEq, PO, ER tab, q2hr (interval), Duration: 2 dose(s)'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #8 (Mnem: 'potassium chloride', Range: 'Current serum level 3.2-3.5') ---[0m
[1m[31mE           DCW Spec : '20 mEq, Feeding Tube, Liq, q2hr (interval), Duration: 2 dose(s)'[0m
[1m[31mE           JSON Gen : '20 mEq, Feeding Tube, Liq, q2hr (interval), Duration: 2 dose(s)'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #9 (Mnem: 'potassium chloride 10 mEq/100 mL intravenous solution', Range: 'Current serum level 3.2-3.5') ---[0m
[1m[31mE           DCW Spec : '10 mEq, IV, q1hr, Duration: 4 dose(s), Infuse over: 1 hr'[0m
[1m[31mE           JSON Gen : '10 mEq, IV, q1hr, Duration: 4 dose(s), Infuse over: 1 hr'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #10 (Mnem: 'potassium chloride 20 mEq/100 mL intravenous solution', Range: 'Current serum level 3.2-3.5') ---[0m
[1m[31mE           DCW Spec : '20 mEq, IV, q1hr, Duration: 2 dose(s), Infuse over: 1 hr'[0m
[1m[31mE           JSON Gen : '20 mEq, IV, q1hr, Duration: 2 dose(s), Infuse over: 1 hr'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #11 (Mnem: 'potassium chloride extended release', Range: 'Current serum level 2.8-3.1') ---[0m
[1m[31mE           DCW Spec : '20 mEq, PO, ER tab, q2hr (interval), Duration: 3 dose(s)'[0m
[1m[31mE           JSON Gen : '20 mEq, PO, ER tab, q2hr (interval), Duration: 3 dose(s)'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #12 (Mnem: 'potassium chloride', Range: 'Current serum level 2.8-3.1') ---[0m
[1m[31mE           DCW Spec : '20 mEq, Feeding Tube, Liq, q2hr (interval), Duration: 3 dose(s)'[0m
[1m[31mE           JSON Gen : '20 mEq, Feeding Tube, Liq, q2hr (interval), Duration: 3 dose(s)'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #13 (Mnem: 'potassium chloride 10 mEq/100 mL intravenous solution', Range: 'Current serum level 2.8-3.1') ---[0m
[1m[31mE           DCW Spec : '10 mEq, IV, q1hr, Duration: 6 dose(s), Infuse over: 1 hr'[0m
[1m[31mE           JSON Gen : '10 mEq, IV, q1hr, Duration: 6 dose(s), Infuse over: 1 hr'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #14 (Mnem: 'potassium chloride 20 mEq/100 mL intravenous solution', Range: 'Current serum level 2.8-3.1') ---[0m
[1m[31mE           DCW Spec : '20 mEq, IV, q1hr, Duration: 3 dose(s), Infuse over: 1 hr'[0m
[1m[31mE           JSON Gen : '20 mEq, IV, q1hr, Duration: 3 dose(s), Infuse over: 1 hr'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #15 (Mnem: 'potassium chloride 10 mEq/100 mL intravenous solution', Range: 'Current serum level < 2.8') ---[0m
[1m[31mE           DCW Spec : '10 mEq, IV, q1hr, Duration: 8 dose(s), Infuse over: 1 hr'[0m
[1m[31mE           JSON Gen : '10 mEq, IV, q1hr, Duration: 8 dose(s), Infuse over: 1 hr'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #16 (Mnem: 'potassium chloride 20 mEq/100 mL intravenous solution', Range: 'Current serum level < 2.8') ---[0m
[1m[31mE           DCW Spec : '20 mEq, IV, q1hr, Duration: 4 dose(s), Infuse over: 1 hr'[0m
[1m[31mE           JSON Gen : '20 mEq, IV, q1hr, Duration: 4 dose(s), Infuse over: 1 hr'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #17 (Mnem: 'K-Phos Neutral (brand name synonym under primary potassium phosphate-sodium phosphate)', Range: 'Current serum level 1.6-2.0') ---[0m
[1m[31mE           DCW Spec : '2 tab(s), PO, Tab, q2hr (interval), Duration: 2 dose(s)'[0m
[1m[31mE           JSON Gen : '2 tab(s), PO, Tab, q2hr (interval), Duration: 2 dose(s)'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #18 (Mnem: 'sodium phosphate', Range: 'Current serum level 1.6-2.0') ---[0m
[1m[31mE           DCW Spec : '15 mmol, IVPB, Inj, Once'[0m
[1m[31mE           JSON Gen : '15 mmol, IVPB, Inj, Once'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #19 (Mnem: 'K-Phos Neutral', Range: 'Current serum level 1.0-1.5') ---[0m
[1m[31mE           DCW Spec : '2 tab(s), PO, Tab, q2hr (interval), Duration: 3 dose(s)'[0m
[1m[31mE           JSON Gen : '2 tab(s), PO, Tab, q2hr (interval), Duration: 3 dose(s)'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #20 (Mnem: 'sodium phosphate', Range: 'Current serum level 1.0-1.5') ---[0m
[1m[31mE           DCW Spec : '15 mmol, IVPB, Inj, q4hr (interval), Duration: 2 dose(s)'[0m
[1m[31mE           JSON Gen : '15 mmol, IVPB, Inj, q4hr (interval), Duration: 2 dose(s)'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #21 (Mnem: 'sodium phosphate', Range: 'Current serum level <1.0') ---[0m
[1m[31mE           DCW Spec : '15 mmol, IVPB, Inj, q4hr (interval), Duration: 2 dose(s)'[0m
[1m[31mE           JSON Gen : '15 mmol, IVPB, Inj, q4hr (interval), Duration: 2 dose(s)'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #22 (Mnem: 'calcium chloride', Range: 'iCal < 1.1') ---[0m
[1m[31mE           DCW Spec : '1 g, IVPB, Inj, Once, Infuse over: 1 hr'[0m
[1m[31mE           JSON Gen : '1 g, IVPB, Inj, Once, Infuse over: 1 hr'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE       assert not "\nDCW vs JSON Sentence Comparison Report for output_cardiac.json:\n\n--- DCW Entry #0 (Mnem: 'magnesium sulfate', Range: 'Current serum level 1.8-2') ---\n  DCW Spec : '1 g, IVPB, Premix, Once, Infuse over: 1 hr'\n  JSON Gen : '1 g, IVPB, Premix, Once, Infuse over: 1 hr'\n  (Score DCW vs JSON: 100%)\n\n--- DCW Entry #1 (Mnem: 'magnesium sulfate', Range: 'Current serum level 1.4-1.7') ---\n  DCW Spec : '2 g, IVPB, Premix, Once, Infuse over: 2 hr'\n  JSON Gen : '2 g, IVPB, Premix, Once, Infuse over: 2 hr'\n  (Score DCW vs JSON: 100%)\n\n--- DCW Entry #2 (Mnem: 'magnesium sulfate', Range: 'Current serum level < 1.4') ---\n  DCW Spec : '2 g, IVPB, Premix, q2hr (interval), Duration: 2 dose(s), Infuse over: 2 hr'\n  JSON Gen : '2 g, IVPB, Premix, q2hr (interval), Duration: 2 dose(s), Infuse over: 2 hr'\n  (Score DCW vs JSON: 100%)\n\n--- DCW Entry #3 (Mnem: 'potassium chloride extended release', Range: 'Current serum level 3.6-3.9') ---\n  DCW Spec : '20 mEq, PO, ER tab, Once'\n  JSON Gen : '20 mEq, PO, ER tab, Once'\n  (Score DCW vs JSON: 100%)\n\n--- DCW Entry #4 (Mnem: 'potassium chloride', Range: 'Current serum level 3.6-3.9') ---\n  DCW Spec : '20 mEq, Feeding Tube, Liq, Once'\n ...-- DCW Entry #18 (Mnem: 'sodium phosphate', Range: 'Current serum level 1.6-2.0') ---\n  DCW Spec : '15 mmol, IVPB, Inj, Once'\n  JSON Gen : '15 mmol, IVPB, Inj, Once'\n  (Score DCW vs JSON: 100%)\n\n--- DCW Entry #19 (Mnem: 'K-Phos Neutral', Range: 'Current serum level 1.0-1.5') ---\n  DCW Spec : '2 tab(s), PO, Tab, q2hr (interval), Duration: 3 dose(s)'\n  JSON Gen : '2 tab(s), PO, Tab, q2hr (interval), Duration: 3 dose(s)'\n  (Score DCW vs JSON: 100%)\n\n--- DCW Entry #20 (Mnem: 'sodium phosphate', Range: 'Current serum level 1.0-1.5') ---\n  DCW Spec : '15 mmol, IVPB, Inj, q4hr (interval), Duration: 2 dose(s)'\n  JSON Gen : '15 mmol, IVPB, Inj, q4hr (interval), Duration: 2 dose(s)'\n  (Score DCW vs JSON: 100%)\n\n--- DCW Entry #21 (Mnem: 'sodium phosphate', Range: 'Current serum level <1.0') ---\n  DCW Spec : '15 mmol, IVPB, Inj, q4hr (interval), Duration: 2 dose(s)'\n  JSON Gen : '15 mmol, IVPB, Inj, q4hr (interval), Duration: 2 dose(s)'\n  (Score DCW vs JSON: 100%)\n\n--- DCW Entry #22 (Mnem: 'calcium chloride', Range: 'iCal < 1.1') ---\n  DCW Spec : '1 g, IVPB, Inj, Once, Infuse over: 1 hr'\n  JSON Gen : '1 g, IVPB, Inj, Once, Infuse over: 1 hr'\n  (Score DCW vs JSON: 100%)"[0m

comparison_report_lines = ["\n--- DCW Entry #0 (Mnem: 'magnesium sulfate', Range: 'Current serum level 1.8-2') ---\n  DCW Spec : '1 g, IVPB, Pre...ver: 1 hr'\n  JSON Gen : '10 mEq, IV, q1hr, Duration: 2 dose(s), Infuse over: 1 hr'\n  (Score DCW vs JSON: 100%)", ...]
comparison_score = 100
config_file_path = '/home/pessk/code/ea-python/generated_configs/output_cardiac.json'
dcw_data   = [{'Electrolyte': 'Magnesium', 'Instructions/Note': 'Recheck BMP and magnesium level with next AM labs.', 'Lab Value Ra... Range': 'Current serum level 3.2-3.4', 'Mnemonic': 'potassium chloride 10 mEq/100 mL intravenous solution', ...}, ...]
dcw_electrolyte = 'Calcium'
dcw_entry  = {'Electrolyte': 'Calcium', 'Instructions/Note': 'Notify provider.                                                     ...                Recheck iCal with next AM labs.', 'Lab Value Range': 'iCal < 1.1', 'Mnemonic': 'calcium chloride', ...}
dcw_mnemonic_cleaned = 'calcium chloride'
dcw_mnemonic_raw = 'calcium chloride'
dcw_range  = 'iCal < 1.1'
dcw_sentence = '1 g, IVPB, Inj, Once, Infuse over: 1 hr'
f          = <_io.TextIOWrapper name='/home/pessk/code/ea-python/generated_configs/output_cardiac.json' mode='r' encoding='utf-8'>
final_output_message = "\nDCW vs JSON Sentence Comparison Report for output_cardiac.json:\n\n--- DCW Entry #0 (Mnem: 'magnesium sulfate', Ran...PB, Inj, Once, Infuse over: 1 hr'\n  JSON Gen : '1 g, IVPB, Inj, Once, Infuse over: 1 hr'\n  (Score DCW vs JSON: 100%)"
found_match_for_dcw_entry = True
index      = 22
is_range_match = True
json_sentence_found = '1 g, IVPB, Inj, Once, Infuse over: 1 hr'
loaded_json_config = {'RCONFIG': {'CCL_POSTPROCESS': 'UHS_MPG_GET_TABBED_ADVISOR', 'JSON_RETURN': '', 'TABS': [{'CANCEL_BUTTON': {}, 'CONCE...rder)', 'TOOLTIP': 'Room type: Critical Care, PCU, Telemetry, MS (Med/Surg) with Telemetry Monitoring order'}], ...}]}}
order      = {'ASC_SHORT_DESCRIPTION': '', 'COMMENT': 'Intravenous', 'MNEMONIC': 'calcium chloride', 'ORDER_SENTENCE': '1 g, IVPB, Inj, Once, Infuse over: 1 hr'}
order_sections = [{'CONCEPT_NAME': '[%{EALABCALCIUMTODO}.COUNT > 0 AND {EALABCALCIUMLT11}%]', 'ORDERS': [{'ASC_SHORT_DESCRIPTION': '', ...1;0400, Blood, Tomorrow AM collect, Once'}], 'SECTION_NAME': 'Calcium Lab Orders', 'SHOW_INACTIVE_DUPLICATES': 0, ...}]
orders_in_section = [{'ASC_SHORT_DESCRIPTION': '', 'COMMENT': 'Intravenous', 'MNEMONIC': 'calcium chloride', 'ORDER_SENTENCE': '1 g, IVPB, Inj, Once, Infuse over: 1 hr'}]
processing_errors = []
protocol   = 'Cardiac'
protocol_dcw_entries = [{'Electrolyte': 'Magnesium', 'Instructions/Note': 'Recheck magnesium level with next AM labs', 'Lab Value Range': 'Cu... Range': 'Current serum level 3.6-3.9', 'Mnemonic': 'potassium chloride 10 mEq/100 mL intravenous solution', ...}, ...]
report_line = "\n--- DCW Entry #22 (Mnem: 'calcium chloride', Range: 'iCal < 1.1') ---\n  DCW Spec : '1 g, IVPB, Inj, Once, Infuse over: 1 hr'\n  JSON Gen : '1 g, IVPB, Inj, Once, Infuse over: 1 hr'\n  (Score DCW vs JSON: 100%)"
section    = {'CONCEPT_NAME': '[%{EALABCALCIUMTODO}.COUNT > 0 AND {EALABCALCIUMLT11}%]', 'ORDERS': [{'ASC_SHORT_DESCRIPTION': '', '...ht: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>', 'SHOW_INACTIVE_DUPLICATES': 0, ...}
section_name = 'Ionized Calcium: < 1.1 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>'
tabs       = [{'CANCEL_BUTTON': {}, 'CONCEPTS': [], 'CONCEPT_FOR_DISMISS': 'EALABMAGTODO', 'CRITERIA': [{'CONCEPT_NAME': '[%true%]'... order)', 'TOOLTIP': 'Room type: Critical Care, PCU, Telemetry, MS (Med/Surg) with Telemetry Monitoring order'}], ...}]
target_tab = {'CANCEL_BUTTON': {}, 'CONCEPTS': [], 'CONCEPT_FOR_DISMISS': 'EALABCALCIUMTODO', 'CRITERIA': [{'CONCEPT_NAME': '[%true...g order)', 'TOOLTIP': 'Room type: Critical Care, PCU, Telemetry, MS (Med/Surg) with Telemetry Monitoring order'}], ...}

[1m[31mtests/test_dcw_sentences.py[0m:280: AssertionError
----------------------------- Captured stdout call -----------------------------

DEBUG ranges_match: Comparing DCW='Current serum level 1.8-2' (Parsed: 1.8-2.0) vs JSON_Section='Magnesium: 1.8 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>' (Parsed: 1.8-2.0)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level 1.4-1.7' (Parsed: 1.4-1.7) vs JSON_Section='Magnesium: 1.8 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>' (Parsed: 1.8-2.0)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 1.4-1.7' (Parsed: 1.4-1.7) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br><small style="font-weight: normal;">Monitoring: Recheck BMP and magnesium level with next AM labs.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 1.4-1.7' (Parsed: 1.4-1.7) vs JSON_Section='Magnesium: 1.4 - 1.7 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>' (Parsed: 1.4-1.7)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level < 1.4' (Parsed: None-1.4) vs JSON_Section='Magnesium: 1.8 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>' (Parsed: 1.8-2.0)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 1.4' (Parsed: None-1.4) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br><small style="font-weight: normal;">Monitoring: Recheck BMP and magnesium level with next AM labs.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 1.4' (Parsed: None-1.4) vs JSON_Section='Magnesium: 1.4 - 1.7 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>' (Parsed: 1.4-1.7)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 1.4' (Parsed: None-1.4) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br><small style="font-weight: normal;">Monitoring: Recheck magnesium level 4 hrs after infusion complete.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 1.4' (Parsed: None-1.4) vs JSON_Section='Magnesium: < 1.4 mg/dL<br><span style="color: red; font-weight: bold; font-size: 14px;">NOTIFY PHYSICIAN if less than 1.2 mg/dL</span><br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>' (Parsed: None-1.4)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level 3.6-3.9' (Parsed: 3.6-3.9) vs JSON_Section='Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 3.6-3.9)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level 3.6-3.9' (Parsed: 3.6-3.9) vs JSON_Section='Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 3.6-3.9)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level 3.6-3.9' (Parsed: 3.6-3.9) vs JSON_Section='Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 3.6-3.9)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level 3.6-3.9' (Parsed: 3.6-3.9) vs JSON_Section='Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 3.6-3.9)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level 3.2-3.5' (Parsed: 3.2-3.5) vs JSON_Section='Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 3.6-3.9)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 3.2-3.5' (Parsed: 3.2-3.5) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br>IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck BMP with next AM labs.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 3.2-3.5' (Parsed: 3.2-3.5) vs JSON_Section='Potassium: 3.2 - 3.5 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 3.2-3.5)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level 3.2-3.5' (Parsed: 3.2-3.5) vs JSON_Section='Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 3.6-3.9)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 3.2-3.5' (Parsed: 3.2-3.5) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br>IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck BMP with next AM labs.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 3.2-3.5' (Parsed: 3.2-3.5) vs JSON_Section='Potassium: 3.2 - 3.5 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 3.2-3.5)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level 3.2-3.5' (Parsed: 3.2-3.5) vs JSON_Section='Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 3.6-3.9)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 3.2-3.5' (Parsed: 3.2-3.5) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br>IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck BMP with next AM labs.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 3.2-3.5' (Parsed: 3.2-3.5) vs JSON_Section='Potassium: 3.2 - 3.5 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 3.2-3.5)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level 3.2-3.5' (Parsed: 3.2-3.5) vs JSON_Section='Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 3.6-3.9)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 3.2-3.5' (Parsed: 3.2-3.5) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br>IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck BMP with next AM labs.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 3.2-3.5' (Parsed: 3.2-3.5) vs JSON_Section='Potassium: 3.2 - 3.5 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 3.2-3.5)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 3.6-3.9)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br>IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck BMP with next AM labs.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='Potassium: 3.2 - 3.5 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 3.2-3.5)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br>ORAL - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck potassium level 4 hours after last dose.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='PERIPHERAL IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck potassium level 1 hr after infusion complete.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='CENTRAL IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck potassium level 1 hr after infusion complete.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='Potassium: 2.8 - 3.1 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>' (Parsed: 2.8-3.1)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 3.6-3.9)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br>IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck BMP with next AM labs.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='Potassium: 3.2 - 3.5 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 3.2-3.5)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br>ORAL - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck potassium level 4 hours after last dose.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='PERIPHERAL IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck potassium level 1 hr after infusion complete.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='CENTRAL IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck potassium level 1 hr after infusion complete.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='Potassium: 2.8 - 3.1 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>' (Parsed: 2.8-3.1)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 3.6-3.9)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br>IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck BMP with next AM labs.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='Potassium: 3.2 - 3.5 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 3.2-3.5)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br>ORAL - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck potassium level 4 hours after last dose.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='PERIPHERAL IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck potassium level 1 hr after infusion complete.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='CENTRAL IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck potassium level 1 hr after infusion complete.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='Potassium: 2.8 - 3.1 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>' (Parsed: 2.8-3.1)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 3.6-3.9)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br>IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck BMP with next AM labs.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='Potassium: 3.2 - 3.5 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 3.2-3.5)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br>ORAL - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck potassium level 4 hours after last dose.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='PERIPHERAL IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck potassium level 1 hr after infusion complete.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='CENTRAL IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck potassium level 1 hr after infusion complete.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='Potassium: 2.8 - 3.1 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>' (Parsed: 2.8-3.1)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-2.8) vs JSON_Section='Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 3.6-3.9)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-2.8) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br>IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck BMP with next AM labs.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-2.8) vs JSON_Section='Potassium: 3.2 - 3.5 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 3.2-3.5)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-2.8) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br>ORAL - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck potassium level 4 hours after last dose.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-2.8) vs JSON_Section='PERIPHERAL IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck potassium level 1 hr after infusion complete.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-2.8) vs JSON_Section='CENTRAL IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck potassium level 1 hr after infusion complete.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-2.8) vs JSON_Section='Potassium: 2.8 - 3.1 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>' (Parsed: 2.8-3.1)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-2.8) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br>ORAL - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck potassium level 4 hrs after last dose.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-2.8) vs JSON_Section='PERIPHERAL IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck potassium level 1 hr after infusion complete.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-2.8) vs JSON_Section='CENTRAL IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck potassium level 1 hr after infusion complete.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-2.8) vs JSON_Section='Potassium: < 2.8 mmol/L<br><span style="color: red; font-weight: bold; font-size: 14px;">NOTIFY PHYSICIAN</span><br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>' (Parsed: None-2.8)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-2.8) vs JSON_Section='Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 3.6-3.9)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-2.8) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br>IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck BMP with next AM labs.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-2.8) vs JSON_Section='Potassium: 3.2 - 3.5 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 3.2-3.5)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-2.8) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br>ORAL - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck potassium level 4 hours after last dose.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-2.8) vs JSON_Section='PERIPHERAL IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck potassium level 1 hr after infusion complete.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-2.8) vs JSON_Section='CENTRAL IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck potassium level 1 hr after infusion complete.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-2.8) vs JSON_Section='Potassium: 2.8 - 3.1 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>' (Parsed: 2.8-3.1)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-2.8) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br>ORAL - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck potassium level 4 hrs after last dose.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-2.8) vs JSON_Section='PERIPHERAL IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck potassium level 1 hr after infusion complete.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-2.8) vs JSON_Section='CENTRAL IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck potassium level 1 hr after infusion complete.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-2.8) vs JSON_Section='Potassium: < 2.8 mmol/L<br><span style="color: red; font-weight: bold; font-size: 14px;">NOTIFY PHYSICIAN</span><br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>' (Parsed: None-2.8)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level 1.6-2.0' (Parsed: 1.6-2.0) vs JSON_Section='Phosphorus: 1.6 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 1.6-2.0)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level 1.6-2.0' (Parsed: 1.6-2.0) vs JSON_Section='Phosphorus: 1.6 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 1.6-2.0)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level 1.0-1.5' (Parsed: 1.0-1.5) vs JSON_Section='Phosphorus: 1.6 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 1.6-2.0)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 1.0-1.5' (Parsed: 1.0-1.5) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br><small style="font-weight: normal;">Monitoring: Recheck phosphorous & calcium levels with next AM labs.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 1.0-1.5' (Parsed: 1.0-1.5) vs JSON_Section='Phosphorus: 1.0 - 1.5 mg/dL<br><span style="color: red; font-weight: bold; font-size: 14px;">NOTIFY PHYSICIAN if less than 1.1 mg/dL</span><br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 1.0-1.5)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level 1.0-1.5' (Parsed: 1.0-1.5) vs JSON_Section='Phosphorus: 1.6 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 1.6-2.0)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 1.0-1.5' (Parsed: 1.0-1.5) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br><small style="font-weight: normal;">Monitoring: Recheck phosphorous & calcium levels with next AM labs.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 1.0-1.5' (Parsed: 1.0-1.5) vs JSON_Section='Phosphorus: 1.0 - 1.5 mg/dL<br><span style="color: red; font-weight: bold; font-size: 14px;">NOTIFY PHYSICIAN if less than 1.1 mg/dL</span><br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 1.0-1.5)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level <1.0' (Parsed: None-1.0) vs JSON_Section='Phosphorus: 1.6 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 1.6-2.0)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level <1.0' (Parsed: None-1.0) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br><small style="font-weight: normal;">Monitoring: Recheck phosphorous & calcium levels with next AM labs.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level <1.0' (Parsed: None-1.0) vs JSON_Section='Phosphorus: 1.0 - 1.5 mg/dL<br><span style="color: red; font-weight: bold; font-size: 14px;">NOTIFY PHYSICIAN if less than 1.1 mg/dL</span><br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 1.0-1.5)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level <1.0' (Parsed: None-1.0) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br>ORAL - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck phosphorous & calcium levels with next AM labs.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level <1.0' (Parsed: None-1.0) vs JSON_Section='IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck phosphorous & calcium levels 2 hrs after infusion.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level <1.0' (Parsed: None-1.0) vs JSON_Section='Phosphorus: < 1.0 mg/dL<br><span style="color: red; font-weight: bold; font-size: 14px;">NOTIFY PHYSICIAN if less than 1.1 mg/dL</span><br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>' (Parsed: None-1.0)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='iCal < 1.1' (Parsed: None-1.1) vs JSON_Section='Ionized Calcium: < 1.1 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>' (Parsed: None-1.1)
DEBUG ranges_match: Comparison result = True
[31m[1m_ test_dcw_sentences_match_generated[/home/pessk/code/ea-python/generated_configs/output_regular.json] _[0m

config_file_path = '/home/pessk/code/ea-python/generated_configs/output_regular.json'
dcw_data = [{'Electrolyte': 'Magnesium', 'Instructions/Note': 'Recheck BMP and magnesium level with next AM labs.', 'Lab Value Ra... Range': 'Current serum level 3.2-3.4', 'Mnemonic': 'potassium chloride 10 mEq/100 mL intravenous solution', ...}, ...]

    @pytest.mark.parametrize("config_file_path", get_generated_config_paths())
    def test_dcw_sentences_match_generated(config_file_path, dcw_data):
        """
        Compares sentences from DCW against generated JSON using fuzzy matching.
        Generates a report showing the comparison and score for each DCW entry.
        """
        try:
            with open(config_file_path, 'r', encoding='utf-8') as f:
                loaded_json_config = json.load(f)
        except Exception as e:
            pytest.fail(f"Failed to load or parse JSON from {config_file_path}: {e}")
    
        protocol = get_protocol_from_filename(config_file_path)
        assert protocol, f"Could not determine protocol from filename: {config_file_path}"
    
        protocol_dcw_entries = [e for e in dcw_data if e.get('Protocol') == protocol]
        if not protocol_dcw_entries:
            print(f"Warning: No DCW entries found for protocol: {protocol}. Skipping verification.")
            return
    
        comparison_report_lines = []
        processing_errors = []
    
        for index, dcw_entry in enumerate(protocol_dcw_entries):
            dcw_electrolyte = dcw_entry.get('Electrolyte')
            dcw_mnemonic_raw = dcw_entry.get('Mnemonic') # Get raw mnemonic
            dcw_range = dcw_entry.get('Lab Value Range') # Keep for context
            dcw_sentence = dcw_entry.get('Order_Sentence')
    
            # Clean the DCW mnemonic - remove parentheses and content within
            dcw_mnemonic_cleaned = re.sub(r'\s*\(.*?\)\s*$', '', dcw_mnemonic_raw).strip() if dcw_mnemonic_raw else None
    
            if not all([protocol, dcw_electrolyte, dcw_mnemonic_cleaned, dcw_sentence]): # Use cleaned mnemonic for check
                # Optionally log skipping due to missing cleaned mnemonic
                # print(f"Skipping DCW entry {index}: Missing required data after cleaning mnemonic.")
                continue
    
            # --- Find JSON Counterpart (by cleaned mnemonic within the correct tab) ---
            json_sentence_found = None
            try:
                tabs = loaded_json_config.get('RCONFIG', {}).get('TABS', [])
                target_tab = next((
                    t for t in tabs
                    if t.get('TAB_KEY') and dcw_electrolyte and (
                        # Standard check
                        (t.get('TAB_KEY').upper() == dcw_electrolyte.upper()) or
                        # Specific mapping for Phosphorus -> PHOSPHATE
                        (dcw_electrolyte.upper() == 'PHOSPHORUS' and t.get('TAB_KEY').upper() == 'PHOSPHATE')
                       )
                ), None)
    
                if target_tab:
                    order_sections = target_tab.get('ORDER_SECTIONS', [])
                    found_match_for_dcw_entry = False # Flag to ensure we find a matching section/order
                    for section in order_sections:
                        section_name = section.get('SECTION_NAME', '')
    
                        # Use the refactored ranges_match function
                        is_range_match = ranges_match(dcw_range, section_name)
    
                        if is_range_match:
                             orders_in_section = section.get('ORDERS', [])
                             for order in orders_in_section:
                                 # Compare JSON mnemonic with the CLEANED DCW mnemonic
                                 if order.get('MNEMONIC') == dcw_mnemonic_cleaned:
                                     json_sentence_found = order.get('ORDER_SENTENCE')
                                     found_match_for_dcw_entry = True # Mark as found
                                     break # Found the correct order in the matching section
                             if found_match_for_dcw_entry:
                                 break # Exit section loop once match is found
    
                    # If no match was found after checking all sections, json_sentence_found remains None
                    if not found_match_for_dcw_entry:
                        json_sentence_found = None # Ensure it's None if no suitable section/order found
    
            except Exception as e:
                processing_errors.append(f"Error finding JSON counterpart for DCW entry {index}: {e}")
                continue
    
            # --- Fuzzy Compare DCW vs JSON --- (Uses json_sentence_found)
            comparison_score = 0
            if json_sentence_found:
                # Compare the original DCW sentence with the found JSON sentence
                comparison_score = fuzz.token_sort_ratio(dcw_sentence, json_sentence_found)
            # else: json_sentence_found remains None
    
            # --- Compile Report Line --- (Show original DCW mnemonic for context)
            report_line = f'''
    --- DCW Entry #{index} (Mnem: '{dcw_mnemonic_raw}', Range: '{dcw_range}') ---
      DCW Spec : {repr(dcw_sentence)}
      JSON Gen : {repr(json_sentence_found) if json_sentence_found else '*** NOT FOUND in JSON Tab ***'}
      (Score DCW vs JSON: {comparison_score}%)'''
            comparison_report_lines.append(report_line)
    
        # --- Final Assertion ---
        final_output_message = ""
        if comparison_report_lines:
            final_output_message += f"\nDCW vs JSON Sentence Comparison Report for {os.path.basename(config_file_path)}:\n"
            final_output_message += "\n".join(comparison_report_lines)
        if processing_errors:
             final_output_message += f"\n\nErrors encountered during processing for {os.path.basename(config_file_path)}:\n"
             final_output_message += "\n".join(processing_errors)
    
        # Fail if there's anything in the report to ensure it's always printed
>       assert not final_output_message, final_output_message
[1m[31mE       AssertionError: [0m
[1m[31mE         DCW vs JSON Sentence Comparison Report for output_regular.json:[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #0 (Mnem: 'magnesium oxide', Range: 'Current serum level 1.4-1.5') ---[0m
[1m[31mE           DCW Spec : '400 mg, PO, Tab, q12hr (interval), Duration: 2 dose(s)'[0m
[1m[31mE           JSON Gen : '400 mg, PO, Tab, q12hr (interval), Duration: 2 dose(s)'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #1 (Mnem: 'magnesium sulfate', Range: 'Current serum level 1.4-1.5') ---[0m
[1m[31mE           DCW Spec : '2 g, IVPB, Premix, Once, Infuse over: 2 hr'[0m
[1m[31mE           JSON Gen : '2 g, IVPB, Premix, Once, Infuse over: 2 hr'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #2 (Mnem: 'magnesium sulfate', Range: 'Current serum level < 1.4') ---[0m
[1m[31mE           DCW Spec : '2 g, IVPB, Premix, q2hr (interval), Duration: 2 dose(s), Infuse over: 2 hr'[0m
[1m[31mE           JSON Gen : '2 g, IVPB, Premix, q2hr (interval), Duration: 2 dose(s), Infuse over: 2 hr'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #3 (Mnem: 'potassium chloride extended release', Range: 'Current serum level 3.2-3.4') ---[0m
[1m[31mE           DCW Spec : '20 mEq, PO, ER tab, q2hr (interval), Duration: 2 dose(s)'[0m
[1m[31mE           JSON Gen : '20 mEq, PO, ER tab, q2hr (interval), Duration: 2 dose(s)'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #4 (Mnem: 'potassium chloride', Range: 'Current serum level 3.2-3.4') ---[0m
[1m[31mE           DCW Spec : '20 mEq, Feeding Tube, Liq, q2hr (interval), Duration: 2 dose(s)'[0m
[1m[31mE           JSON Gen : '20 mEq, Feeding Tube, Liq, q2hr (interval), Duration: 2 dose(s)'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #5 (Mnem: 'potassium chloride 10 mEq/100 mL intravenous solution', Range: 'Current serum level 3.2-3.4') ---[0m
[1m[31mE           DCW Spec : '10 mEq, IV, q1hr, Duration: 4 dose(s), Infuse over: 1 hr'[0m
[1m[31mE           JSON Gen : '10 mEq, IV, q1hr, Duration: 4 dose(s), Infuse over: 1 hr'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #6 (Mnem: 'potassium chloride 20 mEq/100 mL intravenous solution', Range: 'Current serum level 3.2-3.4') ---[0m
[1m[31mE           DCW Spec : '20 mEq, IV, q2hr (interval), Duration: 2 dose(s), Infuse over: 2 hr'[0m
[1m[31mE           JSON Gen : '20 mEq, IV, q2hr (interval), Duration: 2 dose(s), Infuse over: 2 hr'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #7 (Mnem: 'potassium chloride extended release', Range: 'Current serum level 2.8-3.1') ---[0m
[1m[31mE           DCW Spec : '20 mEq, PO, ER tab, q2hr (interval), Duration: 3 dose(s)'[0m
[1m[31mE           JSON Gen : '20 mEq, PO, ER tab, q2hr (interval), Duration: 3 dose(s)'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #8 (Mnem: 'potassium chloride', Range: 'Current serum level 2.8-3.1') ---[0m
[1m[31mE           DCW Spec : '20 mEq, Feeding Tube, Liq, q2hr (interval), Duration: 3 dose(s)'[0m
[1m[31mE           JSON Gen : '20 mEq, Feeding Tube, Liq, q2hr (interval), Duration: 3 dose(s)'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #9 (Mnem: 'potassium chloride 10 mEq/100 mL intravenous solution', Range: 'Current serum level 2.8-3.1') ---[0m
[1m[31mE           DCW Spec : '10 mEq, IV, q1hr, Duration: 6 dose(s), Infuse over: 1 hr'[0m
[1m[31mE           JSON Gen : '10 mEq, IV, q1hr, Duration: 6 dose(s), Infuse over: 1 hr'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #10 (Mnem: 'potassium chloride 20 mEq/100 mL intravenous solution', Range: 'Current serum level 2.8-3.1') ---[0m
[1m[31mE           DCW Spec : '20 mEq, IV, q2hr (interval), Duration: 3 dose(s), Infuse over: 2 hr'[0m
[1m[31mE           JSON Gen : '20 mEq, IV, q2hr (interval), Duration: 3 dose(s), Infuse over: 2 hr'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #11 (Mnem: 'potassium chloride 10 mEq/100 mL intravenous solution', Range: 'Current serum level < 2.8') ---[0m
[1m[31mE           DCW Spec : '10 mEq, IV, q1hr, Duration: 8 dose(s), Infuse over: 1 hr'[0m
[1m[31mE           JSON Gen : '10 mEq, IV, q1hr, Duration: 8 dose(s), Infuse over: 1 hr'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #12 (Mnem: 'potassium chloride 20 mEq/100 mL intravenous solution', Range: 'Current serum level < 2.8') ---[0m
[1m[31mE           DCW Spec : '20 mEq, IV, q2hr (interval), Duration: 4 dose(s), Infuse over: 2 hr'[0m
[1m[31mE           JSON Gen : '20 mEq, IV, q2hr (interval), Duration: 4 dose(s), Infuse over: 2 hr'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #13 (Mnem: 'K-Phos Neutral (brand name synonym under primary potassium phosphate-sodium phosphate)', Range: 'Current serum level 1.6-2.0') ---[0m
[1m[31mE           DCW Spec : '2 tab(s), PO, Tab, q2hr (interval), Duration: 2 dose(s)'[0m
[1m[31mE           JSON Gen : '2 tab(s), PO, Tab, q2hr (interval), Duration: 2 dose(s)'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #14 (Mnem: 'sodium phosphate', Range: 'Current serum level 1.6-2.0') ---[0m
[1m[31mE           DCW Spec : '15 mmol, IVPB, Inj, Once'[0m
[1m[31mE           JSON Gen : '15 mmol, IVPB, Inj, Once'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #15 (Mnem: 'K-Phos Neutral', Range: 'Current serum level 1.0-1.5') ---[0m
[1m[31mE           DCW Spec : '2 tab(s), PO, Tab, q2hr (interval), Duration: 3 dose(s)'[0m
[1m[31mE           JSON Gen : '2 tab(s), PO, Tab, q2hr (interval), Duration: 3 dose(s)'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #16 (Mnem: 'sodium phosphate', Range: 'Current serum level 1.0-1.5') ---[0m
[1m[31mE           DCW Spec : '15 mmol, IVPB, Inj, q4hr (interval), Duration: 2 dose(s)'[0m
[1m[31mE           JSON Gen : '15 mmol, IVPB, Inj, q4hr (interval), Duration: 2 dose(s)'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE         [0m
[1m[31mE         --- DCW Entry #17 (Mnem: 'sodium phosphate', Range: 'Current serum level <1.0') ---[0m
[1m[31mE           DCW Spec : '15 mmol, IVPB, Inj, q4hr (interval), Duration: 2 dose(s)'[0m
[1m[31mE           JSON Gen : '15 mmol, IVPB, Inj, q4hr (interval), Duration: 2 dose(s)'[0m
[1m[31mE           (Score DCW vs JSON: 100%)[0m
[1m[31mE       assert not "\nDCW vs JSON Sentence Comparison Report for output_regular.json:\n\n--- DCW Entry #0 (Mnem: 'magnesium oxide', Range: 'Current serum level 1.4-1.5') ---\n  DCW Spec : '400 mg, PO, Tab, q12hr (interval), Duration: 2 dose(s)'\n  JSON Gen : '400 mg, PO, Tab, q12hr (interval), Duration: 2 dose(s)'\n  (Score DCW vs JSON: 100%)\n\n--- DCW Entry #1 (Mnem: 'magnesium sulfate', Range: 'Current serum level 1.4-1.5') ---\n  DCW Spec : '2 g, IVPB, Premix, Once, Infuse over: 2 hr'\n  JSON Gen : '2 g, IVPB, Premix, Once, Infuse over: 2 hr'\n  (Score DCW vs JSON: 100%)\n\n--- DCW Entry #2 (Mnem: 'magnesium sulfate', Range: 'Current serum level < 1.4') ---\n  DCW Spec : '2 g, IVPB, Premix, q2hr (interval), Duration: 2 dose(s), Infuse over: 2 hr'\n  JSON Gen : '2 g, IVPB, Premix, q2hr (interval), Duration: 2 dose(s), Infuse over: 2 hr'\n  (Score DCW vs JSON: 100%)\n\n--- DCW Entry #3 (Mnem: 'potassium chloride extended release', Range: 'Current serum level 3.2-3.4') ---\n  DCW Spec : '20 mEq, PO, ER tab, q2hr (interval), Duration: 2 dose(s)'\n  JSON Gen : '20 mEq, PO, ER tab, q2hr (interval), Duration: 2 dose(s)'\n  (Score DCW vs JSON: 100%)\n\n--- DCW Entry #4 (Mnem: 'potassium chloride', Rang...: 'Current serum level 1.6-2.0') ---\n  DCW Spec : '2 tab(s), PO, Tab, q2hr (interval), Duration: 2 dose(s)'\n  JSON Gen : '2 tab(s), PO, Tab, q2hr (interval), Duration: 2 dose(s)'\n  (Score DCW vs JSON: 100%)\n\n--- DCW Entry #14 (Mnem: 'sodium phosphate', Range: 'Current serum level 1.6-2.0') ---\n  DCW Spec : '15 mmol, IVPB, Inj, Once'\n  JSON Gen : '15 mmol, IVPB, Inj, Once'\n  (Score DCW vs JSON: 100%)\n\n--- DCW Entry #15 (Mnem: 'K-Phos Neutral', Range: 'Current serum level 1.0-1.5') ---\n  DCW Spec : '2 tab(s), PO, Tab, q2hr (interval), Duration: 3 dose(s)'\n  JSON Gen : '2 tab(s), PO, Tab, q2hr (interval), Duration: 3 dose(s)'\n  (Score DCW vs JSON: 100%)\n\n--- DCW Entry #16 (Mnem: 'sodium phosphate', Range: 'Current serum level 1.0-1.5') ---\n  DCW Spec : '15 mmol, IVPB, Inj, q4hr (interval), Duration: 2 dose(s)'\n  JSON Gen : '15 mmol, IVPB, Inj, q4hr (interval), Duration: 2 dose(s)'\n  (Score DCW vs JSON: 100%)\n\n--- DCW Entry #17 (Mnem: 'sodium phosphate', Range: 'Current serum level <1.0') ---\n  DCW Spec : '15 mmol, IVPB, Inj, q4hr (interval), Duration: 2 dose(s)'\n  JSON Gen : '15 mmol, IVPB, Inj, q4hr (interval), Duration: 2 dose(s)'\n  (Score DCW vs JSON: 100%)"[0m

comparison_report_lines = ["\n--- DCW Entry #0 (Mnem: 'magnesium oxide', Range: 'Current serum level 1.4-1.5') ---\n  DCW Spec : '400 mg, PO, Ta...ver: 1 hr'\n  JSON Gen : '10 mEq, IV, q1hr, Duration: 4 dose(s), Infuse over: 1 hr'\n  (Score DCW vs JSON: 100%)", ...]
comparison_score = 100
config_file_path = '/home/pessk/code/ea-python/generated_configs/output_regular.json'
dcw_data   = [{'Electrolyte': 'Magnesium', 'Instructions/Note': 'Recheck BMP and magnesium level with next AM labs.', 'Lab Value Ra... Range': 'Current serum level 3.2-3.4', 'Mnemonic': 'potassium chloride 10 mEq/100 mL intravenous solution', ...}, ...]
dcw_electrolyte = 'Phosphorus'
dcw_entry  = {'Electrolyte': 'Phosphorus', 'Instructions/Note': 'Recheck phosphorous & calcium levels 2 hrs after infusion', 'Lab Value Range': 'Current serum level <1.0', 'Mnemonic': 'sodium phosphate', ...}
dcw_mnemonic_cleaned = 'sodium phosphate'
dcw_mnemonic_raw = 'sodium phosphate'
dcw_range  = 'Current serum level <1.0'
dcw_sentence = '15 mmol, IVPB, Inj, q4hr (interval), Duration: 2 dose(s)'
f          = <_io.TextIOWrapper name='/home/pessk/code/ea-python/generated_configs/output_regular.json' mode='r' encoding='utf-8'>
final_output_message = "\nDCW vs JSON Sentence Comparison Report for output_regular.json:\n\n--- DCW Entry #0 (Mnem: 'magnesium oxide', Range...tion: 2 dose(s)'\n  JSON Gen : '15 mmol, IVPB, Inj, q4hr (interval), Duration: 2 dose(s)'\n  (Score DCW vs JSON: 100%)"
found_match_for_dcw_entry = True
index      = 17
is_range_match = True
json_sentence_found = '15 mmol, IVPB, Inj, q4hr (interval), Duration: 2 dose(s)'
loaded_json_config = {'RCONFIG': {'CCL_POSTPROCESS': 'UHS_MPG_GET_TABBED_ADVISOR', 'JSON_RETURN': '', 'TABS': [{'CANCEL_BUTTON': {}, 'CONCE...rder)', 'TOOLTIP': 'Room type: Critical Care, PCU, Telemetry, MS (Med/Surg) with Telemetry Monitoring order'}], ...}]}}
order      = {'ASC_SHORT_DESCRIPTION': '', 'COMMENT': 'Intravenous', 'MNEMONIC': 'sodium phosphate', 'ORDER_SENTENCE': '15 mmol, IVPB, Inj, q4hr (interval), Duration: 2 dose(s)'}
order_sections = [{'CONCEPT_NAME': '[%{EALABPHOSTODO}.COUNT > 0 AND {EALABPHOSBTW16AND20}%]', 'ORDERS': [{'ASC_SHORT_DESCRIPTION': '', ...ld; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>', 'SHOW_INACTIVE_DUPLICATES': 0, ...}, ...]
orders_in_section = [{'ASC_SHORT_DESCRIPTION': '', 'COMMENT': 'Intravenous', 'MNEMONIC': 'sodium phosphate', 'ORDER_SENTENCE': '15 mmol, IVPB, Inj, q4hr (interval), Duration: 2 dose(s)'}]
processing_errors = []
protocol   = 'Regular'
protocol_dcw_entries = [{'Electrolyte': 'Magnesium', 'Instructions/Note': 'Recheck BMP and magnesium level with next AM labs.', 'Lab Value Ra... Range': 'Current serum level 3.2-3.4', 'Mnemonic': 'potassium chloride 10 mEq/100 mL intravenous solution', ...}, ...]
report_line = "\n--- DCW Entry #17 (Mnem: 'sodium phosphate', Range: 'Current serum level <1.0') ---\n  DCW Spec : '15 mmol, IVPB, I...tion: 2 dose(s)'\n  JSON Gen : '15 mmol, IVPB, Inj, q4hr (interval), Duration: 2 dose(s)'\n  (Score DCW vs JSON: 100%)"
section    = {'CONCEPT_NAME': '[%{EALABPHOSTODO}.COUNT > 0 AND {EALABPHOSLT10}%]', 'ORDERS': [{'ASC_SHORT_DESCRIPTION': '', 'COMMEN...ht: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>', 'SHOW_INACTIVE_DUPLICATES': 0, ...}
section_name = 'Phosphorus: < 1.0 mg/dL<br><span style="color: red; font-weight: bold; font-size: 14px;">NOTIFY PHYSICIAN if less tha...ong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>'
tabs       = [{'CANCEL_BUTTON': {}, 'CONCEPTS': [], 'CONCEPT_FOR_DISMISS': 'EALABMAGTODO', 'CRITERIA': [{'CONCEPT_NAME': '[%true%]'... order)', 'TOOLTIP': 'Room type: Critical Care, PCU, Telemetry, MS (Med/Surg) with Telemetry Monitoring order'}], ...}]
target_tab = {'CANCEL_BUTTON': {}, 'CONCEPTS': [], 'CONCEPT_FOR_DISMISS': 'EALABPHOSTODO', 'CRITERIA': [{'CONCEPT_NAME': '[%true%]'...g order)', 'TOOLTIP': 'Room type: Critical Care, PCU, Telemetry, MS (Med/Surg) with Telemetry Monitoring order'}], ...}

[1m[31mtests/test_dcw_sentences.py[0m:280: AssertionError
----------------------------- Captured stdout call -----------------------------

DEBUG ranges_match: Comparing DCW='Current serum level 1.4-1.5' (Parsed: 1.4-1.5) vs JSON_Section='Magnesium: 1.4 - 1.5 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 1.4-1.5)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level 1.4-1.5' (Parsed: 1.4-1.5) vs JSON_Section='Magnesium: 1.4 - 1.5 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 1.4-1.5)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level < 1.4' (Parsed: None-1.4) vs JSON_Section='Magnesium: 1.4 - 1.5 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 1.4-1.5)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 1.4' (Parsed: None-1.4) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br><small style="font-weight: normal;">Monitoring: Recheck BMP and magnesium level with next AM labs.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 1.4' (Parsed: None-1.4) vs JSON_Section='Magnesium: < 1.4 mg/dL<br><span style="color: red; font-weight: bold; font-size: 14px;">NOTIFY PHYSICIAN if less than 1.2 mg/dL</span><br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>' (Parsed: None-1.4)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level 3.2-3.4' (Parsed: 3.2-3.4) vs JSON_Section='Potassium: 3.2 - 3.4 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 3.2-3.4)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level 3.2-3.4' (Parsed: 3.2-3.4) vs JSON_Section='Potassium: 3.2 - 3.4 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 3.2-3.4)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level 3.2-3.4' (Parsed: 3.2-3.4) vs JSON_Section='Potassium: 3.2 - 3.4 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 3.2-3.4)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level 3.2-3.4' (Parsed: 3.2-3.4) vs JSON_Section='Potassium: 3.2 - 3.4 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 3.2-3.4)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='Potassium: 3.2 - 3.4 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 3.2-3.4)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br><small style="font-weight: normal;">Monitoring: Recheck BMP with next AM labs.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='Potassium: 2.8 - 3.1 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>' (Parsed: 2.8-3.1)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='Potassium: 3.2 - 3.4 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 3.2-3.4)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br><small style="font-weight: normal;">Monitoring: Recheck BMP with next AM labs.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='Potassium: 2.8 - 3.1 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>' (Parsed: 2.8-3.1)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='Potassium: 3.2 - 3.4 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 3.2-3.4)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br><small style="font-weight: normal;">Monitoring: Recheck BMP with next AM labs.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='Potassium: 2.8 - 3.1 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>' (Parsed: 2.8-3.1)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='Potassium: 3.2 - 3.4 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 3.2-3.4)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br><small style="font-weight: normal;">Monitoring: Recheck BMP with next AM labs.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: 2.8-3.1) vs JSON_Section='Potassium: 2.8 - 3.1 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>' (Parsed: 2.8-3.1)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-2.8) vs JSON_Section='Potassium: 3.2 - 3.4 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 3.2-3.4)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-2.8) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br><small style="font-weight: normal;">Monitoring: Recheck BMP with next AM labs.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-2.8) vs JSON_Section='Potassium: 2.8 - 3.1 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>' (Parsed: 2.8-3.1)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-2.8) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br>ORAL / FEEDING TUBE - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck potassium level 4 hrs after last dose.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-2.8) vs JSON_Section='IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck potassium level 1 hr after infusion complete.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-2.8) vs JSON_Section='Potassium: < 2.8 mmol/L<br><span style="color: red; font-weight: bold; font-size: 14px;">NOTIFY PHYSICIAN</span><br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>' (Parsed: None-2.8)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-2.8) vs JSON_Section='Potassium: 3.2 - 3.4 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 3.2-3.4)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-2.8) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br><small style="font-weight: normal;">Monitoring: Recheck BMP with next AM labs.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-2.8) vs JSON_Section='Potassium: 2.8 - 3.1 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>' (Parsed: 2.8-3.1)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-2.8) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br>ORAL / FEEDING TUBE - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck potassium level 4 hrs after last dose.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-2.8) vs JSON_Section='IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck potassium level 1 hr after infusion complete.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-2.8) vs JSON_Section='Potassium: < 2.8 mmol/L<br><span style="color: red; font-weight: bold; font-size: 14px;">NOTIFY PHYSICIAN</span><br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>' (Parsed: None-2.8)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level 1.6-2.0' (Parsed: 1.6-2.0) vs JSON_Section='Phosphorus: 1.6 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 1.6-2.0)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level 1.6-2.0' (Parsed: 1.6-2.0) vs JSON_Section='Phosphorus: 1.6 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 1.6-2.0)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level 1.0-1.5' (Parsed: 1.0-1.5) vs JSON_Section='Phosphorus: 1.6 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 1.6-2.0)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 1.0-1.5' (Parsed: 1.0-1.5) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br><small style="font-weight: normal;">Monitoring: Recheck phosphorous & calcium levels with next AM labs.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 1.0-1.5' (Parsed: 1.0-1.5) vs JSON_Section='Phosphorus: 1.0 - 1.5 mg/dL<br><span style="color: red; font-weight: bold; font-size: 14px;">NOTIFY PHYSICIAN if less than 1.1 mg/dL</span><br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 1.0-1.5)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level 1.0-1.5' (Parsed: 1.0-1.5) vs JSON_Section='Phosphorus: 1.6 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 1.6-2.0)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 1.0-1.5' (Parsed: 1.0-1.5) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br><small style="font-weight: normal;">Monitoring: Recheck phosphorous & calcium levels with next AM labs.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level 1.0-1.5' (Parsed: 1.0-1.5) vs JSON_Section='Phosphorus: 1.0 - 1.5 mg/dL<br><span style="color: red; font-weight: bold; font-size: 14px;">NOTIFY PHYSICIAN if less than 1.1 mg/dL</span><br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 1.0-1.5)
DEBUG ranges_match: Comparison result = True

DEBUG ranges_match: Comparing DCW='Current serum level <1.0' (Parsed: None-1.0) vs JSON_Section='Phosphorus: 1.6 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 1.6-2.0)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level <1.0' (Parsed: None-1.0) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br><small style="font-weight: normal;">Monitoring: Recheck phosphorous & calcium levels with next AM labs.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level <1.0' (Parsed: None-1.0) vs JSON_Section='Phosphorus: 1.0 - 1.5 mg/dL<br><span style="color: red; font-weight: bold; font-size: 14px;">NOTIFY PHYSICIAN if less than 1.1 mg/dL</span><br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: 1.0-1.5)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level <1.0' (Parsed: None-1.0) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br>ORAL - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck phosphorous & calcium levels with next AM labs.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level <1.0' (Parsed: None-1.0) vs JSON_Section='IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck phosphorous & calcium levels 2 hrs after infusion.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = False

DEBUG ranges_match: Comparing DCW='Current serum level <1.0' (Parsed: None-1.0) vs JSON_Section='Phosphorus: < 1.0 mg/dL<br><span style="color: red; font-weight: bold; font-size: 14px;">NOTIFY PHYSICIAN if less than 1.1 mg/dL</span><br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>' (Parsed: None-1.0)
DEBUG ranges_match: Comparison result = True
[31m[1m_ test_expected_sentences_match_generated[/home/pessk/code/ea-python/generated_configs/output_cardiac.json] _[0m

    @cache
    def load_all_expected_from_csv() -> Dict[str, Set[str]]:
        """Loads all expected sentences from extract.csv into a dictionary.
    
        Reads the CSV file and groups sentences by MNEMONIC.
        Returns a dictionary mapping mnemonic strings to sets of sentence strings.
        Caches the result for performance.
        """
        expected_data: Dict[str, Set[str]] = defaultdict(set)
        if not EXPECTED_EXTRACT_FILE.is_file():
            pytest.fail(f"Expected sentences file not found: {EXPECTED_EXTRACT_FILE}")
    
        try:
            with open(EXPECTED_EXTRACT_FILE, 'r', encoding='utf-8') as f:
>               reader = csv.DictReader(f, delimiter='\\t') # Use DictReader assuming header row, specify tab delimiter

expected_data = defaultdict(<class 'set'>, {})
f          = <_io.TextIOWrapper name='/home/pessk/code/ea-python/expected_sentences/extract.csv' mode='r' encoding='utf-8'>

[1m[31mtests/test_expected_sentences.py[0m:52: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <csv.DictReader object at 0x7fcfd879ae40>
f = <_io.TextIOWrapper name='/home/pessk/code/ea-python/expected_sentences/extract.csv' mode='r' encoding='utf-8'>
fieldnames = None, restkey = None, restval = None, dialect = 'excel', args = ()
kwds = {'delimiter': '\\t'}

    def __init__(self, f, fieldnames=None, restkey=None, restval=None,
                 dialect="excel", *args, **kwds):
        if fieldnames is not None and iter(fieldnames) is fieldnames:
            fieldnames = list(fieldnames)
        self._fieldnames = fieldnames   # list of keys for the dict
        self.restkey = restkey          # key to catch long rows
        self.restval = restval          # default value for short rows
>       self.reader = reader(f, dialect, *args, **kwds)
[1m[31mE       TypeError: "delimiter" must be a 1-character string[0m

args       = ()
dialect    = 'excel'
f          = <_io.TextIOWrapper name='/home/pessk/code/ea-python/expected_sentences/extract.csv' mode='r' encoding='utf-8'>
fieldnames = None
kwds       = {'delimiter': '\\t'}
restkey    = None
restval    = None
self       = <csv.DictReader object at 0x7fcfd879ae40>

[1m[31m/usr/lib/python3.12/csv.py[0m:91: TypeError

[33mDuring handling of the above exception, another exception occurred:[0m

config_file_path = '/home/pessk/code/ea-python/generated_configs/output_cardiac.json'

    @pytest.mark.parametrize("config_file_path", get_generated_config_paths())
    def test_expected_sentences_match_generated(config_file_path):
        """
        Verifies that order sentences in the generated JSON match EXACTLY those defined
        in the expected_sentences/extract.csv file.
        """
        # --- Clear cache (optional, but good practice if data might change between runs) ---
        load_all_expected_from_csv.cache_clear()
        # --- End Clear Cache ---
    
        # Load JSON inside the test
        try:
            with open(config_file_path, 'r', encoding='utf-8') as f:
                loaded_json_config = json.load(f)
        except Exception as e:
            pytest.fail(f"Failed to load or parse JSON from {config_file_path}: {e}")
    
        protocol = get_protocol_from_filename(config_file_path)
        assert protocol, f"Could not determine protocol from filename: {config_file_path}"
    
        errors = []
        processed_json_orders = set()
    
        # Iterate through the generated JSON structure
        try:
            tabs = loaded_json_config.get('RCONFIG', {}).get('TABS', [])
            for tab in tabs:
                tab_key = tab.get('TAB_KEY') # Still useful for context in errors
                if not tab_key:
                    continue
    
                order_sections = tab.get('ORDER_SECTIONS', [])
                for section_index, section in enumerate(order_sections):
                    orders_in_section = section.get('ORDERS', [])
                    for order_index, order in enumerate(orders_in_section):
                        json_mnemonic = order.get('MNEMONIC')
                        json_sentence = order.get('ORDER_SENTENCE')
                        json_order_id = f"{tab_key}-S{section_index}-O{order_index}-{json_mnemonic}"
    
                        if not json_mnemonic or not json_sentence:
                            continue
                        if json_order_id in processed_json_orders:
                            continue
    
                        # --- Debug: Print mnemonic being checked ---
                        # print(f"DEBUG: Checking Mnemonic='{json_mnemonic}', Tab='{tab_key}'")
                        # --- End Debug ---
    
                        # Get expected sentences for this mnemonic from the single CSV
>                       expected_sentences = get_expected_sentences_for_mnemonic(json_mnemonic)

config_file_path = '/home/pessk/code/ea-python/generated_configs/output_cardiac.json'
errors     = []
f          = <_io.TextIOWrapper name='/home/pessk/code/ea-python/generated_configs/output_cardiac.json' mode='r' encoding='utf-8'>
json_mnemonic = 'magnesium sulfate'
json_order_id = 'MAGNESIUM-S0-O0-magnesium sulfate'
json_sentence = '1 g, IVPB, Premix, Once, Infuse over: 1 hr'
loaded_json_config = {'RCONFIG': {'CCL_POSTPROCESS': 'UHS_MPG_GET_TABBED_ADVISOR', 'JSON_RETURN': '', 'TABS': [{'CANCEL_BUTTON': {}, 'CONCE...rder)', 'TOOLTIP': 'Room type: Critical Care, PCU, Telemetry, MS (Med/Surg) with Telemetry Monitoring order'}], ...}]}}
order      = {'ASC_SHORT_DESCRIPTION': '', 'COMMENT': 'Intravenous', 'MNEMONIC': 'magnesium sulfate', 'ORDER_SENTENCE': '1 g, IVPB, Premix, Once, Infuse over: 1 hr'}
order_index = 0
order_sections = [{'CONCEPT_NAME': '[%{EALABMAGTODO}.COUNT > 0 AND {EALABMAGBTW18AND20}%]', 'ORDERS': [{'ASC_SHORT_DESCRIPTION': '', 'C...>Monitoring: Recheck magnesium level 4 hrs after infusion complete.</small>', 'SHOW_INACTIVE_DUPLICATES': 0, ...}, ...]
orders_in_section = [{'ASC_SHORT_DESCRIPTION': '', 'COMMENT': 'Intravenous', 'MNEMONIC': 'magnesium sulfate', 'ORDER_SENTENCE': '1 g, IVPB, Premix, Once, Infuse over: 1 hr'}]
processed_json_orders = set()
protocol   = 'Cardiac'
section    = {'CONCEPT_NAME': '[%{EALABMAGTODO}.COUNT > 0 AND {EALABMAGBTW18AND20}%]', 'ORDERS': [{'ASC_SHORT_DESCRIPTION': '', 'CO...ht: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>', 'SHOW_INACTIVE_DUPLICATES': 0, ...}
section_index = 0
tab        = {'CANCEL_BUTTON': {}, 'CONCEPTS': [], 'CONCEPT_FOR_DISMISS': 'EALABMAGTODO', 'CRITERIA': [{'CONCEPT_NAME': '[%true%]',...g order)', 'TOOLTIP': 'Room type: Critical Care, PCU, Telemetry, MS (Med/Surg) with Telemetry Monitoring order'}], ...}
tab_key    = 'MAGNESIUM'
tabs       = [{'CANCEL_BUTTON': {}, 'CONCEPTS': [], 'CONCEPT_FOR_DISMISS': 'EALABMAGTODO', 'CRITERIA': [{'CONCEPT_NAME': '[%true%]'... order)', 'TOOLTIP': 'Room type: Critical Care, PCU, Telemetry, MS (Med/Surg) with Telemetry Monitoring order'}], ...}]

[1m[31mtests/test_expected_sentences.py[0m:144: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
[1m[31mtests/test_expected_sentences.py[0m:81: in get_expected_sentences_for_mnemonic
    all_expected = load_all_expected_from_csv()
        mnemonic   = 'magnesium sulfate'
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    @cache
    def load_all_expected_from_csv() -> Dict[str, Set[str]]:
        """Loads all expected sentences from extract.csv into a dictionary.
    
        Reads the CSV file and groups sentences by MNEMONIC.
        Returns a dictionary mapping mnemonic strings to sets of sentence strings.
        Caches the result for performance.
        """
        expected_data: Dict[str, Set[str]] = defaultdict(set)
        if not EXPECTED_EXTRACT_FILE.is_file():
            pytest.fail(f"Expected sentences file not found: {EXPECTED_EXTRACT_FILE}")
    
        try:
            with open(EXPECTED_EXTRACT_FILE, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f, delimiter='\\t') # Use DictReader assuming header row, specify tab delimiter
                # Verify expected column names (adjust if different)
                if reader.fieldnames is None: # Check if fieldnames were read
                     pytest.fail(f"Could not read headers from CSV {EXPECTED_EXTRACT_FILE}")
    
                required_columns = ['MNEMONIC', 'ORDER_SENTENCE_DISPLAY_LINE']
                if not all(col in reader.fieldnames for col in required_columns):
                    missing = [col for col in required_columns if col not in reader.fieldnames]
                    pytest.fail(
                        f"CSV {EXPECTED_EXTRACT_FILE.name} missing required columns: {missing}"
                    )
    
                for row in reader:
                    mnemonic = row.get('MNEMONIC')
                    sentence = row.get('ORDER_SENTENCE_DISPLAY_LINE')
                    # Add non-empty sentences to the set for the mnemonic
                    if mnemonic and sentence:
                        expected_data[mnemonic].add(sentence.strip())
        except Exception as e:
>           pytest.fail(f"Failed to read or parse {EXPECTED_EXTRACT_FILE}: {e}")
[1m[31mE           Failed: Failed to read or parse /home/pessk/code/ea-python/expected_sentences/extract.csv: "delimiter" must be a 1-character string[0m

expected_data = defaultdict(<class 'set'>, {})
f          = <_io.TextIOWrapper name='/home/pessk/code/ea-python/expected_sentences/extract.csv' mode='r' encoding='utf-8'>

[1m[31mtests/test_expected_sentences.py[0m:71: Failed
[31m[1m_ test_expected_sentences_match_generated[/home/pessk/code/ea-python/generated_configs/output_regular.json] _[0m

    @cache
    def load_all_expected_from_csv() -> Dict[str, Set[str]]:
        """Loads all expected sentences from extract.csv into a dictionary.
    
        Reads the CSV file and groups sentences by MNEMONIC.
        Returns a dictionary mapping mnemonic strings to sets of sentence strings.
        Caches the result for performance.
        """
        expected_data: Dict[str, Set[str]] = defaultdict(set)
        if not EXPECTED_EXTRACT_FILE.is_file():
            pytest.fail(f"Expected sentences file not found: {EXPECTED_EXTRACT_FILE}")
    
        try:
            with open(EXPECTED_EXTRACT_FILE, 'r', encoding='utf-8') as f:
>               reader = csv.DictReader(f, delimiter='\\t') # Use DictReader assuming header row, specify tab delimiter

expected_data = defaultdict(<class 'set'>, {})
f          = <_io.TextIOWrapper name='/home/pessk/code/ea-python/expected_sentences/extract.csv' mode='r' encoding='utf-8'>

[1m[31mtests/test_expected_sentences.py[0m:52: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <csv.DictReader object at 0x7fcfd863fe90>
f = <_io.TextIOWrapper name='/home/pessk/code/ea-python/expected_sentences/extract.csv' mode='r' encoding='utf-8'>
fieldnames = None, restkey = None, restval = None, dialect = 'excel', args = ()
kwds = {'delimiter': '\\t'}

    def __init__(self, f, fieldnames=None, restkey=None, restval=None,
                 dialect="excel", *args, **kwds):
        if fieldnames is not None and iter(fieldnames) is fieldnames:
            fieldnames = list(fieldnames)
        self._fieldnames = fieldnames   # list of keys for the dict
        self.restkey = restkey          # key to catch long rows
        self.restval = restval          # default value for short rows
>       self.reader = reader(f, dialect, *args, **kwds)
[1m[31mE       TypeError: "delimiter" must be a 1-character string[0m

args       = ()
dialect    = 'excel'
f          = <_io.TextIOWrapper name='/home/pessk/code/ea-python/expected_sentences/extract.csv' mode='r' encoding='utf-8'>
fieldnames = None
kwds       = {'delimiter': '\\t'}
restkey    = None
restval    = None
self       = <csv.DictReader object at 0x7fcfd863fe90>

[1m[31m/usr/lib/python3.12/csv.py[0m:91: TypeError

[33mDuring handling of the above exception, another exception occurred:[0m

config_file_path = '/home/pessk/code/ea-python/generated_configs/output_regular.json'

    @pytest.mark.parametrize("config_file_path", get_generated_config_paths())
    def test_expected_sentences_match_generated(config_file_path):
        """
        Verifies that order sentences in the generated JSON match EXACTLY those defined
        in the expected_sentences/extract.csv file.
        """
        # --- Clear cache (optional, but good practice if data might change between runs) ---
        load_all_expected_from_csv.cache_clear()
        # --- End Clear Cache ---
    
        # Load JSON inside the test
        try:
            with open(config_file_path, 'r', encoding='utf-8') as f:
                loaded_json_config = json.load(f)
        except Exception as e:
            pytest.fail(f"Failed to load or parse JSON from {config_file_path}: {e}")
    
        protocol = get_protocol_from_filename(config_file_path)
        assert protocol, f"Could not determine protocol from filename: {config_file_path}"
    
        errors = []
        processed_json_orders = set()
    
        # Iterate through the generated JSON structure
        try:
            tabs = loaded_json_config.get('RCONFIG', {}).get('TABS', [])
            for tab in tabs:
                tab_key = tab.get('TAB_KEY') # Still useful for context in errors
                if not tab_key:
                    continue
    
                order_sections = tab.get('ORDER_SECTIONS', [])
                for section_index, section in enumerate(order_sections):
                    orders_in_section = section.get('ORDERS', [])
                    for order_index, order in enumerate(orders_in_section):
                        json_mnemonic = order.get('MNEMONIC')
                        json_sentence = order.get('ORDER_SENTENCE')
                        json_order_id = f"{tab_key}-S{section_index}-O{order_index}-{json_mnemonic}"
    
                        if not json_mnemonic or not json_sentence:
                            continue
                        if json_order_id in processed_json_orders:
                            continue
    
                        # --- Debug: Print mnemonic being checked ---
                        # print(f"DEBUG: Checking Mnemonic='{json_mnemonic}', Tab='{tab_key}'")
                        # --- End Debug ---
    
                        # Get expected sentences for this mnemonic from the single CSV
>                       expected_sentences = get_expected_sentences_for_mnemonic(json_mnemonic)

config_file_path = '/home/pessk/code/ea-python/generated_configs/output_regular.json'
errors     = []
f          = <_io.TextIOWrapper name='/home/pessk/code/ea-python/generated_configs/output_regular.json' mode='r' encoding='utf-8'>
json_mnemonic = 'magnesium oxide'
json_order_id = 'MAGNESIUM-S0-O0-magnesium oxide'
json_sentence = '400 mg, PO, Tab, q12hr (interval), Duration: 2 dose(s)'
loaded_json_config = {'RCONFIG': {'CCL_POSTPROCESS': 'UHS_MPG_GET_TABBED_ADVISOR', 'JSON_RETURN': '', 'TABS': [{'CANCEL_BUTTON': {}, 'CONCE...rder)', 'TOOLTIP': 'Room type: Critical Care, PCU, Telemetry, MS (Med/Surg) with Telemetry Monitoring order'}], ...}]}}
order      = {'ASC_SHORT_DESCRIPTION': '', 'COMMENT': 'Oral *', 'MNEMONIC': 'magnesium oxide', 'ORDER_SENTENCE': '400 mg, PO, Tab, q12hr (interval), Duration: 2 dose(s)'}
order_index = 0
order_sections = [{'CONCEPT_NAME': '[%{EALABMAGTODO}.COUNT > 0 AND {EALABMAGBTW14AND15}%]', 'ORDERS': [{'ASC_SHORT_DESCRIPTION': '', 'C...0400, Blood, Tomorrow AM collect, Once'}], 'SECTION_NAME': 'Magnesium Lab Orders', 'SHOW_INACTIVE_DUPLICATES': 0, ...}]
orders_in_section = [{'ASC_SHORT_DESCRIPTION': '', 'COMMENT': 'Oral *', 'MNEMONIC': 'magnesium oxide', 'ORDER_SENTENCE': '400 mg, PO, Tab,...MENT': 'Intravenous', 'MNEMONIC': 'magnesium sulfate', 'ORDER_SENTENCE': '2 g, IVPB, Premix, Once, Infuse over: 2 hr'}]
processed_json_orders = set()
protocol   = 'Regular'
section    = {'CONCEPT_NAME': '[%{EALABMAGTODO}.COUNT > 0 AND {EALABMAGBTW14AND15}%]', 'ORDERS': [{'ASC_SHORT_DESCRIPTION': '', 'CO...ications, the recommended choice of replacement route is to be oral. </span> <br>', 'SHOW_INACTIVE_DUPLICATES': 0, ...}
section_index = 0
tab        = {'CANCEL_BUTTON': {}, 'CONCEPTS': [], 'CONCEPT_FOR_DISMISS': 'EALABMAGTODO', 'CRITERIA': [{'CONCEPT_NAME': '[%true%]',...g order)', 'TOOLTIP': 'Room type: Critical Care, PCU, Telemetry, MS (Med/Surg) with Telemetry Monitoring order'}], ...}
tab_key    = 'MAGNESIUM'
tabs       = [{'CANCEL_BUTTON': {}, 'CONCEPTS': [], 'CONCEPT_FOR_DISMISS': 'EALABMAGTODO', 'CRITERIA': [{'CONCEPT_NAME': '[%true%]'... order)', 'TOOLTIP': 'Room type: Critical Care, PCU, Telemetry, MS (Med/Surg) with Telemetry Monitoring order'}], ...}]

[1m[31mtests/test_expected_sentences.py[0m:144: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
[1m[31mtests/test_expected_sentences.py[0m:81: in get_expected_sentences_for_mnemonic
    all_expected = load_all_expected_from_csv()
        mnemonic   = 'magnesium oxide'
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    @cache
    def load_all_expected_from_csv() -> Dict[str, Set[str]]:
        """Loads all expected sentences from extract.csv into a dictionary.
    
        Reads the CSV file and groups sentences by MNEMONIC.
        Returns a dictionary mapping mnemonic strings to sets of sentence strings.
        Caches the result for performance.
        """
        expected_data: Dict[str, Set[str]] = defaultdict(set)
        if not EXPECTED_EXTRACT_FILE.is_file():
            pytest.fail(f"Expected sentences file not found: {EXPECTED_EXTRACT_FILE}")
    
        try:
            with open(EXPECTED_EXTRACT_FILE, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f, delimiter='\\t') # Use DictReader assuming header row, specify tab delimiter
                # Verify expected column names (adjust if different)
                if reader.fieldnames is None: # Check if fieldnames were read
                     pytest.fail(f"Could not read headers from CSV {EXPECTED_EXTRACT_FILE}")
    
                required_columns = ['MNEMONIC', 'ORDER_SENTENCE_DISPLAY_LINE']
                if not all(col in reader.fieldnames for col in required_columns):
                    missing = [col for col in required_columns if col not in reader.fieldnames]
                    pytest.fail(
                        f"CSV {EXPECTED_EXTRACT_FILE.name} missing required columns: {missing}"
                    )
    
                for row in reader:
                    mnemonic = row.get('MNEMONIC')
                    sentence = row.get('ORDER_SENTENCE_DISPLAY_LINE')
                    # Add non-empty sentences to the set for the mnemonic
                    if mnemonic and sentence:
                        expected_data[mnemonic].add(sentence.strip())
        except Exception as e:
>           pytest.fail(f"Failed to read or parse {EXPECTED_EXTRACT_FILE}: {e}")
[1m[31mE           Failed: Failed to read or parse /home/pessk/code/ea-python/expected_sentences/extract.csv: "delimiter" must be a 1-character string[0m

expected_data = defaultdict(<class 'set'>, {})
f          = <_io.TextIOWrapper name='/home/pessk/code/ea-python/expected_sentences/extract.csv' mode='r' encoding='utf-8'>

[1m[31mtests/test_expected_sentences.py[0m:71: Failed
[36m[1m=========================== short test summary info ============================[0m
[31mFAILED[0m tests/test_dcw_sentences.py::[1mtest_dcw_sentences_match_generated[/home/pessk/code/ea-python/generated_configs/output_cardiac.json][0m - AssertionError: 
[31mFAILED[0m tests/test_dcw_sentences.py::[1mtest_dcw_sentences_match_generated[/home/pessk/code/ea-python/generated_configs/output_regular.json][0m - AssertionError: 
[31mFAILED[0m tests/test_expected_sentences.py::[1mtest_expected_sentences_match_generated[/home/pessk/code/ea-python/generated_configs/output_cardiac.json][0m - Failed: Failed to read or parse /home/pessk/code/ea-python/expected_sentenc...
[31mFAILED[0m tests/test_expected_sentences.py::[1mtest_expected_sentences_match_generated[/home/pessk/code/ea-python/generated_configs/output_regular.json][0m - Failed: Failed to read or parse /home/pessk/code/ea-python/expected_sentenc...
[31m========================= [31m[1m4 failed[0m, [32m29 passed[0m[31m in 0.69s[0m[31m =========================[0m
