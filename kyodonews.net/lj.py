"""
Copyright (c) 2018 vbvbv.com All rights reserved.
Url：http://www.svip.tech/
Url: http://www.vbvbv.com/
"""
# -*- coding: utf-8 -*-
# 用于在文章搜索页面获取文章url
# 可以在url内指定页码数和关键字

import scrapy

class NextSpiderSpider(scrapy.Spider):
    name = "lj"
    start_urls = [
"https://english.kyodonews.net/search/post?phrase=beijing&page=1", 
"https://english.kyodonews.net/search/post?phrase=beijing&page=2", 
    ]

    def parse(self, response):
        lj = response.css("h3 a::attr(href)").extract()[:10]
        lj = '\",\"'.join(lj)
        lj = '\"' + lj + '\"'
        fileName = 'urls.txt' # 定义文件名,如：木心-语录.txt
        lj = lj.encode()
        with open(fileName, "ab") as f: 
                f.write('\n'.encode())  # ‘\n’ 表示换行
                f.write(lj)
                f.close()

        # 判断下一页是否存在，如果存在
        # 继续提交给parse执行，实现链接提交
        #以下内容对于爬虫无作用，可直接删去

        next_page = response.css(".Pagination a::attr(href)").extract()[-1] # css选择器提取下一页链接

        if next_page is not None:  # 判断是否存在下一页
            next_page = response.urljoin(next_page)
            """
             如果是相对路径，如：/page/1
             urljoin能转换为绝对路径，也就是加上域名
            """

            """
            scrapy提供方法：scrapy.Request()，使用了两个参数
            一个是：继续爬取的链接（next_page），这里是下一页链接，当然也可以是内容页
            另一个是：把链接提交给哪一个函数(callback=self.parse)爬取，这里是parse函数，也就是本函数
            当然，也可以在下面另写一个函数，比如：内容页，专门处理内容页的数据
            经过这么一个函数，下一页链接又提交给了parse，那就可以不断的爬取了，直到不存在下一页
            
            """
            yield scrapy.Request(next_page, callback=self.parse)
