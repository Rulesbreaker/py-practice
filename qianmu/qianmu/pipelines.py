# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
import redis
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class RedisPipeline:
    def open_spider(self, spider):
        self.r = redis.Redis(host='127.0.0.1')

    # def close_spider(self, spider):
    #     self.r.close()

    def process_item(self, item, spider):
        if self.r.sadd(spider.name, item['name']):
            return item
        raise DropItem

class MysqlPipeline:
    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            db='qianmu_gp01',
            user='root',
            password='toor',
            charset='utf8'
        )

        self.cur = self.conn.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

    def process_item(self, item, spider):
        # keys = item.keys()
        # values = [item[k] for k in keys]
        keys, values = zip(*item.items())
        sql = "insert into universities ({}) values ({})".format(
            ','.join(keys),
            ','.join(['%s'] * len(values))
        )
        print(sql)
        self.cur.execute(sql, values)
        self.conn.commit()
        print(self.cur._last_executed)
        return item
