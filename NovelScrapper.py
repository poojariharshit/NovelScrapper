import scrapy

class QuotesSpider(scrapy.Spider):
    name = "novels"
    start_urls = ['https://www.wuxiaworld.co/example/']

    def parse(self, response):
        for novel in response.css('div.chapter-wrapper a.chapter-item'):
            #This scrapes the main page of the novel for the links of individual chapters
            yield response.follow(novel, callback=self.parse_page)
            #The spider follows the link to the page 


    def parse_page(self, response):
        #This scrapes the text of the particular page
        yield {
            'text': response.css('.chapter-entity::text').getall(),
            }
