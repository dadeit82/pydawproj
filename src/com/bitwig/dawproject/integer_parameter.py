"""Integer parameter class."""

from dataclasses import dataclass
from typing import Optional

from dataclasses_xml import dataclass_xml

from .parameter import Parameter


@dataclass_xml
@dataclass
class IntegerParameter(Parameter):
    """Represents an integer parameter which can provide a value and be used as
    an automation target.
    """
    
    value: Optional[int] = None
    """Integer value for this parameter."""
    
    min: Optional[int] = None
    """Minimum value this parameter can have (inclusive)."""
    
    max: Optional[int] = None
    """Maximum value this parameter can have (inclusive)."""