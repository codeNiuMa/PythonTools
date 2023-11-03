from allpath import dirver_path
from selenium import webdriver
# 无头骑士
from selenium.webdriver.chrome.options import Options
op = Options()
op.add_argument(argument='--headless')
op.add_argument('--disable-gpu')

# 伪装自己不是selenium
from selenium.webdriver import ChromeOptions
op2 = ChromeOptions()
op2.add_experimental_option('excludeSwitches', ['enable-automation'])



bro = webdriver.Chrome(executable_path=dirver_path, options=op2)

bro.get('https://www.baidu.com')
page = bro.page_source
print(page)