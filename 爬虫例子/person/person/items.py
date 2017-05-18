# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PersonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    sex = scrapy.Field()
    addr = scrapy.Field()
    birthday = scrapy.Field()
