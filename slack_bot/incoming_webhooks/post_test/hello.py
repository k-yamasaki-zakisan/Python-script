import requests
import json

# WEB_HOOK_URLは下準備で発行したURLを設定しください
WEB_HOOK_URL = "https://hooks.slack.com/services/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"

requests.post(WEB_HOOK_URL, data=json.dumps({
    "text" : "Hello World",
}))