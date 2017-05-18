# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

from scrapy.exceptions import DropItem


class QutoesPipeline(object):
    def __init__(self):
        self.file = open('data.json', 'w', encoding='UTF-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(line)
        return item

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass
