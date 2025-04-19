import math

def format_level_for_display(level: float) -> str:
    """Formats a float to one decimal place.

    >>> format_level_for_display(3.14159)
    '3.1'
    >>> format_level_for_display(5.0)
    '5.0'
    >>> format_level_for_display(10)
    '10.0'
    """
    return f"{level:.1f}"

def format_level_for_concept(level: float) -> str:
    """Removes decimal by multiplying by 10 and flooring.

    >>> format_level_for_concept(3.14159)
    '31'
    >>> format_level_for_concept(5.99)
    '59'
    >>> format_level_for_concept(10.0)
    '100'
    """
    return str(math.floor(level * 10)) 