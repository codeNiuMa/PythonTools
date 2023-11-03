import os
from time import sleep

from lxml import etree

import requests as re

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
mulu_url = 'https://mp.weixin.qq.com/s/sSpJwub-euAD7hKyhzqj-Q'
result = re.get(url=mulu_url, headers=head).text
# print(result)

tree = etree.HTML(result)
song_list = tree.xpath('/html/body/div[1]/div[2]/div[1]/div/div[1]/div[3]/p')[5:]
# print(song_list)

desk = os.path.join(os.path.expanduser("~"), 'Desktop')
path = 'cxk'
for item in song_list[:]:
    if item.xpath('./text()'):
        path = item.xpath('./text()')[0]
        print(path)
    elif item.xpath('./a'):
        song_name = item.xpath('./a/text()')[0]
        song_url = item.xpath('./a/@href')[0]
        # print(song_name)

        # 开爬
        sleep(0.2)
        result = re.get(url=song_url, headers=head).text  # 吉他谱界面
        print(f'获取到{song_name}')
        tree = etree.HTML(result)
        pic_list = tree.xpath('/html/body/div[1]/div[2]/div[1]/div/div[1]/div[3]/p')  # 谱子list
        cnt = 1
        song_path = fr'{desk}/yuange666-guitar/{path}/{str(song_name).split("》")[0]}》'
        if os.path.exists(song_path) is False:
            os.makedirs(song_path)
        for p in pic_list:
            if p.xpath('./img'):
                src_url = p.xpath('./img/@data-src')[0]
                src = re.get(src_url).content
                with open(fr'{song_path}/{str(song_name).split("》")[0]}》-{cnt}.png', 'wb') as f:
                    f.write(src)
                    print(f'{song_name}{cnt}.jpg 下载完成')
                    cnt += 1



