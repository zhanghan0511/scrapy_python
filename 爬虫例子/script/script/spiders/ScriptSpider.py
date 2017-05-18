from scrapy.spiders import Spider
from scrapy_splash import SplashRequest
import scrapy
#改脚本实现了：
#splash 执行js
#脚本实现了参数传递

class ScriptSpider(Spider):
    name = "script"
    allowed_domains = ["10.20.70.112:8080"]
    #start_urls = ["http://quotes.toscrape.com/"]
    start_urls = ["http://10.20.70.112:8080/myWebSite/test.html"]

    # def parse(self, response):
    #     button = response.xpath("//button/@onclick").extract()
    #     action = button
    #     print(action)
    #     script = """
    #         function main(splash)
    #             splash:go('http://10.20.70.112:8080/myWebSite/test.html')
    #             splash:wait(0.5)
    #             splash:runjs("displayDate()")
    #             splash:wait(3)
    #             return splash:html()
    #
    #         end
    #         """
    #     yield scrapy.Request("http://10.20.70.112:8080/myWebSite/test.html", self.parse_on, meta={
    #         'splash': {
    #             'args': {'lua_source': script},
    #             'endpoint': 'execute',
    #
    #         }
    #     },dont_filter=True)

    def start_requests(self):
        for url in self.start_urls:
            script = """
                function main(splash)
                    splash:go('http://10.20.70.112:8080/myWebSite/test.html')
                    splash:wait(0.5)
                    splash:runjs(splash.args.action)
                    splash:wait(3)
                    return splash:html()

                end
                """
            action = "displayDate()"
            yield scrapy.Request(url,self.parse_on,meta={
                'splash':{
                    'args':{'lua_source':script,'action':action},
                    'endpoint':'execute',


                }
            })


    def parse_on(self, response):
        doc_title = response.body_as_unicode()
        button = response.xpath("//button/@onclick").extract()
        print(doc_title)
        print(button)









#执行js 原始代码
    # def start_requests(self):
    #     for url in self.start_urls:
    #         script = """
    #         function main(splash)
    #             splash:go('http://quotes.toscrape.com/')
    #             splash:wait(0.5)
    #             local title = splash:evaljs('document.title')
    #             return {title = title}
    #         end
    #         """
    #         yield  scrapy.Request(url,self.parse,meta={
    #             'splash':{
    #                 'args':{'lua_source':script},
    #                 'endpoint':'execute',
    #             }
    #         })
    #
    # def parse(self, response):
    #     doc_title = response.body_as_unicode()
    #     print(doc_title)


    # splash_args = {
    #     'wait': 3,
    #     "http_method": "GET",
    #     # "images":0,
    #     "timeout": 1800,
    #     "render_all": 1,
    #     'lua_source': script,
    #     # "proxy":"http://101.200.153.236:8123",
    # }

    # 更改title
    # yield  SplashRequest( url,endpoint='render.html',
    #                         args={'js_source': 'document.title="Zhang Title";'},
    #     )
