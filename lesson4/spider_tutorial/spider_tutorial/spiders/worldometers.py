import scrapy


class WorldometersSpider(scrapy.Spider):
    name = 'worldometers'
    allowed_domains = ['www.worldometers.info/world-population/population-by-country']
    start_urls = ['http://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        pass
