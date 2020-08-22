from urllib.request import Request, urlopen
import json
import csv
from datetime import datetime as dt
import traceback

YUKICODER_PROBLEM_URL = 'https://yukicoder.me/api/v1/problems/'

def get_problem_list():
    req = Request(YUKICODER_PROBLEM_URL)
    with urlopen(req) as res:
        body = json.load(res)
        return body

    
def csv_writer(problem_list):
    with open('./yukicoder.csv', 'a') as f:
        problem_list = sorted(problem_list, key=lambda x:x['No'])
        for value in problem_list:
            tmp_dick = {}
            for key, val in value.items():
                if key == 'Statistics':
                    continue
                try:
                    if key == 'Date':
                        val = dt.fromisoformat(val[:-15])
                        val = val.strftime('%Y-%m-%d')
                    tmp_dick[key] = val
                except:
                    traceback.print_exc()
                    print("ーーーーーーーーーーーーーーーーーーーーーーーーーーーー")
                    continue

            try:
                writer = csv.DictWriter(f, tmp_dick)
                #writer.writeheader()
                writer.writerow(tmp_dick)
            except:
                print("書き込み失敗")


result = get_problem_list()

csv_writer(result)

