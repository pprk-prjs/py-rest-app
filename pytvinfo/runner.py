'''
Created on Oct 8, 2016

@author: peperk
'''

# import http.client
# print(http.client)
 
#  
# import scrapy.cmdline
#  
# def main():
#     scrapy.cmdline.execute(argv=['scrapy', 'crawl', 'futbal'])
#  
# if  __name__ =='__main__':
#     main()

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

print('START ....')
process = CrawlerProcess(get_project_settings())

# process.crawl('p_analyzer', url_file="/home/projects/_projects/__DATA__/urls.txt") #'yourspidername' is the name of one of the spiders of the project.
process.crawl('tv_info')
process.start() # the script will block here until the crawling is finished
