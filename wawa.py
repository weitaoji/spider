import requests
import json
import os
import time
import random


def spider_comment(page=0):
    url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=30638939356&score=0&sortType=5&page=%s&pageSize=10&isShadowSku=0&fold=1'%page
    r = requests.get(url)
    # print('京东的评论：'+r.text)
    r_json_str = r.text[20:-2]
    # print(r_json_str)
    r_json_obj = json.loads(r_json_str)
    r_json_comments = r_json_obj['comments']
    # print(r_json_comments)
    for r_json_comment in r_json_comments:
        with open('jd.txt', 'a+') as f:
            f.write(r_json_comment['content'] + '\n')
        print(r_json_comment['content'])


def in_end():
    if os.path.exists('jd.txt'):
        os.remove('jd.txt')
    for i in range(100):
        spider_comment(i)
        time.sleep(random.random()*5)


if __name__ == '__main__':
    in_end()
