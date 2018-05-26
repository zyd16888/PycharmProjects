import requests

#实例化session
session = requests.session()

#使用session发送post请求，获取对方保存在本地的cookie
post_url = "https://passport.baidu.com/v2/api/?login"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}
post_data = {"username":"475182659@qq.com","password":"zyd192114123"}
session.post(post_url,headers=headers,data=post_data)

print(post_data)
print(session.post)


# 使用session 请求登陆后的页面
url = "https://www.baidu.com/"
response = session.get(url,headers=headers)

with open("baidu2.html","w",encoding="utf-8") as  f:
    f.write(response.content.decode())