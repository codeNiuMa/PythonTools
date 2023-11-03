import requests as re
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
data = {'kw': 'rose'}
result = re.post('https://fanyi.baidu.com/langdetect', data=data, headers=head)
# json返回的是对象，确认响应是对象才能用
print(result.json())
