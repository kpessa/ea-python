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
# from python.helpers import get_generation_context # OLD IMPORT
from python.env import get_generation_context    # NEW IMPORT
from python.config import generate_config

def main():
    """Main build function to generate JSON configs."""
    # print('Starting Python build process...') # Quieten

    # --- Get Context from Environment Variables ---
    # Similar to TS version, get context once, but generate_config uses it per protocol.
    try:
        base_context = get_generation_context()
        # print(f"Base context: {base_context}") # Quieten
    except ValueError as e:
        print(f"Error reading environment variables: {e}", file=sys.stderr)
        sys.exit(1)

    # --- Define Output Directory (now uses constant) ---
    output_dir = GENERATED_CONFIG_DIR # Use the constant
    # print(f"Output directory set to: {output_dir}") # Quieten
    os.makedirs(output_dir, exist_ok=True) # Ensure the directory exists

    # --- Generate and Write Configs ---
    protocols_to_build: List[Protocol] = ['REGULAR', 'CARDIAC'] # Add 'DKA' when ready

    build_failed = False
    for protocol in protocols_to_build:
        # print(f"\\\\nGenerating config for protocol: {protocol}...") # Quieten

        # Update base_context directly with the current protocol
        base_context['protocol'] = protocol

        try:
            # Pass the updated base_context directly
            config_data = generate_config(base_context)
            output_filename = f"output_{protocol.lower()}.json"
            output_path = os.path.join(output_dir, output_filename)

            # Write the file with pretty printing (indent=2)
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(config_data, f, indent=2, ensure_ascii=False)
            
            # print(f"Successfully wrote {output_filename} to {output_path}") # Quieten

        except Exception as e:
            print(f"Error generating config for protocol {protocol}: {e}", file=sys.stderr)
            import traceback
            traceback.print_exc(file=sys.stderr) # Print stack trace for debugging
            build_failed = True # Mark build as failed but continue

    # print('\\\\nPython build process completed.') # Quieten

    # --- Run Automated Tests ---
    # print("\\\\nRunning automated configuration tests...") # Quieten
    try:
        # Define directories for pytest to scan
        test_dirs = ["tests/", "python/"]  # Scan tests/ and python/ (for doctests)

        # Construct the pytest command
        pytest_command = [
            ".venv/bin/python",
            "-m",
            "pytest",
            "-v",                   # Verbose output
            "--doctest-modules",    # Run doctests in modules
            "--color=yes",          # Force color output
            "--code-highlight=yes", # Enable code highlighting
            "--showlocals",         # Show local variables in tracebacks
            # "--lf",               # Run only last failed tests (useful for iteration)
            *test_dirs
        ]

        # Open the output file
        output_py_path = os.path.join(SCRIPT_DIR, 'output.py')
        with open(output_py_path, 'w', encoding='utf-8') as outfile:
            # Run pytest directing output to the file
            result = subprocess.run(
                pytest_command, 
                check=False, 
                stdout=outfile, # Redirect stdout to file
                stderr=outfile, # Redirect stderr to file
                text=True, 
                encoding='utf-8'
            )
        
        # No longer print stdout/stderr here as it went to the file
        # print(result.stdout) 
        if result.returncode != 0:
            # print(result.stderr, file=sys.stderr) # Output already in file
            # print(f"\\\\nPytest output written to {output_py_path}", file=sys.stderr) # Quieten
            print("\\\\nConfiguration tests failed!", file=sys.stderr)
            build_failed = True # Mark build as failed
        else:
            # print(f"\\\\nPytest output written to {output_py_path}") # Quieten
            # print("Configuration tests passed.") # Quieten
            pass # Keep structure
    # except FileNotFoundError: # Less likely with pytest module execution
    #      print(f"ERROR: Test script not found at {test_script_path}", file=sys.stderr)
    except Exception as e:
        print(f"ERROR: An exception occurred while running tests: {e}", file=sys.stderr)
        build_failed = True

    # --- Final Build Status ---
    if build_failed:
        print("\\\\nBuild finished with errors.", file=sys.stderr)
        sys.exit(1)
    else:
        # print("\\\\nBuild finished successfully.") # Quieten
        pass # Keep structure

if __name__ == "__main__":
    main() 