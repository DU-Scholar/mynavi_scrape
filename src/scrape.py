# coding=utf-8
import requests
from bs4 import BeautifulSoup
import re

import Export


def scrape():
    url = 'https://job.mynavi.jp/21/pc/search/query.html?HR:27/func=PCTopQuickSearch'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    data = []
    for i in range(100):
        element = soup.find_all('a', id='corpNameLink[' + str(i) + ']')
        data.append(element[0].attrs['href'])
        # urlの情報を返す
    return data


def makeData(urls):
    id = 0
    for url in urls:
        print(url)
        id += 1
        data = []
        data.append(id)
        res = requests.get('https://job.mynavi.jp' + url)
        soup = BeautifulSoup(res.content, 'html.parser')

        element = soup.find_all('h1')
        print(element)
        name = element[0].string  # 企業名
        if name is None:
            name = element[0].contents[0]
        data.append(name)

        elements = soup.find_all('span', class_="noLink")
        category = []  # 業種
        for element in elements:
            category.append(element.string)
        data.append(category)

        elements = soup.find_all('th', id=re.compile("outlineInfoListDescTitle"))
        for element in elements:
            if element.string == "代表者":
                CEOTag = element.attrs['id']
                tag = "outlineInfoListDescText" + re.sub("\\D", "", CEOTag)
                CEO = Export.getCorpDescription(soup, tag)  # 代表者
            else:
                CEO = ""
        data.append(CEO)
        location = Export.getCorpDescription(soup, "corpDescDtoListDescText50")  # 住所
        data.append(location)

        url = Export.getUrl(soup, "corpDescDtoListDescText120")  # url
        data.append(url)

        phoneNum = Export.getCorpDescription(soup, "corpDescDtoListDescText220")  # 電話番号
        data.append(phoneNum)

        # データに格納
        print(data)
        Export.writeCsv(data)

#
# def pushFile(scrape):
#     file_name = "../data/url.txt"
#     data = str(scrape)
#     try:
#         file = open(file_name, 'w')
#         file.write(data)
#     finally:
#         file.close()


urls = scrape()
makeData(urls)

# pushFile(str(scrape()))
