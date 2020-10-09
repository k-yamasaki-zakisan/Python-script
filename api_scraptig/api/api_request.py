import requests

def get_api(url:str) -> dict:
    res = requests.get(url)
    return res.json()

def main():
    YUKICODER_PROBLEM_URL = 'https://yukicoder.me/api/v1/problems/'
    return get_api(YUKICODER_PROBLEM_URL)

if __name__ == "__main__":
    result = main()
    print(result)