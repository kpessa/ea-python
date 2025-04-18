============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-8.3.5, pluggy-1.5.0 -- /home/pessk/code/ea-python/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /home/pessk/code/ea-python
plugins: sugar-1.0.0
collecting ... collected 9 items

test_config_sentences.py::test_all_expected_mnemonics_found PASSED       [ 11%]
test_config_sentences.py::test_no_unexpected_mnemonics_without_expectations PASSED [ 22%]
test_config_sentences.py::test_sentence_verification FAILED              [ 33%]
test_config_structure.py::test_generated_config_key_order[output_regular.json] PASSED [ 44%]
test_config_structure.py::test_generated_config_key_order[output_cardiac.json] PASSED [ 55%]
tests/test_dcw_sentences.py::test_dcw_sentences_match_generated[/home/pessk/code/ea-python/generated_configs/output_cardiac.json] FAILED [ 66%]
tests/test_dcw_sentences.py::test_dcw_sentences_match_generated[/home/pessk/code/ea-python/generated_configs/output_regular.json] FAILED [ 77%]
tests/test_expected_sentences.py::test_expected_sentences_match_generated[/home/pessk/code/ea-python/generated_configs/output_cardiac.json] FAILED [ 88%]
tests/test_expected_sentences.py::test_expected_sentences_match_generated[/home/pessk/code/ea-python/generated_configs/output_regular.json] FAILED [100%]

=================================== FAILURES ===================================
__________________________ test_sentence_verification __________________________

