import  json
import  requests

url = "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_domestic_hot/items?os=android&for_mobile=1&start=0&count=18&loc_id=108288&_=1527328317067"

header = {"User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36",
          "Referer": "https://m.douban.com/tv/chinese"}

response = requests.get(url,headers=header)

#获取字符串
json_str = response.content.decode() #json字符串
print(json_str)

ret1 = json.loads(json_str)


with open("shuju01.txt","w",encoding="utf-8")as f:
    f.write(json.dumps(ret1, ensure_ascii=False,indent=2))