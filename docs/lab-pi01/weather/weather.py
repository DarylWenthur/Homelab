#!/usr/bin/env python3

import json
from nws import get_alerts

with open("/srv/weather/data/weather.json", "r") as f:
    weather = json.load(f)

data = weather[0]["lastData"]
alerts = get_alerts()

print("====================================")
print("      HOME ENVIRONMENT")
print("====================================")
print(f"🌤 Outside : {data['tempf']}°F")
print(f"🏠 House   : {data['tempinf']}°F")
print(f"🛠 Shop    : {data['temp1f']}°F")
print("------------------------------------")
print(f"Outside Humidity : {data['humidity']}%")
print(f"Shop Humidity    : {data['humidity1']}%")
print(f"💨 Wind           : {data['windspeedmph']} mph")
print(f"🌧 Rain Today     : {data['dailyrainin']} in")
print("------------------------------------")
print("⚠ Weather Alerts")

for alert in alerts:
    print(f"  • {alert}")

print("====================================")
