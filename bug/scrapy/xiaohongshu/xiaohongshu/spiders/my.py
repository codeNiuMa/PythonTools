import scrapy


class MySpider(scrapy.Spider):
    name = 'my'
    # allowed_domains = ['www.x.com']
    start_urls = ['https://www.jitashe.org/']

    def parse(self, response, *args, **kwargs):
        list = response.xpath('//*[@id="portal_block_143_content"]/div/div/div')
        print(response)
        print(list)
        # l = list.xpath('./div[1]/div/div/div')
        # print(l)

        # for i in list[:3]:
        #     author = i.xpath('./div/div/div/a/span/text()')
        #     content = i.xpath('./div/div/a/span/text()')
        #     print(author+', '+content)
        #     print('sad')
