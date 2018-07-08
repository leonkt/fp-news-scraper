from scrapy.exceptions import DropItem
from scrapy.exporters import CsvItemExporter


class NewscrawlPipeline(object):
    def __init__(self):
        self.visited = set()

    def process_item(self, item, spider):
        file = open("/lkt/NewsCrawl/for_mycsvs/{0}.csv".format(item['title']),
                    'wb')
        exp = CsvItemExporter(file, unicode)
        exp.start_exporting()
        if len(item['text']) == 0:
            raise DropItem("The text was not present for %s\n" % item['title'])
        if(item['title'] in self.visited):
            raise DropItem("This is a duplicate %s\n" % item['title'])
        self.join_text(item)
        self.visited.add(item['title'])
        exp.export_item(item)
        return item

    """
    This joins all elements of a given list of paragraphs in a coherent way to
    resemble an actual formatted news article.
    """
    def join_text(self, item):
        joined = ""
        for paragraph in item['text']:
            joined += paragraph + "\n"
        item['text'] = joined
