import requests
from sys import argv
from json import dumps

WOLFARM_ALPHA_APP_ID = "3JH6TUJUW6"
BaseURL = "http://api.wolframalpha.com/v2/query"
params = {
    "appid": WOLFARM_ALPHA_APP_ID,
    "input": argv[1],
    "format": "plaintext",
    "output": "JSON"
}

res = requests.get(BaseURL, params=params)
if res.status_code == 200:
    data = res.json()
    print(res.text)
    # if data["queryresult"]["success"]:
    #     print(dumps(data["queryresult"]["pods"][1:], ensure_ascii=False))
else:
    print(f"Error: {res.status_code}")