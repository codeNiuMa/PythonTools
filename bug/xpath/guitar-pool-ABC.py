import os
from multiprocessing.dummy import Pool
from time import sleep
import tkinter as tk
from tkinter import filedialog
from lxml import etree
import requests as re

ABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'W', 'X', 'Y', 'Z']
index_list = [0, 11, 21, 35, 47, 50, 60, 78, 100, 111, 115, 130, 144, 160, 164, 177, 180, 201, 211, 246, 268, 287]

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 "
                  "Safari/537.36 "
}
mulu_url = 'https://mp.weixin.qq.com/s/sSpJwub-euAD7hKyhzqj-Q'
result = re.get(url=mulu_url, headers=head).text
# print(result)

tree = etree.HTML(result)
song_list = tree.xpath('/html/body/div[1]/div[2]/div[1]/div/div[1]/div[3]/p')[5:]  # 从A开始取
# print(song_list)
print('请选择保存文件夹')

'''打开选择文件夹对话框'''
root = tk.Tk()
root.withdraw()
# Filepath = filedialog.askopenfilename() #获得选择好的文件
Folderpath = filedialog.askdirectory()  # 获得选择好的文件夹
desk = os.path.join(os.path.expanduser("~"), 'Desktop')

if Folderpath != '':
    desk = Folderpath
else:
    print('不选老子给你放桌面！')
    sleep(1)
    for i in range(3):
        print(str(3-i))
        sleep(1)



def getPath(item):
    index = song_list.index(item)
    for i in range(len(index_list) - 1):
        if index_list[i] <= index <= index_list[i + 1]:
            return ABC[i]
        elif index > index_list[len(index_list) - 1]:
            return 'Z'


def op(item):
    path = getPath(item)
    if item.xpath('./a'):
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
        song_path = fr'{desk}/yuange666-guitar/{path}/{str(song_name).split("》")[0].split("《")[1]}'
        if os.path.exists(song_path) is False:
            os.makedirs(song_path)
        for p in pic_list:
            if p.xpath('./img'):
                src_url = p.xpath('./img/@data-src')[0]
                src = re.get(src_url).content
                with open(fr'{song_path}/{str(song_name).split("》")[0].split("《")[1]}-{cnt}.png', 'wb') as f:
                    f.write(src)
                    print(f'{song_name}{cnt}.jpg 下载完成')
                    cnt += 1


pool = Pool(12)
pool.map(op, song_list)
root.quit()
pool.close()