import os
from time import sleep
from lxml import etree
import requests as re

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
print('===== yuange666-wallheaven爬虫v3.0 =====')
x = input('按回车键继续。。。')
print('杀！！！！！！！！！！！！！！！！！！！！！！！！！！！！！\n')
for i in range(1, 20):
    url = f'https://wallhaven.cc/toplist?page={i}'
    print('开始爬取' + url +'。。。。')
    # 得到网站html内容
    result = re.get(url=url, headers=head).text
    print('获取页面'+url+'成功，开始爬取网页图片')
    # xpath解析网址图片列表
    tree = etree.HTML(result)
    img_list = tree.xpath('/html/body/main/div[1]/section[1]/ul/li')
    print('已获取到源列表。。。')
    # print(img_list)
    path = os.path.join(os.path.expanduser("~"), 'Desktop')

    cnt = 1
    for li in img_list[:]:
        sleep(0.5)  # 访问慢一点
        print(f'\n----- 正在获取Pic[' + str(cnt) + f']/{len(img_list)} -----')
        big_img_url = li.xpath('./figure/a/@href')[0]  # 外面是缩略图，得到大图的网址url
        print('大图网址：' + big_img_url, end='')  # https://wallhaven.cc/w/rrowwm
        # 切分得到图片名字
        name = str(big_img_url).rsplit('/', 1)[-1]  # /wallhaven-rrowwm.png -> rrowwm.png
        if os.path.exists(fr'{path}\yuange666\{name}.jpg') is False and os.path.exists(fr'{path}\yuange666\{name}.png') is False:
            # 请求大图实际网址，并解析到图片源文件
            big_img_url_result = re.get(url=big_img_url, headers=head).text
            tree1 = etree.HTML(big_img_url_result)
            img_xp = tree1.xpath('/html/body/main/section/div[1]/img/@src')[0]
            print('  get大图源：' + img_xp)  # https://w.wallhaven.cc/full/gp/wallhaven-gp9god.jpg
            if os.path.exists(fr'{path}/yuange666') is False:
                os.mkdir(fr'{path}/yuange666')
            print('Downloading...')
            # 请求图片源文件二进制数据
            big_img = re.get(url=img_xp, headers=head).content
            with open(fr'{path}\yuange666\{name}.jpg', 'wb') as f:
                f.write(big_img)
                print('Save ' + name + '.jpg successfully!')
        else:
            print(f'\n{name}.jpg 已存在。')
        cnt += 1 # 计数器++
        if cnt == len(img_list):
            print()