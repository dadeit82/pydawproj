"""Time signature parameter class."""

from dataclasses import dataclass

from .parameter import Parameter


@dataclass
class TimeSignatureParameter(Parameter):
    """Represents a (the) time-signature parameter which can provide a value and be
    used as an automation target.
    """

    numerator: int = 4
    """Numerator of the time-signature (3/4 → 3, 4/4 → 4)."""

    denominator: int = 4
    """Denominator of the time-signature (3/4 → 4, 7/8 → 8)."""
