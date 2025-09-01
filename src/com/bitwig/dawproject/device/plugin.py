"""Plugin base class."""

from dataclasses import dataclass
from typing import Optional

from .device import Device


@dataclass
class Plugin(Device):
    """Abstract base class for all plug-in formats."""

    plugin_version: Optional[str] = None
    """Version of the plug-in"""
