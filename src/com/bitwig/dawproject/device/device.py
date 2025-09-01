"""Base Device class."""

from dataclasses import dataclass, field
from typing import Optional

from ..bool_parameter import BoolParameter
from ..file_reference import FileReference
from ..parameter import Parameter
from ..referenceable import Referenceable
from .device_role import DeviceRole


@dataclass
class Device(Referenceable):
    """Either a Plug-in or native Device within a DAW."""

    enabled: Optional[BoolParameter] = None
    """This device is enabled (as in not bypassed)."""

    device_role: DeviceRole = DeviceRole.AUDIO_FX
    """Role of this device/plug-in."""

    loaded: bool = True
    """If this device/plug-in is loaded/active of not."""

    device_name: str = ""
    """Name of the device/plugin"""

    device_id: Optional[str] = None
    """Unique identifier of device/plug-in.

    Standards which use UUID as an identifier use the canonical textual
    representation of the UUID (8-4-4-4-12 with no braces) (VST3)
    Standards which use an integer as an identifier use the value in decimal
    form. (base-10 unsigned) (VST2)
    Text-based identifiers are used as-is. (CLAP)
    """

    device_vendor: Optional[str] = None
    """Vendor name of the device/plugin"""

    state: Optional[FileReference] = None
    """Path to a file representing the device / plug-in state in its native format.

    This file must be embedded inside the container ZIP and have the
    FileReference configured with (external=false).
    """

    automated_parameters: list[Parameter] = field(default_factory=list)
    """Parameters for this device, which is required for automated parameters in
    order to provide an ID.

    Note: If the automated parameter is already present like the BuiltinDevice
    parameters, it should not be included here as well.
    """
