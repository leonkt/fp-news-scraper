from TagClassifier import TagClassifier as tc

import pymongo

from scrapy import log

from scrapy.conf import settings

from scrapy.exceptions import DropItem


class NewscrawlPipeline(object):

    def __init__(self):
        """
        Establish a connection with the MongoDB server before writing to the
        database. Takes preconfigured settings from the settings.py module.
        """

        connection = pymongo.MongoClient(settings['MONGODB_SERVER'],
                                         settings['MONGODB_PORT'])
        self.db = connection[settings['MONGODB_DB']]
        self.collection = self.db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        """
        Validates and sanitizes malformed data by checking if there is a found
        text or title. If the data is valid (there is substantial text and a
        title), then we join the paragraphs and write the item to the database.
        """
        t = tc.TagClassifier(item['text'])
        if len(item['text']) == 0 or len(item['author']) == 0:
            raise DropItem("The text or title was not present for\
                            %s\n" % item['title'])
        if(self.db.find_one({"title": item['title']}) is not None):
            raise DropItem("This is a duplicate %s\n" % item['title'])
        self.join_text(item)
        self.collection.insert(dict(item)
        if(t.perf_km() == 0):
            item['tag'] = "cons"
        else:
            item['tag'] = "lib"
        log.msg("Slav fun!", level=log.DEBUG, spider=spider)
        return item

    def join_text(self, item):
        """
        Joins the elements of the text field in a given article. Creates a more
        compact and uniform representation of text across various articles,
        esp. those with different num. of paragraphs.
        """

        long_art = ""
        for paragraph in item['text']:
            long_art += paragraph + "\n"
        item['text'] = [long_art]
