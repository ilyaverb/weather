#!/usr/bin/env python3.8
from coordinates import get_gps_coordinates
from weather_api_service import get_weather
from weather_formatter import format_weather


def main():
    coordinates = get_gps_coordinates()
    print(f"Широта:", coordinates.latitude)
    weather = get_weather(coordinates)
    print(format_weather(weather))


if __name__ == '__main__':
    main()
