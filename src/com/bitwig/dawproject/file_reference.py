"""File reference class."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class FileReference:
    """References a file either within a DAWproject container or on disk."""

    path: str = ""
    """File path. Either:
    - path within the container
    - relative to .dawproject file (when external = "true")
    - absolute path (when external = "true" and path starts with a slash or
      windows drive letter)
    """

    external: Optional[bool] = None
    """When true, the path is relative to the .dawproject file.
    Default value is false.
    """
