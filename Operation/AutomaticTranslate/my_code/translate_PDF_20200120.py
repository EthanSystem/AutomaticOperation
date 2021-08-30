"""
自动化操作：热词操作。
根据指定的文件，搜索百度热词，获取相应信息，生成数据导出。
"""

# coding:utf-8

import importlib




import os
import sys
import numpy
import PyPDF2 as pypdf
from pdfminer import *
import os.path

importlib.reload(sys)

os.path.abspath(os.path.dirname(__file__))

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
import hashlib
import string

# import osax
# import appscript

from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage,PDFTextExtractionNotAllowed
from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams



#----------- choose the mode ------------- #
"""
模式'1'：该模式调用百度翻译接口翻译（有可能超过限制而面临收费的可能！）；
模式'2'：该模式通过自动化操作系统安装的欧路词典进行翻译（只适用于该系统的特定设置。）；
"""
args_mode = '1'

# -------------------------------------
# ------------ set parameters -------------------
args_web_url=''
isTranslate=True

## data path
# path_data_original=r'/Users/ethan/Documents/OneDrive - ElementsComplexSystem/CoreFiles/ReferencesFile/经济金融/系统性金融风险/金融风险传染/多层网络'
# path_project = os.path.dirname(os.getcwd())
path_project = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path_data_original = path_project + "/AutomaticTranslate/data/input"


## 之前我写的
# ## 导入pdf文件
# file_pdf_obj=open(path_data_original + r'/Molina-Borboa_2015_A multiplex network analysis of the Mexican banking system- link persistence, overlap and waiting times.pdf','rb')
## 提取的原始文本
# pdf_reader=pypdf.PdfFileReader(file_pdf_obj)
# pdf_reader.numPages
# obj_pdf_page=pdf_reader.getPage(0)
# obj_pdf_page.extractText()

## 获取的PDF名称
filename_data_original=r'PG.pdf'

## 百度翻译接口
filepath_api_url='/Users/ethan/Documents/CoreFiles/DocumentsFile/【个人资料】/被应用程序调用的账号密码文本文件/Baidu_FanYi_API_URL.txt';
filepath_api_id='/Users/ethan/Documents/CoreFiles/DocumentsFile/【个人资料】/被应用程序调用的账号密码文本文件/Baidu_FanYi_API_id.txt';
filepath_api_password='/Users/ethan/Documents/CoreFiles/DocumentsFile/【个人资料】/被应用程序调用的账号密码文本文件/Baidu_FanYi_API_password.txt';

api_url=open(filepath_api_url).read();
api_id=open(filepath_api_id).read();
api_password=open(filepath_api_password).read();

# -----------------------------------

file_En_texts = "EnTexts.txt" ##存储提取的txt
file_Cn_texts = "CnTexts.txt" ##存储翻译的结果




## 获取PDF文件
# def getDataUsingPyPDF(filename):
# 	file_pdf_obj=pdf
#     parser = PDFParser(open(pdffile,'rb')) #以二进制打开文件 ,并创建一个pdf文档分析器
#     doc = PDFDocument() ##创建一个pdf文档
#     #将文档对象和连接分析器连接起来
#     parser.set_document(doc)
#     doc.set_parser(parser)
#     doc.initialize()
# 	pass



