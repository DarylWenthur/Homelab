#!/usr/bin/env python3

import json
import requests
from config import API_KEY, APP_KEY

url = (
    "https://api.ambientweather.net/v1/devices"
    f"?applicationKey={APP_KEY}&apiKey={API_KEY}"
)

response = requests.get(url, timeout=10)
response.raise_for_status()

with open("/srv/weather/data/weather.json", "w") as f:
    json.dump(response.json(), f, indent=4)

print("Weather data saved to /srv/weather/data/weather.json")
