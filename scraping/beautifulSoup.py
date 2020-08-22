from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json
import csv
from datetime import datetime as dt
import os

QIITA_URL = 'https://qiita.com/'

def get_trend_items():
    req = Request(QIITA_URL)
    with urlopen(req) as res:
        body = res.read()
        soup = BeautifulSoup(body, 'html.parser')
        target_div = soup.select('div[data-hyperapp-app="Trend"]')[0]
        trend_items = json.loads(target_div.get('data-hyperapp-props'))
    return trend_items

def csv_writer(trend_items):
    with open('./qiitaTopPage.csv', 'a') as f:
        HeadFlag = True
        for values in trend_items['trend']['edges']:
            for key, val in values.items():
                if key == 'node':
                    tmp_dick = {}
                    for c_key, c_val in val.items():
                        try:
                            if c_key == 'createdAt':
                                #一旦文字列を減らしてdata型で読み込めるようにする　2020-08-21T02:16:52Z  2020-08-21
                                c_val = dt.fromisoformat(c_val[:-10])
                                c_val = c_val.strftime('%Y-%m-%d')

                            if type(c_val) is not dict:
                                tmp_dick[c_key] = c_val
                            else:
                                for c2_key, c2_val in   c_val.items():
                                    tmp_dick[c2_key] = c2_val
                        except:
                           continue
                    try:
                        writer = csv.DictWriter(f, tmp_dick)
                        if os.stat("qiitaTopPage.csv").st_size == 0 and HeadFlag:
                            writer.writeheader()
                            HeadFlag = False
                        writer.writerow(tmp_dick)
                    except:
                        print("書き込み失敗")

result = get_trend_items()

csv_writer(result)