## 使用PDFminer读取
def getDataUsingPyPDF(file_pdf_obj):
    ## 以二进制打开文件，并创建一个pdf文档分析器
    
    pdf_parser = PDFParser(file_pdf_obj)
    ## 创建一个pdf文档
    pdf_document = PDFDocument(pdf_parser)
    ## 将文档对象和连接分析器连接起来
    pdf_parser.set_document(pdf_document)
    # pdf_document.set_parser(pdf_parser)
    # pdf_document.initialize()
    

    ## 判断该pdf是否支持txt转换

    if pdf_document.is_extractable:
        ## 创建一个PDF资源管理器对象
        pdf_resource_manager = PDFResourceManager()
        # 创建一个pdf设备对象
        pdf_laparamas = LAParams()
        pdf_device = PDFPageAggregator(pdf_resource_manager, laparams=pdf_laparamas)
        ## 创建一个PDF解释器对象
        pdf_interpreter = PDFPageInterpreter(pdf_resource_manager, pdf_device)
        pdf_contents = "" #保存读取的text

      
        ## 依次读取每个page的内容
        for page in PDFPage.create_pages(pdf_document):
            pdf_interpreter.process_page(page)
            pdf_layout = pdf_device.get_result() ## 这里layout是一个LTPage对象 里面存放着这个page解析出的各种对象。
            # 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等 想要获取文本就获得对象的text属性，
            ## 在windows下，新文件的默认编码是gbk编码，所以我们在写入文件的时候需要设置一个编码格式，如下：
            for idx_pdf_layout in pdf_layout:
                if(isinstance(idx_pdf_layout,LTTextBoxHorizontal)):
                        pdf_results = idx_pdf_layout.get_text()
                        pdf_results = pdf_results.replace("\n","") ## 去掉换行符 因为排版问题 有的换行导致句子中断
                        pdf_contents += (pdf_results)
       ## 为了看着舒服，每一句为一行
        pdf_contents=pdf_contents.replace(".",".\n")
        saveText(pdf_contents,file_En_texts)
        return pdf_contents
    
    
## 将读取的content以txt格式存放到本地
def saveText(content,Textfile):
    path_data_output = path_project+r'/AutomaticTranslate/data/output/'+Textfile
    with open(path_data_output,"w",encoding='utf-8') as f:
        f.write(content)


## 翻译从pdf提取的content，通过百度翻译平台接口翻译。
def function_translate_1(content):
    salt = str(time.time())[:10]
    final_sign = str(api_id) + content + salt+ api_password
    final_sign = hashlib.md5(final_sign.encode("utf-8")).hexdigest()
    # from to  代表翻译的语言
    paramas = {
            'q':content,
            'from':'en',
            'to':'zh',
            'appid':'%s'%api_id,
            'salt':'%s'%salt,
            'sign':'%s'%final_sign
            }
    my_url = api_url+'?appid='+str(api_id)+'&q='+content+'&from='+'zh'+'&to='+'en'+'&salt='+salt+'&sign='+final_sign
    response = requests.get(api_url,params = paramas).content
    content = str(response,encoding = "utf-8")
    json_reads = json.loads(content)
    return json_reads['trans_result'][0]['dst']+" "
###

## 翻译从pdf提取的content，通过自动化操作本机的欧路词典的翻译功能翻译。
def function_translate_2():
    # TODO 函数：通过自动化操作本机的欧路词典的翻译功能翻译
    # iTunes = appscript.app("iTunes")
    # browserWindows = iTunes.browser_windows()
    # browserWindow = browserWindows[0]
    # playList = browserWindow.view()
    # track = playList.tracks[2]
    # print("Now playing the 2nd track:")
    # print("-") * 50
    # print("Name:"), track.name()
    # track.play()
    pass


## 主程序
def main(args_mode):
    # switch = {'1': function_translate_1(content), '2': function_translate_2()}
    # switch.get(args_mode)
    
    ## 
    ## 导入pdf文件
    filepath_data_original = os.path.join(path_data_original,filename_data_original)
    file_pdf_obj = open(filepath_data_original,'rb')
    
    content = getDataUsingPyPDF(file_pdf_obj)
    print("读取pdf成功，将其保存为txt格式")
    
    if (isTranslate):
        centences = content.split(".")  # split() 通过指定.将英文分成多个句子
        idx_centence = 0
        chinese_centences = ""
        print("一共有" + str(centences.__len__()) + "行需要翻译")
        print("开始翻译...请耐心等待")
        
        while (idx_centence < centences.__len__()):
            chinese_centences += (function_translate_1(centences[idx_centence]).replace("\n", "。"))
            # chinese += '\n'
            idx_centence += 1
            saveText(chinese_centences, file_Cn_texts)
            
            time.sleep(1.5) # 防止百度翻译平台返回调用频繁的错误，延迟1秒调用翻译。
            
            pass
        
        print("翻译结束，ok")
    
    pass


if __name__ == "__main__":
    main(args_mode)

