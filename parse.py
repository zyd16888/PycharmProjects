import requests
from retrying import  retry

# headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36"}

headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36",
          "Referer": "https://m.douban.com/tv/chinese"}

@retry(stop_max_attempt_number=3) #被修饰函数执行三次，三次全部报错才报错，中间有一次正确就不报错
def _parse_url(url):
    print("*"*110)
    response = requests.get(url,headers=headers,timeout=5)
    return response.content.decode()

def parse_url(url):
    try:
        html_str = _parse_url(url)
    except:
        html_str = None
    return html_str

if __name__=='__main__':
    url = "http://www.baidu.com"
    url1 = "www.baidu.com"
    print(parse_url(url1))