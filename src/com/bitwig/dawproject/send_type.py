"""Send type enum."""

from enum import Enum


class SendType(Enum):
    """The type of a send."""

    PRE = "pre"
    """A pre-fader send."""

    POST = "post"
    """A post-fader send."""
