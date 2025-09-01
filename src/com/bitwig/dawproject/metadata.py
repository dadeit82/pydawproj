"""MetaData class for DAWPROJECT format."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class MetaData:
    """Metadata root element of the DAWPROJECT format. This is stored in the file
    metadata.xml file inside the container.
    """

    title: Optional[str] = None
    """Title of the song/project."""

    artist: Optional[str] = None
    """Recording Artist."""

    album: Optional[str] = None
    """Album."""

    original_artist: Optional[str] = None
    """Original Artist."""

    composer: Optional[str] = None
    """Composer."""

    songwriter: Optional[str] = None
    """Songwriter."""

    producer: Optional[str] = None
    """Producer."""

    arranger: Optional[str] = None
    """Arranger."""

    year: Optional[str] = None
    """Year this project/song was recorded."""

    genre: Optional[str] = None
    """Genre/style"""

    copyright: Optional[str] = None
    """Copyright notice."""

    website: Optional[str] = None
    """URL to website related to this project."""

    comment: Optional[str] = None
    """General comment or description."""
