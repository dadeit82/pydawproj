"""Double adapter for handling infinity constants."""

import math
from typing import Optional


def double_to_string(value: Optional[float]) -> Optional[str]:
    """Convert a double value to string, handling infinity constants.

    Args:
        value: The double value to convert

    Returns:
        String representation of the value
    """
    if value is None:
        return None
    if math.isinf(value):
        return "inf" if value > 0 else "-inf"
    return f"{value:.6f}"


def string_to_double(value: Optional[str]) -> Optional[float]:
    """Convert a string to double value, handling infinity constants.

    Args:
        value: The string value to convert

    Returns:
        Double representation of the value
    """
    if value is None or value == "" or value == "null":
        return None
    if value == "inf":
        return math.inf
    if value == "-inf":
        return -math.inf
    return float(value)
