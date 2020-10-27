import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# 先ほど取得したbotアカウントのトークンを指定する
API_TOKEN = os.environ['SLACK_TOKEN']

# このbotのデフォルトの返答を書く
DEFAULT_REPLY = "おはようございます"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']