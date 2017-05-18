from scrapy import Request
from scrapy.spiders import Spider
from scrapy_splash import SplashRequest
from scrapy_splash import SplashMiddleware


class WeixinSpider(Spider):
    name = 'weixin'
    start_urls = [
        'http://weixin.sogou.com/weixin?page={}&type=2&query=%E4%B8%AD%E5%9B%BD'.format(a) for a in range(1, 10)
    ]
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url,
                                self.parse,
                                args={'wait':'0.5'}
                                )
    def parse(self, response):
        div_results = response.xpath('//div[@class="news-box"]/div')
        if not div_results:
            print("no body")
            return
        for div_item in div_results:
            title = div_item.xpath('./div[@class="txt-box"]//h3//text()')
            if title:
                txt = ''.join(title.extract())
                yield {'title': txt}
