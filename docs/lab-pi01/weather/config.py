from dotenv import dotenv_values

config = dotenv_values("/srv/weather/config/.env")

API_KEY = config["API_KEY"]
APP_KEY = config["APP_KEY"]
