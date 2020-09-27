import requests,re,os
from hashlib import md5
from multiprocessing.pool import Pool
from selenium import webdriver
from functools import partial
import time

class Getcookie(object):
    def __init__(self,url):
        self.cookies = self.get_cookies(url)
        self.headers = {
            'cookie': self.cookies,
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
        }
    def get_cookies(self,url):
        str=''
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        browser = webdriver.Chrome(options=options)
        browser.get(url)
        for i in browser.get_cookies():
            try:
                name=i.get('name')
                value=i.get('value')
                str=str+name+'='+value+';'
            except ValueError as e:
                print(e)
        return str

    def get_page(self,offset):
        params = {
            'aid': '24',
            'app_name': 'web_search',
            'offset': offset,
            'format': 'json',
            'keyword': '街拍',
            'autoload': 'true',
            'count': '20',
            'en_qc': '1',
            'cur_tab': '1',
            'from': 'search_tab',
            'pd': 'synthesis',
        }
        url='https://www.toutiao.com/api/search/content/'
        try:
            r=requests.get(url,params=params,headers=self.headers)
            if r.status_code==200:
                return r.json()
            else:
                print('requests get_page error!')
        except requests.ConnectionError:
            return None

    def get_images(self,json):
        data=json.get('data')
        if data:
            for i in data:
                if i.get('title'):
                    title=re.sub('[\t]','',i.get('title'))
                    url=i.get('article_url')
                    if url:
                        r=requests.get(url,headers=self.headers)
                        if r.status_code==200:
                            images_pattern = re.compile('JSON.parse\("(.*?)"\),\n', re.S)
                            result = re.search(images_pattern, r.text)
                            if result:
                                b_url='http://p3.pstatp.com/origin/pgc-image/'
                                up=re.compile('url(.*?)"width',re.S)
                                results=re.findall(up,result.group(1))
                                if results:
                                    for result in results:
                                        yield {
                                            'title':title,
                                            'image':b_url+re.search('F([^F]*)\\\\",',result).group(1)
                                        }
                            else:
                                images = i.get('image_list')
                                for image in images:
                                    origin_image = re.sub("list.*?pgc-image", "large/pgc-image",
                                                          image.get('url'))  # 改成origin/pgc-image是原图
                                    yield {
                                        'image': origin_image,
                                        'title': title
                                    }

def save_image(item):
    img_path = 'img' + os.path.sep + ''.join(re.findall(r'[\u4e00-\u9fa5a-zA-Z0-9]+',item.get('title'),re.S)) #去除不能作为文件名的字符
    if not os.path.exists(img_path):
        os.makedirs(img_path) # 生成目录文件夹
    try:
        resp = requests.get(item.get('image'))
        if requests.codes.ok == resp.status_code:
            file_path = img_path + os.path.sep + '{file_name}.{file_suffix}'.format(
                file_name=md5(resp.content).hexdigest(),
                file_suffix='jpg')  # 单一文件的路径
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(resp.content)
                print('Downloaded image path is %s' % file_path)
            else:
                print('Already Downloaded', file_path)
    except Exception as e:
        print(e,'none123')

def main(offset,getcookie):
    a = getcookie.get_page(offset)
    for i in getcookie.get_images(a):
        save_image(i)


if __name__=='__main__':
    start=time.perf_counter()
    getcookie=Getcookie('https://www.toutiao.com')
    p_work=partial(main,getcookie=getcookie)
    p=Pool()
    groups=[x * 20 for x in range(0, 3)]
    p.map(p_work,groups)
    end=time.perf_counter()
    print('程序运行时间: '+str(end-start)+'秒')