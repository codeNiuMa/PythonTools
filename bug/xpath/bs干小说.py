from bs4 import BeautifulSoup as bs
import requests as re

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
# 网站的url乱了
url = 'https://www.shicimingju.com/book/zhouyi/4.html'
result = re.get(url=url, headers=head).content
soup = bs(result, "html.parser")
title_list = soup.find('div',attrs={'class':"chapter_content"})
print(title_list.text)
