# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

import scrapy

class WebCrawlingItem(scrapy.Item):
    titulo = scrapy.Field()
    resumo = scrapy.Field()
    link = scrapy.Field()