"""Project class - main root element."""

from dataclasses import dataclass, field
from typing import Optional

from .application import Application
from .lane import Lane
from .transport import Transport

# Forward references to timeline classes
Arrangement = "Arrangement"
Scene = "Scene"



@dataclass
class Project:
    """The main root element of the DAWPROJECT format. This is stored in the file
    project.xml file inside the container.
    """

    CURRENT_VERSION = "1.0"

    version: str = CURRENT_VERSION
    """Version of DAWPROJECT format this file was saved as."""

    application: Application = field(default_factory=Application)
    """Metadata (name/version) about the application that saved this file."""

    transport: Optional[Transport] = None
    """Transport element containing playback parameters such as Tempo and Time-signature."""

    structure: list[Lane] = field(default_factory=list)
    """Track/Channel structure of this file."""

    arrangement: Optional[Arrangement] = None
    """The main Arrangement timeline of this file."""

    scenes: list[Scene] = field(default_factory=list)
    """Clip Launcher scenes of this file."""
