from urllib.request import Request, urlopen
import json
import csv

YUKICODER_PROBLEM_URL = 'https://yukicoder.me/api/v1/problems/'

def get_problem_list():
    req = Request(YUKICODER_PROBLEM_URL)
    with urlopen(req) as res:
        body = json.load(res)
        return body

    
def csv_writer(problem_list):
    with open('./yukicoder.csv', 'a') as f:
        tmp_dick = {}
        for value in problem_list:
            for key, val in value.items():
                try:
                    tmp_dick[key] = val
                except:
                    continue

            try:
                writer = csv.DictWriter(f, tmp_dick)
                writer.writeheader()
                writer.writerow(tmp_dick)
            except:
                print("書き込み失敗")





result = get_problem_list()

csv_writer(result)

