"""Channel class for mixer channels."""

from dataclasses import dataclass, field
from typing import Optional

from .bool_parameter import BoolParameter
from .lane import Lane
from .mixer_role import MixerRole
from .real_parameter import RealParameter

# Forward references to avoid circular imports
Send = "Send"
Device = "Device"



@dataclass
class Channel(Lane):
    """Represents a mixer channel. It provides the ability to route signals to other
    channels and can contain Device/Plug-in for processing.
    """

    role: Optional[MixerRole] = None
    """Role of this channel in the mixer."""

    audio_channels: int = 2
    """Number of audio-channels of this mixer channel. (1=mono, 2=stereo…)"""

    volume: Optional[RealParameter] = None
    """Channel volume"""

    pan: Optional[RealParameter] = None
    """Channel pan/balance"""

    mute: Optional[BoolParameter] = None
    """Channel mute"""

    solo: Optional[bool] = None
    """Channel solo"""

    destination: Optional["Channel"] = None
    """Output channel routing"""

    sends: list[Send] = field(default_factory=list)
    """Send levels & destination"""

    devices: list[Device] = field(default_factory=list)
    """Devices & plug-ins of this channel"""
