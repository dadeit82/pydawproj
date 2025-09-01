"""Content type enum."""

from enum import Enum


class ContentType(Enum):
    """The type of the content."""
    
    AUDIO = "audio"
    """Audio content."""
    
    AUTOMATION = "automation"
    """Automation content."""
    
    NOTES = "notes"
    """Notes content."""
    
    VIDEO = "video"
    """Video content."""
    
    MARKERS = "markers"
    """Markers content."""
    
    TRACKS = "tracks"
    """Tracks content."""