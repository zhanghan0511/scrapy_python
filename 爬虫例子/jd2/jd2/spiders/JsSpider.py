import scrapy

from scrapy_splash import SplashRequest

class JsSpider(scrapy.Spider):
    name = "jd2"
    allowed_domains =["jd.com"]
    start_urls = ["http://www.jd.com"]

    #args 分开写参数
    def start_requests(self):
        splash_args = {
            'wait':0.5,
        }
        for url in self.start_urls:
            yield SplashRequest(url,self.parse_result,endpoint='render.html',
                                args=splash_args)
    def parse_result(self, response):
        guessyou = response.xpath('//div[@id="footmark"]/div[1]/div[1]/h2/text()').extract()
        print(guessyou)
        print("###############" + response.url)
        fo = open("jd.html", "wb")
        fo.write(response.body)
        fo.close()
