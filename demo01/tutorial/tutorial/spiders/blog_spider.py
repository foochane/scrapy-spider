from scrapy.spiders import Spider
class BlogSpider(Spider):
    name = 'foochane'
    start_urls = ['https://foochane.cn']
    def parse(self, response):
        titles = response.xpath('//a[@class="post-title-link"]/text()').extract()
        for title in titles:
            print(title.strip())