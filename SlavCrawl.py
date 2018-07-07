import scrapy
from scrapy import ItemLoader
from item import Article


class help_fp(scrapy.Spider):
    name = 'help_fp'
    """
    Starts crawling at the base website to yield links to individual articles.
    This restricts the spider's ability to crawl to other websites not of the
    allowed domain.
    """
    def __init__(self):
        super(help_fp, self).__init__(self)
        self.start_urls = ['http://www.foreignpolicy.com/']
    """
    Creates a generator that yields a Request object for each link on the front
    page and trending. Individual articles are parsed later.
    """
    def parse(self, response):
        for link in response.xpath('//div[@class="excerpt-content\
                                    content-block"]/a[@class="hed-heading\
                                    -excerpt"]/@href').extract():
            yield scrapy.Request(link, callback=self.parse_indiv_articles())
    """
    Collects metadata for each of the articles and populates items generated
    for each of the individual articles. Passed to pipeline to be arranged into
    documents.
    """
    def parse_indiv_articles(self, response):
        il = ItemLoader(item=Article(), response=response)
        il.add_xpath('title', '//head/title/text()')
        il.add_xpath('date', '//time/text()')
        il.add_xpath('text', '//article/div/p/text()')
        return il.load_item()
