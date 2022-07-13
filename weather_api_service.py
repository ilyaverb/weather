from dataclasses import dataclass
from datetime import datetime
from typing import TypeAlias

from coordinates import Coordinates

Celsius: TypeAlias = int


@dataclass(slots=True, frozen=True)
class Weather:
    temperature: Celsius
    weather_type: str
    sunrise: datetime
    sunset: datetime
    city: str


def get_weather(coordinates: Coordinates):
    """Requests weather in OpenWeather API and returns it"""
    pass
