#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2


def load_url(url, file_name):
    print('开始爬取%s的内容' % file_name)
    # 爬取程序
    my_headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'

    }
    request = urllib2.Request(url, headers=my_headers)
    content = urllib2.urlopen(request).read()
    print('爬取%s的内容完成！' % file_name)
    return content


def save_date(data, file_name):
    '''
    作用：主要用于进行数据存储
    param data: 要存储的数据
    param file_name: 要存储的文件名称
    return: 无
    '''
    print('开始保存%s的内容' % file_name)

    with open(file_name, 'w') as f:
        f.write(data)
    print('保存%s的内容完成！' % file_name)


def spider(url, kw, begin, end):
    '''
    用于进行核心爬虫功能的调度
    :param url: 要爬取的地址
    :param kw: 贴吧名称
    :param begin: 起始页码
    :param end: 结束页码
    :return: 无
    '''
    for page in range(begin, end+1):
        pn = (page - 1) * 50
        kw = urllib.urlencode({'kw': kw})
        full_url = url + kw + '&pn=' + str(pn)
        file_name = '网页' + str(page) + '.html'
        html = load_url(full_url, file_name)
        save_date(html, file_name)


if __name__ == '__main__':
    url = 'http://tieba.baidu.com/f?'
    kw = raw_input('请输入要爬取的贴吧的名称：')
    begin = int(raw_input('请输入开始页码：'))
    end = int(raw_input('请输入结束页码：'))

    spider(url, kw, begin, end)