expected_sentences = defaultdict(<class 'set'>, {'BMP': {'Blood, Timed Study collect, Once', 'Blood, ASAP collect, Once', 'Requested Draw D... Once'}, 'sodium phosphate': {'15 mmol, IVPB, Inj, q4hr (interval), Duration: 2 dose(s)', '15 mmol, IVPB, Inj, Once'}})
actual_orders_by_mnemonic = defaultdict(<class 'set'>, {'magnesium sulfate': {'2 g, IVPB, Premix, Once, infuse over 2 hr', '1 g, IVPB, Premix, Onc... {'1 g, IVPB, Inj, Once, infuse over 1 hr'}, 'magnesium oxide': {'400 mg, PO, Tab, q12h interval, Duration: 2 doses'}})

    def test_sentence_verification(expected_sentences, actual_orders_by_mnemonic):
        """Verify that generated sentences for each mnemonic exist in the expected extract.csv pool."""
        mnemonics_to_test = actual_orders_by_mnemonic.keys() # Test all generated mnemonics
    
        failures = [] # Store sentence mismatch errors
    
        for mnemonic in mnemonics_to_test:
            expected_set = expected_sentences.get(mnemonic, set()) # Sentences for this mnemonic in extract.csv
            found_set = actual_orders_by_mnemonic.get(mnemonic, set()) # Sentences generated in JSON
    
            # missing_expected = expected_set - found_set # Domain sentences not generated - IGNORE THIS CASE
            extra_generated = found_set - expected_set  # Generated sentences not in domain extract
    
            # Report generated sentences not matching the domain expectation for this mnemonic
            if extra_generated:
                error_detail = [f"Sentences generated for MNEMONIC '{mnemonic}' that DO NOT match any entry in {EXPECTED_EXTRACT_FILE}:"]
                for sentence in sorted(list(extra_generated)):
                    error_detail.append(f"    - {repr(sentence)}") # Use repr to show quotes clearly
                failures.append("\n".join(error_detail))
    
            # # Report domain sentences that were expected but not generated for this mnemonic - REMOVED
            # if missing_expected:
            #     error_detail = [f"Sentences defined for MNEMONIC '{mnemonic}' in {EXPECTED_EXTRACT_FILE} but NOT generated:"]
            #     for sentence in sorted(list(missing_expected)):
            #         error_detail.append(f"    - {sentence}")
            #     failures.append("\n".join(error_detail))
    
>       assert not failures, "\n\n" + "\n\n".join(failures)
E       AssertionError: 
E         
E         Sentences generated for MNEMONIC 'magnesium sulfate' that DO NOT match any entry in /home/pessk/code/ea-python/expected_sentences/extract.csv:
E             - '1 g, IVPB, Premix, Once, infuse over 1 hr'
E             - '2 g, IVPB, Premix, Once, infuse over 2 hr'
E             - '2 g, IVPB, Premix, q2h interval, Duration: 2 doses, infuse over 2 hr'
E         
E         Sentences generated for MNEMONIC 'potassium chloride extended release' that DO NOT match any entry in /home/pessk/code/ea-python/expected_sentences/extract.csv:
E             - '20 mEq, PO, ER tab, q2h interval, Duration: 2 doses'
E             - '20 mEq, PO, ER tab, q2h interval, Duration: 3 doses'
E         
E         Sentences generated for MNEMONIC 'potassium chloride' that DO NOT match any entry in /home/pessk/code/ea-python/expected_sentences/extract.csv:
E             - '20 mEq, Feeding Tube, Liq, q2h interval, Duration: 2 doses'
E             - '20 mEq, Feeding Tube, Liq, q2h interval, Duration: 3 doses'
E         
E         Sentences generated for MNEMONIC 'potassium chloride 10 mEq/100 mL intravenous solution' that DO NOT match any entry in /home/pessk/code/ea-python/expected_sentences/extract.csv:
E             - '10 mEq, IV, q1h, Duration: 2 doses, infuse over 1 hr'
E             - '10 mEq, IV, q1h, Duration: 4 doses, infuse over 1 hr'
E             - '10 mEq, IV, q1h, Duration: 6 doses, infuse over 1 hr'
E             - '10 mEq, IV, q1h, Duration: 8 doses, infuse over 1 hr'
E         
E         Sentences generated for MNEMONIC 'potassium chloride 20 mEq/100 mL intravenous solution' that DO NOT match any entry in /home/pessk/code/ea-python/expected_sentences/extract.csv:
E             - '20 mEq, IV, Once, infuse over 1 hr'
E             - '20 mEq, IV, q1h, Duration: 2 doses, infuse over 1 hr'
E             - '20 mEq, IV, q1h, Duration: 3 doses, infuse over 1 hr'
E             - '20 mEq, IV, q1h, Duration: 4 doses, infuse over 1 hr'
E             - '20 mEq, IV, q2h, Duration: 2 doses, infuse over 2 hr'
E             - '20 mEq, IV, q2h, Duration: 3 doses, infuse over 2 hr'
E             - '20 mEq, IV, q2h, Duration: 4 doses, infuse over 2 hr'
E         
E         Sentences generated for MNEMONIC 'K-Phos Neutral' that DO NOT match any entry in /home/pessk/code/ea-python/expected_sentences/extract.csv:
E             - '2 tab(s), PO, Tab, q2h interval, Duration: 2 doses'
E             - '2 tab(s), PO, Tab, q2h interval, Duration: 3 doses'
E         
E         Sentences generated for MNEMONIC 'sodium phosphate' that DO NOT match any entry in /home/pessk/code/ea-python/expected_sentences/extract.csv:
E             - '15 mmol, IVPB, Inj, q4h interval, Duration: 2 doses'
E         
E         Sentences generated for MNEMONIC 'calcium chloride' that DO NOT match any entry in /home/pessk/code/ea-python/expected_sentences/extract.csv:
E             - '1 g, IVPB, Inj, Once, infuse over 1 hr'
E         
E         Sentences generated for MNEMONIC 'magnesium oxide' that DO NOT match any entry in /home/pessk/code/ea-python/expected_sentences/extract.csv:
E             - '400 mg, PO, Tab, q12h interval, Duration: 2 doses'
E       assert not ["Sentences generated for MNEMONIC 'magnesium sulfate' that DO NOT match any entry in /home/pessk/code/ea-python/expected_sentences/extract.csv:\n    - '1 g, IVPB, Premix, Once, infuse over 1 hr'\n    - '2 g, IVPB, Premix, Once, infuse over 2 hr'\n    - '2 g, IVPB, Premix, q2h interval, Duration: 2 doses, infuse over 2 hr'", "Sentences generated for MNEMONIC 'potassium chloride extended release' that DO NOT match any entry in /home/pessk/code/ea-python/expected_sentences/extract.csv:\n    - '20 mEq, PO, ER tab, q2h interval, Duration: 2 doses'\n    - '20 mEq, PO, ER tab, q2h interval, Duration: 3 doses'", "Sentences generated for MNEMONIC 'potassium chloride' that DO NOT match any entry in /home/pessk/code/ea-python/expected_sentences/extract.csv:\n    - '20 mEq, Feeding Tube, Liq, q2h interval, Duration: 2 doses'\n    - '20 mEq, Feeding Tube, Liq, q2h interval, Duration: 3 doses'", "Sentences generated for MNEMONIC 'potassium chloride 10 mEq/100 mL intravenous solution' that DO NOT match any entry in /home/pessk/code/ea-python/expected_sentences/extract.csv:\n    - '10 mEq, IV, q1h, Duration: 2 doses, infuse over 1 hr'\n    - '10 mEq, IV, q1h, Duration: 4 doses, infuse over 1 hr'\n    - '10 mEq, IV, q1h, Duration: 6 doses, infuse over 1 hr'\n    - '10 mEq, IV, q1h, Duration: 8 doses, infuse over 1 hr'", "Sentences generated for MNEMONIC 'potassium chloride 20 mEq/100 mL intravenous solution' that DO NOT match any entry in /home/pessk/code/ea-python/expected_sentences/extract.csv:\n    - '20 mEq, IV, Once, infuse over 1 hr'\n    - '20 mEq, IV, q1h, Duration: 2 doses, infuse over 1 hr'\n    - '20 mEq, IV, q1h, Duration: 3 doses, infuse over 1 hr'\n    - '20 mEq, IV, q1h, Duration: 4 doses, infuse over 1 hr'\n    - '20 mEq, IV, q2h, Duration: 2 doses, infuse over 2 hr'\n    - '20 mEq, IV, q2h, Duration: 3 doses, infuse over 2 hr'\n    - '20 mEq, IV, q2h, Duration: 4 doses, infuse over 2 hr'", "Sentences generated for MNEMONIC 'K-Phos Neutral' that DO NOT match any entry in /home/pessk/code/ea-python/expected_sentences/extract.csv:\n    - '2 tab(s), PO, Tab, q2h interval, Duration: 2 doses'\n    - '2 tab(s), PO, Tab, q2h interval, Duration: 3 doses'", ...]

test_config_sentences.py:173: AssertionError
_ test_dcw_sentences_match_generated[/home/pessk/code/ea-python/generated_configs/output_cardiac.json] _

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
            dcw_mnemonic = dcw_entry.get('Mnemonic')
            dcw_range = dcw_entry.get('Lab Value Range') # Keep for context
            dcw_sentence = dcw_entry.get('Order_Sentence')
    
            if not all([protocol, dcw_electrolyte, dcw_mnemonic, dcw_sentence]):
                continue
    
            # --- Find JSON Counterpart (by mnemonic within the correct tab) ---
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
                                 if order.get('MNEMONIC') == dcw_mnemonic:
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
    
            # --- Fuzzy Compare DCW vs JSON ---
            comparison_score = 0
            if json_sentence_found:
                comparison_score = fuzz.token_sort_ratio(dcw_sentence, json_sentence_found)
            # else: json_sentence_found remains None
    
            # --- Compile Report Line ---
            report_line = f'''
    --- DCW Entry #{index} (Mnem: '{dcw_mnemonic}', Range: '{dcw_range}') ---
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
E       AssertionError: 
E         DCW vs JSON Sentence Comparison Report for output_cardiac.json:
E         
E         --- DCW Entry #0 (Mnem: 'magnesium sulfate', Range: 'Current serum level 1.8-2') ---
E           DCW Spec : '1 g, IVPB, Premix, Once, Infuse over: 1 hr'
E           JSON Gen : '1 g, IVPB, Premix, Once, infuse over 1 hr'
E           (Score DCW vs JSON: 100%)
E         
E         --- DCW Entry #1 (Mnem: 'magnesium sulfate', Range: 'Current serum level 1.4-1.7') ---
E           DCW Spec : '2 g, IVPB, Premix, Once, Infuse over: 2 hr'
E           JSON Gen : '1 g, IVPB, Premix, Once, infuse over 1 hr'
E           (Score DCW vs JSON: 95%)
E         
E         --- DCW Entry #2 (Mnem: 'magnesium sulfate', Range: 'Current serum level < 1.4') ---
E           DCW Spec : '2 g, IVPB, Premix, q2h interval, Duration: 2 doses, infuse over 2 hr'
E           JSON Gen : '1 g, IVPB, Premix, Once, infuse over 1 hr'
E           (Score DCW vs JSON: 61%)
E         
E         --- DCW Entry #3 (Mnem: 'potassium chloride extended release', Range: 'Current serum level 3.6-3.9') ---
E           DCW Spec : '20 mEq, PO, ER tab, Once'
E           JSON Gen : '20 mEq, PO, ER tab, Once'
E           (Score DCW vs JSON: 100%)
E         
E         --- DCW Entry #4 (Mnem: 'potassium chloride', Range: 'Current serum level 3.6-3.9') ---
E           DCW Spec : '20 mEq, Feeding Tube, liq, Once'
E           JSON Gen : '20 mEq, Feeding Tube, Liq, Once'
E           (Score DCW vs JSON: 100%)
E         
E         --- DCW Entry #5 (Mnem: 'potassium chloride 10 mEq/100 mL intravenous solution', Range: 'Current serum level 3.6-3.9') ---
E           DCW Spec : '10 mEq, IV, q1h, Duration: 2 doses, Infuse over: 1 hr'
E           JSON Gen : '10 mEq, IV, q1h, Duration: 2 doses, infuse over 1 hr'
E           (Score DCW vs JSON: 100%)
E         
E         --- DCW Entry #6 (Mnem: 'potassium chloride 20 mEq/100 mL intravenous solution', Range: 'Current serum level 3.6-3.9') ---
E           DCW Spec : '20 mEq, IV, q1h, Once, Infuse over: 1 hr'
E           JSON Gen : '20 mEq, IV, Once, infuse over 1 hr'
E           (Score DCW vs JSON: 94%)
E         
E         --- DCW Entry #7 (Mnem: 'potassium chloride extended release', Range: 'Current serum level 3.2-3.5') ---
E           DCW Spec : '20 mEq, PO, ER tab, q2h interval, Duration: 2 doses'
E           JSON Gen : '20 mEq, PO, ER tab, Once'
E           (Score DCW vs JSON: 51%)
E         
E         --- DCW Entry #8 (Mnem: 'potassium chloride', Range: 'Current serum level 3.2-3.5') ---
E           DCW Spec : '20 mEq, Feeding Tube, liq, q2h interval, Duration: 2 doses'
E           JSON Gen : '20 mEq, Feeding Tube, Liq, Once'
E           (Score DCW vs JSON: 59%)
E         
E         --- DCW Entry #9 (Mnem: 'potassium chloride 10 mEq/100 mL intravenous solution', Range: 'Current serum level 3.2-3.5') ---
E           DCW Spec : '10 mEq, IV, q1h, Duration: 4 doses, Infuse over: 1 hr'
E           JSON Gen : '10 mEq, IV, q1h, Duration: 2 doses, infuse over 1 hr'
E           (Score DCW vs JSON: 98%)
E         
E         --- DCW Entry #10 (Mnem: 'potassium chloride 20 mEq/100 mL intravenous solution', Range: 'Current serum level 3.2-3.5') ---
E           DCW Spec : '20 mEq, IV, q1h, Duration: 2 doses, Infuse over: 1 hr'
E           JSON Gen : '20 mEq, IV, Once, infuse over 1 hr'
E           (Score DCW vs JSON: 67%)
E         
E         --- DCW Entry #11 (Mnem: 'potassium chloride extended release', Range: 'Current serum level 2.8-3.1') ---
E           DCW Spec : '20 mEq, PO, ER tab, q2h interval, Duration: 3 doses'
E           JSON Gen : '20 mEq, PO, ER tab, Once'
E           (Score DCW vs JSON: 51%)
E         
E         --- DCW Entry #12 (Mnem: 'potassium chloride', Range: 'Current serum level 2.8-3.1') ---
E           DCW Spec : '20 mEq, Feeding Tube, liq, q2h interval, Duration: 3 doses'
E           JSON Gen : '20 mEq, Feeding Tube, Liq, Once'
E           (Score DCW vs JSON: 59%)
E         
E         --- DCW Entry #13 (Mnem: 'potassium chloride 10 mEq/100 mL intravenous solution', Range: 'Current serum level 2.8-3.1') ---
E           DCW Spec : '10 mEq, IV, q1h, Duration: 6 doses, Infuse over: 1 hr'
E           JSON Gen : '10 mEq, IV, q1h, Duration: 2 doses, infuse over 1 hr'
E           (Score DCW vs JSON: 98%)
E         
E         --- DCW Entry #14 (Mnem: 'potassium chloride 20 mEq/100 mL intravenous solution', Range: 'Current serum level 2.8-3.1') ---
E           DCW Spec : '20 mEq, IV, q1h, Duration: 3 doses, Infuse over: 1 hr'
E           JSON Gen : '20 mEq, IV, Once, infuse over 1 hr'
E           (Score DCW vs JSON: 67%)
E         
E         --- DCW Entry #15 (Mnem: 'potassium chloride 10 mEq/100 mL intravenous solution', Range: 'Current serum level < 2.8') ---
E           DCW Spec : '10 mEq, IV, q1h, Duration: 8 doses, Infuse over: 1 hr'
E           JSON Gen : '10 mEq, IV, q1h, Duration: 2 doses, infuse over 1 hr'
E           (Score DCW vs JSON: 98%)
E         
E         --- DCW Entry #16 (Mnem: 'potassium chloride 20 mEq/100 mL intravenous solution', Range: 'Current serum level < 2.8') ---
E           DCW Spec : '20 mEq, IV, q1h, Duration: 4 doses, Infuse over: 1 hr'
E           JSON Gen : '20 mEq, IV, Once, infuse over 1 hr'
E           (Score DCW vs JSON: 67%)
E         
E         --- DCW Entry #17 (Mnem: 'K-Phos Neutral (brand name synonym under primary potassium phosphate-sodium phosphate)', Range: 'Current serum level 1.6-2.0') ---
E           DCW Spec : '2 tabs, q2h interval, PO, tab, Duration: 2 doses'
E           JSON Gen : *** NOT FOUND in JSON Tab ***
E           (Score DCW vs JSON: 0%)
E         
E         --- DCW Entry #18 (Mnem: 'sodium phosphate', Range: 'Current serum level 1.6-2.0') ---
E           DCW Spec : '15 mmol, IVPB, inj, Once'
E           JSON Gen : '15 mmol, IVPB, Inj, Once'
E           (Score DCW vs JSON: 100%)
E         
E         --- DCW Entry #19 (Mnem: 'K-Phos Neutral', Range: 'Current serum level 1.0-1.5') ---
E           DCW Spec : '2 tabs, q2h interval, PO, tab, Duration: 3 doses'
E           JSON Gen : '2 tab(s), PO, Tab, q2h interval, Duration: 2 doses'
E           (Score DCW vs JSON: 94%)
E         
E         --- DCW Entry #20 (Mnem: 'sodium phosphate', Range: 'Current serum level 1.0-1.5') ---
E           DCW Spec : '15 mmol, IVPB, inj, q4h interval, Duration: 2 dose'
E           JSON Gen : '15 mmol, IVPB, Inj, Once'
E           (Score DCW vs JSON: 52%)
E         
E         --- DCW Entry #21 (Mnem: 'sodium phosphate', Range: 'Current serum level <1.0') ---
E           DCW Spec : '15 mmol, IVPB, inj, q4h interval, Duration: 2 dose'
E           JSON Gen : '15 mmol, IVPB, Inj, Once'
E           (Score DCW vs JSON: 52%)
E         
E         --- DCW Entry #22 (Mnem: 'calcium chloride', Range: 'iCal < 1.1') ---
E           DCW Spec : '1 g, IVPB, Inj, Once, Infuse over: 1 hr'
E           JSON Gen : '1 g, IVPB, Inj, Once, infuse over 1 hr'
E           (Score DCW vs JSON: 100%)
E       assert not "\nDCW vs JSON Sentence Comparison Report for output_cardiac.json:\n\n--- DCW Entry #0 (Mnem: 'magnesium sulfate', Range: 'Current serum level 1.8-2') ---\n  DCW Spec : '1 g, IVPB, Premix, Once, Infuse over: 1 hr'\n  JSON Gen : '1 g, IVPB, Premix, Once, infuse over 1 hr'\n  (Score DCW vs JSON: 100%)\n\n--- DCW Entry #1 (Mnem: 'magnesium sulfate', Range: 'Current serum level 1.4-1.7') ---\n  DCW Spec : '2 g, IVPB, Premix, Once, Infuse over: 2 hr'\n  JSON Gen : '1 g, IVPB, Premix, Once, infuse over 1 hr'\n  (Score DCW vs JSON: 95%)\n\n--- DCW Entry #2 (Mnem: 'magnesium sulfate', Range: 'Current serum level < 1.4') ---\n  DCW Spec : '2 g, IVPB, Premix, q2h interval, Duration: 2 doses, infuse over 2 hr'\n  JSON Gen : '1 g, IVPB, Premix, Once, infuse over 1 hr'\n  (Score DCW vs JSON: 61%)\n\n--- DCW Entry #3 (Mnem: 'potassium chloride extended release', Range: 'Current serum level 3.6-3.9') ---\n  DCW Spec : '20 mEq, PO, ER tab, Once'\n  JSON Gen : '20 mEq, PO, ER tab, Once'\n  (Score DCW vs JSON: 100%)\n\n--- DCW Entry #4 (Mnem: 'potassium chloride', Range: 'Current serum level 3.6-3.9') ---\n  DCW Spec : '20 mEq, Feeding Tube, liq, Once'\n  JSON Gen : '20 mEq, Feeding Tube, Liq, Onc...ration: 2 doses'\n  JSON Gen : *** NOT FOUND in JSON Tab ***\n  (Score DCW vs JSON: 0%)\n\n--- DCW Entry #18 (Mnem: 'sodium phosphate', Range: 'Current serum level 1.6-2.0') ---\n  DCW Spec : '15 mmol, IVPB, inj, Once'\n  JSON Gen : '15 mmol, IVPB, Inj, Once'\n  (Score DCW vs JSON: 100%)\n\n--- DCW Entry #19 (Mnem: 'K-Phos Neutral', Range: 'Current serum level 1.0-1.5') ---\n  DCW Spec : '2 tabs, q2h interval, PO, tab, Duration: 3 doses'\n  JSON Gen : '2 tab(s), PO, Tab, q2h interval, Duration: 2 doses'\n  (Score DCW vs JSON: 94%)\n\n--- DCW Entry #20 (Mnem: 'sodium phosphate', Range: 'Current serum level 1.0-1.5') ---\n  DCW Spec : '15 mmol, IVPB, inj, q4h interval, Duration: 2 dose'\n  JSON Gen : '15 mmol, IVPB, Inj, Once'\n  (Score DCW vs JSON: 52%)\n\n--- DCW Entry #21 (Mnem: 'sodium phosphate', Range: 'Current serum level <1.0') ---\n  DCW Spec : '15 mmol, IVPB, inj, q4h interval, Duration: 2 dose'\n  JSON Gen : '15 mmol, IVPB, Inj, Once'\n  (Score DCW vs JSON: 52%)\n\n--- DCW Entry #22 (Mnem: 'calcium chloride', Range: 'iCal < 1.1') ---\n  DCW Spec : '1 g, IVPB, Inj, Once, Infuse over: 1 hr'\n  JSON Gen : '1 g, IVPB, Inj, Once, infuse over 1 hr'\n  (Score DCW vs JSON: 100%)"

tests/test_dcw_sentences.py:270: AssertionError
----------------------------- Captured stdout call -----------------------------
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 1.8-2' (cleaned: '1.8-2')
DEBUG _parse_range_string: Failed to parse range from: 'Magnesium: 1.8 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>' (cleaned: 'magnesium: 1.8 - 2.0 mg/dl<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br>')

DEBUG ranges_match: Comparing DCW='Current serum level 1.8-2' (Parsed: None-None) vs JSON_Section='Magnesium: 1.8 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 1.4-1.7' (cleaned: '1.4-1.7')
DEBUG _parse_range_string: Failed to parse range from: 'Magnesium: 1.8 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>' (cleaned: 'magnesium: 1.8 - 2.0 mg/dl<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br>')

DEBUG ranges_match: Comparing DCW='Current serum level 1.4-1.7' (Parsed: None-None) vs JSON_Section='Magnesium: 1.8 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level < 1.4' (cleaned: '< 1.4')
DEBUG _parse_range_string: Failed to parse range from: 'Magnesium: 1.8 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>' (cleaned: 'magnesium: 1.8 - 2.0 mg/dl<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br>')

DEBUG ranges_match: Comparing DCW='Current serum level < 1.4' (Parsed: None-None) vs JSON_Section='Magnesium: 1.8 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 3.6-3.9' (cleaned: '3.6-3.9')
DEBUG _parse_range_string: Failed to parse range from: 'Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'potassium: 3.6 - 3.9 mmol/l<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level 3.6-3.9' (Parsed: None-None) vs JSON_Section='Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 3.6-3.9' (cleaned: '3.6-3.9')
DEBUG _parse_range_string: Failed to parse range from: 'Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'potassium: 3.6 - 3.9 mmol/l<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level 3.6-3.9' (Parsed: None-None) vs JSON_Section='Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 3.6-3.9' (cleaned: '3.6-3.9')
DEBUG _parse_range_string: Failed to parse range from: 'Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'potassium: 3.6 - 3.9 mmol/l<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level 3.6-3.9' (Parsed: None-None) vs JSON_Section='Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 3.6-3.9' (cleaned: '3.6-3.9')
DEBUG _parse_range_string: Failed to parse range from: 'Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'potassium: 3.6 - 3.9 mmol/l<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level 3.6-3.9' (Parsed: None-None) vs JSON_Section='Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 3.2-3.5' (cleaned: '3.2-3.5')
DEBUG _parse_range_string: Failed to parse range from: 'Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'potassium: 3.6 - 3.9 mmol/l<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level 3.2-3.5' (Parsed: None-None) vs JSON_Section='Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 3.2-3.5' (cleaned: '3.2-3.5')
DEBUG _parse_range_string: Failed to parse range from: 'Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'potassium: 3.6 - 3.9 mmol/l<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level 3.2-3.5' (Parsed: None-None) vs JSON_Section='Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 3.2-3.5' (cleaned: '3.2-3.5')
DEBUG _parse_range_string: Failed to parse range from: 'Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'potassium: 3.6 - 3.9 mmol/l<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level 3.2-3.5' (Parsed: None-None) vs JSON_Section='Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 3.2-3.5' (cleaned: '3.2-3.5')
DEBUG _parse_range_string: Failed to parse range from: 'Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'potassium: 3.6 - 3.9 mmol/l<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level 3.2-3.5' (Parsed: None-None) vs JSON_Section='Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 2.8-3.1' (cleaned: '2.8-3.1')
DEBUG _parse_range_string: Failed to parse range from: 'Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'potassium: 3.6 - 3.9 mmol/l<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: None-None) vs JSON_Section='Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 2.8-3.1' (cleaned: '2.8-3.1')
DEBUG _parse_range_string: Failed to parse range from: 'Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'potassium: 3.6 - 3.9 mmol/l<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: None-None) vs JSON_Section='Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 2.8-3.1' (cleaned: '2.8-3.1')
DEBUG _parse_range_string: Failed to parse range from: 'Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'potassium: 3.6 - 3.9 mmol/l<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: None-None) vs JSON_Section='Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 2.8-3.1' (cleaned: '2.8-3.1')
DEBUG _parse_range_string: Failed to parse range from: 'Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'potassium: 3.6 - 3.9 mmol/l<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: None-None) vs JSON_Section='Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level < 2.8' (cleaned: '< 2.8')
DEBUG _parse_range_string: Failed to parse range from: 'Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'potassium: 3.6 - 3.9 mmol/l<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-None) vs JSON_Section='Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level < 2.8' (cleaned: '< 2.8')
DEBUG _parse_range_string: Failed to parse range from: 'Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'potassium: 3.6 - 3.9 mmol/l<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-None) vs JSON_Section='Potassium: 3.6 - 3.9 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 1.6-2.0' (cleaned: '1.6-2.0')
DEBUG _parse_range_string: Failed to parse range from: 'Phosphorus: 1.6 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'phosphorus: 1.6 - 2.0 mg/dl<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level 1.6-2.0' (Parsed: None-None) vs JSON_Section='Phosphorus: 1.6 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 1.6-2.0' (cleaned: '1.6-2.0')
DEBUG _parse_range_string: Failed to parse range from: '<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br>IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck phosphorous & calcium levels with next AM labs.</small>' (cleaned: '<strong style="font-size: 18px; font-weight: bold; color: #333;">step 2 - order corresponding follow-up lab(s):</strong><br>iv - labs:<br><small style="font-weight: normal;">monitoring: recheck phosphorous & calcium levels with next am labs.</small>')

DEBUG ranges_match: Comparing DCW='Current serum level 1.6-2.0' (Parsed: None-None) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br>IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck phosphorous & calcium levels with next AM labs.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 1.6-2.0' (cleaned: '1.6-2.0')
DEBUG _parse_range_string: Failed to parse range from: 'Phosphorus: 1.0 - 1.5 mg/dL<br><span style="color: red; font-weight: bold;">NOTIFY PHYSICIAN if less than 1.1 mg/dL<br>CRITICALLY LOW RESULT</span> <br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'phosphorus: 1.0 - 1.5 mg/dl<br><span style="color: red; font-weight: bold;">notify physician if less than 1.1 mg/dl<br>critly low result</span> <br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level 1.6-2.0' (Parsed: None-None) vs JSON_Section='Phosphorus: 1.0 - 1.5 mg/dL<br><span style="color: red; font-weight: bold;">NOTIFY PHYSICIAN if less than 1.1 mg/dL<br>CRITICALLY LOW RESULT</span> <br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 1.6-2.0' (cleaned: '1.6-2.0')
DEBUG _parse_range_string: Failed to parse range from: '<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br>ORAL - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck phosphorous & calcium levels with next AM labs.</small>' (cleaned: '<strong style="font-size: 18px; font-weight: bold; color: #333;">step 2 - order corresponding follow-up lab(s):</strong><br>oral - labs:<br><small style="font-weight: normal;">monitoring: recheck phosphorous & calcium levels with next am labs.</small>')

DEBUG ranges_match: Comparing DCW='Current serum level 1.6-2.0' (Parsed: None-None) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br>ORAL - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck phosphorous & calcium levels with next AM labs.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 1.6-2.0' (cleaned: '1.6-2.0')
DEBUG _parse_range_string: Failed to parse range from: 'IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck phosphorous & calcium levels 2 hrs after infusion.</small>' (cleaned: 'iv - labs:<br><small style="font-weight: normal;">monitoring: recheck phosphorous & calcium levels 2 hrs after infusion.</small>')

DEBUG ranges_match: Comparing DCW='Current serum level 1.6-2.0' (Parsed: None-None) vs JSON_Section='IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck phosphorous & calcium levels 2 hrs after infusion.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 1.6-2.0' (cleaned: '1.6-2.0')
DEBUG _parse_range_string: Failed to parse range from: 'Phosphorus: < 1.0 mg/dL<br><span style="color: red; font-weight: bold;">NOTIFY PHYSICIAN if less than 1.1 mg/dL<br>CRITICALLY LOW RESULT</span> <br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'phosphorus: < 1.0 mg/dl<br><span style="color: red; font-weight: bold;">notify physician if less than 1.1 mg/dl<br>critly low result</span> <br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level 1.6-2.0' (Parsed: None-None) vs JSON_Section='Phosphorus: < 1.0 mg/dL<br><span style="color: red; font-weight: bold;">NOTIFY PHYSICIAN if less than 1.1 mg/dL<br>CRITICALLY LOW RESULT</span> <br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 1.6-2.0' (cleaned: '1.6-2.0')
DEBUG _parse_range_string: Failed to parse range from: '<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br>IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck phosphorous & calcium levels 2 hrs after infusion.</small>' (cleaned: '<strong style="font-size: 18px; font-weight: bold; color: #333;">step 2 - order corresponding follow-up lab(s):</strong><br>iv - labs:<br><small style="font-weight: normal;">monitoring: recheck phosphorous & calcium levels 2 hrs after infusion.</small>')

DEBUG ranges_match: Comparing DCW='Current serum level 1.6-2.0' (Parsed: None-None) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br>IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck phosphorous & calcium levels 2 hrs after infusion.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 1.6-2.0' (cleaned: '1.6-2.0')
DEBUG _parse_range_string: Failed to parse range from: 'Phosphorous Lab Orders' (cleaned: 'phosphorous lab orders')

DEBUG ranges_match: Comparing DCW='Current serum level 1.6-2.0' (Parsed: None-None) vs JSON_Section='Phosphorous Lab Orders' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 1.6-2.0' (cleaned: '1.6-2.0')
DEBUG _parse_range_string: Failed to parse range from: 'Phosphorus: 1.6 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'phosphorus: 1.6 - 2.0 mg/dl<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level 1.6-2.0' (Parsed: None-None) vs JSON_Section='Phosphorus: 1.6 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 1.0-1.5' (cleaned: '1.0-1.5')
DEBUG _parse_range_string: Failed to parse range from: 'Phosphorus: 1.6 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'phosphorus: 1.6 - 2.0 mg/dl<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level 1.0-1.5' (Parsed: None-None) vs JSON_Section='Phosphorus: 1.6 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 1.0-1.5' (cleaned: '1.0-1.5')
DEBUG _parse_range_string: Failed to parse range from: 'Phosphorus: 1.6 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'phosphorus: 1.6 - 2.0 mg/dl<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level 1.0-1.5' (Parsed: None-None) vs JSON_Section='Phosphorus: 1.6 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level <1.0' (cleaned: '<1.0')
DEBUG _parse_range_string: Failed to parse range from: 'Phosphorus: 1.6 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'phosphorus: 1.6 - 2.0 mg/dl<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level <1.0' (Parsed: None-None) vs JSON_Section='Phosphorus: 1.6 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'iCal < 1.1' (cleaned: '< 1.1')
DEBUG _parse_range_string: Failed to parse range from: 'Ionized Calcium: < 1.1 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>' (cleaned: 'ionized calcium: < 1.1 mg/dl<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br>')

DEBUG ranges_match: Comparing DCW='iCal < 1.1' (Parsed: None-None) vs JSON_Section='Ionized Calcium: < 1.1 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
_ test_dcw_sentences_match_generated[/home/pessk/code/ea-python/generated_configs/output_regular.json] _

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
            dcw_mnemonic = dcw_entry.get('Mnemonic')
            dcw_range = dcw_entry.get('Lab Value Range') # Keep for context
            dcw_sentence = dcw_entry.get('Order_Sentence')
    
            if not all([protocol, dcw_electrolyte, dcw_mnemonic, dcw_sentence]):
                continue
    
            # --- Find JSON Counterpart (by mnemonic within the correct tab) ---
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
                                 if order.get('MNEMONIC') == dcw_mnemonic:
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
    
            # --- Fuzzy Compare DCW vs JSON ---
            comparison_score = 0
            if json_sentence_found:
                comparison_score = fuzz.token_sort_ratio(dcw_sentence, json_sentence_found)
            # else: json_sentence_found remains None
    
            # --- Compile Report Line ---
            report_line = f'''
    --- DCW Entry #{index} (Mnem: '{dcw_mnemonic}', Range: '{dcw_range}') ---
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
E       AssertionError: 
E         DCW vs JSON Sentence Comparison Report for output_regular.json:
E         
E         --- DCW Entry #0 (Mnem: 'magnesium oxide', Range: 'Current serum level 1.4-1.5') ---
E           DCW Spec : '400 mg, PO, tab,  q12h interval, Duration: 2 doses'
E           JSON Gen : '400 mg, PO, Tab, q12h interval, Duration: 2 doses'
E           (Score DCW vs JSON: 100%)
E         
E         --- DCW Entry #1 (Mnem: 'magnesium sulfate', Range: 'Current serum level 1.4-1.5') ---
E           DCW Spec : '2 g, IVPB, Premix, Once, Infuse over: 2 hr'
E           JSON Gen : '2 g, IVPB, Premix, Once, infuse over 2 hr'
E           (Score DCW vs JSON: 100%)
E         
E         --- DCW Entry #2 (Mnem: 'magnesium sulfate', Range: 'Current serum level < 1.4') ---
E           DCW Spec : '2 g, IVPB, Premix, q2h interval, Duration: 2 doses, Infuse over: 2 hr'
E           JSON Gen : '2 g, IVPB, Premix, Once, infuse over 2 hr'
E           (Score DCW vs JSON: 65%)
E         
E         --- DCW Entry #3 (Mnem: 'potassium chloride extended release', Range: 'Current serum level 3.2-3.4') ---
E           DCW Spec : '20 mEq, PO, ER tab, q2h interval, Duration: 2 doses'
E           JSON Gen : '20 mEq, PO, ER tab, q2h interval, Duration: 2 doses'
E           (Score DCW vs JSON: 100%)
E         
E         --- DCW Entry #4 (Mnem: 'potassium chloride', Range: 'Current serum level 3.2-3.4') ---
E           DCW Spec : '20 mEq, Feeding Tube, liq, q2h interval, Duration: 2 doses'
E           JSON Gen : '20 mEq, Feeding Tube, Liq, q2h interval, Duration: 2 doses'
E           (Score DCW vs JSON: 100%)
E         
E         --- DCW Entry #5 (Mnem: 'potassium chloride 10 mEq/100 mL intravenous solution', Range: 'Current serum level 3.2-3.4') ---
E           DCW Spec : '10 mEq, IV, q1h, Duration: 4 doses, Infuse over: 1 hr'
E           JSON Gen : '10 mEq, IV, q1h, Duration: 4 doses, infuse over 1 hr'
E           (Score DCW vs JSON: 100%)
E         
E         --- DCW Entry #6 (Mnem: 'potassium chloride 20 mEq/100 mL intravenous solution', Range: 'Current serum level 3.2-3.4') ---
E           DCW Spec : '20 mEq, IV, q2h interval, Duration: 2 doses, Infuse over: 2 hr'
E           JSON Gen : '20 mEq, IV, q2h, Duration: 2 doses, infuse over 2 hr'
E           (Score DCW vs JSON: 91%)
E         
E         --- DCW Entry #7 (Mnem: 'potassium chloride extended release', Range: 'Current serum level 2.8-3.1') ---
E           DCW Spec : '20 mEq, PO, ER tab, q2h interval, Duration: 3 doses'
E           JSON Gen : '20 mEq, PO, ER tab, q2h interval, Duration: 2 doses'
E           (Score DCW vs JSON: 96%)
E         
E         --- DCW Entry #8 (Mnem: 'potassium chloride', Range: 'Current serum level 2.8-3.1') ---
E           DCW Spec : '20 mEq, Feeding Tube, liq, q2h interval, Duration: 3 doses'
E           JSON Gen : '20 mEq, Feeding Tube, Liq, q2h interval, Duration: 2 doses'
E           (Score DCW vs JSON: 96%)
E         
E         --- DCW Entry #9 (Mnem: 'potassium chloride 10 mEq/100 mL intravenous solution', Range: 'Current serum level 2.8-3.1') ---
E           DCW Spec : '10 mEq, IV, q1h, Duration: 6 doses, Infuse over: 1 hr'
E           JSON Gen : '10 mEq, IV, q1h, Duration: 4 doses, infuse over 1 hr'
E           (Score DCW vs JSON: 98%)
E         
E         --- DCW Entry #10 (Mnem: 'potassium chloride 20 mEq/100 mL intravenous solution', Range: 'Current serum level 2.8-3.1') ---
E           DCW Spec : '20 mEq, IV, q2h interval, Duration: 3 doses, Infuse over: 2 hr'
E           JSON Gen : '20 mEq, IV, q2h, Duration: 2 doses, infuse over 2 hr'
E           (Score DCW vs JSON: 87%)
E         
E         --- DCW Entry #11 (Mnem: 'potassium chloride 10 mEq/100 mL intravenous solution', Range: 'Current serum level < 2.8') ---
E           DCW Spec : '10 mEq, IV, q1h, Duration: 8 doses, Infuse over: 1 hr'
E           JSON Gen : '10 mEq, IV, q1h, Duration: 4 doses, infuse over 1 hr'
E           (Score DCW vs JSON: 98%)
E         
E         --- DCW Entry #12 (Mnem: 'potassium chloride 20 mEq/100 mL intravenous solution', Range: 'Current serum level < 2.8') ---
E           DCW Spec : '20 mEq, IV, q2h interval, Duration: 4 doses, Infuse over: 2 hr'
E           JSON Gen : '20 mEq, IV, q2h, Duration: 2 doses, infuse over 2 hr'
E           (Score DCW vs JSON: 87%)
E         
E         --- DCW Entry #13 (Mnem: 'K-Phos Neutral (brand name synonym under primary potassium phosphate-sodium phosphate)', Range: 'Current serum level 1.6-2.0') ---
E           DCW Spec : '2 tabs, q2h interval, PO, tab, Duration: 2 doses'
E           JSON Gen : *** NOT FOUND in JSON Tab ***
E           (Score DCW vs JSON: 0%)
E         
E         --- DCW Entry #14 (Mnem: 'sodium phosphate', Range: 'Current serum level 1.6-2.0') ---
E           DCW Spec : '15 mmol, IVPB, inj, Once'
E           JSON Gen : '15 mmol, IVPB, Inj, Once'
E           (Score DCW vs JSON: 100%)
E         
E         --- DCW Entry #15 (Mnem: 'K-Phos Neutral', Range: 'Current serum level 1.0-1.5') ---
E           DCW Spec : '2 tabs, q2h interval, PO, tab, Duration: 3 doses'
E           JSON Gen : '2 tab(s), PO, Tab, q2h interval, Duration: 2 doses'
E           (Score DCW vs JSON: 94%)
E         
E         --- DCW Entry #16 (Mnem: 'sodium phosphate', Range: 'Current serum level 1.0-1.5') ---
E           DCW Spec : '15 mmol, IVPB, inj, q4h interval, Duration: 2 dose'
E           JSON Gen : '15 mmol, IVPB, Inj, Once'
E           (Score DCW vs JSON: 52%)
E         
E         --- DCW Entry #17 (Mnem: 'sodium phosphate', Range: 'Current serum level <1.0') ---
E           DCW Spec : '15 mmol, IVPB, inj, q4h interval, Duration: 2 dose'
E           JSON Gen : '15 mmol, IVPB, Inj, Once'
E           (Score DCW vs JSON: 52%)
E       assert not "\nDCW vs JSON Sentence Comparison Report for output_regular.json:\n\n--- DCW Entry #0 (Mnem: 'magnesium oxide', Range: 'Current serum level 1.4-1.5') ---\n  DCW Spec : '400 mg, PO, tab,  q12h interval, Duration: 2 doses'\n  JSON Gen : '400 mg, PO, Tab, q12h interval, Duration: 2 doses'\n  (Score DCW vs JSON: 100%)\n\n--- DCW Entry #1 (Mnem: 'magnesium sulfate', Range: 'Current serum level 1.4-1.5') ---\n  DCW Spec : '2 g, IVPB, Premix, Once, Infuse over: 2 hr'\n  JSON Gen : '2 g, IVPB, Premix, Once, infuse over 2 hr'\n  (Score DCW vs JSON: 100%)\n\n--- DCW Entry #2 (Mnem: 'magnesium sulfate', Range: 'Current serum level < 1.4') ---\n  DCW Spec : '2 g, IVPB, Premix, q2h interval, Duration: 2 doses, Infuse over: 2 hr'\n  JSON Gen : '2 g, IVPB, Premix, Once, infuse over 2 hr'\n  (Score DCW vs JSON: 65%)\n\n--- DCW Entry #3 (Mnem: 'potassium chloride extended release', Range: 'Current serum level 3.2-3.4') ---\n  DCW Spec : '20 mEq, PO, ER tab, q2h interval, Duration: 2 doses'\n  JSON Gen : '20 mEq, PO, ER tab, q2h interval, Duration: 2 doses'\n  (Score DCW vs JSON: 100%)\n\n--- DCW Entry #4 (Mnem: 'potassium chloride', Range: 'Current serum level 3.2-3.4') ---\n  DCW Spec : '20 mEq...87%)\n\n--- DCW Entry #13 (Mnem: 'K-Phos Neutral (brand name synonym under primary potassium phosphate-sodium phosphate)', Range: 'Current serum level 1.6-2.0') ---\n  DCW Spec : '2 tabs, q2h interval, PO, tab, Duration: 2 doses'\n  JSON Gen : *** NOT FOUND in JSON Tab ***\n  (Score DCW vs JSON: 0%)\n\n--- DCW Entry #14 (Mnem: 'sodium phosphate', Range: 'Current serum level 1.6-2.0') ---\n  DCW Spec : '15 mmol, IVPB, inj, Once'\n  JSON Gen : '15 mmol, IVPB, Inj, Once'\n  (Score DCW vs JSON: 100%)\n\n--- DCW Entry #15 (Mnem: 'K-Phos Neutral', Range: 'Current serum level 1.0-1.5') ---\n  DCW Spec : '2 tabs, q2h interval, PO, tab, Duration: 3 doses'\n  JSON Gen : '2 tab(s), PO, Tab, q2h interval, Duration: 2 doses'\n  (Score DCW vs JSON: 94%)\n\n--- DCW Entry #16 (Mnem: 'sodium phosphate', Range: 'Current serum level 1.0-1.5') ---\n  DCW Spec : '15 mmol, IVPB, inj, q4h interval, Duration: 2 dose'\n  JSON Gen : '15 mmol, IVPB, Inj, Once'\n  (Score DCW vs JSON: 52%)\n\n--- DCW Entry #17 (Mnem: 'sodium phosphate', Range: 'Current serum level <1.0') ---\n  DCW Spec : '15 mmol, IVPB, inj, q4h interval, Duration: 2 dose'\n  JSON Gen : '15 mmol, IVPB, Inj, Once'\n  (Score DCW vs JSON: 52%)"

tests/test_dcw_sentences.py:270: AssertionError
----------------------------- Captured stdout call -----------------------------
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 1.4-1.5' (cleaned: '1.4-1.5')
DEBUG _parse_range_string: Failed to parse range from: 'Magnesium: 1.4 - 1.5 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'magnesium: 1.4 - 1.5 mg/dl<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level 1.4-1.5' (Parsed: None-None) vs JSON_Section='Magnesium: 1.4 - 1.5 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 1.4-1.5' (cleaned: '1.4-1.5')
DEBUG _parse_range_string: Failed to parse range from: 'Magnesium: 1.4 - 1.5 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'magnesium: 1.4 - 1.5 mg/dl<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level 1.4-1.5' (Parsed: None-None) vs JSON_Section='Magnesium: 1.4 - 1.5 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level < 1.4' (cleaned: '< 1.4')
DEBUG _parse_range_string: Failed to parse range from: 'Magnesium: 1.4 - 1.5 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'magnesium: 1.4 - 1.5 mg/dl<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level < 1.4' (Parsed: None-None) vs JSON_Section='Magnesium: 1.4 - 1.5 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 3.2-3.4' (cleaned: '3.2-3.4')
DEBUG _parse_range_string: Failed to parse range from: 'Potassium: 3.2 - 3.4 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'potassium: 3.2 - 3.4 mmol/l<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level 3.2-3.4' (Parsed: None-None) vs JSON_Section='Potassium: 3.2 - 3.4 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 3.2-3.4' (cleaned: '3.2-3.4')
DEBUG _parse_range_string: Failed to parse range from: 'Potassium: 3.2 - 3.4 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'potassium: 3.2 - 3.4 mmol/l<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level 3.2-3.4' (Parsed: None-None) vs JSON_Section='Potassium: 3.2 - 3.4 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 3.2-3.4' (cleaned: '3.2-3.4')
DEBUG _parse_range_string: Failed to parse range from: 'Potassium: 3.2 - 3.4 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'potassium: 3.2 - 3.4 mmol/l<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level 3.2-3.4' (Parsed: None-None) vs JSON_Section='Potassium: 3.2 - 3.4 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 3.2-3.4' (cleaned: '3.2-3.4')
DEBUG _parse_range_string: Failed to parse range from: 'Potassium: 3.2 - 3.4 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'potassium: 3.2 - 3.4 mmol/l<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level 3.2-3.4' (Parsed: None-None) vs JSON_Section='Potassium: 3.2 - 3.4 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 2.8-3.1' (cleaned: '2.8-3.1')
DEBUG _parse_range_string: Failed to parse range from: 'Potassium: 3.2 - 3.4 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'potassium: 3.2 - 3.4 mmol/l<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: None-None) vs JSON_Section='Potassium: 3.2 - 3.4 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 2.8-3.1' (cleaned: '2.8-3.1')
DEBUG _parse_range_string: Failed to parse range from: 'Potassium: 3.2 - 3.4 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'potassium: 3.2 - 3.4 mmol/l<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: None-None) vs JSON_Section='Potassium: 3.2 - 3.4 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 2.8-3.1' (cleaned: '2.8-3.1')
DEBUG _parse_range_string: Failed to parse range from: 'Potassium: 3.2 - 3.4 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'potassium: 3.2 - 3.4 mmol/l<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: None-None) vs JSON_Section='Potassium: 3.2 - 3.4 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 2.8-3.1' (cleaned: '2.8-3.1')
DEBUG _parse_range_string: Failed to parse range from: 'Potassium: 3.2 - 3.4 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'potassium: 3.2 - 3.4 mmol/l<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level 2.8-3.1' (Parsed: None-None) vs JSON_Section='Potassium: 3.2 - 3.4 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level < 2.8' (cleaned: '< 2.8')
DEBUG _parse_range_string: Failed to parse range from: 'Potassium: 3.2 - 3.4 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'potassium: 3.2 - 3.4 mmol/l<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-None) vs JSON_Section='Potassium: 3.2 - 3.4 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level < 2.8' (cleaned: '< 2.8')
DEBUG _parse_range_string: Failed to parse range from: 'Potassium: 3.2 - 3.4 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'potassium: 3.2 - 3.4 mmol/l<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level < 2.8' (Parsed: None-None) vs JSON_Section='Potassium: 3.2 - 3.4 mmol/L<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 1.6-2.0' (cleaned: '1.6-2.0')
DEBUG _parse_range_string: Failed to parse range from: 'Phosphorus: 1.6 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'phosphorus: 1.6 - 2.0 mg/dl<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level 1.6-2.0' (Parsed: None-None) vs JSON_Section='Phosphorus: 1.6 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 1.6-2.0' (cleaned: '1.6-2.0')
DEBUG _parse_range_string: Failed to parse range from: '<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br>IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck phosphorous & calcium levels with next AM labs.</small>' (cleaned: '<strong style="font-size: 18px; font-weight: bold; color: #333;">step 2 - order corresponding follow-up lab(s):</strong><br>iv - labs:<br><small style="font-weight: normal;">monitoring: recheck phosphorous & calcium levels with next am labs.</small>')

