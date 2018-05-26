import requests

# url = "http://fanyi.baidu.com/extendtrans"
url = "http://fanyi.baidu.com/basetrans"

query_string = {"query": "人生苦短，及时行乐",
                "from":"zh",
                "to": "en"}
headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36"}

response = requests.post(url,data=query_string,headers=headers)

print(response)

print(response.content.decode())

print(response.request.url)

print(response.url)  #response响应的url地址

print(response.request.headers ) #请求头

print(response.headers)  #响应请求

