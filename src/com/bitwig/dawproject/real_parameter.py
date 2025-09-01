"""Real parameter class."""

from dataclasses import dataclass
from typing import Optional

from .parameter import Parameter
from .unit import Unit


@dataclass
class RealParameter(Parameter):
    """Represents a real valued (double) parameter which can provide a value and be
    used as an automation target.
    """

    value: Optional[float] = None
    """Real (double) value for this parameter.

    When serializing value to text for XML, infinite values are allowed and
    should be represented as inf and -inf.
    """

    unit: Optional[Unit] = None
    """Unit in which value, minimum and maximum are defined.

    Using this rather than normalized value ranges allows transfer of parameter
    values and automation data.
    """

    min: Optional[float] = None
    """Minimum value this parameter can have (inclusive)."""

    max: Optional[float] = None
    """Maximum value this parameter can have (inclusive)."""
