# -*- coding: utf-8 -*-
import scrapy


class HrSpider(scrapy.Spider):
    name = 'Hr'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    def parse(self, response):
        tr_list=response.xpath("//table[@class='tablelist']/tr")[1:-1]
        for tr in tr_list:
            item={}
            item["title"]=tr.xpath("./td[1]/a/text()").extract_first()
            item["postion"]=tr.xpath("./td[2]/text()").extract_first()
            item["publish_date"]=tr.xpath("./td[5]/text()").extract_first()
            yield item
        #找到下一页的URL地址,实现翻页请求
        next_url=response.xpath("//a[@id='next']/@href").extract_first()
        if next_url !=" javascript:;":
            next_url="https://hr.tencent.com/"+next_url
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )