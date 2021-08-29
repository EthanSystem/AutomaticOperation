
import time
from selenium import webdriver as Webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
import requests

# 获取网页主页面
web_url = 'http://apps.webofknowledge.com/UA_GeneralSearch_input.do?product=UA&search_mode=GeneralSearch&SID=5Dhq97blVIXuMKqAKzl&preferencesSaved='
# 输入关键词
keyword = 'financial risk contagion'


# 获取输入关键词之后的网页
def get_URL(web_url):
    browser = Webdriver.Chrome()  # 生成浏览器驱动对象

    try:

        browser.get(web_url)
        input_handle = browser.find_element_by_id('value(input1)')
        input_handle.send_keys(keyword)  # 输入关键词
        time.sleep(1)  # 休息一下
        button_handle = browser.find_element_by_class_name(
            'searchButton')  # 模拟点击的手柄
        button_handle.click()  # 模拟点击
        web_url = browser.current_url  # 获取点击之后的网页
        return web_url

    finally:
        # browser.close()
        pass

    pass


# 该函数用Requests库将网页爬取下来
def getHTMLText(url):
    # 爬取网页的通用代码框架
    try:
        # kv = {'user-agent': 'Chrome/81'}  # 该参数是设置用浏览器的形式访问网站
        request_1 = requests.get(
            url, timeout=60)    # 爬取网页生成response对象
        request_1.raise_for_status()
        request_1.encoding = request_1.apparent_encoding    # 判断是否爬取成功
        return request_1.text         # 返回爬虫的文本内容
    except:
        return ""
