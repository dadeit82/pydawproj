"""Base class for everything with a name."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Nameable:
    """Base class for everything with a name."""

    name: Optional[str] = None
    """Name/label of this object."""

    color: Optional[str] = None
    """Color of this object in HTML-style format. (#rrggbb)"""

    comment: Optional[str] = None
    """Comment/description of this object."""
