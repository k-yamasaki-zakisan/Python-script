import requests
import json
import os
from os.path import join, dirname
from dotenv import load_dotenv

input_city = input('天気を知りたい都市名を入力ください 例：東京, 大阪...\n')

# dotenvを用いた.envからのAPI keyの読み出し
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

WHEATHER_KEY = os.environ['WHEATHER_KEY']

city_trance = {
    '東京':'Tokyo',
    '大阪':'Osaka',
    '古賀':'Koga',
    '船橋':'Funabashi'
}

if input_city in city_trance:
    city = city_trance[input_city]
else:
    print('大都市を入力ください')
    exit()

url = f"http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&appid={WHEATHER_KEY}"

response = requests.get(url)

data = response.json()
#print(data)

# きれいに整形されてコンソールに出力される
jsontext = json.dumps(data,indent=4)
print(jsontext)


