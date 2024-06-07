import scrapy


class AudibleSpider(scrapy.Spider):
    name = 'audible'
    allowed_domains = ['www.audible.com']
    # start_urls = ['https://www.audible.com/search']

    def start_requests(self):
        yield scrapy.Request(url="https://www.audible.com/search/", callback=self.parse,
                            headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'})

    def parse(self, response):
        # product_container = response.xpath('//div[@class="adbl-impression-container "]/div/span/ul/li')
        product_container = response.xpath('//div[@class="adbl-impression-container "]//li[contains(@class, "productListItem")]')

        for product in product_container:
            book_title = product.xpath('.//h3[contains(@class, "bc-heading")]/a/text()').get()
            book_author = product.xpath('.//li[contains(@class, "authorLabel")]/span/a/text()').getall()
            book_length = product.xpath('.//li[contains(@class, "runtimeLabel")]/span/text()').get()

            yield {
                "Book_title": book_title,
                "Book_author": book_author,
                "Book_length": book_length,
                "User-Agent":response.request.headers['User-Agent'],
            }

            pagination = response.xpath('//ul[contains(@class, "pagingElements")]/a/text()')
            next_page_url = pagination.xpath('.//span[contains(@class, "nextButton")]/a/@href').get()

            if next_page_url:
                yield response.follow(next_page_url, callback=self.parse,
                                      headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'})
