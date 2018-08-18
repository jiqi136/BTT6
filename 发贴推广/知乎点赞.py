# -*- coding:utf-8
import requests  # 网页浏览
import re  # 正则式
import time  # 时间
import datetime  # 时间
import os  # 本地操作
import pymysql  # 数据库
import random  # 随机
from lxml import etree  # 网页分析
import shutil  # 移动复制文件目录
from lxml import html  # 网页分析
import win32api  # 操作本地文件
import win32clipboard as w# 提取剪切板内容
import win32con#提取剪切板内容
from selenium import webdriver  # 浏览的驱动
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui as pag
import pyautogui
from 发贴推广.知乎收短信 import 类一一公共库# 导入模块

class 类一一知乎点赞(类一一公共库):  # 调用 类的模具 self.模具一一数据库()
    def __init__(self):
        #self.模具一一换头部信息()

        self.模具一一重新激活浏览器窗口()
        #self.模具一一浏览器访问并注册知乎()




    def 模具一一提炼Cookie(self):
        Cookie文本='tgw_l7_route=170010e948f1b2a2d4c7f3737c85e98c; _zap=ce1305a8-7d69-4551-b0c9-3cdf5d6e0b0c; _xsrf=pSfp9xAJvbYsJp1oUeeJVgGwSSWRFG79; q_c1=b2869836ad1545b89e2ca2fe599291f3|1534096133000|1534096133000; d_c0="ABBnPv7jCw6PTvReDG2SZyvJkmkHe8nDvT4=|1534096133"; capsion_ticket="2|1:0|10:1534096136|14:capsion_ticket|44:Mzg1YjZlMGFlOWY4NGE5MmI3M2IxOTA3MzQ3NjdhMTc=|3531eddc76e8d7935cbda485229e69ab672d0ab931d9139acb5a96cd8d1059e0"; z_c0="2|1:0|10:1534096157|4:z_c0|92:Mi4xTGlzSUFBQUFBQUFBRUdjLV91TUxEaVlBQUFCZ0FsVk5IY0ZkWEFBWHFOTTc5V0M5M19NUFMtbHYyaG1YU044MmNn|2163e2d4319ea00dfbc6fd180ec62e5a883da34d05477a0cec2806e10e49d870"'

        cookies = {}
        for 每句 in Cookie文本.split(';'): # 转为列表cookies['tgw_l7_route']
            字典键, 值 = 每句.strip().split('=', 1)  # 1代表只分割一次
            cookies[字典键] = 值
        self.cookies =cookies
        self.cookies浏览操作= {'domain': '.www.zhihu.com',
                        'name': 'tgw_l7_route',
                        'value': 'ec452307db92a7f0fdb158e41da8e5d8',
                       '_zap':cookies['_zap'],
                       '_xsrf':cookies['_xsrf'],
                       'capsion_ticket': cookies['capsion_ticket'],
                       'd_c0':cookies['d_c0'],
                       'z_c0':cookies['z_c0'],
                        'q_c1':cookies['q_c1'],
                        'expiry': None,
                        'path': '/',
                        'httpOnly': False,
                        'secure': False}
        self.cookies = cookies

    def 模具一一浏览器访问并注册知乎(self):
        self.模具一一换头部信息()
        self.模具一一提炼Cookie()

        头部信息 = str(self.头部信息).replace("'User-Agent':", "user-agent=")  # 替换   , 1) 次数 1
        头部信息 = 头部信息.replace("{", "")  # 替换   , 1) 次数 1
        头部信息 = 头部信息.replace("}", "")  # 替换   , 1) 次数 1
        后缀 = 'user-agent=Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'

        options = webdriver.ChromeOptions()  # 设置中文

        # options = Options()

        options.add_argument('disable-infobars')  # 加启动配置 去除正在受到自动软件的控制
        print('头部信息:', 头部信息)
        print('后缀:', 后缀)
        options.add_argument(后缀)



        浏览器操作 = webdriver.Chrome(chrome_options=options)  # 打开chrome浏览器



        url = "https://www.zhihu.com"  # 注册页面  https://www.zhihu.com/signup?next=%2Fexplore
        浏览器操作.get(url)
        time.sleep(2)  # 等待
        主页cookies=浏览器操作.get_cookies()  # 打开主页后获取cookies
        print('登录前主页cookies',主页cookies)
        cookies浏览=主页cookies[0]


        浏览器操作.delete_all_cookies() # 删除第一次建立连接时的cookie

        time.sleep(100000)  # 等待

        for 键名 in self.cookies:

            cookies浏览操作 = {'domain': '.www.zhihu.com',
                           'name': 键名,
                           'value': self.cookies[键名],
                           'expiry':cookies浏览['expiry']+31536000,
                           'path': '/',
                           'httpOnly': False,
                           'secure': False}
            浏览器操作.add_cookie(cookie_dict=cookies浏览操作)


        # 浏览器操作.add_cookie(cookie_dict=self.cookies浏览操作)
        #浏览器操作.add_cookie(cookie_dict=cookies浏览)
        # 浏览器操作.add_cookie({'value': '61066e97b5b7b3b0daad1bff47134a22'})



        time.sleep(2)  # 等待
        主页cookies = 浏览器操作.get_cookies()  # 打开主页后获取cookies
        print('登录后主页cookies', 主页cookies)

        浏览器操作.refresh()  # 刷新当前页面

        time.sleep(20000)  # 等待


if __name__ == '__main__':
    类 = 类一一知乎点赞()