DEBUG ranges_match: Comparing DCW='Current serum level 1.6-2.0' (Parsed: None-None) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br>IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck phosphorous & calcium levels with next AM labs.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 1.6-2.0' (cleaned: '1.6-2.0')
DEBUG _parse_range_string: Failed to parse range from: 'Phosphorus: 1.0 - 1.5 mg/dL<br><span style="color: red; font-weight: bold;">NOTIFY PHYSICIAN if less than 1.1 mg/dL<br>CRITICALLY LOW RESULT</span> <br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'phosphorus: 1.0 - 1.5 mg/dl<br><span style="color: red; font-weight: bold;">notify physician if less than 1.1 mg/dl<br>critly low result</span> <br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level 1.6-2.0' (Parsed: None-None) vs JSON_Section='Phosphorus: 1.0 - 1.5 mg/dL<br><span style="color: red; font-weight: bold;">NOTIFY PHYSICIAN if less than 1.1 mg/dL<br>CRITICALLY LOW RESULT</span> <br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 1.6-2.0' (cleaned: '1.6-2.0')
DEBUG _parse_range_string: Failed to parse range from: '<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br>ORAL - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck phosphorous & calcium levels with next AM labs.</small>' (cleaned: '<strong style="font-size: 18px; font-weight: bold; color: #333;">step 2 - order corresponding follow-up lab(s):</strong><br>oral - labs:<br><small style="font-weight: normal;">monitoring: recheck phosphorous & calcium levels with next am labs.</small>')

