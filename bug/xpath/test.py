from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from lxml import etree
# 1. 初始化配置无可视化界面对象
options = webdriver.ChromeOptions()
# 2. 无界面模式
# options.add_argument('-headless')
# options.add_argument('--disable-gpu')

# 让selenium规避被检测到的风险
options.add_argument('excludeSwitches')

# 传入浏览器的驱动
ser = Service(r'D:\Google\chromedriver-win32\chromedriver.exe')

# 实例化一个浏览器对象
bro = webdriver.Chrome(service=ser, options=options)
bro.get('https://www.zhipin.com/job_detail/f2b441b0f06d2646031-3tu8EFM~.html?lid=Jmb6qJ9UxO.search.55&securityId=Y66sd9vfnY2QW-t139LJ5QH1Gd9h-IqbPa7dibcxWBFhpmjffSCyizlA0PSDZiROkKvHRE1DLLeNzJcMm-w4H09JGEoj_3NoA_sm6H_VOnVxbI_GBw~~&sessionId=')
sleep(5)
inter_text = bro.page_source
tree2 = etree.HTML(inter_text)
a = str(tree2.xpath("//div[@class='job-sec-text']/text()"))
# print('|'.join(job_miaoshu))
b = tree2.xpath("//div[@class='detail-section-item company-address']/div/div[1]/text()")
print(a)
print(b)