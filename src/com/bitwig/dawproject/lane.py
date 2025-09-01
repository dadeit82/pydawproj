"""Lane base class."""

from dataclasses import dataclass

from .referenceable import Referenceable


@dataclass
class Lane(Referenceable):
    """Abstract base class for lanes like channels and tracks."""

    pass
