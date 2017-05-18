from scrapy.spiders import Spider
from scrapy.selector import Selector
from tutorial.items import TutorialItem


class DmozSpider(Spider):
    name = "Myspider";
    allowed_domains =[ "imooc.com"]
    start_urls = ["http://www.imooc.com/course/list"]

    def parse(self, response):
        item = TutorialItem()
        for box in response.xpath('//div[@class="moco-course-wrap"]/a[@target="_self"]'):
            item['url'] = 'http://www.imooc.com' + box.xpath('.//@href').extract()[0]
            item['title'] = box.xpath('.//img/@alt').extract()[0].strip()
            item['image_url'] = box.xpath('.//@src').extract()[0]
            item['student'] = box.xpath('.//span/text()').extract()[0].strip()[:-3]
            item['introduction'] = box.xpath('.//p/text()').extract()[0].strip()
            yield item
        # sel = Selector(response)
        # sites = sel.xpath('//ul/li')
        # filename = response.url.split("/")[-2]
        # open(filename,'wb').write(response.body)
        # for site in sites:
        #     title = site.xpath('a/text()').extract()
        #     link = site.xpath('a/@href').extract()
        #     desc = site.xpath('text()').extract()
        #
        #     print(title)

