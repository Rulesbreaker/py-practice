import sys
import time
import signal
import requests
import threading
from queue import Queue
from lxml import etree
import redis

start_url = 'http://www.qianmu.org/ranking/1528.htm'
link_queue =  Queue()
threads_num = 10
threads = []
download_pages = 0
r = redis.Redis(host='127.0.0.1')
thread_on = True


# 请求并下载网页
def fetch(url):
    try:
        r = requests.get(url, timeout=10)
        if r.status_code != 200:
            r.raise_for_status()
        global download_pages
        download_pages += 1
        return r.text.replace('\t', '')
    except Exception:
        print('error raised when fetch %s' % url)


# 处理大学详情页面
def parse_university(url):
    selector = etree.HTML(fetch(url))
    data = {}
    data['name'] = selector.xpath('//div[@id="wikiContent"]/h1/text()')[0]
    print(data['name'])
    table = selector.xpath(
        '//div[@id="wikiContent"]/div[@class="infobox"]/table')
    if table:
        table = table[0]
        keys = table.xpath('.//td[1]/p/text()')
        cols = table.xpath('.//td[2]')
        values = [' '.join(col.xpath('.//text()')) for col in cols]
        # values = []
        # print(data['name'])
        # for col in cols:
        #     values.append(' '.join(col.xpath('.//text()')))
        if len(keys) != len(values):
            return None
        
        data.update(zip(keys, values))
        # for i in range(len(keys)):
        #     data[keys[i]] = values[i]
        return data


# 处理数据
def process_data(data):
    if data:
        print(data)


def download(i):
    while thread_on:
        # 阻塞直到从队列里获取一条消息
        link = r.lpop('qianmu.queue')
        if link:
            data = parse_university(link)
            process_data(data)
            print('remaining queue: %s' % r.llen('qianmu.queue'))
        time.sleep(0.2)
    print('Thread-%s exit now' % i)


def sigint_handler(signum, frame):
    print('received Ctrl+C, wait for exit gracefully')
    global thread_on
    thread_on = False


# resp = requests.get('http://www.qianmu.org/ranking/1528.htm')
if __name__ == '__main__':
    start_time = time.time()
    # 只有当请求参数有两个，第二个为url的时候才去处理页面，否则就只是负责创建线程
    if len(sys.argv) > 1:
        start_url = sys.argv[1]
        # 1. 请求入口页面
        selector = etree.HTML(fetch(start_url))
        # 2. 提取列表页面的链接
        links = selector.xpath('//div[@class="rankItem"][2]//tr[position()>1]/td[2]/a/@href')
        for link in links:
            if not link.startswith('http://www.qianmu.org'):
                link = 'http://www.qianmu.org/%s' % link
            if r.sadd('qianmu.seen', link):
                r.rpush('qianmu.queue', link)
    else:
        # 启动线程，并将线程对象放入一个列表保存
        for i in range(threads_num):
            t = threading.Thread(target=download, args=(i+1,))
            t.start()
            threads.append(t)

        signal.signal(signal.SIGINT, sigint_handler)
        # 阻塞队列，直到队列被清空
        link_queue.join()
        # 向队列发送N个None，以通知线程退出
        for i in range(threads_num):
            link_queue.put(None)
        # 退出线程
        for t in threads:
            t.join()
    
    cost_seconds = time.time() - start_time
    print('Downloaded %s pages , cost %.2f seconds' % (download_pages, cost_seconds))
