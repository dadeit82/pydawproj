"""Mixer role enum."""

from enum import Enum


class MixerRole(Enum):
    """The role of a track or channel in the mixer."""

    REGULAR = "regular"
    """The 'default' role."""

    MASTER = "master"
    """E.g. the role of a master track."""

    EFFECT_TRACK = "effect"
    """E.g. the role of an effect track."""

    SUBMIX = "submix"
    """E.g. the role of a group track."""

    VCA = "vca"
    """The role of a VCA track."""
