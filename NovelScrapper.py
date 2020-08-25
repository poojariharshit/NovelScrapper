import scrapy

class QuotesSpider(scrapy.Spider):
    name = "novels"
    start_urls = ['https://www.wuxiaworld.co/I-Shall-Seal-the-Heavens/']

    def parse(self, response):
        for novel in response.css('div.chapter-wrapper a.chapter-item'):
            
            yield response.follow(novel, callback=self.parse_page)
            #yield response.follow(a, callback=self.parse)


    def parse_page(self, response):
        yield {
            'text': response.css('.chapter-entity::text').getall(),
            }
