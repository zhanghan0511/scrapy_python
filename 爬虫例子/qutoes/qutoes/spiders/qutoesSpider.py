import scrapy
from  scrapy.linkextractors import LinkExtractor
from scrapy_splash import SplashRequest
from qutoes.items import QutoesItem


#可以爬取 <a 的页面
#启动docker docker run -p 8050:8050 scrapinghub/splash
class qutoesSpider(scrapy.Spider):
    name = "qutoes"
    # allowed_domains =["toscrape.com"]
    # start_urls = ["http://quotes.toscrape.com/"]
    allowed_domains = ["imooc.com"]
    start_urls = ["http://www.imooc.com/course/list?c=javascript"]
    def parse(self, response):
        le = LinkExtractor()
        for link in le.extract_links(response):
            print(link.url)
            yield SplashRequest(
                link.url,
                self.parse_link,
                endpoint= "render.json",
                args={
                    'har':1,
                    'html':1,
                }
            )
    def parse_link(self,response):
        print("PARSED", response.real_url, response.url)
        item = QutoesItem()

        item['url'] = response.url
        item['name'] = response.css("title").extract()
        yield item
        # print(response.datata["har"]["log"]["pages"])
        # print(response.headers.get('Content-Type'))




