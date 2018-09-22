# -*- coding:utf-8


import re  # 正则式
import time  # 时间
import requests  # 网页浏览
import os  # 本地操作
import pymysql  # 数据库
import random  # 随机

import shutil  # 移动复制文件目录

import win32api  # 操作本地文件
import win32clipboard as w# 提取剪切板内容
import win32con#提取剪切板内容

import pyautogui as pag #模拟鼠标键盘操作
import pyautogui#模拟鼠标键盘操作

import json #json格式化

"""
页面1  操作页面
页面2  导出COOKIE
页面3  设置浏览头部信息
页面4  清除 缓存
页面5  查询ip地址
//////////////////////////////////////
SELECT * FROM `知乎话题` WHERE `短标题` != '空' ORDER BY `知乎话题`.`赞同数` DESC 
SELECT * FROM `知乎话题` WHERE `短标题` != '空'and `类型`= '电影' ORDER BY `知乎话题`.`赞同数` DESC 
知乎改名2至8汉字 或16字符
提示保存密码 永不 **********
扩展快捷键  修改  


工具栏左1 导出COOKIE
工具栏2 设置浏览头部信息
删除微博的通知 权限**********

opera清除缓存SimpleClear




"""



class 类一一公共库:  # 调用 类的模具 self.模具一一数据库()
    def __init__(self):

        self.模具一一换头部信息()


    """============单程打开网页================"""

    def 模具一一换头部信息(self):  # 头部信息 def 函数模具内通行变量
        # nonlocal 头部信息  # def 函数模具内通行变量
        global 头部信息, 换IP时间计数  # def 函数模具内通行变量
        换IP时间计数 = int(time.time())
        # {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'}  被BT网站墙了
        随机3位数 = str(random.randrange(101, 1000))
        随机2位数 = str(random.randrange(11, 100))
        随机1位数 = str(random.randrange(6, 10))
        随机11位数 = str(random.randrange(1, 10))
        头部信息 = random.choice([{'User-Agent': 'Opera/随机2位数.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/随机2位数.11'},
                              {
                                  'User-Agent': 'Opera/随机2位数.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/随机2位数.8.{随机3位数 Version/随机2位数.11'},
                              {
                                  'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/随机3位数.5(KHTML,likeGecko)Chrome/随机2位数.0.1084.9Safari/536.5'},
                              {
                                  'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/随机3位数.5(KHTML,likeGecko)Chrome/随机2位数.0.1084.9Safari/536.5'},
                              {
                                  'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/随机3位数.24(KHTML,likeGecko)Chrome/随机2位数.0.1055.1Safari/535.24'},
                              {
                                  'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/随机3位数.24(KHTML,likeGecko)Chrome/随机2位数.0.1055.1Safari/535.24'},
                              {
                                  'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/随机3位数.24(KHTML,likeGecko)Chrome/随机2位数.0.1055.1Safari/535.24'},
                              {
                                  'User-Agent': 'Mozilla/5.0(X11;CrOSi6862268.111.0)AppleWebKit/随机3位数.11(KHTML,likeGecko)Chrome/随机2位数.0.1132.57Safari/536.11'},
                              {
                                  'User-Agent': 'Mozilla/5.0(X11;CrOSi6862268.111.0)AppleWebKit/随机3位数.11(KHTML,likeGecko)Chrome/随机2位数.0.1132.57Safari/536.11'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2;WOW64)AppleWebKit/随机3位数.1(KHTML,likeGecko)Chrome/随机2位数.77.34.5Safari/537.1'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2;WOW64)AppleWebKit/随机3位数.1(KHTML,likeGecko)Chrome/随机2位数.77.34.5Safari/537.1'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2;WOW64)AppleWebKit/随机3位数.24(KHTML,likeGecko)Chrome/随机2位数.0.1055.1Safari/535.24'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/随机3位数.6(KHTML,likeGecko)Chrome/随机2位数.0.1090.0Safari/536.6'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/随机3位数.6(KHTML,likeGecko)Chrome/随机2位数.0.1090.0Safari/536.6'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1062.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1062.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1061.1Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1061.1Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1061.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1061.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/随机3位数.1(KHTML,likeGecko)Chrome/随机2位数.0.1207.1Safari/537.1'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/随机3位数.1(KHTML,likeGecko)Chrome/随机2位数.0.1207.1Safari/537.1'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/随机3位数.6(KHTML,likeGecko)Chrome/随机2位数.0.1092.0Safari/536.6'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/随机3位数.6(KHTML,likeGecko)Chrome/随机2位数.0.1092.0Safari/536.6'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1063.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1063.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1062.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1062.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1061.1Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1061.1Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1061.1Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1061.1Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.0)AppleWebKit/随机3位数.5(KHTML,likeGecko)Chrome/随机2位数.0.1084.36Safari/536.5'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.0)AppleWebKit/随机3位数.5(KHTML,likeGecko)Chrome/随机2位数.0.1084.36Safari/536.5'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT5.1)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1063.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(Macintosh;IntelMacOSX10_8_0)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1063.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(Macintosh;IntelMacOSX10_8_0)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1063.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/随机3位数.50 (KHTML, like Gecko) Version/随机3位数.1 Safari/534.50'},
                              {
                                  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/201随机3位数01 Firefox/随机2位数.0.1'},
                              {
                                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50随机3位数; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:随机2位数.0) like Gecko'},
                              {
                                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:随机2位数.0) Gecko/201随机3位数01 Firefox/随机2位数.0'},
                              {
                                  'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/随机3位数.50 (KHTML, like Gecko) Version/随机3位数.1 Safari/534.50'},
                              {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 随机1位数.0; Windows NT 6.0; Trident/4.0)'},
                              {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 随机1位数.0; Windows NT 6.1)'},
                              {
                                  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/随机3位数.11 (KHTML, like Gecko) Chrome/随机2位数.0.963.56 Safari/535.11'},
                              {
                                  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/201随机3位数01 Firefox/随机2位数.0.1'},
                              {
                                  'User-Agent': 'Mozilla/5.0 (compatible; MSIE 随机1位数.0; Windows NT 5.1; Trident/随机2位数.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.随机2位数727; SE 2.X MetaSr 1.0)'},
                              {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 随机1位数.0; Windows NT 6.0; The World)'},
                              {
                                  'User-Agent': 'Mozilla/5.0 (compatible; MSIE 随机1位数.0; Windows NT 6.2; TencentTraveler 4.0)'},
                              {
                                  'User-Agent': 'Mozilla/5.0 (compatible; MSIE 随机1位数.0; Windows NT 6.1; Maxthon 2.0)'},
                              {
                                  'User-Agent': 'Mozilla/5.0 (compatible; MSIE 随机1位数.0; Windows NT 6.2; Avant Browser)'},
                              {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 随机1位数.0; Windows NT 6.0; 360SE)'},
                              {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 随机1位数.0; Windows NT 6.1)'},
                              {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 随机1位数.0; Windows NT 10.1)'}
                              ])
        头部信息['User-Agent'] = str(头部信息['User-Agent']).replace("随机1位数", 随机1位数)  # 替换   , 1) 次数 1
        头部信息['User-Agent'] = str(头部信息['User-Agent']).replace("随机11位数", 随机11位数)  # 替换   , 1) 次数 1
        头部信息['User-Agent'] = str(头部信息['User-Agent']).replace("随机2位数", 随机2位数)  # 替换   , 1) 次数 1
        头部信息['User-Agent'] = str(头部信息['User-Agent']).replace("随机3位数", 随机3位数)  # 替换   , 1) 次数 1
        self.头部信息=头部信息
        print(头部信息)

    def 模具一一知乎换头部信息(self):  # 头部信息 def 函数模具内通行变量
        # nonlocal 头部信息  # def 函数模具内通行变量
        global 头部信息, 换IP时间计数  # def 函数模具内通行变量
        换IP时间计数 = int(time.time())
        # {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'}  被BT网站墙了
        随机3位数 = str(random.randrange(101, 1000))
        随机2位数 = str(random.randrange(41, 100))
        随机1位数 = str(random.randrange(1, 10))
        随机11位数 = str(random.randrange(1, 10))
        头部信息 = random.choice([{'User-Agent': 'Opera/随机2位数.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/随机2位数.11'},
                              {
                                  'User-Agent': 'Opera/随机2位数.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/随机2位数.8.{随机3位数 Version/随机2位数.11'},
                              {
                                  'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/随机3位数.5(KHTML,likeGecko)Chrome/随机2位数.0.1084.9Safari/536.5'},
                              {
                                  'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/随机3位数.5(KHTML,likeGecko)Chrome/随机2位数.0.1084.9Safari/536.5'},
                              {
                                  'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/随机3位数.24(KHTML,likeGecko)Chrome/随机2位数.0.1055.1Safari/535.24'},
                              {
                                  'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/随机3位数.24(KHTML,likeGecko)Chrome/随机2位数.0.1055.1Safari/535.24'},
                              {
                                  'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/随机3位数.24(KHTML,likeGecko)Chrome/随机2位数.0.1055.1Safari/535.24'},
                              {
                                  'User-Agent': 'Mozilla/5.0(X11;CrOSi6862268.111.0)AppleWebKit/随机3位数.11(KHTML,likeGecko)Chrome/随机2位数.0.1132.57Safari/536.11'},
                              {
                                  'User-Agent': 'Mozilla/5.0(X11;CrOSi6862268.111.0)AppleWebKit/随机3位数.11(KHTML,likeGecko)Chrome/随机2位数.0.1132.57Safari/536.11'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2;WOW64)AppleWebKit/随机3位数.1(KHTML,likeGecko)Chrome/随机2位数.77.34.5Safari/537.1'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2;WOW64)AppleWebKit/随机3位数.1(KHTML,likeGecko)Chrome/随机2位数.77.34.5Safari/537.1'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2;WOW64)AppleWebKit/随机3位数.24(KHTML,likeGecko)Chrome/随机2位数.0.1055.1Safari/535.24'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/随机3位数.6(KHTML,likeGecko)Chrome/随机2位数.0.1090.0Safari/536.6'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/随机3位数.6(KHTML,likeGecko)Chrome/随机2位数.0.1090.0Safari/536.6'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1062.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1062.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1061.1Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1061.1Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1061.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1061.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/随机3位数.1(KHTML,likeGecko)Chrome/随机2位数.0.1207.1Safari/537.1'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/随机3位数.1(KHTML,likeGecko)Chrome/随机2位数.0.1207.1Safari/537.1'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/随机3位数.6(KHTML,likeGecko)Chrome/随机2位数.0.1092.0Safari/536.6'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/随机3位数.6(KHTML,likeGecko)Chrome/随机2位数.0.1092.0Safari/536.6'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1063.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1063.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1062.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1062.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1061.1Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1061.1Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1061.1Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1061.1Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.0)AppleWebKit/随机3位数.5(KHTML,likeGecko)Chrome/随机2位数.0.1084.36Safari/536.5'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.0)AppleWebKit/随机3位数.5(KHTML,likeGecko)Chrome/随机2位数.0.1084.36Safari/536.5'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT5.1)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1063.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(Macintosh;IntelMacOSX10_8_0)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1063.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(Macintosh;IntelMacOSX10_8_0)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1063.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/随机3位数.50 (KHTML, like Gecko) Version/随机3位数.1 Safari/534.50'},
                              {
                                  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/201随机3位数01 Firefox/随机2位数.0.1'},
                              {
                                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50随机3位数; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:随机2位数.0) like Gecko'},
                              {
                                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:随机2位数.0) Gecko/201随机3位数01 Firefox/随机2位数.0'},
                              {
                                  'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/随机3位数.50 (KHTML, like Gecko) Version/随机3位数.1 Safari/534.50'},

                              {
                                  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/随机3位数.11 (KHTML, like Gecko) Chrome/随机2位数.0.963.56 Safari/535.11'},
                              {
                                  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/201随机3位数01 Firefox/随机2位数.0.1'}

                              ])
        头部信息['User-Agent'] = str(头部信息['User-Agent']).replace("随机1位数", 随机1位数)  # 替换   , 1) 次数 1
        头部信息['User-Agent'] = str(头部信息['User-Agent']).replace("随机11位数", 随机11位数)  # 替换   , 1) 次数 1
        头部信息['User-Agent'] = str(头部信息['User-Agent']).replace("随机2位数", 随机2位数)  # 替换   , 1) 次数 1
        头部信息['User-Agent'] = str(头部信息['User-Agent']).replace("随机3位数", 随机3位数)  # 替换   , 1) 次数 1
        self.头部信息=头部信息
        print(头部信息)

    def 模具一一打开的网址请求返回网页内容(self,网址):  # self.返回网页内容
        # global 换IP时间计数  # 时间计数全局变量声明
        循环 = 0
        次数循环 = 0
        缓冲时间 = 0
        while 循环 == 0:  # 条件循环  post

            try:
                此时数2 = int(time.time())
                if 缓冲时间 > 此时数2:
                    time.sleep(0.5)
                    print('缓冲时间 多加 0.5秒')
                返回网页内容 = requests.post(网址, headers=头部信息, timeout=10)
                缓冲时间 = int(time.time()) + 0.5
            except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout,
                    requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout,
                    requests.exceptions.ChunkedEncodingError, requests.exceptions.InvalidSchema) as 异常:
                次数循环 += 1
                print('网络异常等待', 异常)
                print('倒数9秒再连接', 次数循环, '次')
                # time.sleep(3)
                if 'None, 10053,' in str(异常):
                    self.模具一一换头部信息()
            else:
                if '200' in str(返回网页内容):
                    返回网页内容.encoding = "UTF-8"  # 转换encoding='UTF-8' "gbk"
                    return  返回网页内容 # 返回
                else:
                    print('网站网络异常,状态码:', 返回网页内容)
                    print('等待10秒')
                    time.sleep(10)

    def 模具一一换ip连接(self):
        # coding:gbk
        print('宽带连接进行时.....')
        os.system(r"rasphone -h 宽带连接")  # xxx0是你的拨号名称,xp下默认是"宽带连接”.
        os.system(r"rasdial 宽带连接 02007044432@163.gd  77341859")  # xxx0同上,xxx1 拨号用户名 ,xxx2拨号密码.
        time.sleep(3)
        print('换ip再连接完成')
        # ============内容页过滤与提取===================================================
    def 模具一一换ip连接二(self):
        # coding:gbk
        循环 = 0
        次数循环 = 0

        while 循环 == 0:  # 条件循环  post
            print('宽带连接进行时.....')
            os.system(r"rasphone -h 宽带连接")  # xxx0是你的拨号名称,xp下默认是"宽带连接”.
            os.system(r"rasdial 宽带连接 02007044432@163.gd  77341859")  # xxx0同上,xxx1 拨号用户名 ,xxx2拨号密码.
            time.sleep(3)
            print('换ip再连接完成')

            try:
                返回网页内容 = requests.post('https://www.baidu.com/', headers=头部信息, timeout=3)
            except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout,
                    requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout,
                    requests.exceptions.ChunkedEncodingError, requests.exceptions.InvalidSchema) as 异常:
                次数循环 += 1
                print('网络异常等待', 异常)
                print('倒数60秒再连接', 次数循环, '次')
                time.sleep(60)
                if 'None, 10053,' in str(异常):
                    pass
            else:
                if '200' in str(返回网页内容):

                    break  # 结束循环
                else:
                    print('网站网络异常,状态码:', 返回网页内容)
                    print('等待60秒')
                    time.sleep(60)





    """============短信平台================"""
    def 模具一一提取影视剧数据库里的易码短信平台账户信息(self):
        # 提取数据库里的过滤网址
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "", "帐号", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句
        sql = "SELECT `登录cookie` FROM `3e影视网站` WHERE `网站`='易码短信平台账户信息' "
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        cookie组列表= cursor.fetchall()
        cookie组=cookie组列表[0]
        # self.cookie=cookie组[0]
        self.通信令牌token=cookie组[0]

        # 关闭数据库连接
        db.close()

    def 模具一一易码短信平台账户信息(self):

        # 通信令牌token =self.cookie

        令牌网址 = 'http://api.fxhyd.cn/UserInterface.aspx?action=getaccountinfo&token={}'.format(self.通信令牌token)  # 不换行 end=""

        网址内容 = self.模具一一打开的网址请求返回网页内容(令牌网址)
        账户信息 = 网址内容.text.replace("success|", "")  # 替换   , 1) 次数 1
        文本列表 = 账户信息.split("|")
        print('用户名:', 文本列表[0])
        print('账户状态:', 文本列表[1])
        print('账户等级:', 文本列表[2])
        print('账户余额:', 文本列表[3])
        print('冻结金额:', 文本列表[4])
        print('账户折扣:', 文本列表[5])
        print('获取号码最大数量:', 文本列表[6])
        print('=========================')

    def 模具一一获取接收的手机号码(self):
        # 通信令牌token = self.cookie
        self.项目编号 = "891"
        排除号段 = ''
        获取手机号码接口网址 = "http://api.fxhyd.cn/UserInterface.aspx?action=getmobile&token={}&itemid={}&excludeno={}".format(
            self.通信令牌token, self.项目编号, 排除号段)
        网址内容 = self.模具一一打开的网址请求返回网页内容(获取手机号码接口网址)

        self.手机号码 = 网址内容.text.replace("success|", "")  # 替换   , 1) 次数 1
        print('手机号码:', self.手机号码)

    def 模具一一获取短信(self):

        #pag.hotkey('altleft', 'tab')  # press()一次完整的击键.hotkey('ctrl','c'):热键函数 .keyDown()按下某个键.keyUp()松开某个键.

        #通信令牌token = self.cookie
        self.项目编号 = "891"

        获取短信网址 = "http://api.fxhyd.cn/UserInterface.aspx?action=getsms&token={}&itemid={}&mobile={}".format(
            self.通信令牌token,
            self.项目编号, self.手机号码)
        """&release=1  自动释放号码标识符 若该参数值为1时,获取到短信的同时系统将自己释放该手机号码.若要继续使用该号码,请勿带入该参数."""


        条件循环 =0
        while 条件循环 < 3:  # 条件循环  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            self.短信内容 = ''

            for i in 'few52676t':
                print('等待 15秒:')
                time.sleep(14)  # 等待
                网址内容 = self.模具一一打开的网址请求返回网页内容(获取短信网址)
                if 'success' in 网址内容.text:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                    self.短信内容 = 网址内容.text.replace("success|", "")  # 替换   , 1) 次数 1
                    print('短信内容:', self.短信内容)
                    条件循环 = 998

                    return#返回
                elif '3001' in 网址内容.text:  # 其它条件.
                    print('短信尚未到达:3001,应继续调用取短信接口,直到超时为止.')

                else:  # 否则
                    print('请求失败:', 网址内容.text)
            条件循环 =条件循环+1
            self.模具一一重新激活浏览器窗口()
            pag.PAUSE = 5  # 增加延迟
            pag.moveTo(740, 456)  # 鼠标移动X.Y 方位  发送验证码 按钮
            pag.rightClick()  # 右击pag.rightClick()
            self.开始计时数 = int(time.time())



        释放手机号码接口 = "http://api.fxhyd.cn/UserInterface.aspx?action=release&token={}&itemid={}&mobile={}".format(
            self.通信令牌token, self.项目编号, self.手机号码)
        释放手机号码网址内容 = self.模具一一打开的网址请求返回网页内容(释放手机号码接口)

    """===========共用库================"""

    def 模具一一启动浏览器Chrome68(self):
        win32api.ShellExecute(0, 'open', r'E:\Ean\Google Chrome68\Chrome.exe', '', '', 1)  # 主页已经设置为 注册知乎页

        time.sleep(8)



    def 模具一一随机取女名(self):
        def 模具一一随机取名个位数(内容):
            合名 = ''
            随机取名个位数 = int(random.choice('55667'))
            for 字符 in range(1, 随机取名个位数):  # 范围 range
                名 = random.choice(内容)
                合名 = 合名 + 名
            return 合名  # 返回
        内容 = """柔蓉安蓝春语彤晴语菱霜紫莲翠烟南寻慕蕊雪海沛宛晓菡巧
        听卉靖枫梓晨丽丹佩惠月玉婉晓玲倩瑞静颖棋芹萍幻露灵含雅薇瑶丹丽云亿仪伊伶佳依俞俪倩偲兰冰凝凡凤叆呤
        爱姿惠娇媛妩萱娈瑷悠源赫晗贻楚梦琪忆柳桃慕兰岚香沛菡珊曼菱寒薇忆旋芷蕾代
        芙盼蝶筠瑶珍谷荷画嘉囡女如妃妍妙妮妹姐姑姗姝姞姣梅梦楠檀欢欣歆毓水洁涵淑清滟滢漪漫澜灵煜燕
        玉玥玫环玲珂珊珍珠姬娅娆娇娉娜娟娣娥娴婉婕婧婵婷媚媛嫔嫣嫱安宛宜宝容巧希彤彩心忆念怀怜思怡情惠
        慧敏旭春晴曼月琦琪琬琰琳琴琼瑗瑛瑜瑶瑾璇璐璟白盈盼碧秀筠红绮美翠艳芃芊芝芬芮芯芳芷芸苑若苹茗茜茵茹荔荭
        荷莉莎莲莹菁菡菲萍萱蓉蓓蔓蕊蕾薇诗语贞采钰银雅雨雪雯霏霖霜霞露青靖静音韵颖颜香馨黛"""

        内容 = 内容.replace("\n", "")
        内容 = 内容.replace(" ", "")
        合名 = ''

        for 字符 in self.用户名:  # 范围 range
            if '\u4e00' <= 字符 <= '\u9fff':
                合名 = 合名+字符
        if len(合名)>3:
            名 = random.choice(内容)
            合名 = 合名 + 名
            名 = random.choice(内容)
            合名 = 合名 + 名
            名 = random.choice(内容)
            合名 = 合名 + 名
        名 = random.choice(内容)
        合名 = 合名 + 名
        print('随机取女名', 合名)
        return 合名# 返回

    def 模具一一随机取名合并网址名(self):
        内容 = """柔蓉安蓝春语彤晴语菱霜紫莲翠烟南寻慕蕊雪海沛宛晓菡巧
                听卉靖枫梓晨丽丹佩惠月玉婉晓玲倩瑞静颖棋芹萍幻露灵含雅薇瑶丹丽云亿仪伊伶佳依俞俪倩偲兰冰凝凡凤叆呤
                爱姿惠娇媛妩萱娈瑷悠源赫晗贻楚梦琪忆柳桃慕兰岚香沛菡珊曼菱寒薇忆旋芷蕾代
                芙盼蝶筠瑶珍谷荷画嘉囡女如妃妍妙妮妹姐姑姗姝姞姣梅梦楠檀欢欣歆毓水洁涵淑清滟滢漪漫澜灵煜燕
                玉玥玫环玲珂珊珍珠姬娅娆娇娉娜娟娣娥娴婉婕婧婵婷媚媛嫔嫣嫱安宛宜宝容巧希彤彩心忆念怀怜思怡情惠
                慧敏旭春晴曼月琦琪琬琰琳琴琼瑗瑛瑜瑶瑾璇璐璟白盈盼碧秀筠红绮美翠艳芃芊芝芬芮芯芳芷芸苑若苹茗茜茵茹荔荭
                荷莉莎莲莹菁菡菲萍萱蓉蓓蔓蕊蕾薇诗语贞采钰银雅雨雪雯霏霖霜霞露青靖静音韵颖颜香馨黛"""

        内容 = 内容.replace("\n", "")
        内容 = 内容.replace(" ", "")

        名 = random.choice(内容)
        电影美剧表=['电影','美剧']
        电影美剧名 = random.choice(电影美剧表)
        合名 =名+电影美剧名+'3e38丶com'

        print('随机取名合并网址名', 合名)
        return 合名  # 返回





    def 模具一一随机职业名(self):

        if self.知乎发贴号 == 0:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            职业列表 = ['作者', '作家', '资料登录员', '壮工', '主管', '主编', '钟表匠', '置景工', '职员', '执行官',
                    '园丁', '宇航员', '渔夫', '油漆匠', '邮政工人', '银行经理', '银行出纳员', '医生', '业务经理', '药剂师', '演员',
                    '学生', '心理学者', '鞋店鞋匠', '小学生', '消防人员', '洗碗机', '舞蹈演员', '维修工程师', '外科医生', '土木工程师',
                    '屠宰商', '小贩', '统计员', '速记打字员', '私人司机', '司仪', '司机', '水手长', '水手', '水管工人', '兽医', '售货员', '收票员', '摄影师',
                    '摄影记者', '上班一族', '仆人', '女演员', '女侍者', '服务生', '女仆', '内科医师助理', '内科医师', '奶妈', '牧羊人', '牧师', '木匠',
                    '模特儿', '面包师', '秘书', '美容师', '律师', '旅行团的服务员', '旅行社', '临时照顾幼儿者', '理发师', '老师', '垃圾清洁工', '矿工',
                    '客机服务员', '科学家', '看管者', '卡车司机', '酒店业主', '酒吧招待', '酒吧侍者', '精神病医师', '节目主持人', '接待员', '教授', '技师', '记者',
                    '计划员', '计程车司机', '机械工', '机车司机', '会计', '换工住宿的女孩', '护士', '航海家', '行政助理', '行李管理者', '焊接工', '海员', '雇员',
                    '顾问', '公交司机', '工程师', '歌手', '副驾驶员', '服务员', '飞行员', '房地产经纪人', '翻译者', '发型师', '发报员', '儿科医师', '店员',
                    '电影制片人', '电台的音乐节目主持人', '电工', '导演', '导师', '档案管理者', '大厨', '打扫房屋者', '船长', '厨师', '出租车司机',
                    '产科医师', '叉式升降机操作员', '测量技师', '餐厅侍者助手', '餐馆老板', '裁缝师', '宝石商']
            职业名 = random.choice(职业列表)
        else:  # 否则
            职业名  = r"电影美剧→→: http://3e38.com"


        print('职业名', 职业名)

        return 职业名  # 返回



    def 模具一一获取剪切板内容(self):# 获取剪切板内容
        w.OpenClipboard()
        t = w.GetClipboardData(win32con.CF_TEXT)
        w.CloseClipboard()

        t = t.decode('gbk')  # 解码为 编程的中文

        return t


    def 模具一一写入剪切板内容(self,内容): # 写入剪切板内容
        内容 = str(内容).encode('gbk')  # encoding='UTF-8'为 WIN7 系统 的中文
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_TEXT, 内容)
        w.CloseClipboard()
    def 模具一一写入剪切板内容不变编码(self,内容): # 写入剪切板内容
        # 内容 = str(内容)  # encoding='UTF-8'为 WIN7 系统 的中文
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_TEXT, 内容)
        w.CloseClipboard()


    def 模具一一测试页面属性一等待(self,页面关键词):
        time.sleep(3)  # 等待

        for i in '123365854':
            time.sleep(0.5)  # 等待  # 增加延迟
            pag.hotkey('ctrlleft', 'a')  # press()一次完整的击键.hotkey('ctrl','c'):复制内容

            time.sleep(1)  # 等待  # 增加延迟

            pag.hotkey('ctrlleft', 'c')  # press()一次完整的击键.hotkey('ctrl','c'):复制内容
            time.sleep(1)  # 等待  # 增加延迟

            页面属性 = self.模具一一获取剪切板内容()
            if 页面关键词 in 页面属性:
                print('通过', 页面关键词, '页面')
                return  # 返回
            else:  # 否则
                time.sleep(10)  # 等待


    def 模具一一测试页面属性(self,页面关键词):
        time.sleep(3)  # 等待

        for i in '123':
            time.sleep(0.5)  # 等待  # 增加延迟
            pag.hotkey('ctrlleft', 'a')  # press()一次完整的击键.hotkey('ctrl','c'):复制内容

            time.sleep(1) # 等待  # 增加延迟

            pag.hotkey('ctrlleft', 'c')  # press()一次完整的击键.hotkey('ctrl','c'):复制内容
            time.sleep(1)  # 等待  # 增加延迟

            页面属性 = self.模具一一获取剪切板内容()
            if 页面关键词 in 页面属性:
                print('通过', 页面关键词, '页面')
                页面属性=''
                return  # 返回
            else:  # 否则
                time.sleep(10)  # 等待

        pag.hotkey('ctrlleft', 'r')  # 刷新页面
        time.sleep(2) # 增加延迟
        # pag.moveTo(77, 46)  # 鼠标移动X.Y 方位  刷新页面
        # pag.rightClick()  # 右击pag.rightClick()

        self.模具一一测试页面属性(页面关键词)

    """============浏览器操作================"""
    def 模具一一地址栏输入网址(self,输入的网址):
        # =========== 定位 地址栏 ============
        pag.hotkey('ctrlleft', '1')  # 鼠标移动X.Y 方位  浏览器 主 页面
        time.sleep(1)  # 等待  # 增加延迟

        pag.moveTo(981, 52)  # 鼠标移动 定位  页面 空白处
        time.sleep(0.5)  # 等待  # 增加延迟

        pag.hotkey('ctrlleft', 'e')  # 鼠标移动X.Y 方位  定位 地址栏
        time.sleep(1)  # 等待  # 增加延迟
        pag.press('delete')  # press()一次完整的击键. 清空 地址栏
        time.sleep(1)  # 等待  # 增加延迟
        #===========输入网址============
        self.模具一一写入剪切板内容(输入的网址)
        time.sleep(0.5)  # 等待  # 增加延迟
        pag.hotkey('ctrlleft', 'shiftleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c')


        #pag.press('enter')  # press()一次完整的击键.hotkey('ctrl','c')

        time.sleep(5)  # 等待  # 增加延迟

    def 模具一一布置浏览头(self,浏览头网址):
        pag.hotkey('ctrlleft', '1')  # 鼠标移动X.Y 方位  浏览器 主 页面


        time.sleep(1)  # 等待  # 增加延迟
        pag.hotkey('altleft', '2')  # 鼠标移动X.Y 方位  cookie插件布置 页面
        # pag.moveTo(1252 , 49)  # 鼠标移动 定位  确定布置浏览头 按钮
        # pag.rightClick()  # 右击
        time.sleep(1)  # 等待  # 增加延迟

        # pag.moveTo(1009, 93)  # 鼠标移动 定位  布置浏览头 空白处
        # pag.rightClick()  # 右击
        # time.sleep(1)  # 等待  # 增加延迟


        # ==============================
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c') 添加浏览头网址 方框


        self.模具一一写入剪切板内容(浏览头网址)
        time.sleep(0.3)  # 等待  # 增加延迟
        pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.5)  # 等待  # 增加延迟

        # ====================================
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')
        self.模具一一知乎换头部信息()

        self.模具一一写入剪切板内容(self.头部信息['User-Agent'])
        time.sleep(0.3)  # 等待  # 增加延迟
        pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.5)  # 等待  # 增加延迟

        # ====================================
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')  定位  add添加 按钮

        time.sleep(0.5)  # 等待  # 增加延迟
        pag.press('enter')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.5)  # 等待  # 增加延迟

        pag.moveTo(981, 52)  # 鼠标移动 定位  页面 空白处
        time.sleep(0.5)  # 等待  # 增加延迟



    def 模具一一新界面布置浏览头(self):

        pag.hotkey('ctrlleft', '3')  # 鼠标移动X.Y 方位  cookie插件布置 页面

        time.sleep(1)  # 等待  # 增加延迟
        pag.moveTo(600, 200)  # 鼠标移动X.Y 方位  确定布置浏览头 页面
        pag.rightClick()  # 右击
        time.sleep(0.5)  # 等待  # 增加延迟

        # pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')
        # pag.PAUSE = 0.3  # 增加延迟
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.5)  # 等待  # 增加延迟
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c') 添加浏览头网址 方框

        浏览头网址 = 'zhihu.com'
        self.模具一一写入剪切板内容(浏览头网址)
        time.sleep(0.3)  # 等待  # 增加延迟
        pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.5)  # 等待  # 增加延迟

        # ====================================
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')
        self.模具一一换头部信息()

        self.模具一一写入剪切板内容(self.头部信息['User-Agent'])
        time.sleep(0.3)  # 等待  # 增加延迟
        pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.5)  # 等待  # 增加延迟

        # ====================================
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')

        time.sleep(0.5)  # 等待  # 增加延迟
        pag.press('enter')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(1)  # 等待  # 增加延迟

        # pag.hotkey('ctrlleft', 'F4')  # 确认  关闭当前标签页   按钮

    def 模具一一提取浏览器地址栏网址(self):

        # =========== 定位 地址栏 ============
        pag.hotkey('ctrlleft', '1')  # 鼠标移动X.Y 方位  浏览器 主 页面
        time.sleep(0.5)  # 等待  # 增加延迟
        pag.hotkey('ctrlleft', 'e')  # 鼠标移动X.Y 方位  定位 地址栏
        time.sleep(0.5)  # 等待  # 增加延迟

        # ===========提取网址============

        time.sleep(0.3)  # 等待  # 增加延迟
        pag.hotkey('ctrlleft', 'c')  # press()一次完整的击键.hotkey('ctrl','c')

        time.sleep(0.5)  # 等待  # 增加延迟
        提取网址 = self.模具一一获取剪切板内容()
        time.sleep(0.5)  # 等待  # 增加延迟
        return  提取网址# 返回值

    def 模具一一提取登录界面的cookie(self):
        cookie=''
        time.sleep(0.5)  # 等待  # 增加延迟
        pag.hotkey('altleft', '2')  # 鼠标移动X.Y 方位  cookie插件布置 页面
        #pag.moveTo(1222, 50)  # 鼠标移动X.Y 方位  cookie图标 按钮

        #pag.rightClick()  # 右击
        time.sleep(4)  # 等待  # 增加延迟




        pag.moveTo(1043, 89)  # 鼠标移动X.Y 方位  导出到剪切板 按钮
        pag.rightClick()  # 右击

        time.sleep(2)  # 等待  # 增加延迟
        self.cookie =self.模具一一获取剪切板内容()

        self.cookie = json.dumps(self.cookie,indent =4)  # 编码为json

        print('cookie\n',self.cookie)
        time.sleep(0.5)  # 等待  # 增加延迟

        # time.sleep(0.5)  # 等待  # 增加延迟
        # pag.moveTo(418, 120)  # 鼠标移动X.Y 方位  清除全部cookie    按钮
        # pag.rightClick()  # 右击

    def 模具一一新界面提取登录界面的cookie(self):
        cookie=''
        time.sleep(1)  # 等待  # 增加延迟

        pag.hotkey('ctrlleft', '2')  # 鼠标移动X.Y 方位  cookie插件布置 页面
        time.sleep(2)  # 等待  # 增加延迟
        if self.清除全部 == 0:


            pag.moveTo(736, 113)  # 鼠标移动X.Y 方位  导出到剪切板 按钮
            pag.rightClick()  # 右击

            time.sleep(2)  # 等待  # 增加延迟
            self.cookie =self.模具一一获取剪切板内容()

            self.cookie = json.dumps(self.cookie,indent =4)  # 编码为json


            print('cookie\n',self.cookie)

        time.sleep(0.5)  # 等待  # 增加延迟
        pag.moveTo(418, 120)  # 鼠标移动X.Y 方位  清除全部cookie    按钮
        # pag.rightClick()  # 右击

    def 模具一一导入界面的登录cookie(self,帐号):

        print('导入帐号：',帐号)

        # pag.moveTo(1222, 50)  # 鼠标移动X.Y 方位  cookie图标 按钮
        # pag.rightClick()  # 右击
        pag.hotkey('altleft', '2')  # 鼠标移动X.Y 方位  cookie插件布置 页面
        time.sleep(4)  # 等待  # 增加延迟


        pag.moveTo(943, 90)  # 鼠标移动X.Y 方位  导入 按钮
        pag.rightClick()  # 右击

        time.sleep(2)  # 等待  # 增加延迟
        pag.moveTo(921, 166)  # 鼠标移动X.Y 定位  输入框
        pag.rightClick()  # 右击

        self.模具一一写入剪切板内容(self.cookie)

        pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c')

        time.sleep(0.5)  # 等待  # 增加延迟
        pag.moveTo(960, 659)  # 鼠标移动X.Y 方位  绿色勾选 按钮
        pag.rightClick()  # 右击
        time.sleep(1)  # 等待  # 增加延迟

        # pag.hotkey('ctrlleft', 'F4')  # 确认  关闭当前标签页   按钮

    def 模具一一新界面导入界面的登录cookie(self):

        pag.hotkey('ctrlleft', '2')  # 鼠标移动X.Y 方位  cookie插件布置 页面

        time.sleep(1)  # 等待  # 增加延迟
        pag.moveTo(652, 120)  # 鼠标移动X.Y 方位  导入 按钮
        pag.rightClick()  # 右击

        time.sleep(0.5)  # 等待  # 增加延迟
        pag.moveTo(590, 210)  # 鼠标移动X.Y 方位  输入框 位置
        pag.rightClick()  # 右击

        self.模具一一写入剪切板内容(self.cookie)

        pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c')

        time.sleep(0.5)  # 等待  # 增加延迟
        pag.moveTo(650, 630)  # 鼠标移动X.Y 方位  绿色勾选 按钮
        pag.rightClick()  # 右击

        # pag.hotkey('ctrlleft', 'F4')  # 确认  关闭当前标签页   按钮

    """==========电脑操作==============="""

    def 模具一一清除浏览器历史缓存(self):

        print('清除浏览器历史缓存')
        pag.hotkey('ctrlleft', 'delete')  # 页面

        # pag.hotkey('ctrlleft', '1')  #   页面

        time.sleep(1)  # 等待  # 增加延迟
        #
        # pag.moveTo(90, 82)  # 鼠标移动X.Y 方位  清除历史缓存 按钮
        #  pag.rightClick()  # 右击

        # 清除历史缓存网址='opera://settings/clearBrowserData'
        # self.模具一一地址栏输入网址(清除历史缓存网址)

        # time.sleep(4)  # 增加延迟 等待清除新窗口

        # pag.moveTo(855, 700)  # 鼠标移动X.Y 方位  清除历史缓存 按钮
        # # pag.rightClick()  # 右击
        # time.sleep(0.5)

        # pag.moveTo(855, 700)  # 鼠标移动X.Y 方位  清除历史缓存 按钮
        # pag.rightClick()  # 右击

        # time.sleep(2)
    def 模具一一刷新知乎点赞页(self):

        pag.hotkey('ctrlleft', '1')  # 鼠标移动X.Y 方位  cookie插件布置 页面
        time.sleep(1)
        pag.hotkey('ctrlleft', 'r')  # 刷新页面
        time.sleep(3)  # 增加延迟


    def 模具一一重新激活浏览器窗口(self):
        print('重新激活浏览器窗口')
        pag.hotkey('winleft', 'd')  # press()一次完整的击键.hotkey('ctrl','c'):热键函数 .keyDown()按下某个键.keyUp()松开某个键.

        time.sleep(0.5)  # 等待  # 增加延迟
        pag.moveTo(221, 920)  # 鼠标移动X.Y 方位  重新激活浏览器窗口 在CMD 与  回归桌面之间
        pag.rightClick()  # 右击
        time.sleep(2)  # 等待  # 增加延迟



    """=========上传图片========================"""
    def 模具一一图片目录地址框(self):
        pag.moveTo(366, 45)  # 鼠标移动X.Y 方位  确定  图片目录地址框
        pag.rightClick()  # 右击
        time.sleep(0.3)  # 等待  # 增加延迟

        pag.hotkey('ctrlleft', 'a')  # press()一次完整的击键.hotkey('ctrl','c') 全选 图片
        time.sleep(0.3)  # 等待  # 增加延迟
        pag.press('delete')  # press()一次完整的击键.hotkey('ctrl','c') 确认
        time.sleep(0.3)  # 等待  # 增加延迟

        图片目录地址= r"F:\影视发帖推广\临时图片"

        self.模具一一写入剪切板内容(图片目录地址)

        pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.3)  # 等待  # 增加延迟
        pag.press('enter')  # press()一次完整的击键.hotkey('ctrl','c') 确认
        time.sleep(1)  # 等待  # 增加延迟

    def 模具一一清空临时图片目录(self):


        子目录列表与文件列表 = os.listdir(self.临时图片目录)  # 分离出目录列表与文件列表
        for 子目录或文件 in 子目录列表与文件列表:
            根目录的子目录或文件路径 = os.path.join(self.临时图片目录, 子目录或文件)
            os.unlink(根目录的子目录或文件路径)  # 删除原来 文件 与文件
        print('清空移动文件目录:', self.临时图片目录)

    def 模具一一移动图片文件至临时图片目录(self):
        time.sleep(0.5)  # 等待  # 增加延迟
        子目录列表与文件列表 = os.listdir(self.旧目录路径)  # 分离出目录列表与文件列表

        for 子目录或文件 in 子目录列表与文件列表[0:2]:
            根目录的子目录或文件路径 = os.path.join(self.旧目录路径, 子目录或文件)

            if os.path.isfile(根目录的子目录或文件路径):  # 判断是不是文件  判断文件 os.path.isfile
                # os.path.isfile() 函数判断某一路径是否为文件
                self.用户名 = 子目录或文件
                self.图片文件 = 根目录的子目录或文件路径
                print(self.图片文件, '移动文件:', self.临时图片目录)
                shutil.move(self.图片文件, self.临时图片目录)
                time.sleep(0.5)  # 等待  # 增加延迟

                return  # 返回 只移动一个图片

    def 模具一一上传图片窗口选择图片(self):


        pag.moveTo(227, 156)  # 鼠标移动X.Y 方位  确定  第一张图片
        pag.rightClick()  # 右击

        time.sleep(1)  # 等待  # 增加延迟

        pag.hotkey('altleft', 'o')  # press()一次完整的击键.hotkey('ctrl','c') 提交图片
        time.sleep(5)  # 等待  # 增加延迟 已经有等待 3秒了

        pag.moveTo(655, 705)  # 鼠标移动X.Y 方位  定位 保存  按钮
        pag.rightClick()  # 右击
        time.sleep(1)  # 等待  # 增加延迟

    """=========文本整理========================"""

    def 模具一一文本随机插入字符测试(self,正文,分隔数):
        def 保存至文本(内容):
            文本 = open("F:\影视发帖推广\临时文本.txt", 'w', encoding='UTF-8')

            文本.write(内容)  # read() #读取
            文本.close()
            print('保存至临时文本;')
        计数器 = 0
        文本 = ''
        for 每个字 in 正文:
            计数器 = 计数器 + 1
            if 计数器 == 分隔数:
                符号表 = random.choice(' ↕↟↡↥↧↨↾↿⇂⇃⇞⇟⇡⇣´`ˆ')


                文本 = 文本 + str(符号表)
                计数器 = 0
            文本 = 文本 + 每个字
        保存至文本(文本)

    def 模具一一提取文本内容(self):
        win32api.ShellExecute(0, 'open', 'notepad.exe', 'F:\影视发帖推广\临时文本.txt', '', 1)
        time.sleep(1)  # 等待  # 增加延迟
        pag.hotkey('ctrlleft', 'a')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(1)  # 等待  # 增加延迟
        pag.hotkey('ctrlleft', 'c')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(1)  # 等待  # 增加延迟
        pag.hotkey('altleft', 'f4')  # press()一次完整的击键.hotkey('ctrl','c')


    """============旧模具================"""

    def 模具一一手机模式访问并注册知乎(self):
        头部信息 = "user - agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_5 like Mac OS X) AppleWebKit/612.1.60(KHTML, like Gecko) CriOS/66.0.2524.75 Mobile/15E5239e Safari/612.1'"

        # url = "http://www.sunchateau.com/free/UA.htm"#  浏览器UA头部信息 在线查询
        url = "https://www.zhihu.com/signin?next=https://www.zhihu.com/"
        # 随机手机型号= random.choice(["iPhone 5","iPhone 6","iPhone 6 Plus","iPhone 7","iPhone 7 Plus","iPhone 8","iPhone 8 Plus","iPhone X"])

        随机手机型号 = random.choice(
            ["iPhone 5", "iPhone 6", "iPhone 6 Plus", "iPad Pro", "iPad"])

        随机手机型号 = "iPhone 6"
        print('随机手机型号', 随机手机型号)

        mobile_emulation = {"deviceName": 随机手机型号}  # 设置成手机模式
        options = Options()
        options = webdriver.ChromeOptions()  # 设置中文
        options.add_experimental_option("mobileEmulation", mobile_emulation)  # 更改 浏览头部信息为手机模式
        # options.add_argument(头部信息)

        # options.add_argument('disable-infobars')# 加启动配置 去除正在受到自动软件的控制
        # options.add_argument('headless')  # 静默模式

        # prefs = {"profile.managed_default_content_settings.images": 2}#配置不加载图片
        # options.add_experimental_option("prefs", prefs)#配置不加载图片

        操作 = webdriver.Chrome(chrome_options=options)  # 打开chrome浏览器
        # driver = webdriver.Chrome(chrome_options=options)

        # self.模具一一获取接收的手机号码()
        # self.手机号码='17131632268'

        操作.get(url)  # 访问网址

        time.sleep(1000)  # 等待

        time.sleep(5)  # 等待
        # 操作.find_element_by_xpath("//*[@id=\"address\"]").send_keys(Keys.CONTROL,'DELETE') # 键盘按击或输入  请空输入框:clear()
        # 操作.find_element_by_xpath("//*[@id=\"address\"]").click()# 光标 点击.click()
        # 操作.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/header/div/div/div/a[2]").click()  # 光标 点击.click()

        # 操作.find_element_by_name("username").send_keys(self.手机号码)  # 键盘按击或输入  请空输入框:clear()
        操作.find_element_by_xpath("//*[@id=\"root\"]/div/main/div/form/div[1]/div[1]/div[2]/div[1]/input").send_keys(
            self.手机号码)  # 键盘按击或输入  请空输入框:clear()
        time.sleep(1)  # 等待
        # 操作.find_element_by_class_name("CountingDownButton").click() # 光标 点击.click()

        定位 = 操作.find_element_by_xpath('//*[@id="root"]/div/main/div/form/div[1]/div[2]/button')  # 触摸事件 发送验证码 按扭
        TouchActions(操作).tap(定位).perform()
        time.sleep(1)  # 等待

        self.模具一一获取短信()
        self.模具一一知乎短信内容清洗()
        # self.短信内容='623516'
        操作.find_element_by_name("digits").send_keys(self.短信内容)  # 键盘按击或输入  请空输入框:clear()
        time.sleep(1)  # 等待

        定位 = 操作.find_element_by_xpath('//*[@id="root"]/div/main/div/form/button')  # 触摸事件 登录 按扭
        TouchActions(操作).tap(定位).perform()

        time.sleep(5)  # 等待

        保存cookie = [item["name"] + ":" + item["value"] for item in 操作.get_cookies()]
        print('保存cookie:\n', 保存cookie)

        time.sleep(1000)  # 等待

        # 操作.quit()  # 关闭浏览器U

    def 模具一一浏览器访问并注册知乎(self):
        self.模具一一换头部信息()

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
        time.sleep(500)  # 等待

    def 模具一一提炼Cookie(self):
        Cookie文本 = 'tgw_l7_route=170010e948f1b2a2d4c7f3737c85e98c; _zap=ce1305a8-7d69-4551-b0c9-3cdf5d6e0b0c; _xsrf=pSfp9xAJvbYsJp1oUeeJVgGwSSWRFG79; q_c1=b2869836ad1545b89e2ca2fe599291f3|1534096133000|1534096133000; d_c0="ABBnPv7jCw6PTvReDG2SZyvJkmkHe8nDvT4=|1534096133"; capsion_ticket="2|1:0|10:1534096136|14:capsion_ticket|44:Mzg1YjZlMGFlOWY4NGE5MmI3M2IxOTA3MzQ3NjdhMTc=|3531eddc76e8d7935cbda485229e69ab672d0ab931d9139acb5a96cd8d1059e0"; z_c0="2|1:0|10:1534096157|4:z_c0|92:Mi4xTGlzSUFBQUFBQUFBRUdjLV91TUxEaVlBQUFCZ0FsVk5IY0ZkWEFBWHFOTTc5V0M5M19NUFMtbHYyaG1YU044MmNn|2163e2d4319ea00dfbc6fd180ec62e5a883da34d05477a0cec2806e10e49d870"'

        cookies = {}
        for 每句 in Cookie文本.split(';'):  # 转为列表cookies['tgw_l7_route']
            字典键, 值 = 每句.strip().split('=', 1)  # 1代表只分割一次
            cookies[字典键] = 值
        self.cookies = cookies
        self.cookies浏览操作 = {'domain': '.www.zhihu.com',
                            'name': 'tgw_l7_route',
                            'value': 'ec452307db92a7f0fdb158e41da8e5d8',
                            '_zap': cookies['_zap'],
                            '_xsrf': cookies['_xsrf'],
                            'capsion_ticket': cookies['capsion_ticket'],
                            'd_c0': cookies['d_c0'],
                            'z_c0': cookies['z_c0'],
                            'q_c1': cookies['q_c1'],
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
        主页cookies = 浏览器操作.get_cookies()  # 打开主页后获取cookies
        print('登录前主页cookies', 主页cookies)
        cookies浏览 = 主页cookies[0]

        浏览器操作.delete_all_cookies()  # 删除第一次建立连接时的cookie

        time.sleep(100000)  # 等待

        for 键名 in self.cookies:
            cookies浏览操作 = {'domain': '.www.zhihu.com',
                           'name': 键名,
                           'value': self.cookies[键名],
                           'expiry': cookies浏览['expiry'] + 31536000,
                           'path': '/',
                           'httpOnly': False,
                           'secure': False}
            浏览器操作.add_cookie(cookie_dict=cookies浏览操作)

        # 浏览器操作.add_cookie(cookie_dict=self.cookies浏览操作)
        # 浏览器操作.add_cookie(cookie_dict=cookies浏览)
        # 浏览器操作.add_cookie({'value': '61066e97b5b7b3b0daad1bff47134a22'})

        time.sleep(2)  # 等待
        主页cookies = 浏览器操作.get_cookies()  # 打开主页后获取cookies
        print('登录后主页cookies', 主页cookies)

        浏览器操作.refresh()  # 刷新当前页面

        time.sleep(20000)  # 等待