DEBUG ranges_match: Comparing DCW='Current serum level 1.6-2.0' (Parsed: None-None) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br>ORAL - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck phosphorous & calcium levels with next AM labs.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 1.6-2.0' (cleaned: '1.6-2.0')
DEBUG _parse_range_string: Failed to parse range from: 'IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck phosphorous & calcium levels 2 hrs after infusion.</small>' (cleaned: 'iv - labs:<br><small style="font-weight: normal;">monitoring: recheck phosphorous & calcium levels 2 hrs after infusion.</small>')

DEBUG ranges_match: Comparing DCW='Current serum level 1.6-2.0' (Parsed: None-None) vs JSON_Section='IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck phosphorous & calcium levels 2 hrs after infusion.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 1.6-2.0' (cleaned: '1.6-2.0')
DEBUG _parse_range_string: Failed to parse range from: 'Phosphorus: < 1.0 mg/dL<br><span style="color: red; font-weight: bold;">NOTIFY PHYSICIAN if less than 1.1 mg/dL<br>CRITICALLY LOW RESULT</span> <br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'phosphorus: < 1.0 mg/dl<br><span style="color: red; font-weight: bold;">notify physician if less than 1.1 mg/dl<br>critly low result</span> <br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level 1.6-2.0' (Parsed: None-None) vs JSON_Section='Phosphorus: < 1.0 mg/dL<br><span style="color: red; font-weight: bold;">NOTIFY PHYSICIAN if less than 1.1 mg/dL<br>CRITICALLY LOW RESULT</span> <br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 1.6-2.0' (cleaned: '1.6-2.0')
DEBUG _parse_range_string: Failed to parse range from: '<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br>IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck phosphorous & calcium levels 2 hrs after infusion.</small>' (cleaned: '<strong style="font-size: 18px; font-weight: bold; color: #333;">step 2 - order corresponding follow-up lab(s):</strong><br>iv - labs:<br><small style="font-weight: normal;">monitoring: recheck phosphorous & calcium levels 2 hrs after infusion.</small>')

