"""Application metadata class."""

from dataclasses import dataclass
from typing import Optional

from dataclasses_xml import dataclass_xml


@dataclass_xml
@dataclass
class Application:
    """Metadata about the application which saved the DAWPROJECT file."""
    
    name: str
    """Name of the application."""
    
    version: str  
    """Version number of the application."""