# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

class StockPipeline:
    def open_spider(self,spider):
        pass
    def process_item(self, item, spider):
        with open('output.text','a') as file:
            file.write(item['stock_name']+'\t'+item['stock_price']+'\n')
        return item
    def close_spider(self,spider):
        pass