DEBUG ranges_match: Comparing DCW='Current serum level 1.6-2.0' (Parsed: None-None) vs JSON_Section='<strong style="font-size: 18px; font-weight: bold; color: #333;">Step 2 - Order corresponding follow-up lab(s):</strong><br>IV - Labs:<br><small style="font-weight: normal;">Monitoring: Recheck phosphorous & calcium levels 2 hrs after infusion.</small>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 1.6-2.0' (cleaned: '1.6-2.0')
DEBUG _parse_range_string: Failed to parse range from: 'Phosphorous Lab Orders' (cleaned: 'phosphorous lab orders')

DEBUG ranges_match: Comparing DCW='Current serum level 1.6-2.0' (Parsed: None-None) vs JSON_Section='Phosphorous Lab Orders' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 1.6-2.0' (cleaned: '1.6-2.0')
DEBUG _parse_range_string: Failed to parse range from: 'Phosphorus: 1.6 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'phosphorus: 1.6 - 2.0 mg/dl<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level 1.6-2.0' (Parsed: None-None) vs JSON_Section='Phosphorus: 1.6 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 1.0-1.5' (cleaned: '1.0-1.5')
DEBUG _parse_range_string: Failed to parse range from: 'Phosphorus: 1.6 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'phosphorus: 1.6 - 2.0 mg/dl<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level 1.0-1.5' (Parsed: None-None) vs JSON_Section='Phosphorus: 1.6 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level 1.0-1.5' (cleaned: '1.0-1.5')
DEBUG _parse_range_string: Failed to parse range from: 'Phosphorus: 1.6 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'phosphorus: 1.6 - 2.0 mg/dl<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level 1.0-1.5' (Parsed: None-None) vs JSON_Section='Phosphorus: 1.6 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
DEBUG _parse_range_string: Failed to parse range from: 'Current serum level <1.0' (cleaned: '<1.0')
DEBUG _parse_range_string: Failed to parse range from: 'Phosphorus: 1.6 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (cleaned: 'phosphorus: 1.6 - 2.0 mg/dl<br><strong style="font-size: 18px; font-weight: bold; color: #333;">step 1 - order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* if patient is not npo, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>')

DEBUG ranges_match: Comparing DCW='Current serum level <1.0' (Parsed: None-None) vs JSON_Section='Phosphorus: 1.6 - 2.0 mg/dL<br><strong style="font-size: 18px; font-weight: bold; color: #333;">Step 1 - Order most appropriate replacement:</strong><br><span style="font-size: 14px; color: #666; line-height: 1.5;">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>' (Parsed: None-None)
DEBUG ranges_match: Comparison result = True
_ test_expected_sentences_match_generated[/home/pessk/code/ea-python/generated_configs/output_cardiac.json] _

config_file_path = '/home/pessk/code/ea-python/generated_configs/output_cardiac.json'

    @pytest.mark.parametrize("config_file_path", get_generated_config_paths())
    def test_expected_sentences_match_generated(config_file_path):
        """
        Verifies that order sentences in the generated JSON match EXACTLY those defined
        in the individual files within expected_sentences/.
        """
        # --- Clear cache before each test run ---
        load_expected_sentences.cache_clear()
        # --- End Clear Cache ---
    
        # Load JSON inside the test now
        try:
            with open(config_file_path, 'r', encoding='utf-8') as f:
                loaded_json_config = json.load(f)
        except Exception as e:
            pytest.fail(f"Failed to load or parse JSON from {config_file_path}: {e}")
    
        protocol = get_protocol_from_filename(config_file_path)
        assert protocol, f"Could not determine protocol from filename: {config_file_path}"
    
        errors = []
        processed_json_orders = set()
        # No longer need unmatched_domain_sentences tracking based on extract.csv
    
        # Iterate through the generated JSON structure first
        try:
            tabs = loaded_json_config.get('RCONFIG', {}).get('TABS', [])
            for tab in tabs:
                tab_key = tab.get('TAB_KEY')
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
    
                        # --- Debug: Print mnemonic being loaded ---
                        print(f"DEBUG: Loading expected for Mnemonic='{json_mnemonic}', Tab='{tab_key}'")
                        # --- End Debug ---
    
                        # Load expected sentences from individual file for this mnemonic
                        expected_sentences = load_expected_sentences(json_mnemonic, tab_key)
    
                        if not expected_sentences:
                            # Mnemonic in JSON does not have a corresponding expected file or file is empty!
                            errors.append(
                                f"  - Unexpected/Missing File: Mnemonic '{json_mnemonic}' in Tab '{tab_key}'\n"
                                f"    JSON Sentence: {repr(json_sentence)}\n"
                                f"    (No corresponding file found or file empty in expected_sentences/)"
                            )
                            processed_json_orders.add(json_order_id)
                            continue
    
                        # --- Exact Comparison Logic ---
                        if json_sentence in expected_sentences:
                            # Exact match found - good!
                            processed_json_orders.add(json_order_id)
                        else:
                            # Exact match NOT found - this is an error
                            # Format expected sentences for error message
                            expected_list_str = "\n      Expected Sentences in File:\n"
                            preview_count = 3
                            expected_list_str += "\n".join([f"        - {repr(s)}" for s in list(expected_sentences)[:preview_count]])
                            if len(expected_sentences) > preview_count:
                                expected_list_str += f"\n        - ... ({len(expected_sentences) - preview_count} more)"
    
                            errors.append(
                                f"  - Sentence Mismatch: Mnemonic '{json_mnemonic}' in Tab '{tab_key}'\n"
                                f"    JSON    : {repr(json_sentence)}\n"
                                f"    Expected: Not found exactly in its expected file.{expected_list_str}"
                            )
                            processed_json_orders.add(json_order_id)
    
        except Exception as e:
            pytest.fail(f"Error processing JSON structure in {config_file_path}: {e}")
    
        # --- Final Assertion ---
        if errors:
            final_error_message = f"\nFound Discrepancies (JSON vs Expected Files) in {os.path.basename(config_file_path)}:\n"
            final_error_message += "\n".join(errors)
