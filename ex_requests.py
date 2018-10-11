
import requests

url = 'https://www.baidu.com/'
url1 = 'http://httpbin.org/get'
url2 = 'http://httpbin.org/get?name=gemey&age=22'
data = {
    'name': 'Ryan',
    'age': 30
}

response = requests.get(url, params=data)
print (response.text)