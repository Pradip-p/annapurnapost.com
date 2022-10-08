# from scrapy import signals
# from scrapy.exporters import CsvItemExporter, XmlItemExporter

# class AmazonPipeline(object):
#     @classmethod
#     def from_crawler(cls, crawler):
#         pipeline = cls()
#         crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
#         crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
#         return pipeline

            
#     def spider_opened(self, spider):
#         # self.file = open('output.xlsx', 'w+b')
#         self.file = open('output.json','w+b')
#         self.exporter = CsvItemExporter(self.file)
#         self.exporter.start_exporting()

#     def spider_closed(self, spider):    
#         self.exporter.finish_exporting()
#         self.file.close()

#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return


import json

from itemadapter import ItemAdapter

class JsonWriterPipeline:

    def open_spider(self, spider):
        self.file = open('items.jl', 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict(), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item