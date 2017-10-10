'''
Created on Oct 8, 2016

@author: peperk
'''
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import sys

print('START ....')
process = CrawlerProcess(get_project_settings())

process.crawl('epg_td')
process.crawl('epg_tm')
# the script will block here until the crawling is finished
process.start() 
print('FINISH ....')
sys.exit(0)