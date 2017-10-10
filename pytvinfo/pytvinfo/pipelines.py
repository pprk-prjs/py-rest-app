# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
from scrapy.exporters import  JsonItemExporter
from pytvinfo.p_libs.p_utils import get_data_dir
from scrapy.utils.python import to_bytes


class MyJsonItemExporter(JsonItemExporter):

    def start_exporting(self):
        self.file.write(b"{")
        self._beautify_newline()

    def finish_exporting(self):
        self._beautify_newline()
        self.file.write(b"}")

    def export_item(self, item):
        if self.first_item:
            self.first_item = False
        else:
            self.file.write(b',')
            self._beautify_newline()
        itemdict = dict(self._get_serialized_fields(item))
        data = self.encoder.encode(itemdict)
        data = data[1:len(data)-1]
        self.file.write(to_bytes(data, self.encoding))


class PytvinfoPipeline(object):

    def __init__(self):
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        data_dir = get_data_dir()
        file = open(data_dir + '/%s.json' % spider.name, 'wb')
        self.files[spider] = file
        self.exporter = MyJsonItemExporter(file, encoding='utf-8')
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(dict(item))
        return item
    

