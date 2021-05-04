import requests
from lxml import etree

start_url = 'http://www.qianmu.org/ranking/1528.htm'

#请求并下载网页
def fetch(url):
    r = requests.get(url)
    if r.status_code != 200:
        r.raise_for_status()
    return r.text.replace('\t', '')

#处理大学详情页面
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

#处理数据
def process_data(data):
    if data:
        print(data)

# resp = requests.get('http://www.qianmu.org/ranking/1528.htm')
if __name__ == '__main__':
    # 1. 请求入口页面
    selector = etree.HTML(fetch(start_url))
    # 2. 提取列表页面的链接
    links = selector.xpath('//div[@class="rankItem"][2]//tr[position()>1]/td[2]/a/@href')
    for link in links:
        if not link.startswith('http://www.qianmu.org'):
            link = 'http://www.qianmu.org/%s' % link
        # 3. 提起详情页的信息
        data = parse_university(link)
        # 4. 处理信息
        process_data(data)