>           assert not final_error_message, final_error_message
E           AssertionError: 
E             Found Discrepancies (JSON vs Expected Files) in output_cardiac.json:
E               - Sentence Mismatch: Mnemonic 'magnesium sulfate' in Tab 'MAGNESIUM'
E                 JSON    : '1 g, IVPB, Premix, Once, infuse over 1 hr'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '2 g, IVPB, Premix, q2hr (interval), Duration: 2 dose(s), Infuse over: 2 hr'
E                     - '1 g, IVPB, Premix, Once, Infuse over: 1 hr'
E                     - '2 g, IVPB, Premix, Once, Infuse over: 2 hr'
E               - Sentence Mismatch: Mnemonic 'magnesium sulfate' in Tab 'MAGNESIUM'
E                 JSON    : '2 g, IVPB, Premix, Once, infuse over 2 hr'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '2 g, IVPB, Premix, q2hr (interval), Duration: 2 dose(s), Infuse over: 2 hr'
E                     - '1 g, IVPB, Premix, Once, Infuse over: 1 hr'
E                     - '2 g, IVPB, Premix, Once, Infuse over: 2 hr'
E               - Sentence Mismatch: Mnemonic 'magnesium sulfate' in Tab 'MAGNESIUM'
E                 JSON    : '2 g, IVPB, Premix, q2h interval, Duration: 2 doses, infuse over 2 hr'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '2 g, IVPB, Premix, q2hr (interval), Duration: 2 dose(s), Infuse over: 2 hr'
E                     - '1 g, IVPB, Premix, Once, Infuse over: 1 hr'
E                     - '2 g, IVPB, Premix, Once, Infuse over: 2 hr'
E               - Sentence Mismatch: Mnemonic 'potassium chloride 10 mEq/100 mL intravenous solution' in Tab 'POTASSIUM'
E                 JSON    : '10 mEq, IV, q1h, Duration: 2 doses, infuse over 1 hr'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '10 mEq, IV, q1hr, Duration: 8 dose(s), Infuse over: 1 hr'
E                     - '10 mEq, IV, q1hr, Duration: 4 dose(s), Infuse over: 1 hr'
E                     - '10 mEq, IV, q1hr, Duration: 6 dose(s), Infuse over: 1 hr'
E                     - ... (1 more)
E               - Sentence Mismatch: Mnemonic 'potassium chloride 20 mEq/100 mL intravenous solution' in Tab 'POTASSIUM'
E                 JSON    : '20 mEq, IV, Once, infuse over 1 hr'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '20 mEq, IV, q1hr, Duration: 2 dose(s), Infuse over: 1 hr'
E                     - '20 mEq, IV, q1hr, Duration: 3 dose(s), Infuse over: 1 hr'
E                     - '20 mEq, IV, Once, Infuse over: 1 hr'
E                     - ... (4 more)
E               - Sentence Mismatch: Mnemonic 'potassium chloride extended release' in Tab 'POTASSIUM'
E                 JSON    : '20 mEq, PO, ER tab, q2h interval, Duration: 2 doses'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '20 mEq, PO, ER tab, q2hr (interval), Duration: 2 dose(s)'
E                     - '20 mEq, PO, ER tab, q2hr (interval), Duration: 3 dose(s)'
E                     - '20 mEq, PO, ER tab, Once'
E               - Sentence Mismatch: Mnemonic 'potassium chloride' in Tab 'POTASSIUM'
E                 JSON    : '20 mEq, Feeding Tube, Liq, q2h interval, Duration: 2 doses'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '20 mEq, Feeding Tube, Liq, q2hr (interval), Duration: 3 dose(s)'
E                     - '20 mEq, Feeding Tube, Liq, q2hr (interval), Duration: 2 dose(s)'
E                     - '20 mEq, Feeding Tube, Liq, Once'
E               - Sentence Mismatch: Mnemonic 'potassium chloride 10 mEq/100 mL intravenous solution' in Tab 'POTASSIUM'
E                 JSON    : '10 mEq, IV, q1h, Duration: 4 doses, infuse over 1 hr'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '10 mEq, IV, q1hr, Duration: 8 dose(s), Infuse over: 1 hr'
E                     - '10 mEq, IV, q1hr, Duration: 4 dose(s), Infuse over: 1 hr'
E                     - '10 mEq, IV, q1hr, Duration: 6 dose(s), Infuse over: 1 hr'
E                     - ... (1 more)
E               - Sentence Mismatch: Mnemonic 'potassium chloride 20 mEq/100 mL intravenous solution' in Tab 'POTASSIUM'
E                 JSON    : '20 mEq, IV, q1h, Duration: 2 doses, infuse over 1 hr'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '20 mEq, IV, q1hr, Duration: 2 dose(s), Infuse over: 1 hr'
E                     - '20 mEq, IV, q1hr, Duration: 3 dose(s), Infuse over: 1 hr'
E                     - '20 mEq, IV, Once, Infuse over: 1 hr'
E                     - ... (4 more)
E               - Sentence Mismatch: Mnemonic 'potassium chloride extended release' in Tab 'POTASSIUM'
E                 JSON    : '20 mEq, PO, ER tab, q2h interval, Duration: 3 doses'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '20 mEq, PO, ER tab, q2hr (interval), Duration: 2 dose(s)'
E                     - '20 mEq, PO, ER tab, q2hr (interval), Duration: 3 dose(s)'
E                     - '20 mEq, PO, ER tab, Once'
E               - Sentence Mismatch: Mnemonic 'potassium chloride' in Tab 'POTASSIUM'
E                 JSON    : '20 mEq, Feeding Tube, Liq, q2h interval, Duration: 3 doses'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '20 mEq, Feeding Tube, Liq, q2hr (interval), Duration: 3 dose(s)'
E                     - '20 mEq, Feeding Tube, Liq, q2hr (interval), Duration: 2 dose(s)'
E                     - '20 mEq, Feeding Tube, Liq, Once'
E               - Sentence Mismatch: Mnemonic 'potassium chloride 10 mEq/100 mL intravenous solution' in Tab 'POTASSIUM'
E                 JSON    : '10 mEq, IV, q1h, Duration: 6 doses, infuse over 1 hr'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '10 mEq, IV, q1hr, Duration: 8 dose(s), Infuse over: 1 hr'
E                     - '10 mEq, IV, q1hr, Duration: 4 dose(s), Infuse over: 1 hr'
E                     - '10 mEq, IV, q1hr, Duration: 6 dose(s), Infuse over: 1 hr'
E                     - ... (1 more)
E               - Sentence Mismatch: Mnemonic 'potassium chloride 20 mEq/100 mL intravenous solution' in Tab 'POTASSIUM'
E                 JSON    : '20 mEq, IV, q1h, Duration: 3 doses, infuse over 1 hr'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '20 mEq, IV, q1hr, Duration: 2 dose(s), Infuse over: 1 hr'
E                     - '20 mEq, IV, q1hr, Duration: 3 dose(s), Infuse over: 1 hr'
E                     - '20 mEq, IV, Once, Infuse over: 1 hr'
E                     - ... (4 more)
E               - Sentence Mismatch: Mnemonic 'potassium chloride 10 mEq/100 mL intravenous solution' in Tab 'POTASSIUM'
E                 JSON    : '10 mEq, IV, q1h, Duration: 8 doses, infuse over 1 hr'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '10 mEq, IV, q1hr, Duration: 8 dose(s), Infuse over: 1 hr'
E                     - '10 mEq, IV, q1hr, Duration: 4 dose(s), Infuse over: 1 hr'
E                     - '10 mEq, IV, q1hr, Duration: 6 dose(s), Infuse over: 1 hr'
E                     - ... (1 more)
E               - Sentence Mismatch: Mnemonic 'potassium chloride 20 mEq/100 mL intravenous solution' in Tab 'POTASSIUM'
E                 JSON    : '20 mEq, IV, q1h, Duration: 4 doses, infuse over 1 hr'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '20 mEq, IV, q1hr, Duration: 2 dose(s), Infuse over: 1 hr'
E                     - '20 mEq, IV, q1hr, Duration: 3 dose(s), Infuse over: 1 hr'
E                     - '20 mEq, IV, Once, Infuse over: 1 hr'
E                     - ... (4 more)
E               - Sentence Mismatch: Mnemonic 'K-Phos Neutral' in Tab 'PHOSPHATE'
E                 JSON    : '2 tab(s), PO, Tab, q2h interval, Duration: 2 doses'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '2 tab(s), PO, Tab, q2hr (interval), Duration: 3 dose(s)'
E                     - '2 tab(s), PO, Tab, q2hr (interval), Duration: 2 dose(s)'
E               - Sentence Mismatch: Mnemonic 'K-Phos Neutral' in Tab 'PHOSPHATE'
E                 JSON    : '2 tab(s), PO, Tab, q2h interval, Duration: 3 doses'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '2 tab(s), PO, Tab, q2hr (interval), Duration: 3 dose(s)'
E                     - '2 tab(s), PO, Tab, q2hr (interval), Duration: 2 dose(s)'
E               - Sentence Mismatch: Mnemonic 'sodium phosphate' in Tab 'PHOSPHATE'
E                 JSON    : '15 mmol, IVPB, Inj, q4h interval, Duration: 2 doses'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '15 mmol, IVPB, Inj, q4hr (interval), Duration: 2 dose(s)'
E                     - '15 mmol, IVPB, Inj, Once'
E               - Sentence Mismatch: Mnemonic 'sodium phosphate' in Tab 'PHOSPHATE'
E                 JSON    : '15 mmol, IVPB, Inj, q4h interval, Duration: 2 doses'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '15 mmol, IVPB, Inj, q4hr (interval), Duration: 2 dose(s)'
E                     - '15 mmol, IVPB, Inj, Once'
E               - Sentence Mismatch: Mnemonic 'calcium chloride' in Tab 'CALCIUM'
E                 JSON    : '1 g, IVPB, Inj, Once, infuse over 1 hr'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '1 g, IVPB, Inj, Once, Infuse over: 1 hr'
E           assert not "\nFound Discrepancies (JSON vs Expected Files) in output_cardiac.json:\n  - Sentence Mismatch: Mnemonic 'magnesium sulfate' in Tab 'MAGNESIUM'\n    JSON    : '1 g, IVPB, Premix, Once, infuse over 1 hr'\n    Expected: Not found exactly in its expected file.\n      Expected Sentences in File:\n        - '2 g, IVPB, Premix, q2hr (interval), Duration: 2 dose(s), Infuse over: 2 hr'\n        - '1 g, IVPB, Premix, Once, Infuse over: 1 hr'\n        - '2 g, IVPB, Premix, Once, Infuse over: 2 hr'\n  - Sentence Mismatch: Mnemonic 'magnesium sulfate' in Tab 'MAGNESIUM'\n    JSON    : '2 g, IVPB, Premix, Once, infuse over 2 hr'\n    Expected: Not found exactly in its expected file.\n      Expected Sentences in File:\n        - '2 g, IVPB, Premix, q2hr (interval), Duration: 2 dose(s), Infuse over: 2 hr'\n        - '1 g, IVPB, Premix, Once, Infuse over: 1 hr'\n        - '2 g, IVPB, Premix, Once, Infuse over: 2 hr'\n  - Sentence Mismatch: Mnemonic 'magnesium sulfate' in Tab 'MAGNESIUM'\n    JSON    : '2 g, IVPB, Premix, q2h interval, Duration: 2 doses, infuse over 2 hr'\n    Expected: Not found exactly in its expected file.\n      Expected Sentences in File:\n        - '2 g, IVPB, Premix, q2hr ...terval, Duration: 3 doses'\n    Expected: Not found exactly in its expected file.\n      Expected Sentences in File:\n        - '2 tab(s), PO, Tab, q2hr (interval), Duration: 3 dose(s)'\n        - '2 tab(s), PO, Tab, q2hr (interval), Duration: 2 dose(s)'\n  - Sentence Mismatch: Mnemonic 'sodium phosphate' in Tab 'PHOSPHATE'\n    JSON    : '15 mmol, IVPB, Inj, q4h interval, Duration: 2 doses'\n    Expected: Not found exactly in its expected file.\n      Expected Sentences in File:\n        - '15 mmol, IVPB, Inj, q4hr (interval), Duration: 2 dose(s)'\n        - '15 mmol, IVPB, Inj, Once'\n  - Sentence Mismatch: Mnemonic 'sodium phosphate' in Tab 'PHOSPHATE'\n    JSON    : '15 mmol, IVPB, Inj, q4h interval, Duration: 2 doses'\n    Expected: Not found exactly in its expected file.\n      Expected Sentences in File:\n        - '15 mmol, IVPB, Inj, q4hr (interval), Duration: 2 dose(s)'\n        - '15 mmol, IVPB, Inj, Once'\n  - Sentence Mismatch: Mnemonic 'calcium chloride' in Tab 'CALCIUM'\n    JSON    : '1 g, IVPB, Inj, Once, infuse over 1 hr'\n    Expected: Not found exactly in its expected file.\n      Expected Sentences in File:\n        - '1 g, IVPB, Inj, Once, Infuse over: 1 hr'"

