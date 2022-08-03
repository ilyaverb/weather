from dataclasses import dataclass
from subprocess import Popen, PIPE

from exceptions import CantGetCoordinates

import json


# @dataclass(frozen=True, slots=True)
@dataclass
class Coordinates:
    __slots__ = ('latitude', 'longitude')
    latitude: float
    longitude: float


def get_gps_coordinates() -> Coordinates:
    """Returns current coordinates using IP"""
    process = Popen(["curl", "https://ipinfo.io/"], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    if err is not None or exit_code != 0:
        raise CantGetCoordinates
    data = json.loads(output)['loc']
    latitude, longitude = data.strip().split(',')
    return Coordinates(longitude=float(longitude), latitude=float(latitude))


if __name__ == "__main__":
    print(get_gps_coordinates())

