import os
from time import sleep
from lxml import etree
import requests as re
from chaojiying_Python.chaojiying import getCode

session = re.session()
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

pic_url = 'https://so.gushiwen.cn/RandCode.ashx'
pic = session.get(pic_url, headers=head).content
with open('code.jpg', 'wb') as fp:
    fp.write(pic)

i = input('if 调用超级鹰？(y/n)\n')
code = ''
if i == 'y':
    code = getCode('code.jpg', 1004)
else:
    pass
login_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
print(code)

result1 = session.post(url=login_url, headers=head)
print(result1.status_code)
result2 = session.get(url='https://so.gushiwen.cn/user/collect.aspx', headers=head)
# 弹幕说要用session。访问不到登录后的数据
print(result2.text)