tests/test_expected_sentences.py:200: AssertionError
----------------------------- Captured stdout call -----------------------------
DEBUG: Loading expected for Mnemonic='magnesium sulfate', Tab='MAGNESIUM'
DEBUG: Loading expected for Mnemonic='Magnesium Level', Tab='MAGNESIUM'
DEBUG: Loading expected for Mnemonic='magnesium sulfate', Tab='MAGNESIUM'
DEBUG: Loading expected for Mnemonic='Magnesium Level', Tab='MAGNESIUM'
DEBUG: Loading expected for Mnemonic='magnesium sulfate', Tab='MAGNESIUM'
DEBUG: Loading expected for Mnemonic='Magnesium Level', Tab='MAGNESIUM'
DEBUG: Loading expected for Mnemonic='Magnesium Level', Tab='MAGNESIUM'
DEBUG: Loading expected for Mnemonic='Magnesium Level', Tab='MAGNESIUM'
DEBUG: Loading expected for Mnemonic='BMP', Tab='MAGNESIUM'
DEBUG: Loading expected for Mnemonic='Magnesium Level', Tab='MAGNESIUM'
DEBUG: Loading expected for Mnemonic='potassium chloride extended release', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='potassium chloride', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='potassium chloride 10 mEq/100 mL intravenous solution', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='potassium chloride 20 mEq/100 mL intravenous solution', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='BMP', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='potassium chloride extended release', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='potassium chloride', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='potassium chloride 10 mEq/100 mL intravenous solution', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='potassium chloride 20 mEq/100 mL intravenous solution', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='Potassium Level', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='Potassium Level', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='Potassium Level', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='potassium chloride extended release', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='potassium chloride', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='potassium chloride 10 mEq/100 mL intravenous solution', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='potassium chloride 20 mEq/100 mL intravenous solution', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='Potassium Level', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='Potassium Level', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='Potassium Level', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='potassium chloride 10 mEq/100 mL intravenous solution', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='potassium chloride 20 mEq/100 mL intravenous solution', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='Phosphate Level', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='Magnesium Level', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='Potassium Level', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='Potassium Level', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='BMP', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='Magnesium Level', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='Phosphate Level', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='Potassium Level', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='BMP', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='Magnesium Level', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='Phosphate Level', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='K-Phos Neutral', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='sodium phosphate', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Phosphate Level', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Calcium Level Ionized, Serum', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Calcium Level Ionized, Whole Blood', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='K-Phos Neutral', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='sodium phosphate', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Phosphate Level', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Calcium Level Ionized, Serum', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Calcium Level Ionized, Whole Blood', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Phosphate Level', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Calcium Level Ionized, Serum', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Calcium Level Ionized, Whole Blood', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='sodium phosphate', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Phosphate Level', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Calcium Level Ionized, Serum', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Calcium Level Ionized, Whole Blood', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Phosphate Level', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Calcium Level Ionized, Serum', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Calcium Level Ionized, Whole Blood', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Phosphate Level', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Calcium Level Ionized, Serum', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Calcium Level Ionized, Whole Blood', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Phosphate Level', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Calcium Level Ionized, Serum', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Calcium Level Ionized, Whole Blood', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='calcium chloride', Tab='CALCIUM'
DEBUG: Loading expected for Mnemonic='Calcium Level Ionized, Serum', Tab='CALCIUM'
DEBUG: Loading expected for Mnemonic='Calcium Level Ionized, Whole Blood', Tab='CALCIUM'
DEBUG: Loading expected for Mnemonic='Calcium Level Ionized, Serum', Tab='CALCIUM'
DEBUG: Loading expected for Mnemonic='Calcium Level Ionized, Whole Blood', Tab='CALCIUM'
DEBUG: Loading expected for Mnemonic='Calcium Level Ionized, Serum', Tab='CALCIUM'
DEBUG: Loading expected for Mnemonic='Calcium Level Ionized, Whole Blood', Tab='CALCIUM'
_ test_expected_sentences_match_generated[/home/pessk/code/ea-python/generated_configs/output_regular.json] _

config_file_path = '/home/pessk/code/ea-python/generated_configs/output_regular.json'

    @pytest.mark.parametrize("config_file_path", get_generated_config_paths())
    def test_expected_sentences_match_generated(config_file_path):
        """
        Verifies that order sentences in the generated JSON match EXACTLY those defined
        in the individual files within expected_sentences/.
        """
        # --- Clear cache before each test run ---
        load_expected_sentences.cache_clear()
        # --- End Clear Cache ---
    
        # Load JSON inside the test now
        try:
            with open(config_file_path, 'r', encoding='utf-8') as f:
                loaded_json_config = json.load(f)
        except Exception as e:
            pytest.fail(f"Failed to load or parse JSON from {config_file_path}: {e}")
    
        protocol = get_protocol_from_filename(config_file_path)
        assert protocol, f"Could not determine protocol from filename: {config_file_path}"
    
        errors = []
        processed_json_orders = set()
        # No longer need unmatched_domain_sentences tracking based on extract.csv
    
        # Iterate through the generated JSON structure first
        try:
            tabs = loaded_json_config.get('RCONFIG', {}).get('TABS', [])
            for tab in tabs:
                tab_key = tab.get('TAB_KEY')
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
    
                        # --- Debug: Print mnemonic being loaded ---
                        print(f"DEBUG: Loading expected for Mnemonic='{json_mnemonic}', Tab='{tab_key}'")
                        # --- End Debug ---
    
                        # Load expected sentences from individual file for this mnemonic
                        expected_sentences = load_expected_sentences(json_mnemonic, tab_key)
    
                        if not expected_sentences:
                            # Mnemonic in JSON does not have a corresponding expected file or file is empty!
                            errors.append(
                                f"  - Unexpected/Missing File: Mnemonic '{json_mnemonic}' in Tab '{tab_key}'\n"
                                f"    JSON Sentence: {repr(json_sentence)}\n"
                                f"    (No corresponding file found or file empty in expected_sentences/)"
                            )
                            processed_json_orders.add(json_order_id)
                            continue
    
                        # --- Exact Comparison Logic ---
                        if json_sentence in expected_sentences:
                            # Exact match found - good!
                            processed_json_orders.add(json_order_id)
                        else:
                            # Exact match NOT found - this is an error
                            # Format expected sentences for error message
                            expected_list_str = "\n      Expected Sentences in File:\n"
                            preview_count = 3
                            expected_list_str += "\n".join([f"        - {repr(s)}" for s in list(expected_sentences)[:preview_count]])
                            if len(expected_sentences) > preview_count:
                                expected_list_str += f"\n        - ... ({len(expected_sentences) - preview_count} more)"
    
                            errors.append(
                                f"  - Sentence Mismatch: Mnemonic '{json_mnemonic}' in Tab '{tab_key}'\n"
                                f"    JSON    : {repr(json_sentence)}\n"
                                f"    Expected: Not found exactly in its expected file.{expected_list_str}"
                            )
                            processed_json_orders.add(json_order_id)
    
        except Exception as e:
            pytest.fail(f"Error processing JSON structure in {config_file_path}: {e}")
    
        # --- Final Assertion ---
        if errors:
            final_error_message = f"\nFound Discrepancies (JSON vs Expected Files) in {os.path.basename(config_file_path)}:\n"
            final_error_message += "\n".join(errors)
