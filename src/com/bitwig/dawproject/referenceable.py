"""Base class for everything which can be referenced."""

from dataclasses import dataclass, field
from typing import Optional

from dataclasses_xml import dataclass_xml

from .nameable import Nameable


# Global counter for auto-generated IDs
_id_counter = 0
_enable_auto_id = False


def _generate_id() -> Optional[str]:
    """Generate an automatic ID if enabled."""
    global _id_counter, _enable_auto_id
    if _enable_auto_id:
        _id_counter += 1
        return f"id{_id_counter}"
    return None


@dataclass_xml
@dataclass
class Referenceable(Nameable):
    """Base class for everything which can be referenced."""
    
    id: Optional[str] = field(default_factory=_generate_id)
    """Unique string identifier of this element. This is used for referencing this
    instance from other elements.
    """
    
    @staticmethod
    def set_auto_id(enable: bool) -> None:
        """Enable automatic creation of XML IDs. Resets the IDs as well to 0.
        
        Args:
            enable: True to enable automatic ID creation for all instances of Referenceable
        """
        global _enable_auto_id, _id_counter
        _enable_auto_id = enable
        _id_counter = 0