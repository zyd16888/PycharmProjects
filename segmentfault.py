from lxml import etree
import requests
import pymongo

url = "https://segmentfault.com/hottest"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
}

response = requests.get(url, headers=headers, timeout=3)
html_str = response.content.decode()

# print(html_str)
# 文本修正
html = etree.HTML(html_str)
# print(html)
#
# url_list = html.xpath("//div[@class='news-list']/div/div/a[@target='_blank']/@href")
# print(url_list)
# title_name = html.xpath("//div[@class='news-list']/div/div/a/div[@class='mb5 mt5']//text()")
# print(title_name)
# article = html.xpath("//div[@class='news-list']/div/div/a/div[@class='article-excerpt']/text()")
# print(article)
# votes_num = html.xpath("//div[@class='news-list']/div/div//span/span[2]/text()")
# print(votes_num)
# author = html.xpath("//div[@class='news-list']/div/div//span[@class='author pr20']/a/text()")
# print(author)
# time = html.xpath("//div[@class='news-list']/div/div//span[@class='author pr20']/text()")
# print(time)

# print("---------------------------------------------------------------")
ret = html.xpath("//div[@class='news-list']/div/div")

# client = pymongo.MongoClient(host = 'localhost', port = 27017)
# db = client.pythonlearn
# collection = db.segmentfault10
for table in ret:
    item = {}
    item['title'] = table.xpath("./a/div[@class='mb5 mt5']//text()")[0]
    item['href'] = table.xpath("./a[@target='_blank']/@href")[0].replace("/a", "https://segmentfault.com/a").strip()
    item['article'] = table.xpath("./a/div[@class='article-excerpt']/text()")[0].replace("\n", "").strip()
    item['votes'] = table.xpath(".//span/span[2]/text()")[0]
    # if (item['votes']) :
    #     item['votes']
    # else:
    #     item['votes'] = "0"
    item['author'] = table.xpath(".//span[@class='author pr20']/a/text()")[0]
    item['time'] = table.xpath(".//span[@class='author pr20']/text()")[0]
    # print(item)
    stress = str(item)
    with open("segmentfault热门.json", "a", encoding="utf-8") as f:
            f.write(stress)
            f.write("\n")
    print("保存成功")
    # r23 = collection.insert_one(item)
    # print(r23)