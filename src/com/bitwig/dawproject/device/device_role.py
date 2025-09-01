"""Device role enum."""

from enum import Enum


class DeviceRole(Enum):
    """The role of a device."""

    INSTRUMENT = "instrument"
    """An instrument device."""

    NOTE_FX = "noteFX"
    """A note/MIDI effect device."""

    AUDIO_FX = "audioFX"
    """An audio effect device."""

    ANALYZER = "analyzer"
    """An analyzer device."""
