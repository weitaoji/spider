import requests
from bs4 import BeautifulSoup
import os
import time

save_dir = '一拳超人'
if save_dir not in os.listdir('./'):
    os.mkdir(save_dir)
url = 'https://manhua.fzdm.com/132'
re = requests.get(url)
soup = BeautifulSoup(re.text,'lxml')
lis = soup.find_all('li',class_="pure-u-1-2 pure-u-lg-1-4")
# print(lis)
j = []
chapter_names=[]
chapter_urls=[]
for i in lis:
    j=i.find('a')
    # print(j)
    name = j.get('title')
    urls = j.get('href')
    url0 = "https://www.fzdm.com/manhua/132" + '/' +urls
    
    chapter_names.insert(0,name)
    chapter_urls.insert(0,url0)
print(chapter_names)
print(chapter_urls)
for chapter_name in chapter_names:
    if save_dir not in os.listdir('./一拳超人/'):
        os.mkdir('./一拳超人/'+chapter_name)


def parse(chapter_url):
    r = requests.get(chapter_url)
    html = r.text
    b = BeautifulSoup(html,'lxml')
    img_0=b.find('div',id='mhimg0')
    img_1=img_0.find('img')







