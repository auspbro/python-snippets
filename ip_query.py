#!/usr/bin/env python
# coding: utf-8

import urllib2
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


input_data = raw_input("请输入IP地址:")
url = "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query=" + input_data + "&co=&resource_id=6006"
response_data = urllib2.urlopen(url).read().decode('gbk')
# print(response_data)

print (json.loads(response_data)["data"][0]["location"])
