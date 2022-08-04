import json
from dataclasses import dataclass
from subprocess import Popen, PIPE
from typing import Literal, Union, List, Dict

import config
from exceptions import CantGetCoordinates


# @dataclass(frozen=True, slots=True)
@dataclass
class Coordinates:
    __slots__ = ('latitude', 'longitude')
    latitude: float
    longitude: float


def get_gps_coordinates() -> Coordinates:
    """Returns current coordinates using IP"""
    coordinates = _get_ip_coordinates()
    return _round_coordinates(coordinates)


def _get_ip_coordinates() -> Coordinates:
    ipinfo_output = _get_ipinfo_output()
    coordinates = _parse_coordinates(ipinfo_output)
    return coordinates


def _get_ipinfo_output() -> bytes:
    process = Popen(["curl", "https://ipinfo.io/"], stdout=PIPE)
    output, err = process.communicate()
    exit_code = process.wait()
    if err is not None or exit_code != 0:
        raise CantGetCoordinates
    return output


def _parse_coordinates(ipinfo_output: bytes) -> Coordinates:
    output = json.loads(ipinfo_output)
    latitude, longitude = _parse_coord(output, "loc")
    return Coordinates(
        latitude=latitude,
        longitude=longitude
    )


def _parse_coord(
        output: Dict[str, str],
        coord_type: Literal["loc"]) -> List[float]:
    return _parse_float_coordinates(output[coord_type].strip().split(','))


def _parse_float_coordinates(values: List[str]) -> List[float]:
    try:
        return [float(value) for value in values]
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
