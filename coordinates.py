from typing import NamedTuple


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


def get_gps_coordinates() -> Coordinates:
    """Returns current coordinates using IP"""
    return Coordinates(10, 20)
