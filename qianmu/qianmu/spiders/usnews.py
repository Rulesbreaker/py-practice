import scrapy

from qianmu.items import UniversityItem


class UsnewsSpider(scrapy.Spider):
    name = 'usnews'
    # 允许爬url的域名必须要在此字段内
    # genspider的时候指定
    allowed_domains = ['www.qianmu.org']
    # 爬虫的入口地址，可以写多个
    start_urls = ['http://www.qianmu.org/ranking/1528.htm']

    def parse_university(self, response):
        response = response.replace(body=response.text.replace('\t', '').replace('\r\n', ''))
        item = UniversityItem()
        data = {}
        item['name'] = response.xpath('//div[@id="wikiContent"]/h1/text()')[0]
        print(item['name'])
        table = response.xpath(
            '//div[@id="wikiContent"]/div[@class="infobox"]/table')
        if table:
            table = table[0]
            keys = table.xpath('.//td[1]/p/text()').extract()
            cols = table.xpath('.//td[2]')
            # 当我们确定解析出来的数据只有一个时，可以使用extract_first函数直接提取列表内的内容
            values = [' '.join(col.xpath('.//text()').extract_first()) for col in cols]
            # values = []
            # print(data['name'])
            # for col in cols:
            #     values.append(' '.join(col.xpath('.//text()')))
            if len(keys) == len(values):
                data.update(zip(keys, values))
        # yield出去的数据，会被框架接受，进行下一步的处理
        # 如果没有任何处理，会打印到控制台里
        item['rank'] = data.get('排名')
        item['country'] = data.get('国家')
        item['state'] = data.get('周省')
        item['city'] = data.get('城市')
        item['undergraduate_num'] = data.get('本科生人数')
        item['postgraduate_num'] = data.get('研究生人数')
        item['website'] = data.get('网址')
        yield item

    # 当框架请求start_urls内的链接成功以后，就会调用该方法
    def parse(self, response):
        # 解析链接，并提取，extract函数返回的永远是列表，即使只有一个数据
        links = response.xpath('//div[@class="rankItem"][2]//tr[position()>1]/td[2]/a/@href').extract()
        for link in links:
            if not link.startswith('http://www.qianmu.org'):
                link = 'http://www.qianmu.org/%s' % link
            # 让框架继续跟随这个链接，也就是说会再次发起请求
            # 请求成功以后，会异步调用指定的callback函数parse_university
            yield response.follow(link, self.parse_university)
