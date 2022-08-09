from dataclasses import dataclass
import urllib.request
from urllib.error import URLError

import config
from exceptions import CantGetCoordinates


@dataclass
class Coordinates:
    __slots__ = ('latitude', 'longitude')
    latitude: float
    longitude: float


def get_gps_coordinates() -> Coordinates:
    """Returns current coordinates using IP"""
    coordinates = _get_ipinfo_coordinates()
    return _round_coordinates(coordinates)


def _get_ipinfo_coordinates() -> Coordinates:
    ipinfo_output = _get_ipinfo_output()
    coordinates = _parse_coordinates(ipinfo_output)
    return coordinates


def _get_ipinfo_output() -> str:
    try:
        resource = urllib.request.urlopen("https://ipinfo.io/loc?token=" + config.IPINFO_API)
        return resource.read().decode(resource.headers.get_content_charset())
    except URLError:
        raise CantGetCoordinates


def _parse_coordinates(ipinfo_output: str) -> Coordinates:
    output = ipinfo_output.strip().split(",")
    return Coordinates(
        latitude=_parse_float_coordinate(output[0]),
        longitude=_parse_float_coordinate(output[1])
    )


def _parse_float_coordinate(value: str) -> float:
    try:
        return float(value)
    except ValueError:
        raise CantGetCoordinates


def _round_coordinates(coordinates: Coordinates) -> Coordinates:
    if not config.USE_ROUNDED_COORDS:
        return coordinates
    return Coordinates(*map(
        lambda c: round(c, 1),
        [coordinates.latitude, coordinates.longitude]
    ))


if __name__ == "__main__":
    print(get_gps_coordinates())
