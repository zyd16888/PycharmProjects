import requests

url = "https://www.baidu.com/"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}

cookie = "BIDUPSID=194CF29894514C08CF58B290A6465367; PSTM=1577325758; BAIDUID=194CF29894514C080A4A15569F611466:FG=1; BD_UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; yjs_js_security_passport=07e013a41e8ecdd0b2ee8b2af2a37b526e15c63a_1578272630_js; delPer=0; BD_CK_SAM=1; PSINO=1; H_PS_645EC=f1ffYil9T2P%2BkrrWrLgzH2Cv4ewoPdMg045EZ%2FnhE8oaDSLx4ye8BGtwj70; BDUSS=URNMDZiMVZmbVhtN3FJaGRHSkMwN05mQVlVUDhKUEFyQjZHVVFWYlJ6YjVGVHBlRVFBQUFBJCQAAAAAAAAAAAEAAAAISMdEs77Pq8ur19MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPmIEl75iBJeT; BD_HOME=1; H_PS_PSSID=30583_1454_21106_30210_30328_30283_30481; sugstore=1"

cookie_dict = {i.split("=")[0]:i.split("=") for i in cookie.split("; ")}
print(cookie_dict)
response = requests.get(url,headers=headers,cookies=cookie)

with open("baidu1.html","w",encoding="utf-8") as  f:
    f.write(response.content.decode())