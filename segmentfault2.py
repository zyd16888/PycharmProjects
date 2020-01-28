import json
import requests

url = "https://segmentfault.com/api/timelines/hottest/month?page=1&_=45a771e5aea54c6d4df014a413a36b6c"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
    "cookie": "_ga=GA1.2.1547598423.1577975349; Hm_lvt_e23800c454aa573c0ccb16b52665ac26=1578291712; _gid=GA1.2.1322846332.1578444187; PHPSESSID=web1~mtdbg2te8t7o159btes5hv3qf5",
    "referer": "https://segmentfault.com/hottest/monthly"
    # "sec-fetch-mode": "cors",
    # "sec-fetch-site": "same-origin"
    # "x-requested-with": "XMLHttpRequest"
}

response = requests.get(url, headers = headers)
print(response.content.decode())

json_str = response.content.decode()

ret1 = json.loads(json_str)
print(json.dumps(ret1, ensure_ascii=False, indent=2))

# with open("sf.txt", "w", encoding="utf-8") as f:
#     f.write(json.dumps(ret1, ensure_ascii=False, indent=2))