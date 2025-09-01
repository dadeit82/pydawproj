"""Transport class."""

from dataclasses import dataclass
from typing import Optional

from .real_parameter import RealParameter
from .time_signature_parameter import TimeSignatureParameter


@dataclass
class Transport:
    """Transport element containing playback parameters such as Tempo and
    Time-signature.
    """

    tempo: Optional[RealParameter] = None
    """Tempo parameter for setting and/or automating the tempo."""

    time_signature: Optional[TimeSignatureParameter] = None
    """Time-signature parameter."""
