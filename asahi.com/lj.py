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
    start_urls = ['http://sitesearch.asahi.com/ajwsitesearch/index.php?Keywords=sino&start=10']

    def parse(self, response):
        lj = response.css(".ListBlock a::attr(href)").extract()[:10]
        lj = '\',\''.join(lj)
        lj = '\'' + lj + '\''
        fileName = 'urls.txt' # 定义文件名
        lj = lj.encode()
        with open(fileName, "ab") as f: 
                f.write('\n'.encode())  # ‘\n’ 表示换行
                f.write(lj)
                f.close()
