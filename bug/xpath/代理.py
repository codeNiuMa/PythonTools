from lxml import etree
import requests as re

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

url = 'https://www.baidu.com/s?wd=ip'
result = re.get(url=url, headers=head, proxies={'https://': '122.136.212.132:53281'})
print(result.status_code)
with open('1.html', 'w', encoding='utf-8') as f:
    f.write(result.text)
