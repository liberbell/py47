import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TranscriptsSpider(CrawlSpider):
    name = "transcripts"
    allowed_domains = ["subslikescript.com"]
    custom_settings = {
        'DOWNLOAD_DELAY': 0.5,
    }
    start_urls = ["https://subslikescript.com/movies"]

    rules = (Rule(LinkExtractor(restrict_xpaths=("//ul[@class='scripts-list']/li/a")), callback="parse_item", follow=True),)

    def parse_item(self, response):
        print(response.url)
