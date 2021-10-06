"""
Copyright (c) 2018 vbvbv.com All rights reserved.
Url：http://www.svip.tech/
Url: http://www.vbvbv.com/
"""
# -*- coding: utf-8 -*-
# 在url列表放置获取的所有链接
# 每个网页获取正文.txt和json索引文件

import scrapy

class simpleUrl(scrapy.Spider):
    name = "wz"
    start_urls = [  #无需定义start_requests方法
        'http://www.asahi.com/ajw/articles/AJ201808190038.html'
    ]

    def parse(self, response):
        #title = response.css('title::text').extract_first()
        title = response.css(".ArticleTitle .Title h1 *::text").extract_first()
        body = response.css('.ArticleText *::text').extract()
        body = '\n'.join(body)
        body = title + "\n" + body
        body = body.encode()
        filename = '%s.txt' % title  #title使用一次
        syfilename = 'suoyin.txt'
        title = "\nnode\ntitle:" + title + "\n" #title加入换行和标签
        path = "\npath:" + response.url + "\n"
        author = "\nauthor:" + response.css(".EnArticleName::text").extract_first() + "\n"
        publicated_time = "\npublicated_time:" + response.css(".EnLastUpdated::text").extract_first() + "\n"
        sybody = title + path + author + publicated_time
        sybody = sybody.encode()
        with open(filename, 'wb') as f:
            f.write(body)
        with open(syfilename, 'ab') as f:
            f.write(sybody)	
        self.log('保存文件: %s' % filename)
