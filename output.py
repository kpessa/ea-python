[1m============================= test session starts ==============================[0m
platform linux -- Python 3.12.3, pytest-8.3.5, pluggy-1.5.0 -- /home/pessk/code/ea-python/.venv/bin/python
cachedir: .pytest_cache
rootdir: /home/pessk/code/ea-python
plugins: sugar-1.0.0
[1mcollecting ... [0mcollected 33 items

tests/unit/test_dcw_sentences.py::test_dcw_sentences_match_generated[/home/pessk/code/ea-python/generated_configs/output_cardiac.json] [32mPASSED[0m[32m [  3%][0m
tests/unit/test_dcw_sentences.py::test_dcw_sentences_match_generated[/home/pessk/code/ea-python/generated_configs/output_regular.json] [32mPASSED[0m[32m [  6%][0m
tests/unit/test_expected_sentences.py::test_expected_sentences_match_generated[/home/pessk/code/ea-python/generated_configs/output_cardiac.json] [32mPASSED[0m[32m [  9%][0m
tests/unit/test_expected_sentences.py::test_expected_sentences_match_generated[/home/pessk/code/ea-python/generated_configs/output_regular.json] [32mPASSED[0m[32m [ 12%][0m
tests/unit/test_generated_output.py::test_top_level_structure[regular_config] [32mPASSED[0m[32m [ 15%][0m
tests/unit/test_generated_output.py::test_top_level_structure[cardiac_config] [32mPASSED[0m[32m [ 18%][0m
tests/unit/test_generated_output.py::test_rconfig_structure[regular_config] [32mPASSED[0m[32m [ 21%][0m
tests/unit/test_generated_output.py::test_rconfig_structure[cardiac_config] [32mPASSED[0m[32m [ 24%][0m
tests/unit/test_generated_output.py::test_tab_structure[regular_config] [32mPASSED[0m[32m [ 27%][0m
tests/unit/test_generated_output.py::test_tab_structure[cardiac_config] [32mPASSED[0m[32m [ 30%][0m
tests/unit/test_generated_output.py::test_order_basic_fields[regular_config] [32mPASSED[0m[32m [ 33%][0m
tests/unit/test_generated_output.py::test_order_basic_fields[cardiac_config] [32mPASSED[0m[32m [ 36%][0m
tests/unit/test_generated_output.py::test_lab_sentence_format[regular_config] [32mPASSED[0m[32m [ 39%][0m
tests/unit/test_generated_output.py::test_lab_sentence_format[cardiac_config] [32mPASSED[0m[32m [ 42%][0m
tests/unit/test_generated_output.py::test_med_sentence_start_format[regular_config] [32mPASSED[0m[32m [ 45%][0m
tests/unit/test_generated_output.py::test_med_sentence_start_format[cardiac_config] [32mPASSED[0m[32m [ 48%][0m
tests/unit/test_generated_output.py::test_med_sentence_frequency_format[regular_config] [32mPASSED[0m[32m [ 51%][0m
tests/unit/test_generated_output.py::test_med_sentence_frequency_format[cardiac_config] [32mPASSED[0m[32m [ 54%][0m
tests/unit/test_generated_output.py::test_med_sentence_infuse_over_format[regular_config] [32mPASSED[0m[32m [ 57%][0m
tests/unit/test_generated_output.py::test_med_sentence_infuse_over_format[cardiac_config] [32mPASSED[0m[32m [ 60%][0m
src/formatting.py::src.formatting.format_level_for_concept [32mPASSED[0m[32m        [ 63%][0m
src/formatting.py::src.formatting.format_level_for_display [32mPASSED[0m[32m        [ 66%][0m
src/lab_orders.py::src.lab_orders.create_specific_timed_lab [32mPASSED[0m[32m       [ 69%][0m
src/lab_orders.py::src.lab_orders.get_timed_lab [32mPASSED[0m[32m                   [ 72%][0m
src/naming.py::src.naming.create_between_concept [32mPASSED[0m[32m                  [ 75%][0m
src/naming.py::src.naming.create_between_section_name [32mPASSED[0m[32m             [ 78%][0m
src/naming.py::src.naming.create_less_than_concept [32mPASSED[0m[32m                [ 81%][0m
src/naming.py::src.naming.create_less_than_section_name [32mPASSED[0m[32m           [ 84%][0m
src/naming.py::src.naming.get_concept_name [32mPASSED[0m[32m                        [ 87%][0m
src/order_builder.py::src.order_builder.create_lab_order [32mPASSED[0m[32m          [ 90%][0m
src/tab_builder.py::src.tab_builder._create_graphed_results [32mPASSED[0m[32m       [ 93%][0m
src/tab_builder.py::src.tab_builder._create_mnemonic [32mPASSED[0m[32m              [ 96%][0m
src/text.py::src.text.create_notify_provider_text [32mPASSED[0m[32m                 [100%][0m

[32m============================== [32m[1m33 passed[0m[32m in 0.41s[0m[32m ==============================[0m
