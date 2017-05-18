from muke.items import MukeItem
from scrapy.spiders import Spider
import  scrapy

#获取url 继续爬取
class MukeSpider(Spider):
    name = "muke"
    allowed_domains = ["www.imooc.com"]
    start_urls = ["http://www.imooc.com/course/list"]
    def parse(self, response):
        item = MukeItem()
        for box in response.xpath('//div[@class="index-card-container course-card-container container "]/a[@target="_blank"]'):
            # body = box.extract()
            # print(body)
            item['url'] ='http://www.imooc.com'+box.xpath('@href').extract()[0]
            item['title'] = box.xpath('.//h3/text()').extract()[0].strip()
            # item['image_url'] = box.xpath('.//@src').extract()[0]
            item['student'] = box.xpath('.//span/text()').extract()[0]
            item['introduction'] = box.xpath('.//p/text()').extract()[0].strip()
            print(item['url'])
            print(item['title'])
            # print(item['image_url'])
            print(item['student'])
            print(item['introduction'])
            yield item
        url = response.xpath("//a[contains(text(),'下一页')]/@href").extract()
        if url:
            # 将信息组合成下一页的url
            page = 'http://www.imooc.com' + url[0]
            # 返回url
            yield scrapy.Request(page, callback=self.parse)
