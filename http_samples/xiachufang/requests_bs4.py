import os
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests

s = requests.Session()
s.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
s.headers['Host'] = 'trackbeat.xiachufang.com'
r = s.get('http://www.xiachufang.com/')
soup = BeautifulSoup(r.text,features="lxml")

img_list = []
for img in soup.select('img'):
    if img.has_attr('data-src'):
        img_list.append(img.attrs['data-src'])
    else:
        img_list.append(img.attrs['src'])

# 初始化下载文件目录
image_dir = os.path.join(os.curdir, 'images')
if not os.path.isdir(image_dir):
    os.mkdir(image_dir)

for img in img_list:
    o = urlparse(img)
    filename = o.path[1:].split('@')[0]
    filepath = os.path.join(image_dir, o.path[1:])
    # 下载原图而不是小图
    url = '%s://%s%s' % (o.scheme, o.netloc, filename)
    print(url)
    resp = requests.get(url)
    with open(filepath, 'wb') as f:
        for chunk in resp.iter_content(1024):
            f.write(chunk)