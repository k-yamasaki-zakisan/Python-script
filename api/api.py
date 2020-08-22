from urllib.request import Request, urlopen
import json
import csv
from datetime import datetime as dt
import traceback
import os

def get_api(url:str) -> dict:
    req = Request(url)
    with urlopen(req) as res:
        body = json.load(res)
        return body

    
def csv_proble_writer(problem_list:object):
    with open('./yukicoderProblem.csv', 'a') as f:
        problem_list = sorted(problem_list, key=lambda x:x['No'])
        headFlag = True
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
                    #traceback.print_exc()
                    #print("ーーーーーーーーーーーーーーーーーーーーーーーーーーーー")
                    pass

            try:
                writer = csv.DictWriter(f, tmp_dick)
                if os.stat("./yukicoderProblem.csv").st_size == 0 and headFlag:
                    writer.writeheader()
                    headFlag = False
                writer.writerow(tmp_dick)
            except:
                print("書き込み失敗")
    print("問題書き込み終了！！")


def csv_pass_contest_writer(pass_contest_list:object):
    with open('./yukicoderPassContest.csv', 'a') as f:
        pass_contest_list = sorted(pass_contest_list, key=lambda x:x['Id'])
        headFlag = True
        for value in pass_contest_list:
            tmp_dick = {}
            for key, val in value.items():
                try:
                    if key == 'Date' or key == 'EndDate':
                        val = dt.fromisoformat(val[:-15])
                        val = val.strftime('%Y-%m-%d')
                    tmp_dick[key] = val
                except:
                    #traceback.print_exc()
                    #print("ーーーーーーーーーーーーーーーーーーーーーーーーーーーー")
                    pass

            try:
                writer = csv.DictWriter(f, tmp_dick)
                if os.stat("./yukicoderPassContest.csv").st_size == 0 and headFlag:
                    writer.writeheader()
                    headFlag = False
                writer.writerow(tmp_dick)
            except:
                print("書き込み失敗")
    print("コンテスト書き込み終了！！")



YUKICODER_PROBLEM_URL = 'https://yukicoder.me/api/v1/problems/'
YUKICODER_PASS_CONTEST_URL = 'https://yukicoder.me/api/v1/contest/past'

result_problems = get_api(YUKICODER_PROBLEM_URL)
result_pass_contests = get_api(YUKICODER_PASS_CONTEST_URL)

csv_proble_writer(result_problems),
csv_pass_contest_writer(result_pass_contests),




# #API叩き方参考
##GET(クエリパラメータ)##
# url = 'https://example.com/api/v1/resource'
# params = {
#     'foo': 123,
# }

# req = urllib.request.Request('{}?{}'.format(url, urllib.parse.urlencode(params)))
# with urllib.request.urlopen(req) as res:
#     body = res.read()


###POST#
# url = "http://xxxx/xxxx" 
# method = "POST"
# headers = {"Content-Type" : "application/json"}

# # PythonオブジェクトをJSONに変換する
# obj = {"xxx" : "xxxx", 123 : 123} 
# json_data = json.dumps(obj).encode("utf-8")
# # httpリクエストを準備してPOST

# request = urllib.request.Request(url, data=json_data, method=method, headers=headers)
# with urllib.request.urlopen(request) as response:
#     response_body = response.read().decode("utf-8")

##メソッド種類##
# method='PUT'
# method='PATCH'
# method='DELETE'

##例外処理##
# url = 'https://example.com/api/v1/resource'

# req = urllib.request.Request(url)
# try:
#     with urllib.request.urlopen(req) as res:
#         body = res.read()
# except urllib.error.HTTPError as err:
#     print(err.code)
# except urllib.error.URLError as err:
#     print(err.reason)