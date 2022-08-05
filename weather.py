#!/usr/bin/env python3.8
from pathlib import Path

from coordinates import get_gps_coordinates
from weather_api_service import get_weather
from weather_formatter import format_weather
from exceptions import CantGetCoordinates, ApiServiceError
from history import PlainFileWeatherStorage, save_weather


def main():
    try:
        coordinates = get_gps_coordinates()
    except CantGetCoordinates:
        print("Не смог получить GPS-координаты")
        exit(1)
    try:
        weather = get_weather(coordinates)
    except ApiServiceError:
        print("Не смог получить погоду в API-сервиса погоды")
        exit(1)
    save_weather(
        weather,
        PlainFileWeatherStorage(Path.cwd() / "history.txt")
    )
    print(format_weather(weather))


if __name__ == '__main__':
    main()
