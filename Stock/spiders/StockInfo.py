# -*- coding: utf-8 -*-
import scrapy
import cssselect
import re
from Stock.items import StockItem

class StockinfoSpider(scrapy.Spider):
    name = 'StockInfo'
    start_urls = [
        'http://quote.eastmoney.com/stock_list.html'
    ]
    def parse(self, response):
        counter=0
        for each in response.css('li a').getall():
            try:
                match = re.search(r'[com]/.*?\(\d{6}\)<',str(each))
                url = 'https://xueqiu.com/S/' + match.group(0)[2:10]
                print('*'*42)
                print(match.group(0)[17:-1])
                print('*'*42)
                yield scrapy.Request(url, callback=self.parse_stock, meta={'name':match.group(0)[17:-1]})
                counter+=1
                if counter>5:
                    break
            except:
                continue
    def parse_stock(self, response):
        price = str(response.xpath('//div[contains(@class,"stock-current")]/strong/text()').get())
        stockItem = StockItem(stock_name=response.meta['name'],stock_price=price)
        return stockItem