>           assert not final_error_message, final_error_message
E           AssertionError: 
E             Found Discrepancies (JSON vs Expected Files) in output_regular.json:
E               - Sentence Mismatch: Mnemonic 'magnesium oxide' in Tab 'MAGNESIUM'
E                 JSON    : '400 mg, PO, Tab, q12h interval, Duration: 2 doses'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '400 mg, PO, Tab, q12hr (interval), Duration: 2 dose(s)'
E               - Sentence Mismatch: Mnemonic 'magnesium sulfate' in Tab 'MAGNESIUM'
E                 JSON    : '2 g, IVPB, Premix, Once, infuse over 2 hr'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '2 g, IVPB, Premix, q2hr (interval), Duration: 2 dose(s), Infuse over: 2 hr'
E                     - '1 g, IVPB, Premix, Once, Infuse over: 1 hr'
E                     - '2 g, IVPB, Premix, Once, Infuse over: 2 hr'
E               - Sentence Mismatch: Mnemonic 'magnesium sulfate' in Tab 'MAGNESIUM'
E                 JSON    : '2 g, IVPB, Premix, q2h interval, Duration: 2 doses, infuse over 2 hr'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '2 g, IVPB, Premix, q2hr (interval), Duration: 2 dose(s), Infuse over: 2 hr'
E                     - '1 g, IVPB, Premix, Once, Infuse over: 1 hr'
E                     - '2 g, IVPB, Premix, Once, Infuse over: 2 hr'
E               - Sentence Mismatch: Mnemonic 'potassium chloride extended release' in Tab 'POTASSIUM'
E                 JSON    : '20 mEq, PO, ER tab, q2h interval, Duration: 2 doses'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '20 mEq, PO, ER tab, q2hr (interval), Duration: 2 dose(s)'
E                     - '20 mEq, PO, ER tab, q2hr (interval), Duration: 3 dose(s)'
E                     - '20 mEq, PO, ER tab, Once'
E               - Sentence Mismatch: Mnemonic 'potassium chloride' in Tab 'POTASSIUM'
E                 JSON    : '20 mEq, Feeding Tube, Liq, q2h interval, Duration: 2 doses'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '20 mEq, Feeding Tube, Liq, q2hr (interval), Duration: 3 dose(s)'
E                     - '20 mEq, Feeding Tube, Liq, q2hr (interval), Duration: 2 dose(s)'
E                     - '20 mEq, Feeding Tube, Liq, Once'
E               - Sentence Mismatch: Mnemonic 'potassium chloride 10 mEq/100 mL intravenous solution' in Tab 'POTASSIUM'
E                 JSON    : '10 mEq, IV, q1h, Duration: 4 doses, infuse over 1 hr'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '10 mEq, IV, q1hr, Duration: 8 dose(s), Infuse over: 1 hr'
E                     - '10 mEq, IV, q1hr, Duration: 4 dose(s), Infuse over: 1 hr'
E                     - '10 mEq, IV, q1hr, Duration: 6 dose(s), Infuse over: 1 hr'
E                     - ... (1 more)
E               - Sentence Mismatch: Mnemonic 'potassium chloride 20 mEq/100 mL intravenous solution' in Tab 'POTASSIUM'
E                 JSON    : '20 mEq, IV, q2h, Duration: 2 doses, infuse over 2 hr'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '20 mEq, IV, q1hr, Duration: 2 dose(s), Infuse over: 1 hr'
E                     - '20 mEq, IV, q1hr, Duration: 3 dose(s), Infuse over: 1 hr'
E                     - '20 mEq, IV, Once, Infuse over: 1 hr'
E                     - ... (4 more)
E               - Sentence Mismatch: Mnemonic 'potassium chloride extended release' in Tab 'POTASSIUM'
E                 JSON    : '20 mEq, PO, ER tab, q2h interval, Duration: 3 doses'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '20 mEq, PO, ER tab, q2hr (interval), Duration: 2 dose(s)'
E                     - '20 mEq, PO, ER tab, q2hr (interval), Duration: 3 dose(s)'
E                     - '20 mEq, PO, ER tab, Once'
E               - Sentence Mismatch: Mnemonic 'potassium chloride' in Tab 'POTASSIUM'
E                 JSON    : '20 mEq, Feeding Tube, Liq, q2h interval, Duration: 3 doses'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '20 mEq, Feeding Tube, Liq, q2hr (interval), Duration: 3 dose(s)'
E                     - '20 mEq, Feeding Tube, Liq, q2hr (interval), Duration: 2 dose(s)'
E                     - '20 mEq, Feeding Tube, Liq, Once'
E               - Sentence Mismatch: Mnemonic 'potassium chloride 10 mEq/100 mL intravenous solution' in Tab 'POTASSIUM'
E                 JSON    : '10 mEq, IV, q1h, Duration: 6 doses, infuse over 1 hr'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '10 mEq, IV, q1hr, Duration: 8 dose(s), Infuse over: 1 hr'
E                     - '10 mEq, IV, q1hr, Duration: 4 dose(s), Infuse over: 1 hr'
E                     - '10 mEq, IV, q1hr, Duration: 6 dose(s), Infuse over: 1 hr'
E                     - ... (1 more)
E               - Sentence Mismatch: Mnemonic 'potassium chloride 20 mEq/100 mL intravenous solution' in Tab 'POTASSIUM'
E                 JSON    : '20 mEq, IV, q2h, Duration: 3 doses, infuse over 2 hr'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '20 mEq, IV, q1hr, Duration: 2 dose(s), Infuse over: 1 hr'
E                     - '20 mEq, IV, q1hr, Duration: 3 dose(s), Infuse over: 1 hr'
E                     - '20 mEq, IV, Once, Infuse over: 1 hr'
E                     - ... (4 more)
E               - Sentence Mismatch: Mnemonic 'potassium chloride 10 mEq/100 mL intravenous solution' in Tab 'POTASSIUM'
E                 JSON    : '10 mEq, IV, q1h, Duration: 8 doses, infuse over 1 hr'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '10 mEq, IV, q1hr, Duration: 8 dose(s), Infuse over: 1 hr'
E                     - '10 mEq, IV, q1hr, Duration: 4 dose(s), Infuse over: 1 hr'
E                     - '10 mEq, IV, q1hr, Duration: 6 dose(s), Infuse over: 1 hr'
E                     - ... (1 more)
E               - Sentence Mismatch: Mnemonic 'potassium chloride 20 mEq/100 mL intravenous solution' in Tab 'POTASSIUM'
E                 JSON    : '20 mEq, IV, q2h, Duration: 4 doses, infuse over 2 hr'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '20 mEq, IV, q1hr, Duration: 2 dose(s), Infuse over: 1 hr'
E                     - '20 mEq, IV, q1hr, Duration: 3 dose(s), Infuse over: 1 hr'
E                     - '20 mEq, IV, Once, Infuse over: 1 hr'
E                     - ... (4 more)
E               - Sentence Mismatch: Mnemonic 'K-Phos Neutral' in Tab 'PHOSPHATE'
E                 JSON    : '2 tab(s), PO, Tab, q2h interval, Duration: 2 doses'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '2 tab(s), PO, Tab, q2hr (interval), Duration: 3 dose(s)'
E                     - '2 tab(s), PO, Tab, q2hr (interval), Duration: 2 dose(s)'
E               - Sentence Mismatch: Mnemonic 'K-Phos Neutral' in Tab 'PHOSPHATE'
E                 JSON    : '2 tab(s), PO, Tab, q2h interval, Duration: 3 doses'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '2 tab(s), PO, Tab, q2hr (interval), Duration: 3 dose(s)'
E                     - '2 tab(s), PO, Tab, q2hr (interval), Duration: 2 dose(s)'
E               - Sentence Mismatch: Mnemonic 'sodium phosphate' in Tab 'PHOSPHATE'
E                 JSON    : '15 mmol, IVPB, Inj, q4h interval, Duration: 2 doses'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '15 mmol, IVPB, Inj, q4hr (interval), Duration: 2 dose(s)'
E                     - '15 mmol, IVPB, Inj, Once'
E               - Sentence Mismatch: Mnemonic 'sodium phosphate' in Tab 'PHOSPHATE'
E                 JSON    : '15 mmol, IVPB, Inj, q4h interval, Duration: 2 doses'
E                 Expected: Not found exactly in its expected file.
E                   Expected Sentences in File:
E                     - '15 mmol, IVPB, Inj, q4hr (interval), Duration: 2 dose(s)'
E                     - '15 mmol, IVPB, Inj, Once'
E           assert not "\nFound Discrepancies (JSON vs Expected Files) in output_regular.json:\n  - Sentence Mismatch: Mnemonic 'magnesium oxide' in Tab 'MAGNESIUM'\n    JSON    : '400 mg, PO, Tab, q12h interval, Duration: 2 doses'\n    Expected: Not found exactly in its expected file.\n      Expected Sentences in File:\n        - '400 mg, PO, Tab, q12hr (interval), Duration: 2 dose(s)'\n  - Sentence Mismatch: Mnemonic 'magnesium sulfate' in Tab 'MAGNESIUM'\n    JSON    : '2 g, IVPB, Premix, Once, infuse over 2 hr'\n    Expected: Not found exactly in its expected file.\n      Expected Sentences in File:\n        - '2 g, IVPB, Premix, q2hr (interval), Duration: 2 dose(s), Infuse over: 2 hr'\n        - '1 g, IVPB, Premix, Once, Infuse over: 1 hr'\n        - '2 g, IVPB, Premix, Once, Infuse over: 2 hr'\n  - Sentence Mismatch: Mnemonic 'magnesium sulfate' in Tab 'MAGNESIUM'\n    JSON    : '2 g, IVPB, Premix, q2h interval, Duration: 2 doses, infuse over 2 hr'\n    Expected: Not found exactly in its expected file.\n      Expected Sentences in File:\n        - '2 g, IVPB, Premix, q2hr (interval), Duration: 2 dose(s), Infuse over: 2 hr'\n        - '1 g, IVPB, Premix, Once, Infuse over: 1 hr'\n        - '2 g, I... Sentences in File:\n        - '2 tab(s), PO, Tab, q2hr (interval), Duration: 3 dose(s)'\n        - '2 tab(s), PO, Tab, q2hr (interval), Duration: 2 dose(s)'\n  - Sentence Mismatch: Mnemonic 'K-Phos Neutral' in Tab 'PHOSPHATE'\n    JSON    : '2 tab(s), PO, Tab, q2h interval, Duration: 3 doses'\n    Expected: Not found exactly in its expected file.\n      Expected Sentences in File:\n        - '2 tab(s), PO, Tab, q2hr (interval), Duration: 3 dose(s)'\n        - '2 tab(s), PO, Tab, q2hr (interval), Duration: 2 dose(s)'\n  - Sentence Mismatch: Mnemonic 'sodium phosphate' in Tab 'PHOSPHATE'\n    JSON    : '15 mmol, IVPB, Inj, q4h interval, Duration: 2 doses'\n    Expected: Not found exactly in its expected file.\n      Expected Sentences in File:\n        - '15 mmol, IVPB, Inj, q4hr (interval), Duration: 2 dose(s)'\n        - '15 mmol, IVPB, Inj, Once'\n  - Sentence Mismatch: Mnemonic 'sodium phosphate' in Tab 'PHOSPHATE'\n    JSON    : '15 mmol, IVPB, Inj, q4h interval, Duration: 2 doses'\n    Expected: Not found exactly in its expected file.\n      Expected Sentences in File:\n        - '15 mmol, IVPB, Inj, q4hr (interval), Duration: 2 dose(s)'\n        - '15 mmol, IVPB, Inj, Once'"

tests/test_expected_sentences.py:200: AssertionError
----------------------------- Captured stdout call -----------------------------
DEBUG: Loading expected for Mnemonic='magnesium oxide', Tab='MAGNESIUM'
DEBUG: Loading expected for Mnemonic='magnesium sulfate', Tab='MAGNESIUM'
DEBUG: Loading expected for Mnemonic='BMP', Tab='MAGNESIUM'
DEBUG: Loading expected for Mnemonic='Magnesium Level', Tab='MAGNESIUM'
DEBUG: Loading expected for Mnemonic='magnesium sulfate', Tab='MAGNESIUM'
DEBUG: Loading expected for Mnemonic='Magnesium Level', Tab='MAGNESIUM'
DEBUG: Loading expected for Mnemonic='Magnesium Level', Tab='MAGNESIUM'
DEBUG: Loading expected for Mnemonic='Magnesium Level', Tab='MAGNESIUM'
DEBUG: Loading expected for Mnemonic='BMP', Tab='MAGNESIUM'
DEBUG: Loading expected for Mnemonic='Magnesium Level', Tab='MAGNESIUM'
DEBUG: Loading expected for Mnemonic='potassium chloride extended release', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='potassium chloride', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='potassium chloride 10 mEq/100 mL intravenous solution', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='potassium chloride 20 mEq/100 mL intravenous solution', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='BMP', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='potassium chloride extended release', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='potassium chloride', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='potassium chloride 10 mEq/100 mL intravenous solution', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='potassium chloride 20 mEq/100 mL intravenous solution', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='Potassium Level', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='Potassium Level', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='Potassium Level', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='potassium chloride 10 mEq/100 mL intravenous solution', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='potassium chloride 20 mEq/100 mL intravenous solution', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='Phosphate Level', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='Magnesium Level', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='Potassium Level', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='Magnesium Level', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='Potassium Level', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='BMP', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='Magnesium Level', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='Phosphate Level', Tab='POTASSIUM'
DEBUG: Loading expected for Mnemonic='K-Phos Neutral', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='sodium phosphate', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Phosphate Level', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Calcium Level Ionized, Serum', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Calcium Level Ionized, Whole Blood', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='K-Phos Neutral', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='sodium phosphate', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Phosphate Level', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Calcium Level Ionized, Serum', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Calcium Level Ionized, Whole Blood', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Phosphate Level', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Calcium Level Ionized, Serum', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Calcium Level Ionized, Whole Blood', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='sodium phosphate', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Phosphate Level', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Calcium Level Ionized, Serum', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Calcium Level Ionized, Whole Blood', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Phosphate Level', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Calcium Level Ionized, Serum', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Calcium Level Ionized, Whole Blood', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Phosphate Level', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Calcium Level Ionized, Serum', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Calcium Level Ionized, Whole Blood', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Phosphate Level', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Calcium Level Ionized, Serum', Tab='PHOSPHATE'
DEBUG: Loading expected for Mnemonic='Calcium Level Ionized, Whole Blood', Tab='PHOSPHATE'
========================= 5 failed, 4 passed in 0.58s ==========================
