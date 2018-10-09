#!/usr/bin/env python3
# coding: utf-8

from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context()


url = "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query=223.104.210.104&co=&resource_id=6006"
response_data = request.urlopen(url).read().decode('utf-8')
print(response_data)
