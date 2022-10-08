#PID: 5 Description: thread_test

import json
import os
from turtle import title
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from lazy_crawler.crawler.spiders.base_crawler import LazyBaseCrawler
from lazy_crawler.lib.user_agent import get_user_agent
from lazy_crawler.lib.html import to_browser
import ipdb

class LazyCrawler(LazyBaseCrawler):
    #main url="https://annapurnapost.com/tags/corona-virus"
    name = "exam"
    
    pageNumber = 1

    def start_requests(self):
        

        settings = get_project_settings()
        
        # corona virus news
        url = 'https://bg.annapurnapost.com/api/tags/news?page=1&per_page=20&tag=corona-virus'
        
        yield scrapy.Request(url, self.parse)

    def parse(self, response):

        #load the response 
        datas =json.loads(response.text)

        #get news id from this page
    
        for data in datas['data']:
            __id = data['id']
            url = 'https://bg.annapurnapost.com/api/news/'+str(__id)
            yield scrapy.Request(url, self.parse_details, dont_filter=True)

    def parse_details(self, response):
        
        # ipdb.set_trace()
        details = response.json()
        title = details["news"]["title"]
        content = details["news"]["content"] 
        publishedOn  = details["news"]["publishedOn"]
        metaDescriptions = details["news"]["metaDescriptions"]

        yield{
            "title": title,
            "content": content,
            "publishedOn": publishedOn,
            "metaDescriptions": metaDescriptions
        }

        if self.pageNumber <= 7:
            self.pageNumber = self.pageNumber + 1
            next_url = "https://bg.annapurnapost.com/api/tags/news?page="+str(self.pageNumber)+"&per_page=20&tag=corona-virus"
            # yield response.follow(next_url, self.parse, dont_filter=True)
            yield scrapy.Request(next_url, self.parse, dont_filter=True)
        else:
            print("All data downloaded!!")
        
settings_file_path = 'lazy_crawler.crawler.settings'
os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_file_path)
process = CrawlerProcess(get_project_settings())  
process.crawl(LazyCrawler)
process.start() # the script will block here until the crawling is finished
