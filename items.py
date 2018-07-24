# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
'''
This class creates the neccessary fields for an article of the news sites
to crawl. To categorize properly, the article title, publishing date,
text are considered.
'''


class Article(scrapy.Item):
    title = scrapy.Field()
    date = scrapy.Field()
    text = scrapy.Field()
    tags = scrapy.Field()
