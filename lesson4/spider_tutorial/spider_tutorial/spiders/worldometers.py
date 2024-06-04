import scrapy


class WorldometersSpider(scrapy.Spider):
    name = 'worldometers'
    allowed_domains = ['www.worldometers.info']
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
            # yield scrapy.Request(url=absolute_url)
            yield response.follow(url=country_url, callback=self.parse_country)

    def parse_country(self, response):
        # response.xpath('(//table[@class="table table-striped table-bordered table-hover table-condensed table-list"])[1]/tbody/tr')
        rows = response.xpath("(//table[contains(@class, 'table')][1]/tbody/tr")
        for row in rows:
            year = row.xpath('.//td[1]/text()').get()
            population = row.xpath('.//td[2]/strong/text()').get()

            yield {
                "Year": year,
                "Population": population,
            }


# /html/body/div[2]/div[2]/div/div/div[1]/h1
# /html/body/div[2]/div[4]/div/div/div[8]/table
# /html/body/div[2]/div[4]/div/div/div[8]/table
# /html/body/div[2]/div[4]/div/div/div[8]/table
# <table class="table table-striped table-bordered table-hover table-condensed table-list"><thead> <tr> <th>Year</th><th>Population</th><th>Yearly % <br> Change</th><th>Yearly<br> Change</th><th>Migrants (net)</th><th>Median Age</th><th>Fertility Rate</th><th>Density (P/Km²)</th><th>Urban<br> Pop %</th><th>Urban Population</th><th>Country's Share of<br> World Pop</th><th>World Population</th><th>India<br>Global Rank</th></tr></thead><tbody> <tr> <td>2024</td> <td><strong>1,441,719,852</strong></td> <td>0.92 %</td> <td>13,092,189</td> <td>-486,784</td> <td>28.6</td> <td>1.98</td> <td>485</td> <td>36.8 %</td> <td>530,387,142</td> <td>17.76 %</td> <td>8,118,835,999</td> <td>1</td> </tr> <tr> <td>2023</td> <td><strong>1,428,627,663</strong></td> <td>0.81 %</td> <td>11,454,490</td> <td>-486,136</td> <td>28.2</td> <td>2.00</td> <td>481</td> <td>36.3 %</td> <td>518,239,122</td> <td>17.76 %</td> <td>8,045,311,447</td> <td>1</td> </tr> <tr> <td>2022</td> <td><strong>1,417,173,173</strong></td> <td>0.68 %</td> <td>9,609,331</td> <td>-487,303</td> <td>27.9</td> <td>2.01</td> <td>477</td> <td>35.7 %</td> <td>506,304,869</td> <td>17.77 %</td> <td>7,975,105,156</td> <td>2</td> </tr> <tr> <td>2020</td> <td><strong>1,396,387,127</strong></td> <td>0.96 %</td> <td>13,275,077</td> <td>-34,772</td> <td>27.3</td> <td>2.05</td> <td>470</td> <td>34.6 %</td> <td>483,098,640</td> <td>17.81 %</td> <td>7,840,952,880</td> <td>2</td> </tr><tr> <td>2015</td> <td><strong>1,322,866,505</strong></td> <td>1.29 %</td> <td>16,450,577</td> <td>-475,094</td> <td>25.5</td> <td>2.29</td> <td>445</td> <td>32.4 %</td> <td>429,069,459</td> <td>17.81 %</td> <td>7,426,597,537</td> <td>2</td> </tr><tr> <td>2010</td> <td><strong>1,240,613,620</strong></td> <td>1.45 %</td> <td>17,194,981</td> <td>-380,087</td> <td>24.0</td> <td>2.60</td> <td>417</td> <td>30.7 %</td> <td>380,744,554</td> <td>17.76 %</td> <td>6,985,603,105</td> <td>2</td></tr><tr> <td>2005</td> <td><strong>1,154,638,713</strong></td> <td>1.73 %</td> <td>19,001,008</td> <td>-550,186</td> <td>22.6</td> <td>2.96</td> <td>388</td> <td>29.0 %</td> <td>334,479,406</td> <td>17.61 %</td> <td>6,558,176,119</td> <td>2</td> </tr><tr> <td>2000</td> <td><strong>1,059,633,675</strong></td> <td>1.90 %</td> <td>19,070,909</td><td>-149,966</td> <td>21.6</td> <td>3.35</td> <td>356</td> <td>27.5 %</td> <td>291,350,282</td> <td>17.23 %</td> <td>6,148,898,975</td> <td>2</td></tr><tr> <td>1995</td> <td><strong>964,279,129</strong></td> <td>2.07 %</td> <td>18,765,393</td> <td>-57,139</td> <td>20.7</td> <td>3.65</td> <td>324</td> <td>26.5 %</td> <td>255,558,824</td> <td>16.79 %</td> <td>5,743,219,454</td> <td>2</td></tr><tr> <td>1990</td> <td><strong>870,452,165</strong></td> <td>2.21 %</td> <td>18,042,016</td> <td>108,465</td> <td>20.0</td> <td>4.05</td> <td>293</td> <td>25.5 %</td> <td>222,296,728</td> <td>16.37 %</td> <td>5,316,175,862</td> <td>2</td></tr><tr> <td>1985</td> <td><strong>780,242,084</strong></td> <td>2.29 %</td> <td>16,682,740</td> <td>-112,781</td> <td>19.5</td> <td>4.43</td> <td>262</td> <td>24.4 %</td> <td>190,321,782</td> <td>16.05 %</td> <td>4,861,730,613</td> <td>2</td></tr><tr> <td>1980</td> <td><strong>696,828,385</strong></td> <td>2.25 %</td> <td>14,660,833</td> <td>202,323</td> <td>19.0</td> <td>4.78</td> <td>234</td> <td>23.1 %</td> <td>160,941,941</td> <td>15.68 %</td> <td>4,444,007,706</td> <td>2</td></tr><tr> <td>1975</td> <td><strong>623,524,219</strong></td> <td>2.26 %</td> <td>13,204,584</td> <td>-225,989</td> <td>18.6</td> <td>5.20</td> <td>210</td> <td>21.3 %</td> <td>132,533,810</td> <td>15.32 %</td> <td>4,069,437,231</td> <td>2</td></tr><tr> <td>1970</td> <td><strong>557,501,301</strong></td> <td>2.20 %</td> <td>11,477,391</td> <td>-45,792</td> <td>18.3</td> <td>5.62</td> <td>188</td> <td>19.6 %</td> <td>109,388,950</td> <td>15.09 %</td> <td>3,695,390,336</td> <td>2</td></tr><tr> <td>1965</td> <td><strong>500,114,346</strong></td> <td>2.32 %</td> <td>10,831,953</td> <td>19,077</td> <td>18.5</td> <td>5.94</td> <td>168</td> <td>18.7 %</td> <td>93,493,844</td> <td>14.99 %</td> <td>3,337,111,983</td> <td>2</td></tr><tr> <td>1960</td> <td><strong>445,954,579</strong></td> <td>2.27 %</td> <td>9,475,317</td> <td>52,264</td> <td>19.2</td> <td>5.92</td> <td>150</td> <td>18.1 %</td> <td>80,565,723</td> <td>14.77 %</td> <td>3,019,233,434</td> <td>2</td></tr><tr> <td>1955</td> <td><strong>398,577,992</strong></td> <td>2.23 %</td> <td>8,311,378</td> <td>-115,107</td> <td>19.7</td> <td>5.91</td> <td>134</td> <td>18.1 %</td> <td>71,958,495</td> <td>14.51 %</td> <td>2,746,072,141</td> <td>2</td></tr></tbody></table>