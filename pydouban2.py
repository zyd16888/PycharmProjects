import requests as rt
import pymysql
import traceback
from bs4 import BeautifulSoup as bs
def getpage(staUrl, intNumber):
    pass

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    }
    params = {
        'offset': str(intNumber)
    }

    response = rt.get(staUrl, headers=header, params=params)
    print(response.url)
    return response.text
k=range(0,250,25)
conn = pymysql.connect(host = 'localhost', user = 'root', password = 'root', db ='douban')
cursor = conn.cursor()
for i in k:
    my_url="https://movie.douban.com/top250?start="+str(i)+"&filter="
    my_getdata=rt.get(my_url)
    x1=bs(getpage(my_url,i*10),"html.parser")
    x2=x1.find_all("li")
    # print(type(x2),x2)
    for i in x2:
        if i.find("em")!=None:
            try:
                em=i.find("em").text
                title=i.find("span",class_="title").text
                other=i.find("span", class_="other").text
                p=str(i.find("p", class_="").text)
                p=p[29:]
                star=i.find("div", class_="star")
                j=star.find_all("span")
                score=j[1].text
                num=j[3].text
                inq=str(i.find("span", class_="inq").text)
                try:
                    sql1='insert into douban value ("{}","{}","{}","{}","{}","{}","{}")'
                    sql=sql1.format(em,title,other,p,score,num,inq)
                    print(sql)
                    cursor.execute(sql)
                    result=111111
                    result = cursor.rowcount
                    conn.commit()
                    print(result)
                except:
                    print('database error')
            except:
                pass
            print()
conn.close()


