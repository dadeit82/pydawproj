"""Units for parameter values."""

from enum import Enum


class Unit(Enum):
    """Units for parameter values."""

    LINEAR = "linear"
    """Linear."""

    NORMALIZED = "normalized"
    """A normalized value (0-1)."""

    PERCENT = "percent"
    """A percentage value (0-100)."""

    DECIBEL = "decibel"
    """A decibel value (dB)."""

    HERTZ = "hertz"
    """A frequency value in Hertz."""

    SEMITONES = "semitones"
    """A semi-tone value."""

    SECONDS = "seconds"
    """A time value in seconds."""

    BEATS = "beats"
    """A time value in beats (quarter notes)."""

    BPM = "bpm"
    """A beats-per-minute value."""
