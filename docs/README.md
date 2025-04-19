# EA Python Project

This Python project generates JSON configurations for Electrolyte Advisor protocols.

## Project Structure

```
ea-python/
├── src/                  # All production code
│   ├── protocols/        # Protocol-specific implementations
│   │   ├── CARDIAC/      # Cardiac protocol logic
│   │   └── REGULAR/      # Regular protocol logic
│   └── utils/            # Utility functions and helpers
├── tests/                # Test suite
│   ├── fixtures/         # Test data
│   │   ├── dcw_sentences/    # DCW order sentence data
│   │   └── expected_sentences/    # Expected sentence data
│   ├── unit/             # Unit tests
│   └── integration/      # Integration tests (future)
├── generated_configs/    # Output directory for generated JSON
├── scripts/              # Helper scripts
│   └── build.py          # Main build script
└── docs/                 # Documentation
```

## Running the Build

To run the build and generate configurations:

```bash
python scripts/build.py
```

This will:
1. Generate JSON configurations for all protocols
2. Run all tests
3. Output results to output.py

## Testing

Tests are run as part of the build process, but can also be run directly:

```bash
python -m pytest tests/unit
```

Test fixtures are stored in `tests/fixtures/` and used by the tests to validate the generated output. 