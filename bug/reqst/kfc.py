import requests as re

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
para = {'cname': '',
        'pid': '',
        'keyword': '上海',
        'pageIndex': '1',
        'pageSize': '10'}
result = re.post('https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword', params=para, headers=head)
# json返回的是对象，确认响应是对象才能用
print(result.text)
