
# -*- coding:utf-8
import grequests  # 并发协程
import requests  # 网页浏览
import pymysql  # 数据库
import time  # 时间
import random  # 随机
import win32api  # 操作本地文件
import pyautogui  # 键盘控制
import win32gui #窗口控件
import win32con#提取剪切板内容
import os  # 本地操作

from 服务公共库 import 类一一服务公共库# 导入模块



"""
from 网页采集公共库 import 类一一采集公共库# 导入模块
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

class 类一一采集公共库(类一一服务公共库): #调用 类的模具  self.模具一一查看变量输出文本值('变量名', self.测试打印, 8)
    def __init__(self):

        self.测试打印 = '测试'
        self.模具一一高位换头部信息()
        self.贴吧目录网址列表=['http://t.cn/EABJkRw']
        返回网页一链接组列表 = self.模具一一gr无序网址列表请求返回网页内容(self.贴吧目录网址列表)#, 编码="gbk"
        print('完成下载')
        返回网页一链接组=返回网页一链接组列表[0]
        print(返回网页一链接组[0].text)


    def 模具一一示例(self):
        pass
        返回网页一链接组列表 = self.模具一一gr无序网址列表请求返回网页内容(self.贴吧目录网址列表, 编码="gbk")
        for 返回网页一链接组 in 返回网页一链接组列表:
            返回网页内容 = 返回网页一链接组[0]
            网址 = 返回网页一链接组[1]

        self.数据库名 = "影视发帖推广"
        self.sql语句 = "UPDATE `微博抽奖转发内容` SET `转发`='是' WHERE `ID`={}".format(self.数据库id)  # '代入 '{}' #'
        self.模具一一内容数据库("更新 转发栏为 是")
        self.数据库内容组列表 = self.数据库内容组列表

        帖子链接 = ''
        self.模具一一查看变量输出文本值("过滤的网址", 帖子链接, 8)
        pass


    def 模具一一换ip连接二(self):
        win32api.ShellExecute(0, 'open', 'E:\PY学习文件\BTT影视剧\工具集\换ip连接二.py', '', '', 1)

        pyautogui.alert('等待.....换ip连接')


    """============gr无序网址列表================"""

    def 模具一一gr无序网址列表请求返回网页内容(self, 网址列表, 分流数=100, 并发数=5,编码= "UTF-8"):  # 返回网页一链接组列表

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

                        返回网页内容.encoding = 编码


                        返回网页一链接组 = []
                        返回网页一链接组.append(返回网页内容)
                        返回网页一链接组.append(返回网页内容.url)
                        返回网页一链接组列表.append(返回网页一链接组)

                        #print('成功采集网页：', 返回网页内容.url)

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


采集公共库=类一一采集公共库()
            