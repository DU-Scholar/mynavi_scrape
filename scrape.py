# coding=utf-8
import requests
from bs4 import BeautifulSoup


def hello_world():
    url = 'https://jp.indeed.com/jobs?q=&l=大阪府+堺市&jt=new_grad&start=0'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup

file_name = "./data/mynavi.txt"

data = str(hello_world())
try:
    file = open(file_name, 'w')
    file.write(data)
finally:
    file.close()

hello_world()