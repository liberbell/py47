import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TranscriptsSpider(CrawlSpider):
    name = "transcripts"
    allowed_domains = ["subslikescript.com"]
    custom_settings = {
        'DOWNLOAD_DELAY': 0.5,
    }
    start_urls = ["https://subslikescript.com/movies_letter-X"]

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//ul[@class='scripts-list']/li/a")), callback="parse_item", follow=True),
        Rule(LinkExtractor(restrict_xpaths=("(//a[@rel='next'])[1]"))),
    )

    def parse_item(self, response):
        article = response.xpath("//article[@class='main-article']")
        yield {
            "title": article.xpath("./h1/text()").get(),
            "plot": article.xpath("./p/text()").get(),
            # "transcript": article.xpath("./div[@class='full-script']").getall(),
            "url": response.url,
        }
