import requests
from retrying import  retry
import json
import pymongo

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
    "cookie": "_ga=GA1.2.1547598423.1577975349; Hm_lvt_e23800c454aa573c0ccb16b52665ac26=1578291712; _gid=GA1.2.1322846332.1578444187; PHPSESSID=web1~mtdbg2te8t7o159btes5hv3qf5",
    "referer": "https://segmentfault.com/hottest/monthly"
}

@retry(stop_max_attempt_number=3)
def _parse_url(url):
    # print("*"*110)
    response = requests.get(url, headers=headers, timeout=5)
    return response.content.decode()

def parse_url(url):
    try:
        html_str = _parse_url(url)
    except:
        html_str = None
    return html_str


class SegmentFault:

    def __init__(self):
        self.temp_url = "https://segmentfault.com/api/timelines/hottest/month?page={}&_=45a771e5aea54c6d4df014a413a36b6c"

    def get_content_list(self, html_str):
        dict_data = json.loads(html_str)
        content_list = dict_data["data"]
        return content_list

    def save_content_list(self,content_list):
        with open("sf2.json", "a", encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")
        print("保存成功")

    def save_mongodb(self,content_list):
        client = pymongo.MongoClient(host='localhost', port=27017)
        db = client.pythonlearn
        collection = db.MonthHottest3
        for content in content_list:
            collection.insert_one(content)
        print("保存成功")

    def run(self):
        num = 1
        total = 6
        while num < total:
            # 1.url
            url = self.temp_url.format(num)
            print(url)
            # 2.发送请求
            html_str = parse_url(url)
            # 3.提取数据
            content_list = self.get_content_list(html_str)
            # 4.保存
            self.save_content_list(content_list)
            # 5.下一页url地址
            num += 1


if __name__ == '__main__':
    sf = SegmentFault()
    sf.run()