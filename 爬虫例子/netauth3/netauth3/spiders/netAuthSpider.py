from netauth3.items import Netauth3Item
from scrapy.spiders import Spider
from scrapy_splash import SplashRequest
from scrapy import Selector
import scrapy

#设置cookies  登陆访问文件
class NetAuthSpider(Spider):
    name = "netauth3"
    allowed_domains = ["10.20.83.66:10000"]
    start_urls = ["http://10.20.83.66:10000/idm/jsp/login.jsp",
                  "http://10.20.83.66:10000/idm/jsp/synchaccount/addsynconfig.jsp"]

    #meta={'cookiejar': 1},
    # meta={'cookiejar': response.meta['cookiejar']},
    # 添加cookie
    #模拟登陆
    def start_requests(self):
        return [scrapy.FormRequest("http://10.20.83.66:10000/idm/jsp/doLogin",
                                  meta={'cookiejar': 1},
                                  formdata={'logname': 'admin', 'password': '123456'},
                                  callback=self.login)]
    def login(self,response):
        yield  scrapy.FormRequest("http://10.20.83.66:10000/idm/jsp/common/main.jsp",
                                   meta={'cookiejar': response.meta['cookiejar']},
                                  callback=self.get_from,dont_filter=True)

        # dont_filter 是否过滤domains
    def parse_data(self,response):

        item = Netauth3Item()
        sel = Selector(response)
        sites = sel.xpath('//li[@class="active"]')
        for site in sites:
            url = site.xpath(".//a/@href").extract()
            title  = site.xpath(".//a/text()").extract()
            print(url)
            print(title)

    def get_from(self,response):

        sel = Selector(response)
        sites = sel.xpath("//a")
        for site in sites:
            url = site.xpath("@onclick").extract()
            print(url)
            script = """
            function main(splash)
                splash: runjs("rightOpen(3)")
                splash: wait(9)
                return splash: html()
            end
            """
            yield scrapy.FormRequest('http://10.20.83.66:10000/idm/jsp/common/main.jsp', self.parse, meta={
                'splash': {
                    'args': {'lua_source': script,'html':1},
                    'endpoint': 'execute',
                },
                'cookiejar': response.meta['cookiejar'],
            }, dont_filter=True)

    def parse(self, response):
        doc = response.body_as_unicode()
        print("###")
        print(doc)
        print(response.url)
        # fo = open('data2.html', 'wb')
        # fo.write(response.body)
        # fo.close()
