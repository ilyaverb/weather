class CantGetCoordinates(Exception):
    """Program can't get current GPS coordinates"""


class ApiServiceError(Exception):
    """Program can't get weather from API service"""


class CantSaveHistory(Exception):
    """Program can't save a file"""
