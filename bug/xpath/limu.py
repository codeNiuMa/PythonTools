import os
from multiprocessing.dummy import Pool
from time import sleep
from lxml import etree
import requests as re

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
mulu_url = 'https://api.bilibili.com/x/series/archives?mid=1567748478&series_id=358497&only_normal=true&sort=desc&pn=1&ps=90'
result = re.get(url=mulu_url, headers=head).json()
# print(type(result))
l = result['data']['archives']
# print(len(l))
# print(l[0]['title'])
# print(l[0]['duration'])
with open(r'./课程时间.txt', 'w', encoding='utf-8')as f:
    n = len(l)
    for i in l:
        f.write(str(n))
        f.write(',')
        f.write(str(i['title']).split('【动')[0].split(' ')[-1])
        f.write(',')
        f.write("{:.2f}".format(i['duration']/60))
        f.write('\n')
        n -= 1





