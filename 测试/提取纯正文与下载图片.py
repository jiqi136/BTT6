import re  # 正则式
import time  # 时间
import datetime  # 时间

import pymysql  # 数据库


# -*- coding:utf-8
import grequests  # 并发协程
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
from selenium import webdriver  # 浏览的驱动
import win32api  # 操作本地文件
import asyncio, aiohttp # 异步浏览


class 类一一公共库: #调用 类的模具 self.模具一一数据库()
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
        随机1位数 = str(random.randrange(1, 10))
        随机11位数 = str(random.randrange(1, 10))
        头部信息 = random.choice([{'User-Agent': 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'},
                              {
                                  'User-Agent': 'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.{随机3位数 Version/随机2位数.11'},
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
                              {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 随机1位数.0; Windows NT 6.0)'},
                              {
                                  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/随机3位数.11 (KHTML, like Gecko) Chrome/随机2位数.0.963.56 Safari/535.11'},
                              {
                                  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/201随机3位数01 Firefox/随机2位数.0.1'},
                              {
                                  'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/随机2位数.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.随机2位数727; SE 2.X MetaSr 1.0)'},
                              {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 随机1位数.0; Windows NT 随机11位数.1; The World)'},
                              {
                                  'User-Agent': 'Mozilla/4.0 (compatible; MSIE 随机1位数.0; Windows NT 随机11位数.1; TencentTraveler 4.0)'},
                              {
                                  'User-Agent': 'Mozilla/4.0 (compatible; MSIE 随机1位数.0; Windows NT 随机11位数.1; Maxthon 2.0)'},
                              {
                                  'User-Agent': 'Mozilla/4.0 (compatible; MSIE 随机1位数.0; Windows NT 随机11位数.1; Avant Browser)'},
                              {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 随机1位数.0; Windows NT 随机11位数.1; 360SE)'},
                              {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 随机1位数.0; Windows NT 随机11位数.1)'},
                              {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 随机1位数.0; Windows NT 随机11位数.1)'}
                              ])
        头部信息['User-Agent'] = str(头部信息['User-Agent']).replace("随机1位数", 随机1位数)  # 替换   , 1) 次数 1
        头部信息['User-Agent'] = str(头部信息['User-Agent']).replace("随机11位数", 随机11位数)  # 替换   , 1) 次数 1
        头部信息['User-Agent'] = str(头部信息['User-Agent']).replace("随机2位数", 随机2位数)  # 替换   , 1) 次数 1
        头部信息['User-Agent'] = str(头部信息['User-Agent']).replace("随机3位数", 随机3位数)  # 替换   , 1) 次数 1
        print(头部信息)

    def 模具一一打开的网址请求返回网页内容(self, 网址):#self.返回网页内容
        # global 换IP时间计数  # 时间计数全局变量声明
        循环 = 0
        次数循环 = 0
        缓冲时间 = 0
        while 循环 == 0:  # 条件循环  post
            此时数 = int(time.time())
            if 此时数 > 换IP时间计数 + 200:
                self.模具一一换ip连接()
                self.模具一一换头部信息()
            try:
                此时数2 = int(time.time())
                if 缓冲时间 > 此时数2:
                    time.sleep(0.5)
                    print('缓冲时间 多加 0.5秒')
                self.返回网页内容 = requests.post(网址, headers=头部信息,timeout=5)
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
                if '200' in str(self.返回网页内容):
                    self.返回网页内容.encoding = "UTF-8"  # 转换encoding='UTF-8' "gbk"
                    return  # 返回
                else:
                    print('网站网络异常,状态码:', self.返回网页内容)
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

    def 模具一一gr无序单网址请求返回网页内容(self,单网址):# grequests.imap(任务列
        单网址列表 = []
        单网址列表.append(单网址)

        单网址列表=单网址列表*3
        规则 = '.{1,}hread'
        任务列表 = []
        for 各帖子链接 in 单网址列表:
            if 'thread' in 各帖子链接:
                各帖子链接 = re.sub(规则, 'http://91btbtt.com/?thread', 各帖子链接)  # 替换
                # if 各帖子链接 in self.过滤帖子网址:
                # continue  # 跳过当前循环,继续进行下一轮循环
            任务 = grequests.get(各帖子链接, headers=头部信息)  # timeout=len(任务列表)//2,
            任务列表.append(任务)

        条件循环 = 1
        次数循环 = 0
        while 条件循环 == 1:
            此时数 = int(time.time())
            if 此时数 > 换IP时间计数 + 60:
                self.模具一一换ip连接()
                self.模具一一换头部信息()
            try:  # 调用异常处理,应对易发生错误的位置
                返回网页内容集 = grequests.imap(任务列表, size=5)  # size=3 并发数 3  gtimeout超时时间
            except (grequests.exceptions.ConnectTimeout, grequests.exceptions.ReadTimeout,
                    grequests.exceptions.ConnectionError, grequests.exceptions.ConnectTimeout,
                    grequests.exceptions.ChunkedEncodingError, grequests.exceptions.InvalidSchema) as 异常:
                print('网络异常等待', 异常)
                print('倒数6秒再连接', 次数循环, '次')
                # time.sleep(3)
            else:

                for 返回网页内容 in 返回网页内容集:
                    返回网页内容文本 = str(返回网页内容)
                    if '<Response [200]>' in 返回网页内容文本 :
                        # print('返回网页内容', 返回网页内容)
                        返回网页内容.encoding = "UTF-8"

                        return 返回网页内容  # 返回


    def 模具一一grequests打开网址随机无序集(self, 网址总列表):  # grequests.imap(任务列
        网址分列表 = []
        倒数 = len(网址总列表)
        内容总列表 = []
        规则 = '.{1,}hread'
        for 各帖子链接 in 网址总列表:
            网址分列表.append(各帖子链接)
            倒数 = 倒数 - 1
            if len(网址分列表) == 20 or 倒数 == 0:
                print('等待响应网页倒数', 倒数)
                任务列表 = []
                for 各帖子链接 in 网址分列表:
                    if 'thread' in 各帖子链接:
                        各帖子链接 = re.sub(规则, 'http://91btbtt.com/thread', 各帖子链接)  # 替换
                        # if 各帖子链接 in self.过滤帖子网址:
                        # continue  # 跳过当前循环,继续进行下一轮循环
                    任务 = grequests.get(各帖子链接, headers=头部信息)  # timeout=len(任务列表)//2,
                    任务列表.append(任务)
                网址分列表 = []
                条件循环 = 1
                次数循环 = 0
                while 条件循环 == 1:
                    此时数 = int(time.time())
                    if 此时数 > 换IP时间计数 + 60:
                        self.模具一一换ip连接()
                        self.模具一一换头部信息()
                    try:  # 调用异常处理,应对易发生错误的位置
                        返回网页内容集 = grequests.imap(任务列表, size=5)  # size=3 并发数 3  gtimeout超时时间
                    except (grequests.exceptions.ConnectTimeout, grequests.exceptions.ReadTimeout,
                            grequests.exceptions.ConnectionError, grequests.exceptions.ConnectTimeout,
                            grequests.exceptions.ChunkedEncodingError, grequests.exceptions.InvalidSchema) as 异常:
                        print('网络异常等待', 异常)
                        print('倒数9秒再连接', 次数循环, '次')
                        # time.sleep(3)
                    else:
                        返回网页内容列表 = []
                        for 返回网页内容 in 返回网页内容集:
                            返回网页内容文本 = str(返回网页内容)
                            if '200' in 返回网页内容文本 and 'None' not in 返回网页内容文本 and '40' not in 返回网页内容文本:
                                # print('返回网页内容', 返回网页内容)
                                返回网页内容.encoding = "UTF-8"
                                返回网页内容列表.append(返回网页内容)
                            if len(任务列表) == len(返回网页内容列表):
                                内容总列表 = 内容总列表 + 返回网页内容列表
                                条件循环 = 520
        print('返回网页内容数', len(内容总列表))                       # break # 结束循环
        return 内容总列表  # 返回

    """============异步打开网页================"""

    async def 模具一一异步打开网页(self,url):

        # conn = aiohttp.TCPConnector(limit=10)  # 默认100,0表示无限
        async with aiohttp.ClientSession(headers=头部信息, connector=aiohttp.TCPConnector(limit=10)) as 会话:

            try:  # 调用异常处理,应对易发生错误的位置
                async with 会话.request("GET", url) as 内容:  # "GET" 是个重要的请求方法
                    返回网页 = await 内容.text(encoding="utf-8")  # 或者直接await r.read()不encoding='UTF-8',直接读取,适合于图像等无法encoding='UTF-8'文件

            except:# () as 异常
                #print('网络异常等待', 异常)
                    print('倒数6秒再连接', '次')
                    # time.sleep(3)
            else:
                if '[200 OK]' in str(内容):
                   pass
                else:  # 否则
                    内容 = self.模具一一gr无序单网址请求返回网页内容(url)
                    返回网页 = 内容.text
                    print('重新修正内容', 内容)
                返回网页一链接组 = []
                返回网页一链接组.append(返回网页)
                返回网页一链接组.append(url)
                self.返回网页一链接组列表.append(返回网页一链接组)


    def 模具一一异步调度(self,网址列表):
        此时数 = int(time.time())
        if 此时数 > 换IP时间计数 + 60:
            self.模具一一换ip连接()
            self.模具一一换头部信息()

        self.返回网页一链接组列表 = []
        任务列表 = []
        规则 = '.{1,}hread'
        for 各帖子链接 in 网址列表:
            if 'thread' in 各帖子链接:
                各帖子链接 = re.sub(规则, 'http://91btbtt.com/?thread', 各帖子链接)  # 替换
                # if 各帖子链接 in self.过滤帖子网址:
                # continue  # 跳过当前循环,继续进行下一轮循环
            print('各帖子链接', 各帖子链接)

            任务 = asyncio.ensure_future(self.模具一一异步打开网页(各帖子链接))
            任务列表.append(任务)

        event_loop = asyncio.get_event_loop()
        results = event_loop.run_until_complete(asyncio.wait(任务列表))# 等待任务完成
        event_loop.close()

    def 模具一一异步返回网页一链接组列表(self):
        网址列表 = []

        self.模具一一异步调度(网址列表)  # self.返回网页一链接组列表
        for 返回网页一链接组 in self.返回网页一链接组列表:
            返回网页内容 = 返回网页一链接组[0]
            链接 = 返回网页一链接组[1]
            print('链接', 链接)
        print('返回网页内容', 返回网页内容)

    """============测试库================"""
        
            


class 类一一提取纯正文与下载图片(类一一公共库): #调用 类的模具 self.模具一一数据库()
    def __init__(self):
        self.模具一一换头部信息()
        self.模具一一提取豆瓣电影标题()
        self.计数器 = 0


        self.新旧影视库 = '电影与合集'
        self.模具一一整理正文与图片()

        self.新旧影视库 = '最新影视剧'
        self.模具一一整理正文与图片()

        print('self.计数器', self.计数器)

    def 模具一一提取豆瓣电影标题(self):
        # 提取数据库里的过滤网址
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "", "影视发帖推广", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句 self.各帖子链接
        sql = "SELECT `标题` FROM `2018上半年豆瓣电影` WHERE `类型`='电影'"
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        self.标题组列表 = cursor.fetchall()

        # 关闭数据库连接
        db.close()

    def 模具一一保存数据库正文(self):
        # 提取数据库里的过滤网址
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "", "影视发帖推广", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句 self.各帖子链接
        sql = "UPDATE `2018上半年豆瓣电影` SET `正文`='{}' WHERE `标题`='{}'".format(self.正文,self.短标题)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            db.rollback()
            print('数据库执行发生错误')
        # 关闭数据库连接
        db.close()
        print('保存数据库正文')

    def 模具一一提取剧数据库里的正文(self):
        # 提取数据库里的过滤网址
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "",self.新旧影视库, charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句 self.各帖子链接
        sql = "SELECT  `正文` FROM `网站文章内容` WHERE `短标题`='{}'" .format(self.短标题)
        cursor.execute(sql)
        # 获取所有记录列表
        self.正文组列表 = cursor.fetchall()
        # 关闭数据库连接
        db.close()



    def 模具一一整理正文与图片(self):


        for 标题组 in self.标题组列表:
            self.短标题=标题组[0]

            self.模具一一提取剧数据库里的正文()

            for 正文组 in self.正文组列表:
                self.数据正文 = 正文组[0]
                self.模具一一整理正文()
                self.模具一一保存数据库正文()
                self.模具一一整理图片并下载()
                self.计数器 = self.计数器 + 1

    def 模具一一整理正文(self):

        正文 = self.数据正文.replace("</p>", "\n") #替换   , 1) 次数 1
        正文 = 正文.replace("<br />", "\n")  # 替换   , 1) 次数 1
        规则='<.{1,}?>'
        正文 =re.sub(规则, "", 正文,0,re.S)#替换   ,count=0,re.S|re.I

        规则 = '获奖.{1,}'
        正文 = re.sub(规则, "", 正文, 0, re.S)  # 替换   ,count=0,re.S|re.I

        规则 = '◎译.{1,}?◎'
        文本列表 = re.findall(规则, 正文,re.S)  # 提取列表
        译名 = ''
        if len(文本列表) > 0:
            译名 = 文本列表[0]

        规则 = '◎产.{1,}?◎'
        文本列表 = re.findall(规则, 正文, re.S)  # 提取列表
        产地 = ''
        if len(文本列表)>0:
            产地 = 文本列表[0]

        规则 = '.{1,}◎简'
        正文 = re.sub(规则, "简", 正文, 0, re.S)  # 替换   ,count=0,re.S|re.I

        规则 = '.{1,}简介'
        正文 = re.sub(规则, "简介", 正文, 0, re.S)  # 替换   ,count=0,re.S|re.I
        列表=['字幕','7MM','资源无','深影','翻托邦','MM','\[译制团']
        for 字符 in 列表:
            规则 = '{}'.format(字符) + '.{1,}'
            正文 = re.sub(规则, "", 正文,0, re.S)#

            规则 = '{}'.format(字符) + '.{0,}'
            正文 = re.sub(规则, "", 正文 ,0, re.S)  #

        正文 =译名+'\n'+产地+'\n'+正文

        正文 = 正文.replace("　　", "")  # 替换   , 1) 次数 1
        正文 = 正文.replace("◎", "")  # 替换   , 1) 次数 1
        正文 = 正文.replace("&nbsp;", "")  # 替换   , 1) 次数 1
        正文 = 正文.replace("产地", "地区")  # 替换   , 1) 次数 1
        正文 = 正文.replace("\n\n\n", "\n")  # 替换   , 1) 次数 1
        正文 = 正文.replace("\n\n", "\n")  # 替换   , 1) 次数 1
        self.正文 = 正文

        print('正文:\n',正文)



    def 模具一一整理图片并下载(self):
        图片列表 = self.数据正文.split(".jpg\"")
        计数 = 0
        for 图片下载地址 in 图片列表:
            if 'src=' in 图片下载地址 and 'http'in 图片下载地址:

                规则=".{1,}src=\""
                图片下载地址 =re.sub(规则, '', 图片下载地址)#替换   ,count=0,re.S|re.I
                图片下载地址 = 图片下载地址 + ".jpg"

                print('图片下载地址：',图片下载地址)

                网址内容 = self.模具一一gr无序单网址请求返回网页内容(图片下载地址)
                计数 =计数+1

                图片目录 = r"F:/影视发帖推广/知乎/电影图/{}/".format(self.短标题)#
                图片名 =  r"{}{}.jpg".format(self.短标题,计数)#
                图片目录与图片名 = 图片目录 + 图片名

                创建图片目录 =图片目录.strip('/')
                if not os.path.exists(创建图片目录):  # 必有条件选择,否则出错
                    os.makedirs(创建图片目录)  # makedirs 创建多级目录文件夹,mkdir创建一个文件夹

                if os.path.exists(图片目录与图片名):  # 必有条件选择,否则出错
                    continue#跳过循环

                with open(图片目录与图片名, 'wb') as fout:  # 返回值 随后 被赋值给as后面的变量
                    fout.write(网址内容.content)  # read() #读取
                    fout.close()
                    print('完成下载', 图片目录与图片名)





类=类一一提取纯正文与下载图片()