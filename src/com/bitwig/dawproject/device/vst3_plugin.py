"""VST3 Plugin class."""

from dataclasses import dataclass

from .plugin import Plugin


@dataclass
class Vst3Plugin(Plugin):
    """A VST3 Plug-in instance.

    The VST3 plug-in state should be stored in .vstpreset format.
    """

    pass
