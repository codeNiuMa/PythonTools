import requests as re
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

result = re.get('https://pics5.baidu.com/feed/1f178a82b9014a90e43e6ca3679e3c18b21bee9b.jpeg'
                 , headers=head)
# content返回的是二进制数据
with open('./1.jpg', 'wb')as fp:
    fp.write(result.content)