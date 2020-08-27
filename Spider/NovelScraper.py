import scrapy
from scrapy.loader import ItemLoader
from items import TestItem

class NovelsSpider(scrapy.Spider):
    name = "novels"
    allowed_domains = ["www.wuxiaworld.co"]
    start_urls = ['https://www.wuxiaworld.co/I-Shall-Seal-the-Heavens/']


    def parse(self, response):
        self.logger.info('Parse function called on {}'.format(response.url))
        for novel in response.css('div.chapter-wrapper a.chapter-item'):
            yield response.follow(novel, self.parse_page)

    def parse_page(self, response):
        loader = ItemLoader(item=TestItem(), response=response)
        loader.add_css('Page', '.chapter-entity')
        yield loader.load_item()
