#!/bin/bash

API_KEY=""
APP_KEY=""

curl -s "https://api.ambientweather.net/v1/devices?applicationKey=${APP_KEY}&apiKey=${API_KEY}" | python3 -c '
import json
import sys

data = json.load(sys.stdin)[0]["lastData"]

print("======================================")
print("      Home Environment")
print("======================================")
print(f"Outside : {data['\''tempf'\'']}°F")
print(f"Humidity: {data['\''humidity'\'']}%")
print(f"Wind    : {data['\''windspeedmph'\'']} mph")
print(f"Pressure: {data['\''baromrelin'\'']} inHg")
print(f"Rain    : {data['\''dailyrainin'\'']} in")
print()
print(f"House   : {data['\''tempinf'\'']}°F")
print()
print(f"Shop    : {data['\''temp1f'\'']}°F")
print(f"Humidity: {data['\''humidity1'\'']}%")
print("======================================")
'
