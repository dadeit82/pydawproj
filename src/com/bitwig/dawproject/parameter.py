"""Base Parameter class."""

from abc import ABC
from dataclasses import dataclass
from typing import Optional

from dataclasses_xml import dataclass_xml

from .referenceable import Referenceable


@dataclass_xml
@dataclass
class Parameter(Referenceable, ABC):
    """Represents a parameter which can provide a value and be used as an automation target."""
    
    parameter_id: Optional[int] = None
    """Parameter ID as used by VST2 (index), VST3(ParamID)."""