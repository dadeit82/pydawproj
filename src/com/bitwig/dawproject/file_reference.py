"""File reference class."""

from dataclasses import dataclass
from typing import Optional

from dataclasses_xml import dataclass_xml


@dataclass_xml
@dataclass
class FileReference:
    """References a file either within a DAWproject container or on disk."""
    
    path: str
    """File path. Either:
    - path within the container
    - relative to .dawproject file (when external = "true")
    - absolute path (when external = "true" and path starts with a slash or windows drive letter)
    """
    
    external: Optional[bool] = None
    """When true, the path is relative to the .dawproject file. Default value is false."""