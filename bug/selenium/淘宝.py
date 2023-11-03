from time import sleep
from selenium import webdriver
from lxml import etree

bro = webdriver.Chrome(executable_path='D:\Google\chromedriver_win32\chromedriver.exe')
bro.get('https://www.taobao.com/')

input = bro.find_element_by_xpath('//*[@id="q"]')
input.send_keys('蔡徐坤')
sleep(2)

# 滚动操作
bro.execute_script('window.scrollTo(0, document.body.scrollHeight/2)')
sleep(2)
# click
yes_button = bro.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button')
yes_button.click()
sleep(2)
# get again
bro.get('https://www.baidu.com')
sleep(2)
# back
bro.back()
sleep(2)
# 前进
bro.forward()





bro.close()