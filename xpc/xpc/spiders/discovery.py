import random
import string

import scrapy
import json
import re
from scrapy import Request


def strip(s):
    if s:
        return s.strip()
    return ''


# 对带逗号的数字字符串进行替换
def convert_int(s):
    if isinstance(s, str):
        return int(s.replace(',', ''))
    return 0


cookies = dict(
    Authorization='A37AB29030DC8844A'
)


def gen_sessionid():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=26))


class DiscoverySpider(scrapy.Spider):
    name = 'discovery'
    allowed_domains = ['xinpianchang.com', 'openapi-vtom.vmovier.com']
    start_urls = ['https://www.xinpianchang.com/channel/index/sort-like?from=navigator']
    page_count = 0

    def parse(self, response):
        # 用来查看response
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
        self.page_count += 1
        # 当爬取页面超过100的时候，由于网站会查session id来进行反爬虫，所以这里重新生成下session id
        if self.page_count >= 100:
            cookies.update(PHPSESSID=gen_sessionid())
            self.page_count = 0
        post_list = response.xpath('//ul[@class="video-list"]/li')
        url = "https://www.xinpianchang.com/a%s?from=ArticleList"
        for post in post_list:
            pid = post.xpath('./@data-articleid').get()
            # print(url % pid)
            # 将pid传到下个函数
            request = response.follow(url % pid, self.parse_post)
            request.meta['pid'] = pid
            # 取到懒加载的缩略图
            request.meta['thumbnail'] = post.xpath('./a/img/@_src').get()
            # yield request
        # 翻页爬取
        pages = response.xpath('//div[@class="page"]/a/@href').extract()
        for page in pages:
            yield response.follow(page, self.parse(), cookies=cookies)


    def parse_post(self, response):
        pid = response.meta['pid']
        post = dict(pid=pid)
        post['thumbnail'] = response.meta['thumbnail']
        post['title'] = response.xpath('//div[@class="title-wrap"]/h3/text()').get()

        vid, = re.findall('vid: \"(\w+)\"\,', response.text)
        video_url = 'https://openapi-vtom.vmovier.com/v3/video/%s?expand=resource,resource_origin?'
        cates = response.xpath('//span[contains(@class, "cate")]//text()').extract()
        post['category'] = ''.join([cate.strip() for cate in cates])
        post['created_at'] = response.xpath('//span[contains(@class, "update-time")]/i/text()').get()
        post['play_counts'] = response.xpath('//i[contains(@class, "play-counts")]/@data-curplaycounts').get()
        post['like_counts'] = response.xpath('//span[contains(@class, "like-counts")]/@data-counts').get()
        post['description'] = strip(response.xpath('//p[contains(@class, "desc")]/text()').get())
        post[''] = response.xpath('').get()
        request = Request(video_url % vid, callback=self.parse_video)
        yield request

        # comment_url = 'http://www.xinpianchang.com/article/filmplay/ts-getCommentApi?id=%s&ajax=1&page=1'
        comment_url = 'http://www.xinpianchang.com/article/filmplay/ts-getCommentApi?id=%s&page=1'
        request = Request(comment_url % pid, callback=self.parse_comment)
        request.meta['pid'] = pid
        yield request

    def parse_video(self, response):
        post = response.meta['post']
        result = json.loads(response.text)
        post['video'] = result['data']['resource']['default']['url']
        post['preview'] = result['data']['video']['cover']
        post['duration'] = result['data']['video']['duration']
        yield post

    def parse_comment(self, response):
        # elements = response.xpath('//li')
        # for li in elements:
        #     comment = {}
        #     comment['uname'] = li.xpath('.//span[contains(@class, "user-name")]/text()').get()
        #     comment['avator'] = li.xpath('.//img[@class="user-avator"]/@src').get()
        #     yield comment
        result = json.loads(response.text)

        for c in result['data']['list']:
            comment = {}
            comment['uname'] = c['userInfo']['username']
            comment['avator'] = c['userInfo']['face']
            comment['cid'] = c['userInfo']['userid']
            comment['commentid'] = c['commentid']
            comment['pid'] = c['articleid']
            comment['created_at'] = c['addtime_int']
            comment['like_counts'] = c['count_approve']
            comment['content'] = c['content']
            if c['reply']:
                comment['reply'] = c['reply']['commentid']
            yield comment

        next_page = result['date']['next_page_url']
        if next_page:
            yield response.follow(next_page, self.parse_comment)

    def parse_composer(self, response):
        banner = response.xpath('//div[@class="banner-wrap"]/@style').get()
        composer = {}
        composer['banner'], = re.findall('background-image:url\((.+?)\)', banner)
        composer['name'] = response.xpath('//p[contains(@class, "creator-name")]/text()').get()
        composer['intro'] = response.xpath('//p[contains(@class, "creator-desc")]/text()').get()
        composer['like_counts'] = convert_int(response.xpath('//span[contains(@class, "like-counts")]/text()').get())
        composer['fans_counts'] = convert_int(response.xpath('//span[contains(@class, "fans-counts")]/text()').get())
        composer['follow_counts'] = convert_int(response.xpath('//span[@class="follow-wrap"]/span[last()]/text()').get())
