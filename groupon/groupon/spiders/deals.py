import scrapy


class DealsSpider(scrapy.Spider):
    name = 'deals'
    allowed_domains = ['www.groupon.com']
    start_urls = ['https://www.groupon.com/landing/deal-of-the-day/']

    def parse(self, response):
        outputs=response.xpath("//div[@class='grpn-dc-content']")
        for output in outputs:
            yield{
                "title":output.xpath(".//div[@class='grpn-dc-title']/text()").get(),
                "Original Price":output.xpath(".//s[@class='wh-dc-price-original']/text()").get(),
                "Regular Price" :output.xpath("//span[@class='wh-dc-price-regular']/text()").get(),
                "Discount Price":output.xpath(".//span[@class='wh-dc-price-discount wh-dc-urgent']/text()").get()\
                    

            }


#scrapy crawl deals --o groupondealsdata.json