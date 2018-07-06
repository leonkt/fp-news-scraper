import scrapy
import items


class help_fp(scrapy.Spider):
    name = 'help_fp'

    def __init__(self):
        super(help_fp, self).__init__(self)
        self.start_urls = ['http://www.foreignpolicy.com/']

    def parse(self, response):
        for info in response.xpath('//article[@class="article"]/'):
            article = items.Article()
            article.title = response.xpath('//head/title/text()').extract()
            article.date = response.xpath('//div[@class="meta-data"]/time\
                                          /@title').extract()
            article.author = response.xpath('//address[@class="author-list"]\
                                            /a[@class="author"]\
                                            /text()').extract()
            article.topic = response.xpath('//div[@class="the-tags"]\
                                            /a/text()').extract()
            yield article

        for link in response.xpath('//div[@class="excerpt-content\
                                    content-block"]/a[@class="hed-heading\
                                    -excerpt"]/@href').extract():
            yield scrapy.Request(link, callback=self.parse)
