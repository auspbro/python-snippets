#!/usr/bin/env python
# coding: utf-8

import urllib2
import json
# 如果这个请求是https的，需要加上下面两句，意思是吧ssl认证关掉
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

input_data = raw_input("请输入IP地址:")
url = "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query=" + input_data + "&co=&resource_id=6006"

headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
    "Connection": "keep-alive",
    "Cookie": "BIDUPSID=4F4A0725B47B47515FA081EE2055CAEB; PSTM=1537069142; BDUSS=0FKLUNLUWRtallMdWRua0lqdGlEVjZHT3JHNy11WjQxMHNDWS1EdGVhR1lOdGhiQVFBQUFBJCQAAAAAAAAAAAEAAAANhpwvYXVzcGJybzgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJipsFuYqbBbd; BAIDUID=1728889E43FC52B8CB715D2D43CD1DFB:FG=1; MCITY=-%3A; H_PS_PSSID=1436_21098_22158; delPer=0; PSINO=1",
    "Host": "sp0.baidu.com",
    "Referer": "https://www.baidu.com/s?wd=ip%E5%9C%B0%E5%9D%80",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}

# 构建请求的对象
request_attr = urllib2.Request(url=url, headers=headers)
# 获得 response 并且进行转码
response_data = urllib2.urlopen(request_attr).read().decode('gbk')
# 如果不需要带着 headers 请求，我们可以直接使用 urlopen
# response_data = urllib2.urlopen(url=url).read().decode('gbk')
# print(response_data)

print (json.loads(response_data)["data"][0]["location"])
