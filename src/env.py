import os
from typing import cast
from .types import GenerationContext, Protocol

def get_generation_context() -> GenerationContext:
    """Reads environment variables to determine build context."""
    # Default values mimic compile.sh
    raw_protocol = os.environ.get('EA_PROTOCOL', 'REGULAR')

    # Basic validation
    protocol = cast(Protocol, raw_protocol)
    if protocol not in ['REGULAR', 'CARDIAC', 'DKA']:
        raise ValueError(f"Invalid EA_PROTOCOL: {protocol}")

    return {
        'protocol': protocol,
    } 