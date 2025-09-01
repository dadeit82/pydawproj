"""Application metadata class."""

from dataclasses import dataclass


@dataclass
class Application:
    """Metadata about the application which saved the DAWPROJECT file."""

    name: str = ""
    """Name of the application."""

    version: str = ""
    """Version number of the application."""
