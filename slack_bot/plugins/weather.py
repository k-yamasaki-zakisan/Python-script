import requests
import json
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

def get_weather():
    city = 'Tokyo'
    WHEATHER_KEY = os.environ['WHEATHER_KEY']
    url = f"http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&appid={WHEATHER_KEY}"

    response = requests.get(url)
    data = response.json()
    jsontext = json.dumps(data,indent=4)
    print(jsontext)

if __name__ == "__main__":
    get_weather()