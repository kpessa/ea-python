#!/usr/bin/env python
import pandas as pd
import os
from typing import List, Dict, Optional

# Updated path relative to project root if script moves
# DCW_FILE = 'dcw_order_sentences/dcw.txt' 

# Known identifiers to help parsing state
PROTOCOLS = ["Regular", "Cardiac", "DKA"]
ELECTROLYTES = ["Magnesium", "Potassium", "Phosphorus", "Calcium"]
HEADER_START = "Mnemonic\tOrder_Sentence"

def parse_dcw_file(filepath: str) -> List[Dict[str, Optional[str]]]:
    """Parses the structured text file into a list of order dictionaries."""
    if not os.path.exists(filepath):
        print(f"ERROR: File not found: {filepath}")
        return []

    all_orders: List[Dict[str, Optional[str]]] = []
    current_protocol: Optional[str] = None
    current_electrolyte: Optional[str] = None
    in_data_section = False
    header_columns = []
    lines_iterator = None # To manually advance the iterator

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            # Use an iterator to allow peeking/consuming the next line
            lines_iterator = enumerate(f)
            
            while True: # Loop until StopIteration
                try:
                    line_num, line = next(lines_iterator)
                except StopIteration:
                    break # End of file

                line = line.strip()
                if not line:
                    in_data_section = False
                    continue

                # --- State Machine (remains the same) ---
                if line in PROTOCOLS:
                    current_protocol = line
                    current_electrolyte = None
                    in_data_section = False
                    continue
                if current_protocol and line in ELECTROLYTES:
                    current_electrolyte = line
                    in_data_section = False
                    continue
                if current_protocol and current_electrolyte and line.startswith(HEADER_START):
                    header_columns = [h.strip() for h in line.split('\t')]
                    if header_columns[0].lower() != 'mnemonic':
                         print(f"Warning L{line_num+1}: Unexpected header start: {line}")
                         continue
                    in_data_section = True
                    continue
                
                # --- Data Parsing (modified again) ---
                if in_data_section and current_protocol and current_electrolyte:
                    parts = [p.strip() for p in line.split('\t')] 
                    last_field_override = None

                    # Check if the last field is just '"', indicating continuation
                    if len(parts) == len(header_columns) and parts[-1] == '"':
                        try:
                            # Read the next line, assuming it's the continuation
                            _, next_line_content = next(lines_iterator)
                            # Clean up potential quotes and whitespace
                            last_field_override = next_line_content.strip().strip('"') 
                        except StopIteration:
                            print(f"Warning L{line_num+1}: Found trailing quote but reached end of file: {line}")
                            # Keep parts[-1] as '"' in this case
                        except Exception as e_inner:
                             print(f"Warning L{line_num+1}: Error reading continuation line after quote: {e_inner}")
                             # Keep parts[-1] as '"'

                    # Create dictionary safely
                    order_data: Dict[str, Optional[str]] = {
                        'Protocol': current_protocol,
                        'Electrolyte': current_electrolyte,
                    }
                    for i, col_name in enumerate(header_columns):
                        try:
                            # Use the override if it exists for the last column
                            if last_field_override is not None and i == len(header_columns) - 1:
                                order_data[col_name] = last_field_override
                            else:
                                order_data[col_name] = parts[i]
                        except IndexError:
                            # This handles cases where the line had fewer columns than expected initially
                            order_data[col_name] = None 
                    
                    # Explicitly strip Instructions/Note field if it exists (still useful)
                    instr_note_key = 'Instructions/Note'
                    if instr_note_key in order_data and isinstance(order_data[instr_note_key], str):
                        order_data[instr_note_key] = order_data[instr_note_key].strip()
                        
                    if order_data.get('Mnemonic') and order_data.get('Order_Sentence'):
                        all_orders.append(order_data)
                    else:
                        pass # Ignore lines that still don't parse correctly
                        
    except Exception as e:
        print(f"ERROR: Failed to read or parse file {filepath}: {e}")
        return [] # Return empty on error

    return all_orders

# Keep the main execution block for potential direct script running/testing
if __name__ == "__main__":
    # Adjust path relative to the new location if run directly
    # Assumes running from project root: python -m python.utils.parse_dcw
    DCW_FILE = 'dcw_order_sentences/dcw.txt'
    print(f"Parsing file: {DCW_FILE}")
    parsed_data = parse_dcw_file(DCW_FILE)

    if parsed_data:
        df = pd.DataFrame(parsed_data)
        print("\n--- Parsed Data DataFrame Info ---")
        df.info()
        print("\n--- Parsed Data DataFrame Head ---")
        print(df.head())
        print("\n--- Parsed Data DataFrame Tail ---")
        print(df.tail())
        # Optionally save to CSV
        # output_csv = 'dcw_parsed.csv'
        # df.to_csv(output_csv, index=False)
        # print(f"\nParsed data saved to {output_csv}")
    else:
        print("\nNo data parsed.") 