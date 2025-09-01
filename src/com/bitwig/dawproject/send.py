"""Send class for mixer sends."""

from dataclasses import dataclass
from typing import Optional

from .bool_parameter import BoolParameter
from .real_parameter import RealParameter
from .referenceable import Referenceable
from .send_type import SendType

# Forward reference to avoid circular import
Channel = "Channel"



@dataclass
class Send(Referenceable):
    """A single send of a mixer channel."""

    volume: RealParameter
    """Send level."""

    pan: Optional[RealParameter] = None
    """Send pan/balance."""

    enable: Optional[BoolParameter] = None
    """Send enable."""

    type: SendType = SendType.POST
    """Send type."""

    destination: Optional[Channel] = None
    """Send destination."""
