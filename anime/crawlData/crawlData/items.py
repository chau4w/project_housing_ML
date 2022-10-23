# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlDataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    read = scrapy.Field()
    comment = scrapy.Field()
    heart = scrapy.Field()
    new_chap = scrapy.Field()
    time_new_chap = scrapy.Field()
    url = scrapy.Field()




