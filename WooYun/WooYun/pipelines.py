# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
 
from scrapy import log
from scrapy.conf import settings
from scrapy.exceptions import DropItem

import json


class JsonWriterPipeline(object):

    def __init__(self):
        self.file = open('items.jl', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
 
class MongoDBPipeline(object):
    def __init__(self):
        # self.server = settings['MONGODB_SERVER']
        # self.port = settings['MONGODB_PORT']
        # self.db = settings['MONGODB_DB']
        # self.col = settings['MONGODB_COLLECTION']
        self.server = "192.168.1.220"
        self.port = 27017
        self.db = "WooYun"
        self.col = "wy_vun"
        connection = pymongo.Connection(self.server, self.port)
        self.dbs = connection[self.db]
        
 
    def process_item(self, item, spider):
        err_msg = ''
        for field, data in item.items():
            if not data:
                err_msg += 'Missing %s of poem from %s\n' % (field, item['url'])
        if err_msg:
            raise DropItem(err_msg)
        info_dict = dict(item)
        self.collection = self.dbs[info_dict.pop("mes_type")]
        self.collection.insert(info_dict)
        log.msg('Item written to MongoDB database %s/%s' % (self.db, self.col),
                level=log.DEBUG, spider=spider)
        return item
