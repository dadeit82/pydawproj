"""Boolean parameter class."""

from dataclasses import dataclass
from typing import Optional

from .parameter import Parameter


@dataclass
class BoolParameter(Parameter):
    """Represents a parameter which can provide a boolean (true/false) value and be
    used as an automation target.
    """

    value: Optional[bool] = None
    """Boolean value for this parameter."""
