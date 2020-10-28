import requests
import json

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../../.env')
load_dotenv(dotenv_path)

# WEB_HOOK_URLは下準備で発行したURLを設定しください
WEB_HOOK_URL = os.environ['WEB_HOOK_URL']

requests.post(WEB_HOOK_URL, data=json.dumps({
    "text" : "Hello World",
}))