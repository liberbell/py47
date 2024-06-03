import scrapy


class WorldometersSpider(scrapy.Spider):
    name = 'worldometers'
    allowed_domains = ['www.worldometers.info/']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        # title = response.xpath('//h1/text()').get()
        countries = response.xpath("//td/a")

        for country in countries:
            country_name = country.xpath(".//text()").get()
            country_url = country.xpath(".//@href").get()

            # absolute_url = f"https://www.worldometers.info/{country_url}"
            absolute_url = response.urljoin(country_url)

            # yield {
            #     # "countries": countries,
            #     # "title": title,
            #     # "countries": countries,
            #     # "country_name": country_name,
            #     # "country_url": country_url,
            #     "absolute_url": absolute_url,
            # }
            yield response.Request(url=absolute_url)
            # yield response.follow(url=country_url)

# /html/body/div[2]/div[2]/div/div/div[1]/h1