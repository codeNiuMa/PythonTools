import scrapy


class MyfileSpider(scrapy.Spider):
    name = 'myfile'
    # 限定下面哪个基本域名可以请求，不用得了
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.baidu.com/']

    # 解析数据
    def parse(self, response):
        print(response)
