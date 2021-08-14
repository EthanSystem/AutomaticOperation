"""
自动化操作：热词操作。
根据指定的文件，搜索百度热词，获取相应信息，生成数据导出。
"""

# coding:utf-8
import urllib
# import re
# import threading
# from urllib import request
# from urllib import quote
# import HTMLParser
import openpyxl
import time
from selenium import webdriver as Webdriver
from lxml import etree
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
import requests
import json
import csv

# 导入Excel文档
file_path = r'/Users/ethan/Documents/OneDrive - ElementsComplexSystem/CoreFiles/ProjectsFile/Commissioned/LiJie/互联网金融测度.xlsx'
data_excel = openpyxl.load_workbook(file_path)
data_sheet = data_excel.get_sheet_by_name('十大热词')
data_sheet_2 = data_sheet['B2':'K11']

# 生成要写出的csv文件
file_output = open('data/output.csv', 'w', newline='')
csv_writer = csv.writer(file_output)


for i in range(len(data_sheet_2)):
# for i in range(2):
    keyword_list = []
    data_output_list = []
    for j in range(len(data_sheet_2[0])):
        keyword = data_sheet_2[i][j].internal_value
        keyword_list.append(keyword)
    pass
    keyword_list_str = ','.join(keyword_list)
    url = r'http://api.91cha.com/index?key=8b3e58b7383b4b5fb96a267504a031cf&kws='+keyword_list_str
    response = requests.get(url)
    data_result = json.loads(response.text)
    for k in range(len(data_result["data"])):
        data_output_list.append(data_result["data"][k]["allindex"])
    pass

    csv_writer.writerow(data_output_list)

pass

file_output.close()


## 别人家的
# wordList = set()
# wordsList = set()
# def strip_tags(html):
#     html = html.strip()
#     html = html.strip("\n")
#     result = []
#     parse = HTMLParser.HTMLParser()
#     parse.handle_data = result.append
#     parse.feed(html)
#     parse.close()
#     return "".join(result)

# def getBaiduTopWords():
#     url = "http://top.baidu.com/boards"
#     webcontent = urllib.urlopen(url).read()

#     idList = re.findall('href="\./buzz\?b=(\d+)?"',webcontent)
#     idSet = set(idList)
#     for i in range(10):
#         print "Thread %s Start..."%(i+1)
#         t = threading.Thread(target=doGetWords,args=(idSet,))
#         t.start()
#         t.join(1)

# def doGetWords(idSet):
#     while len(idSet) > 0:
#         print "idSet length ",len(idSet)
#         try:
#             uid = idSet.pop()
#             print "id = ",uid
#             url = 'http://top.baidu.com/buzz?b='+uid
#             webcontent = urllib.urlopen(url).read()
#             words = re.findall('<a class="list-title".*?">(.*?)</a>',webcontent)
#             print len(words),"words found."
#             wordList.update(words)
#         except Exception,e:
#             print e
#             #retry
#             idSet.add(uid)
#             continue

#     print "threading activeCount",threading.activeCount()
#     if threading.activeCount() == 2:
#         print len(wordList),"words found in total."
#         print wordList
#         print threading.enumerate()
#         for i in range(10):
#             print "Thread %s Start..."%(i+1)
#             t = threading.Thread(target=getWords,args=())
#             t.start()
#             t.join(1)

# def getWords():
#     while len(wordList) > 0:
#         try:
#             keyword = wordList.pop()
#             req = urllib2.Request("http://tool.chinaz.com/baidu/words.aspx")
#             req.add_header("User-Agent","Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; InfoPath.3)")
#             req.add_header("Referer","http://tool.chinaz.com/baidu/words.aspx")
#             data = "kw="+quote(keyword.decode("gbk").encode("utf8"))
#             print data
#             opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
#             response = opener.open(req, data)
#             html = response.read()
#             kw = re.findall('<td class="kw">(.*?)</td>',html)
#             kw = map(strip_tags,kw)
#             print len(kw)
#             if len(kw) == 0:
#                 wordsList.add(keyword)
#             else:
#                 wordsList.update(kw)
#         except:
#             wordList.add(keyword)

#     print "getWords threading activeCount",threading.activeCount()
#     f = open("words.inc", "w")
#     f.writelines(wordsList)
#     f.close()

# getBaiduTopWords()
