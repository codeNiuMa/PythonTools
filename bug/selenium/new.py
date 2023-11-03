from time import sleep

from selenium import webdriver

from allpath import dirver_path

bro = webdriver.Chrome(executable_path=dirver_path)
bro.get('https://qzone.qq.com/')
# 切换到iframe
bro.switch_to.frame('login_frame')
# 点击密码登录
ex_div = bro.find_element_by_xpath('//*[@id="switcher_plogin"]')
ex_div.click()
# 获取账号密码域并输入
zhanghao = bro.find_element_by_xpath('//*[@id="u"]')
zhanghao.send_keys('2325415123')
sleep(0.5)
mima = bro.find_element_by_xpath('//*[@id="p"]')
mima.send_keys('200111Abc')
sleep(0.5)
# 点击登录
denglu = bro.find_element_by_xpath('/html/body/div[1]/div[5]/div/div[1]/div[3]/form/div[4]/a/input')
denglu.click()

sleep(2)
bro.close()
