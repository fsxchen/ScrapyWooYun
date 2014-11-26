# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WooyunItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pb_time = scrapy.Field()
    pb_url = scrapy.Field()
    pb_name = scrapy.Field()
    pb_auth = scrapy.Field()
