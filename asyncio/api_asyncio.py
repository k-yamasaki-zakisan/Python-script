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

async def get_async(path:str) -> dict:
    print(f"/{path} async request")
    url = BASE_URL + path
    loop = asyncio.get_event_loop()
    res = await loop.run_in_executor(None, requests.get, url)
    print(f"/{path} async request done")
    return res.json()

@calc_time
def main_async():
    loop = asyncio.get_event_loop()
    tasks = asyncio.gather(
        get_async("problems"),
        get_async("languages"),
        get_async("ranking/golfer"),
        get_async("statistics/tags"),
        get_async("contest/future"),
    )
    
    # 非同期実行、それぞれが終わるまで
    results = loop.run_until_complete(tasks)
    return results

if __name__ == "__main__":
    results = main_async()

