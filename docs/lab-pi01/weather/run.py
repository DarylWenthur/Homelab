#!/usr/bin/env python3

import subprocess

print("Updating weather...")

subprocess.run(["python3", "/srv/weather/api.py"], check=True)
subprocess.run(["python3", "/srv/weather/output.py"], check=True)
subprocess.run(["python3", "/srv/weather/weather.py"], check=True)

print("\nDone.")
