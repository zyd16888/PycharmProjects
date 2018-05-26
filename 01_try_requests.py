import requests

url = "http://www.baidu.com"
response = requests.get(url)
# print(response)

# response.encoding = "utf-8"

# print(response.text)

print(response.content.decode())