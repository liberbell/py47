import scrapy


class AudibleSpider(scrapy.Spider):
    name = 'audible'
    allowed_domains = ['www.audible.com']
    start_urls = ['https://www.audible.com/search']

    def parse(self, response):
        product_container = response.xpath('//div[@class="adbl-impression-container "]/div/span/ul/li')

        for product in product_container:
            book_author = product.xpaht('.//li[contains(@class, "authorLabel")]/span/a/text()').getall()
            book_length = product.xpaht('.//li[contains(@class, "runtimeLabel")]/span/text()').getall()
