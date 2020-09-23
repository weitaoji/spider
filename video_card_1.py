import requests
from bs4 import BeautifulSoup
import os


def page_con():
    url = 'https://search.jd.com/Search?keyword=%E6%98%BE%E5%8D%A1&wq=%E6%98%BE%E5%8D%A1&page=1&s=1&click=0'
    r = requests.get(url)
    # print(r.text)
    b = BeautifulSoup(r.text,'lxml')
    # print(b)
    li = b.find_all('li',class_='gl-item')
    # print(li)
    for l in li:
        # print(l)
        # print('---------------------------------------------------------------------')
        a = l.find('a')
        # print(a)
        b = l.find('div',class_='p-price')
        # print(b)
        c = l.find('div',class_='p-name p-name-type-2')
        # print(c)
        href_0=l['data-sku']
        href='https://item.jd.com/'+href_0+'.html'
        # print(href)
        price=b.find('i').text
        # print(price)
        name=c.find('em').text
        #print(name)
        with open('Video_card.txt','a+') as f:
            f.write(name+' '+price+''+' '+href+'\n')
if os.path.exists('Video_card.txt'):
    os.remove('Video_card.txt')
page_con()
