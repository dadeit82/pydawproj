"""Boolean parameter class."""

from dataclasses import dataclass
from typing import Optional

from dataclasses_xml import dataclass_xml

from .parameter import Parameter


@dataclass_xml
@dataclass
class BoolParameter(Parameter):
    """Represents a parameter which can provide a boolean (true/false) value and be
    used as an automation target.
    """
    
    value: Optional[bool] = None
    """Boolean value for this parameter."""