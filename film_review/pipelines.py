# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy import Item
import redis

class FilmReviewPipeline(object):
    # def process_item(self, item, spider):
    #     item_string = str(item)
    #     with open(r'影评.txt', 'a', encoding='utf-8') as f:
    #         f.write(item_string)
    #         f.write('\n')
    #     return item
    # 连接数据库
    def open_spider(self, spider):
        db_host = spider.settings.get('REDIS_HOST', 'localhost')
        db_port = spider.settings.get('REDIS_PORT', 6379)
        db_index = spider.settings.get('REDIS_DB_INDEX', 2)
        self.db_conn = redis.StrictRedis(host=db_host, port=db_port, db=db_index)
        self.item_i = 0

    # 关闭数据库
    def close_spider(self, spider):
        self.db_conn.connection_pool.disconnect()


    # 插入数据
    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    def insert_db(self, item):
        if isinstance(item, Item):
            item = dict(item)

        self.item_i += 1
        self.db_conn.hmset('comments:{}'.format(self.item_i), item)
