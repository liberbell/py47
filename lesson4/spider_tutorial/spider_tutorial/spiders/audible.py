import scrapy


class AudibleSpider(scrapy.Spider):
    name = 'audible'
    allowed_domains = ['www.audible.com']
    start_urls = ['http://www.audible.com/']

    def parse(self, response):
        pass
