# coding:utf-8

"""
自动化操作：文献获取
自动操作Web of Science标记文献的程序；
"""

import re
import time
from selenium import webdriver as Webdriver
from lxml import etree
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
import requests


#----------- choose the mode ------------- #
"""
模式'1'：该模式范围从载入网页到添加到标记列表结束；
模式'2'：该模式范围从进入标记列表开始，假设前面已经进行过高级搜索和输入关键词并点击搜索按钮了。
"""
args_mode = '2'

# -------------------------------------
# ------------ set parameters -------------------
args_web_url=''
keyword=''
# -----------------------------------


def main(args_mode):
    switch = {
        '1': function_1(keyword),
        '2': function_2(web_url=args_web_url)
    }
    switch.get(args_mode)

    pass

# 获取输入关键词之后的网页


def function_1(keyword):
    # 获取输入关键词之后的网页
    browser = Webdriver.Chrome()  # 生成浏览器驱动对象
    try:
        # 获取并载入该网页
        browser.get('http://apps.webofknowledge.com/UA_GeneralSearch_input.do?product=UA&search_mode=GeneralSearch&SID=5Dhq97blVIXuMKqAKzl&preferencesSaved=')
        # 输入关键词并点击搜索按钮
        input_handle = browser.find_element_by_id('value(input1)')
        input_handle.send_keys(keyword)  # 输入关键词
        time.sleep(1)  # 等待
        button_handle = browser.find_element_by_class_name(
            'searchButton')  # 模拟点击的手柄
        button_handle.click()  # 模拟点击
        time.sleep(6)  # 等待
        # 选择每页显示50项
        web_url = browser.current_url  # 获取点击之后的网页网址
        button_handle = browser.find_element_by_class_name(
            'select2-selection__rendered')  # 下拉菜单：每页显示更多项
        button_handle.click()  # 模拟点击
        web_url = browser.current_url  # 获取点击之后的网页网址
        time.sleep(1)  # 等待

        # 模式匹配寻找每页显示50项的那个网页元素
        # 弃用以下注释部分
        # html=requests.get(web_url)
        # html.raise_for_status()
        # html.encoding = html.apparent_encoding  # 判断是否爬取成功
        # html_text=html.text
        # html_tree=etree.HTML(html_text)
        html = browser.find_element_by_xpath("//*").get_attribute("outerHTML")
        html_tree = etree.HTML(html)
        html_node = html_tree.xpath(
            "//ul[@class='select2-results__options']/li[text()=' 每页 50 条 ']")
        # pattern_words = r'(.+50)'
        # urlre = re.compile(pattern_words)
        # element_text = urlre.findall(html_tree)
        button_handle = browser.find_element_by_id(
            html_node[0].attrib['id'])  # 选择每页显示50项
        button_handle.click()  # 模拟点击
        time.sleep(3)  # 等待

        # 每页选择全部项目添加到标记结果列表然后翻页，直至最后一页。
        web_url = browser.current_url
        html_element = browser.find_element_by_id('pageCount.top')
        page_last = int(html_element.text)
        pages = range(1, page_last+1-1)
        for page in pages:
            button_handle = browser.find_element_by_name(
                'SelectPage')  # “选择页面”按钮
            button_handle.click()  # 模拟点击
            time.sleep(1)  # 等待
            button_handle = browser.find_element_by_class_name(
                'addToMarkedListButton')  # 添加到标记结果列表
            button_handle.click()  # 模拟点击
            time.sleep(1)  # 等待
            button_handle = browser.find_element_by_class_name(
                'paginationNext.snowplow-navigation-nextpage-bottom')  # 下一页
            button_handle.click()  # 模拟点击
            time.sleep(1)  # 等待
            web_url = browser.current_url  # 获取执行了下一页之后的网页网址
            pass
        button_handle = browser.find_element_by_name('SelectPage')  # “选择页面”按钮
        button_handle.click()  # 模拟点击
        time.sleep(1)  # 等待
        button_handle = browser.find_element_by_class_name(
            'addToMarkedListButton')  # 添加到标记结果列表
        button_handle.click()  # 模拟点击
        time.sleep(1)  # 等待
        web_url = browser.current_url  # 获取执行了下一页之后的网页网址

    finally:
        # browser.close()
        pass


def function_2(web_url):
    # 获取输入关键词之后的网页
    browser = Webdriver.Chrome()  # 生成浏览器驱动对象
    try:
        ## 假设前面已经进行过高级搜索和输入关键词并点击搜索按钮了。
        # 获取并载入该网页
        browser.get(web_url)
       
        # 选择每页显示50项
        web_url = browser.current_url  # 获取点击之后的网页网址
        button_handle = browser.find_element_by_class_name(
            'select2-selection__rendered')  # 下拉菜单：每页显示更多项
        button_handle.click()  # 模拟点击
        web_url = browser.current_url  # 获取点击之后的网页网址
        time.sleep(1)  # 等待

        # 模式匹配寻找每页显示50项的那个网页元素
        # 弃用以下注释部分
        # html=requests.get(web_url)
        # html.raise_for_status()
        # html.encoding = html.apparent_encoding  # 判断是否爬取成功
        # html_text=html.text
        # html_tree=etree.HTML(html_text)
        html = browser.find_element_by_xpath("//*").get_attribute("outerHTML")
        html_tree = etree.HTML(html)
        html_node = html_tree.xpath(
            "//ul[@class='select2-results__options']/li[text()=' 每页 50 条 ']")
        # pattern_words = r'(.+50)'
        # urlre = re.compile(pattern_words)
        # element_text = urlre.findall(html_tree)
        button_handle = browser.find_element_by_id(
            html_node[0].attrib['id'])  # 选择每页显示50项
        button_handle.click()  # 模拟点击
        time.sleep(3)  # 等待

        # 每页选择全部项目添加到标记结果列表然后翻页，直至最后一页。
        web_url = browser.current_url
        html_element = browser.find_element_by_id('pageCount.top')
        page_last = int(html_element.text)
        pages = range(1, page_last+1-1)
        for page in pages:
            button_handle = browser.find_element_by_name(
                'SelectPage')  # “选择页面”按钮
            button_handle.click()  # 模拟点击
            time.sleep(1)  # 等待
            button_handle = browser.find_element_by_class_name(
                'addToMarkedListButton')  # 添加到标记结果列表
            button_handle.click()  # 模拟点击
            time.sleep(1)  # 等待
            button_handle = browser.find_element_by_class_name(
                'paginationNext.snowplow-navigation-nextpage-bottom')  # 下一页
            button_handle.click()  # 模拟点击
            time.sleep(1)  # 等待
            web_url = browser.current_url  # 获取执行了下一页之后的网页网址
            pass
        button_handle = browser.find_element_by_name('SelectPage')  # “选择页面”按钮
        button_handle.click()  # 模拟点击
        time.sleep(1)  # 等待
        button_handle = browser.find_element_by_class_name(
            'addToMarkedListButton')  # 添加到标记结果列表
        button_handle.click()  # 模拟点击
        time.sleep(1)  # 等待
        web_url = browser.current_url  # 获取执行了下一页之后的网页网址

    finally:
        # browser.close()
        pass


if __name__ == '__main__':
    main()
