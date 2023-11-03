from lxml import etree
import requests as re

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
# 网站的url乱了
url = 'https://sh.58.com/ershoufang/'
result = re.get(url=url, headers=head).text
# print(result)
tree = etree.HTML(result)
div_list = tree.xpath('/html/body/div[1]/div/div/section/section[3]/section[1]/section[2]/div')
# print(div_list)
for house in div_list:
    # ['     假一罚万 万科有山 豪装下叠 拎包入住 南北双花园']加个[0]只取内容文字
    # ./ 从当前标签路径开始往下解析
    name = house.xpath('./a/div[2]/div[1]/div[1]/h3//text()')[0]
    print(name)
