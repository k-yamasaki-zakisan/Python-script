import time
import requests
import asyncio

BASE_URL = "https://yukicoder.me/api/v1/"

def calc_time(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        fn(*args, **kwargs)
        end = time.time()
        print(f"[{fn.__name__}] elapsed time: {end - start}")
        return
    return wrapper

def get_sync(path:str) -> dict:
    print(f"/{path} request")
    res = requests.get(BASE_URL + path)
    print(f"/{path} request done")
    return res.json()

@calc_time
def main_sync():
    data_ls = []
    paths = [
        'problems',
        'languages',
        'ranking/golfer',
        'statistics/tags',
        'contest/future',
    ]
    for path in paths:
        data_ls.append(get_sync(path))
    return data_ls

if __name__ == "__main__":
    result = main_sync()
