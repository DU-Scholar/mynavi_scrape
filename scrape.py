# coding=utf-8
import requests
from bs4 import BeautifulSoup
import re


def scrape():
    url = 'https://job.mynavi.jp/21/pc/search/query.html?HR:27/func=PCTopQuickSearch'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    data = []
    for i in range(100):
        element = soup.find_all('a', id='corpNameLink[' + str(i) + ']')
        print(element[0])
        print(element[0].attrs['href'])
        data.append(element[0].attrs['href'])
        # urlの情報を返す
    return data


def makeObj(urls):
    res = requests.get('https://job.mynavi.jp' + urls[0])
    soup = BeautifulSoup(res.content, 'html.parser')

    element = soup.find_all('h1')
    company = element[0].string  # 企業名

    elements = soup.find_all('span', class_="noLink")
    category = []  # 業種
    for element in elements:
        category.append(element.string)
    print(category)

    elements = soup.find_all('td', id="corpDescDtoListDescText50")
    data = elements[0].contents
    locations = []
    for i in range(len(data)):
        if (i+2) % 2 == 0:
            locations.append(data[i])
    location = "".join(locations)
    print(location)  # 住所


def pushFile(scrape):
    file_name = "./data/mynavi.txt"
    data = str(scrape())
    try:
        file = open(file_name, 'w')
        file.write(data)
    finally:
        file.close()


makeObj(['/21/pc/search/corp102356/outline.html'])


# pushFile(str(scrape()))