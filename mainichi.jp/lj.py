"""
Copyright (c) 2018 GYqyy All rights reserved.
Url：http://www.gyqyy.com/
Url: http://www.vbvbv.com/
"""
# -*- coding: utf-8 -*-
# 用于在文章搜索页面获取文章url
# 可以在url内指定页码数和关键字

import scrapy

class NextSpiderSpider(scrapy.Spider):
    name = "lj"
    start_urls = [
"https://mainichi.jp/english/search?q=china&t=kiji&s=match&p=101"
]

    def parse(self, response):
        lj = response.css(".main-box a::attr(href)").extract()
        lj = '\',\''.join(lj)
        lj = '\'' + lj + '\''
        fileName = 'urls.txt' # 定义文件名
        lj = lj.encode()
        with open(fileName, "ab") as f: 
                f.write('\n'.encode())  # ‘\n’ 表示换行
                f.write(lj)
                f.close()
