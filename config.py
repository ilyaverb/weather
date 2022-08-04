USE_ROUNDED_COORDS = True
OPENWEATHER_API = "b917e851cda5301bb25c365cb81bf06b"
OPENWEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/weather?"
    "lat={latitude}&lon={longitude}&"
    "appid=" + OPENWEATHER_API + "&lang=ru&"
    "units=metric"
)
