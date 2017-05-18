from scrapy.spiders import Spider
from scrapy import Selector
from scrapy_splash import SplashRequest
import scrapy

class NetAuthSpider(Spider):
    name = "netauth4"
    allowed_domains =["10.20.83.66:10000"]

    #start_urls = [""]
    def start_requests(self):
        return [scrapy.FormRequest("http://10.20.83.66:10000/idm/jsp/doLogin",
                                   meta={'cookiejar': 1},
                                   formdata={'logname': 'admin', 'password': '123456'},
                                   callback=self.after_login)]
    def after_login(self,response):
        script = """
        function main(splash)
            splash:go('http://10.20.83.66:10000/idm/jsp/common/main.jsp')
            splash:wait(0.5)
            local title = splash:runjs('document.title')
            return {title}
        end
        """
        yield scrapy.Request('http://10.20.83.66:10000/idm/jsp/common/main.jsp',self.parse,meta={
                'splash':{
                    'args':{'lua_source':script},
                    'endpoint':'execute',
                },
                'cookiejar': response.meta['cookiejar'],
            },dont_filter=True)
    # def start_requests(self):
    #     return [scrapy.FormRequest("http://10.20.83.66:10000/idm/jsp/doLogin",
    #                                meta={'cookiejar': 1},
    #                                formdata={'logname': 'admin', 'password': '123456'},
    #                                callback=self.after_login)]
    # def after_login(self,response):
    #     script = """
    #     function main(splash)
    #         splash:go('http://10.20.83.66:10000/idm/jsp/common/main.jsp')
    #         splash:wait(0.5)
    #         local title = splash:runjs('document.title')
    #         return {title = title}
    #     end
    #     """
    #     yield scrapy.Request('http://10.20.83.66:10000/idm/jsp/common/main.jsp',self.parse,meta={
    #             'splash':{
    #                 'args':{'lua_source':script},
    #                 'endpoint':'execute',
    #             },
    #             'cookiejar': response.meta['cookiejar'],
    #         },dont_filter=True)
    def parse(self, response):
        # doc_title = response.body_as_unicode()
        # print(doc_title)
        # fo = open("data1.html","wb")
        # fo.write(response.body)
        # fo.close()

        pass