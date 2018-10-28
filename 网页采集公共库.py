
# -*- coding:utf-8
import grequests  # 并发协程
import requests  # 网页浏览
import pymysql  # 数据库
import time  # 时间
import random  # 随机
import win32api  # 操作本地文件
import pyautogui  # 键盘控制



"""

import requests  # 网页浏览
import re  # 正则式

import datetime  # 时间
import os  # 本地操作

from lxml import etree  # 网页分析
import shutil  # 移动复制文件目录
from lxml import html  # 网页分析
from selenium import webdriver  # 浏览的驱动

import asyncio, aiohttp # 异步浏览


"""

class 类一一采集公共库: #调用 类的模具 self.模具一一数据库()
    def __init__(self):
        self.模具一一高位换头部信息()

        pass

    def 模具一一示例(self):
        pass

    def 模具一一高位换头部信息(self):  # 头部信息 def 函数模具内通行变量
        # nonlocal 头部信息  # def 函数模具内通行变量

        self.换IP时间计数 = int(time.time())
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


    def 模具一一换ip连接二(self):
        win32api.ShellExecute(0, 'open', 'E:\PY学习文件\BTT影视剧\工具集\换ip连接二.py', '', '', 1)

        pyautogui.alert('等待.....换ip连接')


    """============gr无序网址列表================"""

    def 模具一一gr无序网址列表请求返回网页内容(self, 网址列表, 分流数=100, 并发数=5):  # grequests.imap(任务列

        初始网址列表数 = len(网址列表)

        条件循环 = 1

        返回网页一链接组列表 = []

        while 条件循环 == 1:

            此时数 = int(time.time())
            if 此时数 > self.换IP时间计数 + 60:
                self.模具一一高位换头部信息()
                # self.模具一一换ip连接()
            网址列表数 = len(网址列表)
            任务列表 = []
            网址分列表 = []
            for 各帖子链接 in 网址列表[0:分流数]:
                网址分列表.append(各帖子链接)

            if len(网址列表) > 分流数 - 1:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                网址列表 = 网址列表[分流数:]
            else:  # 否则
                网址列表 = []

            for 各帖子链接 in 网址分列表:
                任务 = grequests.get(各帖子链接, headers=self.头部信息)  # timeout=len(任务列表)//2,
                任务列表.append(任务)

            try:  # 调用异常处理,应对易发生错误的位置
                返回网页内容集 = grequests.imap(任务列表, size=并发数)  # size=3 并发数 3  gtimeout超时时间
            except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout,
                    requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout,
                    requests.exceptions.ChunkedEncodingError, requests.exceptions.InvalidSchema) as 异常:

                print('gr无序异常，倒数6秒再连接', 异常)
                # 网址列表.append(返回网页内容.url)

                time.sleep(3)
            else:

                for 返回网页内容 in 返回网页内容集:
                    网页内容文本 = str(返回网页内容)

                    if '<Response [200]>' in 网页内容文本 and "访问过于频繁" not in 返回网页内容.text:
                        # print('返回网页内容', 返回网页内容)

                        返回网页内容.encoding = "UTF-8"

                        返回网页一链接组 = []
                        返回网页一链接组.append(返回网页内容)
                        返回网页一链接组.append(返回网页内容.url)
                        返回网页一链接组列表.append(返回网页一链接组)

                        print('成功采集网页：', 返回网页内容.url)

                    else:  # 否则
                        网址列表.append(返回网页内容.url)

                此时数 = int(time.time())
                if len(网址列表) == 0:
                    print('网页采集,全部完成')

                    条件循环 = 998
                elif 此时数 > self.换IP时间计数 + 初始网址列表数 * 3:
                    print('网页未完成采集数:', 初始网址列表数 - len(返回网页一链接组列表))

                    条件循环 = 998

                time.sleep(1)  # 等待

        return 返回网页一链接组列表  # 返回
    """============异步打开网页================"""

    def 模具一一异步调度(self, 网址列表, 分流数=100, 并发数=5, 内容格式='text'):
        self.返回网页一链接组列表 = []
        self.重新无序单网址列表 = []
        self.并发数 = 并发数

        self.网址列表 = 网址列表
        初始网址列表数 = len(self.网址列表)
        print('分流数', 分流数)
        print('并发数', 并发数)

        事件循环 = asyncio.get_event_loop()
        条件循环 = 1
        次数循环 = 0
        返回网页一链接组列表 = []

        有效返回网页内容集 = []
        while 条件循环 == 1:
            self.此时数 = int(time.time())
            if self.此时数 > self.换IP时间计数 + 60:
                self.模具一一换ip连接()
                self.模具一一换头部信息()
            任务列表 = []
            网址分列表 = []
            for 各帖子链接 in self.网址列表[0:分流数]:
                网址分列表.append(各帖子链接)

            if len(self.网址列表) > 分流数 - 1:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                self.网址列表 = self.网址列表[分流数:]
            else:  # 否则
                self.网址列表 = []

            任务列表 = []
            for 各帖子链接 in 网址分列表:
                if 'text' in 内容格式:
                    任务 = asyncio.ensure_future(self.模具一一异步打开网页(各帖子链接))  #

                else:  # 否则
                    任务 = asyncio.ensure_future(self.模具一一下载异步打开网页(各帖子链接, 内容格式))  #
                任务列表.append(任务)
            results = 事件循环.run_until_complete(asyncio.wait(任务列表))  # 等待任务完成
            # 事件循环.close()

            此时数 = int(time.time())
            if len(self.网址列表) == 0:
                print('网页采集,全部完成')
                条件循环 = 998
                return self.返回网页一链接组列表  # 返回

            elif 此时数 > self.换IP时间计数 + 初始网址列表数 * 3:
                print('网页未完成采集数:', 初始网址列表数 - len(self.返回网页一链接组列表))

                条件循环 = 998
                return self.返回网页一链接组列表  # 返回

            time.sleep(2)  # 等待

    async def 模具一一异步打开网页(self, url):

        # conn = aiohttp.TCPConnector(limit=10)  # limit 并发 默认100,0表示无限
        async with aiohttp.ClientSession(headers=self.头部信息, connector=aiohttp.TCPConnector(limit=self.并发数)) as 会话:

            try:  # 调用异常处理,应对易发生错误的位置
                async with 会话.request("GET", url) as 内容:  # "GET" 是个重要的请求方法
                    返回网页 = await 内容.text(
                        encoding="utf-8")  # 或者直接await r.read()不encoding='UTF-8',直接读取,适合于图像等无法encoding='UTF-8'文件

            except (AttributeError) as 异常:  # (AttributeError) as 异常
                # print('网络异常等待', 异常)
                print(异常, '异步连接异常，倒数6秒再连接', '次')
                # time.sleep(3)
            else:
                if '[200 OK]' in str(内容):
                    返回网页一链接组 = []
                    返回网页一链接组.append(返回网页)
                    返回网页一链接组.append(url)
                    self.返回网页一链接组列表.append(返回网页一链接组)
                    print('成功采集网页：', url)

                else:  # 否则
                    self.网址列表.append(url)

    """============gr无序网址列表================"""
    def 模具一一内容数据库(self,数据库='提交'):
       #self.sql语句 = """
       #print('打开数据库连接')
        # 打开数据库连接,
        数据库执行 = pymysql.connect("localhost", "root", "", self.数据库名, charset="utf8")
        # 使用cursor()方法获取操作游标
        操作游标 = 数据库执行.cursor()

        # 执行sql语句
        操作游标.execute(self.sql语句)

        if '提交' in 数据库:
            try:
                # 提交到数据库执行
                数据库执行.commit()
                print('=提交至保存数据库')
            except:

                # 如果发生错误则回滚
                print('==========数据库执行发生错误:======')
                数据库执行.rollback()

        else:  # 否则 为查询
            # 获取所有记录列表
            self.数据库内容组列表 = 操作游标.fetchall()
            print('数据库完成查询')




        数据库执行.close()# 关闭数据库连接


            