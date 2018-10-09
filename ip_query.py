#!/usr/bin/env python
# coding: utf-8

import urllib2
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


url = "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query=223.104.210.104&co=&resource_id=6006"
response_data = urllib2.urlopen(url).read().decode('gbk')
print(response_data)
