# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
from scrapy.exporters import XmlItemExporter
import json

class PytvinfoPipeline(object):

    def __init__(self):
        self.files = {}
#         print('ITEMS::::')

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
#         print('spider_opened!!')
        file = open('/home/peperk/Downloads/%s_products.json' % spider.name, 'w')
        file.write("[")        
        self.files[spider] = file
#         self.exporter = XmlItemExporter(file)
#         self.exporter.start_exporting()

    def spider_closed(self, spider):
#         self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.write("]")        
        file.close()

    def process_item(self, item, spider):
#         print('process_item::', item)
#         self.exporter.export_item(item)
        f = self.files[spider]
        line = json.dumps(dict(item)) + ",\n"
        f.write(line)        
        return item
