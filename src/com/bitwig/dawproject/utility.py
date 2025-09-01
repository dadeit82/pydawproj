"""Utility class for creating DAWproject objects."""


from .channel import Channel
from .content_type import ContentType
from .mixer_role import MixerRole
from .real_parameter import RealParameter
from .track import Track
from .unit import Unit


class Utility:
    """Helper class to create different DAWproject objects."""

    @staticmethod
    def create_track(
        name: str,
        content_types: set[ContentType],
        mixer_role: MixerRole,
        volume: float,
        pan: float,
    ) -> Track:
        """Create a track.

        Args:
            name: The name of the track
            content_types: The content types that can be placed on the track
            mixer_role: The mixer role of the track
            volume: The volume setting of the track
            pan: The panorama setting of the track

        Returns:
            The track instance
        """
        track = Track()
        track.channel = Channel()
        track.name = name
        track.channel.volume = Utility.create_real_parameter(Unit.LINEAR, volume)
        track.channel.pan = Utility.create_real_parameter(Unit.NORMALIZED, pan)
        track.content_type = list(content_types)
        track.channel.role = mixer_role
        return track

    @staticmethod
    def create_real_parameter(unit: Unit, value: float) -> RealParameter:
        """Create a real parameter instance.

        Args:
            unit: The unit of the parameter
            value: The value of the parameter

        Returns:
            The parameter
        """
        param = RealParameter()
        param.unit = unit
        param.value = value
        return param

    @staticmethod
    def create_real_parameter_with_range(
        unit: Unit, min_val: float, max_val: float, value: float
    ) -> RealParameter:
        """Create a real parameter instance with range.

        Args:
            unit: The unit of the parameter
            min_val: The minimum value of the parameter
            max_val: The maximum value of the parameter
            value: The value of the parameter

        Returns:
            The parameter
        """
        param = Utility.create_real_parameter(unit, value)
        param.min = min_val
        param.max = max_val
        return param
