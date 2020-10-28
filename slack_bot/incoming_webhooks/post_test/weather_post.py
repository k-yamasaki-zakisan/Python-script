import requests
import json

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../../.env')
load_dotenv(dotenv_path)

WHEATHER_KEY = os.environ['WHEATHER_KEY']

url = f"http://api.openweathermap.org/data/2.5/weather?units=metric&q=Tokyo&appid={WHEATHER_KEY}"

data = requests.get(url)
data = data.json()
# jsontext = json.dumps(data,indent=4)

weather_text = ''

weather_text += f"都市：{data['name']}\n"
weather_text += f"天候：{data['weather'][0]['main']}\n"
weather_text += f"温度：{str(data['main']['temp'])}度\n"

# WEB_HOOK_URLは下準備で発行したURLを設定しください
WEB_HOOK_URL = os.environ['WEB_HOKK_URL']

requests.post(WEB_HOOK_URL, data=json.dumps({
    "text" : weather_text,
    "icon_emoji" : ":mostly_sunny:",
    "username" : "weather_news_bot",
    # "color":"#D00000",
    # "fields":[
    #     {
    #         "title":"Notes",
    #         "value":"This is much easier than I thought it would be.",
    #         "short":False
    #     }
    # ]
}))