"""Track class for sequencer tracks."""

from dataclasses import dataclass, field
from typing import Optional

from .channel import Channel
from .content_type import ContentType
from .lane import Lane


@dataclass
class Track(Lane):
    """Represents a sequencer track."""

    content_type: Optional[list[ContentType]] = None
    """Role of this track in timelines & arranger. Can be multiple."""

    loaded: Optional[bool] = None
    """If this track is loaded/active of not."""

    channel: Optional[Channel] = None
    """Mixer channel used for the output of this track."""

    tracks: list["Track"] = field(default_factory=list)
    """Child tracks, typically used to represent group/folder tracks with
    contentType="tracks".
    """
