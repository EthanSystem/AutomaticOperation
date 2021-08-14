# -*- coding: utf-8 -*-
import scrapy


class VoteSpider(scrapy.Spider):
    name = 'vote'
    allowed_domains = ['digitallibrary.un.org/search?ln=zh_CN&cc=Voting+Data&p=&f=&rm=&ln=zh_CN&sf=&so=d&rg=50&c=Voting+Data&c=&of=hb&fti=0&fct__2=General+Assembly&fct__9=Vote&fct__3=2013&fti=0&fct__2=General+Assembly&fct__9=Vote']
    start_urls = ['https://digitallibrary.un.org/search?ln=zh_CN&cc=Voting+Data&p=&f=&rm=&ln=zh_CN&sf=&so=d&rg=50&c=Voting+Data&c=&of=hb&fti=0&fct__2=General+Assembly&fct__9=Vote&fct__3=2013&fti=0&fct__2=General+Assembly&fct__9=Vote']

    def parse(self, response):
        pass
