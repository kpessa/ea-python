[1m============================= test session starts ==============================[0m
platform linux -- Python 3.12.3, pytest-8.3.5, pluggy-1.5.0 -- /home/pessk/code/ea-python/.venv/bin/python
cachedir: .pytest_cache
rootdir: /home/pessk/code/ea-python
configfile: pyproject.toml
plugins: sugar-1.0.0
[1mcollecting ... [0mcollected 38 items

tests/unit/test_dcw_sentences.py::test_dcw_sentences_match_generated[/home/pessk/code/ea-python/generated_configs/output_cardiac.json] [32mPASSED[0m[32m [  2%][0m
tests/unit/test_dcw_sentences.py::test_dcw_sentences_match_generated[/home/pessk/code/ea-python/generated_configs/output_regular.json] [32mPASSED[0m[32m [  5%][0m
tests/unit/test_expected_sentences.py::test_expected_sentences_match_generated[/home/pessk/code/ea-python/generated_configs/output_cardiac.json] [32mPASSED[0m[32m [  7%][0m
tests/unit/test_expected_sentences.py::test_expected_sentences_match_generated[/home/pessk/code/ea-python/generated_configs/output_regular.json] [32mPASSED[0m[32m [ 10%][0m
tests/unit/test_generated_output.py::test_top_level_structure[regular_config] [32mPASSED[0m[32m [ 13%][0m
tests/unit/test_generated_output.py::test_top_level_structure[cardiac_config] [32mPASSED[0m[32m [ 15%][0m
tests/unit/test_generated_output.py::test_rconfig_structure[regular_config] [32mPASSED[0m[32m [ 18%][0m
tests/unit/test_generated_output.py::test_rconfig_structure[cardiac_config] [32mPASSED[0m[32m [ 21%][0m
tests/unit/test_generated_output.py::test_tab_structure[regular_config] [32mPASSED[0m[32m [ 23%][0m
tests/unit/test_generated_output.py::test_tab_structure[cardiac_config] [32mPASSED[0m[32m [ 26%][0m
tests/unit/test_generated_output.py::test_order_basic_fields[regular_config] [32mPASSED[0m[32m [ 28%][0m
tests/unit/test_generated_output.py::test_order_basic_fields[cardiac_config] [32mPASSED[0m[32m [ 31%][0m
tests/unit/test_generated_output.py::test_lab_sentence_format[regular_config] [32mPASSED[0m[32m [ 34%][0m
tests/unit/test_generated_output.py::test_lab_sentence_format[cardiac_config] [32mPASSED[0m[32m [ 36%][0m
tests/unit/test_generated_output.py::test_med_sentence_start_format[regular_config] [32mPASSED[0m[32m [ 39%][0m
tests/unit/test_generated_output.py::test_med_sentence_start_format[cardiac_config] [32mPASSED[0m[32m [ 42%][0m
tests/unit/test_generated_output.py::test_med_sentence_frequency_format[regular_config] [32mPASSED[0m[32m [ 44%][0m
tests/unit/test_generated_output.py::test_med_sentence_frequency_format[cardiac_config] [32mPASSED[0m[32m [ 47%][0m
tests/unit/test_generated_output.py::test_med_sentence_infuse_over_format[regular_config] [32mPASSED[0m[32m [ 50%][0m
tests/unit/test_generated_output.py::test_med_sentence_infuse_over_format[cardiac_config] [32mPASSED[0m[32m [ 52%][0m
tests/integration/test_config_sentences.py::test_all_expected_mnemonics_found [32mPASSED[0m[32m [ 55%][0m
tests/integration/test_config_sentences.py::test_no_unexpected_mnemonics_without_expectations [32mPASSED[0m[32m [ 57%][0m
tests/integration/test_config_sentences.py::test_sentence_verification [32mPASSED[0m[32m [ 60%][0m
tests/integration/test_config_structure.py::test_generated_config_key_order[output_regular.json] [32mPASSED[0m[32m [ 63%][0m
tests/integration/test_config_structure.py::test_generated_config_key_order[output_cardiac.json] [32mPASSED[0m[32m [ 65%][0m
src/orders/lab_orders.py::src.orders.lab_orders.create_specific_timed_lab [32mPASSED[0m[32m [ 68%][0m
src/orders/lab_orders.py::src.orders.lab_orders.get_timed_lab [32mPASSED[0m[32m     [ 71%][0m
src/orders/order_builder.py::src.orders.order_builder.create_lab_order [32mPASSED[0m[32m [ 73%][0m
src/tab_builder.py::src.tab_builder._create_graphed_results [32mPASSED[0m[32m       [ 76%][0m
src/tab_builder.py::src.tab_builder._create_mnemonic [32mPASSED[0m[32m              [ 78%][0m
src/text.py::src.text.create_notify_provider_text [32mPASSED[0m[32m                 [ 81%][0m
src/utils/formatting.py::src.utils.formatting.format_level_for_concept [32mPASSED[0m[32m [ 84%][0m
src/utils/formatting.py::src.utils.formatting.format_level_for_display [32mPASSED[0m[32m [ 86%][0m
src/utils/naming.py::src.utils.naming.create_between_concept [32mPASSED[0m[32m      [ 89%][0m
src/utils/naming.py::src.utils.naming.create_between_section_name [32mPASSED[0m[32m [ 92%][0m
src/utils/naming.py::src.utils.naming.create_less_than_concept [32mPASSED[0m[32m    [ 94%][0m
src/utils/naming.py::src.utils.naming.create_less_than_section_name [32mPASSED[0m[32m [ 97%][0m
src/utils/naming.py::src.utils.naming.get_concept_name [32mPASSED[0m[32m            [100%][0m

[32m============================== [32m[1m38 passed[0m[32m in 0.36s[0m[32m ==============================[0m
