from scrapy.spiders import Spider


import scrapy
#http://10.20.70.112:8080/myWebSite/test.html
class TestSpider(Spider):
    name = "mytest"
    allowed_domains =["10.20.70.112:8080"]
    start_urls = ["http://10.20.70.112:8080/myWebSite/test.html"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse_on, meta = {
                'splash': {
                    'args': {'wait': 0.5},
                    'endpoint':'render.html'
                }
            })
        # data = response.xpath("//button/@onclik").extract()
        # print(data)
    def parse_on(self, response):
        doc = response.body_as_unicode()
        data = response.xpath("//button/@onclick").extract()
        print(data)
        pass