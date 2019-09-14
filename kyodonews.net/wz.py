"""
Copyright (c) 2018 GYqyy All rights reserved.
Url：http://www.gyqyy.com/
Url: http://www.vbvbv.com/
"""
# -*- coding: utf-8 -*-
# 在url列表放置获取的所有链接
# 每个网页获取正文.txt和json索引文件

import scrapy

class simpleUrl(scrapy.Spider):
    name = "wz"
    start_urls = [  #无需定义start_requests方法
        "https://english.kyodonews.net/news/2018/10/61e207c57861-japan-eyes-allowing-skilled-blue-collar-workers-to-stay-permanently.html"
    ]

    def parse(self, response):
        #title = response.css('title::text').extract_first()
        title = response.css(".col-lg-8 .main h1 *::text").extract_first()
        body = response.css(".article-body p  *::text").extract()
        body = '\n'.join(body)
        body = title + "\n" + body
        body = body.encode()
        filename = '%s.txt' % title  #title使用一次
        syfilename = '%s.json' % title
        title = "{\"node\":\"\",\n\"title\":\"" + title + "\"," #title加入换行和标签
        path = "\n\"path\":\"" + response.url + "\",\n"
        author = "\"author\":\"" + response.css(".credit a::text").extract_first() + "\",\n"
        publicated_time = "\n\"publicated_time\":\"" + response.css(".credit::text").extract()[2] + "\"}"
        sybody = title + path + author + publicated_time
        sybody = sybody.encode()
        with open(filename, 'wb') as f:
            f.write(body)
        with open(syfilename, 'wb') as f:
            f.write(sybody)	
        self.log('保存文件: %s' % filename)
