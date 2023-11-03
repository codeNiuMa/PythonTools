from time import sleep

from lxml import etree
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

bro = webdriver.Chrome(executable_path='D:\Google\chromedriver_win32\chromedriver.exe')
bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
bro.switch_to.frame('iframeResult')
div = bro.find_element(by=By.XPATH, value='//*[@id="draggable"]')

action = ActionChains(bro)
# 点击且长安
action.click_and_hold(div)

for i in range(5):
    # x,y方向拖动像素，perform立即执行
    action.move_by_offset(20,0).perform()
    sleep(1)

action.release()







sleep(3)
bro.quit()


