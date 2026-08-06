#!/usr/bin/env python3

from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

os.chdir("/srv/weather/data")

server = HTTPServer(("0.0.0.0", 8088), SimpleHTTPRequestHandler)

print("Serving weather data on port 8088")

server.serve_forever()
