import json
import os
import sys
import subprocess # Added for running test script
from typing import List, cast

# --- Constants ---
# Define paths relative to the script's location (assumed project root)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
GENERATED_CONFIG_DIR = os.path.join(SCRIPT_DIR, 'generated_configs')
DCW_ORDER_SENTENCES_FILE = os.path.join(SCRIPT_DIR, 'dcw_order_sentences', 'dcw.txt')

# Ensure the parent directory (project root) is in the path for relative imports
# This might not be strictly necessary depending on how the script is run,
# but helps ensure modules are found when running `python python/build.py` from root.
# current_dir = os.path.dirname(os.path.abspath(__file__))
# project_root = os.path.dirname(current_dir)
# if project_root not in sys.path:
#     sys.path.insert(0, project_root)

# Use absolute imports assuming 'python' is a package relative to project root
from python.types import GenerationContext, Protocol
from python.helpers import get_generation_context
from python.config import generate_config

def main():
    """Main build function to generate JSON configs."""
    print('Starting Python build process...')

    # --- Get Context from Environment Variables ---
    # Similar to TS version, get context once, but generate_config uses it per protocol.
    try:
        base_context = get_generation_context()
        print(f"Base context: {base_context}")
    except ValueError as e:
        print(f"Error reading environment variables: {e}", file=sys.stderr)
        sys.exit(1)

    # --- Define Output Directory (now uses constant) ---
    # Output to a 'generated_configs' subdirectory within the project root
    # script_dir = os.path.dirname(os.path.abspath(__file__)) # No longer needed here
    # project_root = script_dir # No longer needed here
    output_dir = GENERATED_CONFIG_DIR # Use the constant
    print(f"Output directory set to: {output_dir}")
    os.makedirs(output_dir, exist_ok=True) # Ensure the directory exists

    # --- Generate and Write Configs ---
    protocols_to_build: List[Protocol] = ['REGULAR', 'CARDIAC'] # Add 'DKA' when ready

    build_failed = False
    for protocol in protocols_to_build:
        print(f"\nGenerating config for protocol: {protocol}...")

        # Create context specific to this protocol iteration
        current_context: GenerationContext = {
            'protocol': protocol,
            'routeStyle': base_context['routeStyle'],
            'showTotalDose': base_context['showTotalDose'],
        }

        try:
            config_data = generate_config(current_context)
            output_filename = f"output_{protocol.lower()}.json"
            output_path = os.path.join(output_dir, output_filename)

            # Write the file with pretty printing (indent=2)
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(config_data, f, indent=2, ensure_ascii=False)
            
            print(f"Successfully wrote {output_filename} to {output_path}")

        except Exception as e:
            print(f"Error generating config for protocol {protocol}: {e}", file=sys.stderr)
            import traceback
            traceback.print_exc(file=sys.stderr) # Print stack trace for debugging
            build_failed = True # Mark build as failed but continue

    print('\nPython build process completed.')

    # --- Run Automated Tests ---
    print("\nRunning automated configuration tests...")
    try:
        # Assuming test_configs.py is in the same directory as build.py (project root)
        # test_script_path = os.path.join(os.path.dirname(__file__), 'test_configs.py') # Old way
        
        # Ensure pytest is installed (optional but good practice)
        # You might run `pip install -r requirements.txt` separately before the build
        
        # Run pytest using the same Python executable that ran build.py
        # pytest will automatically discover tests in files named test_*.py or *_test.py
        # The -v flag increases verbosity for clearer output
        # The -r w flag adds warnings to the short test summary info
        # The -W always flag attempts to show all warnings
        pytest_command = [sys.executable, '-m', 'pytest', '-v', '-r', 'w', '-W', 'always']
        result = subprocess.run(pytest_command, check=False, capture_output=True, text=True, encoding='utf-8')
        print(result.stdout)
        if result.returncode != 0:
            print(result.stderr, file=sys.stderr) # Print pytest stderr output
            print("\nConfiguration tests failed!", file=sys.stderr)
            build_failed = True # Mark build as failed
        else:
            print("Configuration tests passed.")
    # except FileNotFoundError: # Less likely with pytest module execution
    #      print(f"ERROR: Test script not found at {test_script_path}", file=sys.stderr)
    #      build_failed = True
    except Exception as e:
        print(f"ERROR: An exception occurred while running tests: {e}", file=sys.stderr)
        build_failed = True

    # --- Final Build Status ---
    if build_failed:
        print("\nBuild finished with errors.", file=sys.stderr)
        sys.exit(1)
    else:
        print("\nBuild finished successfully.")

if __name__ == "__main__":
    main() 