import requests

url = "https://www.baidu.com/"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}

cookie = "BAIDUID=1D8425D7D6F9985C3820DAC431F3CF75:FG=1; BIDUPSID=1D8425D7D6F9985C3820DAC431F3CF75; PSTM=1526007029; BD_UPN=12314753; BDUSS=80RlQ3dGlObkd2WnpIWVlsRmcyVWd6Z29-TnB4MnQwam5nUWl6NTktdnN6aDFiQVFBQUFBJCQAAAAAAAAAAAEAAAAISMdEs77Pq8ur19MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOxB9lrsQfZadm; plus_cv=1::m:caddfa4f; plus_lsv=de8ce127d8872de4; BDORZ=AE84CDB3A529C0F8A2B9DCDD1D18B695; SE_LAUNCH=5%3A25452581; lsv=globalTjs_56c8eef-wwwTcss_e63f8cf-wwwBcss_31ec113-framejs_34681cc-globalBjs_a5d0910-sugjs_5132c2c-wwwjs_d34e944; MSA_WH=360_640; MSA_PBT=146; MSA_ZOOM=1000; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1527154901; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1527154901; wpr=0; pgv_pvi=680395776; BDRCVFR[CSdx1UAgyk0]=mk3SLVN4HKm; BD_CK_SAM=1; PSINO=1; pgv_si=s5168408576; BD_HOME=1; H_PS_PSSID=1437_21080_20930; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_645EC=8d4etPQMNJRJtQ7gesDUAqBx0GJdzYfdLvUmWgL2QmjTsVjOdNSJw6a4uCI"

cookie_dict = {i.split("=")[0]:i.split("=") for i in cookie.split("; ")}

print(cookie_dict)

response = requests.get(url,headers=headers,cookies=cookie_dict)

with open("baidu1.html","w",encoding="utf-8") as  f:
    f.write(response.content.decode())