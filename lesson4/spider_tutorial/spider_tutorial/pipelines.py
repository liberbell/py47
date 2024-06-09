# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging


class SpiderTutorialPipeline:
    def open_spider(self, spider):
        logging.warning("Spider opened")

    def close_spider(self, spider):
        logging.warning("Spider closed")

    def process_item(self, item, spider):
        return item
