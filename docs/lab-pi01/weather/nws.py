#!/usr/bin/env python3

import requests

LAT = 47.9212
LON = -121.9651

HEADERS = {
    "User-Agent": "LabPi01 Weather Service"
}


def get_alerts():
    url = f"https://api.weather.gov/alerts/active?point={LAT},{LON}"

    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()

    alerts = response.json()["features"]

    if not alerts:
        return ["No Weather Alerts"]

    return [alert["properties"]["event"] for alert in alerts]


if __name__ == "__main__":
    for alert in get_alerts():
        print(alert)
