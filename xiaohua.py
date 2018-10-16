
import re
import requests

'''
爬取校花网视频基础版
'''
response = requests.get('http://www.xiaohuar.com/v/')
# print(response.status_code)
# print(response.content)
# print(response.text)
urls = re.findall(r'class="items".*?href="(.*?)"', response.text, re.S) #re.S 把文本信息转换成1行匹配
# print(urls)
url = urls[2]
result = requests.get(url)
mp4_url = re.findall(r'id="media".*?src="(.*?)"', result.text, re.S)[0]

video = requests.get(mp4_url)

with open('./a.mp4', 'wb') as f:
    f.write(video.content)
