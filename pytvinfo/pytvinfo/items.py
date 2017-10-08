# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PytvinfoItem(scrapy.Item):

    tv_id = scrapy.Field()
    nazov = scrapy.Field()
    cas = scrapy.Field()
    end = scrapy.Field()
    popis = scrapy.Field()
    relacia = scrapy.Field()
    tv_name = scrapy.Field()
    
    def set_nazov(self, nazov):
        nn = ""
        for n in nazov:
            if len(n) > 0:
                n = n[0]
                nn += n + " "
        self['nazov'] = nn
        
    def get_skrateny_popis(self):
        return "{0} \t {1}\n{2}".format(self['nazov'], self['cas'], self['relacia'])

    def get_cely_popis(self):
        return "{0} \t {1}\n{2}\n{3}".format(self['nazov'], self['cas'], self['relacia'], self['popis'])
    
    def __str__(self):
        return "Nazov:: {0}\nCas:: {1}\nEnd:: {4}\nPopis:: {2}\nRelacia:: {3}".format(self['nazov'], self['cas'], self['popis'], self['relacia'], self['end']) 


