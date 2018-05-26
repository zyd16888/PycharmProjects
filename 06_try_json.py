import requests
import json

# url = "http://fanyi.baidu.com/extendtrans"
url = "http://fanyi.baidu.com/basetrans"

query_str = input("请输入要翻译的中文：")

data  = {"query":query_str,
                "from":"zh",
                "to": "en"}

headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36"}

response = requests.post(url,data=data,headers=headers)

#获取字符串
html_str = response.content.decode() #json字符串

#转码
dict_ret = json.loads(html_str)

print(dict_ret)
print(type(dict_ret))
print(html_str)
print(response)
ret = dict_ret["trans"][0]["dst"]

print("翻译结果是："+ret)