#!/bin/bash

API_KEY="2b054d97142a48ffa6d1b91755205d0c829b2fe5a9c4474692ed0cd358f1b27b"
APP_KEY="66fd10b2dac54ba5a2c41039f1ee1d80a509c62993414b0d81aaae99a9c9bb3e"

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
