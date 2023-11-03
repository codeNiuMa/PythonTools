from bs4 import BeautifulSoup as bs
import requests as re

head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
index = 0  # 记录页数，一次加25
cnt = 1  # 记录No.12345
while index != 250:
    content = re.get('https://movie.douban.com/top250?start='+str(index), headers=head).text
    soup = bs(content, "html.parser")
    hds = soup.findAll('div', attrs={'class': 'hd'})
    for h in hds:
        names = h.findAll('span', attrs={'class': 'title'})
        print('No.'+str(cnt), end=' ')
        print(names[0].string)  # 每一个hd里面的第一个span
        cnt += 1
    index += 25

'''
No.1 肖申克的救赎
No.2 霸王别姬
No.3 阿甘正传
No.4 泰坦尼克号
No.5 这个杀手不太冷
No.6 千与千寻
。。。。。
'''

