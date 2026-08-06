#!/usr/bin/env python3

import json
from nws import get_alerts

# Read downloaded weather data
with open("/srv/weather/data/weather.json", "r") as f:
    weather = json.load(f)

data = weather[0]["lastData"]

homepage = {
    "outside_temp": data["tempf"],
    "outside_humidity": data["humidity"],
    "house_temp": data["tempinf"],
    "shop_temp": data["temp1f"],
    "shop_humidity": data["humidity1"],
    "wind": data["windspeedmph"],
    "rain_today": data["dailyrainin"],
    "alerts": get_alerts()
}

with open("/srv/weather/data/homepage.json", "w") as f:
    json.dump(homepage, f, indent=4)

print("Created /srv/weather/data/homepage.json")
