# -*- coding:utf-8


import re  # 正则式
import time  # 时间
import pyautogui as pag #模拟鼠标键盘操作
import pyautogui#模拟鼠标键盘操作
import win32api  #  文件
import win32gui#窗口控件
import asyncio,aiohttp #异步打开网页
from lxml import etree,html #解析与定位网页
import grequests #无序单网址请求返回网页内容
import requests #网址请求返回网页内容
from 推广公共库 import 类一一公共库# 导入模块 E:\PY学习文件\BTT影视剧\电影与合集一并发协程.py

"""


"""
class 类一一维护代理IP(类一一公共库):  # 调用 类的模具 self.模具一一数据库()
    def __init__(self):
        self.模具一一高位换头部信息()
        self.模具一一换ip连接二()


        self.待检测代理类型IP端口列表 = []
        self.异常代理IP=''
        self.模具一一读取文本代理IP()


        self.模具一一提取ip网址列表()

        self.模具一一异步调度(self.提取ip网址列表)  # self.返回网页一链接组列表


        print('返回帖子内容数', len(self.返回网页一链接组列表))

        for 返回网页一链接组 in self.返回网页一链接组列表:


            self.帖子内容 = 返回网页一链接组[0]
            self.各帖子链接 = 返回网页一链接组[1]
            #print('帖子内容为空',self.帖子内容)
            if '西刺' in self.帖子内容:
                self.模具一一西刺清洗IP端口组(self.帖子内容)

            elif '快代理' in str(self.帖子内容):
                self.模具一一快代理清洗IP端口组(self.帖子内容)

            elif '云代理' in str(self.帖子内容):
                self.模具一一云代理清洗IP端口组(self.帖子内容)

            elif '小幻' in str(self.帖子内容):
                self.模具一一小幻清洗IP端口组(self.帖子内容)


        self.模具一一百度首页测试代理()

    """============ip网址列表================"""

    def 模具一一提取ip网址列表(self):
        self.提取ip网址列表 = []
        # =========西刺
        for 数序 in range(1,6,1):
            提取ip网址 = 'http://www.xicidaili.com/nn/{}'.format(数序)#'代入 '{}'
            self.提取ip网址列表.append(提取ip网址)
        # =========快代理
        for 数序 in range(1,20, 1):
            提取ip网址 ='https://www.kuaidaili.com/free/inha/{}'.format(数序)#'代入 '{}'
            self.提取ip网址列表.append(提取ip网址)
        # =========云代理
        for 数序 in range(1,8, 1):
            提取ip网址 ='http://www.ip3366.net/free/?stype=1&page={}'.format(数序)#'代入 '{}'
            self.提取ip网址列表.append(提取ip网址)

        # =========小幻
        小幻页数字典={'1':'b97827cc','2':'4ce63706','3':'5crfe930','4':'f3k1d581','5':'ce1d45977','6':'881aaf7b5','7':'eas7a436','8':'981o917f5',
                '9':'2d28bd81a','10':'a42g5985d','11':'came0299','12':'e92k59727','13':'242r0e7b5','14':'bc265a560','15':'622b6a5d3','16':'ae3g7e7aa'}

        for 数序 in range(1, 10, 1):
            数序 = str(数序)
            for 字典键 in 小幻页数字典:
                if 字典键 == 数序:
                    提取ip网址 = 'https://ip.ihuan.me/address/5Lit5Zu9.html?page={}'.format(小幻页数字典[字典键])  # '代入 '{}'
                    del 小幻页数字典[字典键]  # 删除键 'Name'
                    self.提取ip网址列表.append(提取ip网址)
                    break # 结束循环
    def 模具一一百度首页测试代理(self):
        self.正常代理IP列表 = []
        self.待检测代理类型IP端口列表 = list(set(self.待检测代理类型IP端口列表))
        self.模具一一设置代理异步调度()  # self.返回网页一链接组列表

        保存文本内容=''

        正常代理IP列表=list(set(self.正常代理IP列表))
        print('正常代理IP数', len(正常代理IP列表))


        for 正常代理IP in 正常代理IP列表:
            正常代理IP = 正常代理IP.strip()  # 默认则是去除空格
            正常代理IP = 正常代理IP.strip('\n')  # 默认则是去除空格
            print('正常代理IP',正常代理IP)
            保存文本内容 =保存文本内容+'{}:正常\n'.format(正常代理IP)#'代入 '{}'

        self.模具一一保存代理IP至文本(保存文本内容)
        新增代理IP = set(正常代理IP列表) - set(self.保存文本的IP端口列表)
        print('新增代理IP数', len(新增代理IP))

        #集差=set(self.待检测代理类型IP端口列表)-set(self.正常代理IP列表)
        #self.模具一一追加保存代理IP至文本(str(集差))


    """============清洗IP端口组================"""
    def 模具一一西刺清洗IP端口组(self, 内容):
        print('模具一一西刺清洗IP端口组')
        帖子内容html = etree.HTML(内容)
        # ========代理类型列表
        规则 = '//*[@id="ip_list"]/tbody/tr[*]/td[6]/text()'
        规则 = str(规则).replace("/tbody", "")
        代理类型列表 = 帖子内容html.xpath(规则)


        #========IP列表
        #
        规则 = '//*[@id="ip_list"]/tbody/tr[*]/td[2]/text()'
        规则 = str(规则).replace("/tbody", "")
        IP列表 = 帖子内容html.xpath(规则)

        # ========端口列表
        规则 = '//*[@id="ip_list"]/tbody/tr[*]/td[3]/text()'
        规则 = str(规则).replace("/tbody", "")
        端口列表 = 帖子内容html.xpath(规则)

        # ========IP端口组列表

        print('IP列表数', len(IP列表))
        print('端口列表数', len(端口列表))
        print('代理类型列表', len(代理类型列表))
        if len(IP列表) != len(端口列表) and len(IP列表) != len(代理类型列表):
            print('ip端口数据组不匹配,结束程序')
            等待用户输入 = input("\n按下 enter 确认键后继续")
        for 代理类型, IP, 端口 in zip(代理类型列表, IP列表, 端口列表):
            IP端口 = "{}://{}:{}".format(代理类型, IP, 端口)  # '代入 '{}'
            self.待检测代理类型IP端口列表.append(IP端口)

    def 模具一一快代理清洗IP端口组(self, 内容):
        print('模具一一快代理清洗IP端口组')
        帖子内容html = etree.HTML(内容)
        # ========代理类型列表
        规则 = '//*[@id="list"]/table/tbody/tr[*]/td[4]/text()'
        代理类型列表 = 帖子内容html.xpath(规则)
        规则二 = str(规则).replace("/tbody", "")
        代理类型列表 =代理类型列表+(帖子内容html.xpath(规则二))


        #========IP列表
        #
        规则 = '//*[@id="list"]/table/tbody/tr[*]/td[1]/text()'
        IP列表 = 帖子内容html.xpath(规则)
        规则二 = str(规则).replace("/tbody", "")
        IP列表 = IP列表 + (帖子内容html.xpath(规则二))

        # ========端口列表
        规则 = '//*[@id="list"]/table/tbody/tr[*]/td[2]/text()'
        端口列表 = 帖子内容html.xpath(规则)
        规则二 = str(规则).replace("/tbody", "")
        端口列表 = 端口列表 + (帖子内容html.xpath(规则二))

        # ========IP端口组列表

        print('IP列表数', len(IP列表))
        print('端口列表数', len(端口列表))
        print('代理类型列表', len(代理类型列表))
        if len(IP列表) != len(端口列表) and len(IP列表) != len(代理类型列表):
            print('ip端口数据组不匹配,结束程序')
            等待用户输入 = input("\n按下 enter 确认键后继续")
        for 代理类型, IP, 端口 in zip(代理类型列表, IP列表, 端口列表):
            IP端口 = "{}://{}:{}".format(代理类型, IP, 端口)  # '代入 '{}'
            self.待检测代理类型IP端口列表.append(IP端口)

    def 模具一一云代理清洗IP端口组(self, 内容):
        print('模具一一云代理清洗IP端口组')
        帖子内容html = etree.HTML(内容)
        # ========代理类型列表
        规则 = '//*[@id="list"]/table/tbody/tr[*]/td[4]/text()'
        代理类型列表 = 帖子内容html.xpath(规则)
        规则二 = str(规则).replace("/tbody", "")
        代理类型列表 =代理类型列表+(帖子内容html.xpath(规则二))


        #========IP列表
        #
        规则 = '//*[@id="list"]/table/tbody/tr[*]/td[1]/text()'
        IP列表 = 帖子内容html.xpath(规则)
        规则二 = str(规则).replace("/tbody", "")
        IP列表 = IP列表 + (帖子内容html.xpath(规则二))

        # ========端口列表
        规则 = '//*[@id="list"]/table/tbody/tr[*]/td[2]/text()'
        端口列表 = 帖子内容html.xpath(规则)
        规则二 = str(规则).replace("/tbody", "")
        端口列表 = 端口列表 + (帖子内容html.xpath(规则二))

        # ========IP端口组列表

        print('IP列表数', len(IP列表))
        print('端口列表数', len(端口列表))
        print('代理类型列表', len(代理类型列表))
        if len(IP列表) != len(端口列表) and len(IP列表) != len(代理类型列表):
            print('ip端口数据组不匹配,结束程序')
            等待用户输入 = input("\n按下 enter 确认键后继续")
        for 代理类型, IP, 端口 in zip(代理类型列表, IP列表, 端口列表):
            IP端口 = "{}://{}:{}".format(代理类型, IP, 端口)  # '代入 '{}'
            self.待检测代理类型IP端口列表.append(IP端口)

    def 模具一一小幻清洗IP端口组(self, 内容):
        print('模具一一小幻清洗IP端口组')
        帖子内容html = etree.HTML(内容)
        #========IP列表
        #
        规则 = '//div[2]/div[2]/table/tbody/tr[*]/td[1]/a/text()'
        IP列表 = 帖子内容html.xpath(规则)
        规则二 = str(规则).replace("/tbody", "")
        IP列表 = IP列表 + (帖子内容html.xpath(规则二))

        # ========端口列表
        规则 = '//div[2]/div[2]/table/tbody/tr[*]/td[2]/text()'
        端口列表 = 帖子内容html.xpath(规则)
        规则二 = str(规则).replace("/tbody", "")
        端口列表 = 端口列表 + (帖子内容html.xpath(规则二))

        # ========代理类型列表
        代理类型列表 = ['http']*len(IP列表)


        # ========IP端口组列表

        print('IP列表数', len(IP列表))
        print('端口列表数', len(端口列表))
        print('代理类型列表', len(代理类型列表))
        if len(IP列表) != len(端口列表) and len(IP列表) != len(代理类型列表):
            print('ip端口数据组不匹配,结束程序')
            等待用户输入 = input("\n按下 enter 确认键后继续")
        for 代理类型, IP, 端口 in zip(代理类型列表, IP列表, 端口列表):
            IP端口 = "{}://{}:{}".format(代理类型, IP, 端口)  # '代入 '{}'
            self.待检测代理类型IP端口列表.append(IP端口)

    """===========文本读取与保存================"""
    def 模具一一读取文本代理IP(self):
        self.保存文本的IP端口列表=[]


        try:  # 调用异常处理
            文本 = open(r"E:\PY学习文件\BTT影视剧\py快捷方式\代理IP.txt", 'r', encoding='UTF-8')
            文本内容列表 = 文本.readlines()  # read() #全部读取   readlines每一行
        except UnicodeDecodeError as 异常原因:  # 异常处理
            print(异常原因)
            文本 = open(r"E:\PY学习文件\BTT影视剧\py快捷方式\代理IP.txt", 'r', encoding='gbk')
            文本内容列表 = 文本.readlines()  # read() #全部读取   readlines每一行
        else:  # 必须放在所有的except子句之后.这个子句将在try子句没有发生任何异常的时候执行.
            文本.close()


        for 行内容 in 文本内容列表:
            if '正常' in 行内容 and 'HTTP' in 行内容:
                行内容 = 行内容.replace(":正常", "")  # 替换   , 1) 次数 1 IP端口组 = 行内容.split(":")
                行内容 = 行内容.replace("\\n", "")
                #print('行内容',行内容)

                self.保存文本的IP端口列表.append(行内容)

            else:
                self.异常代理IP =self.异常代理IP+行内容

            self.待检测代理类型IP端口列表 = self.待检测代理类型IP端口列表 + self.保存文本的IP端口列表

    def 模具一一保存代理IP至文本(self,内容):
        文本 = open(r"E:\PY学习文件\BTT影视剧\py快捷方式\代理IP.txt", 'w', encoding='UTF-8')

        文本.write(内容)  # write 写入  read() #读取
        文本.close()
        print('保存至文本')

    def 模具一一追加保存代理IP至文本(self, 内容):
        文本 = open(r"E:\PY学习文件\BTT影视剧\py快捷方式\代理IP.txt", 'a', encoding='UTF-8')

        文本.write(内容)  # write 写入  read() #读取
        文本.close()
        print('追加,保存至文本')


    """============异步打开网页================"""
    def 模具一一网页列表示范例(self, url):

        条件循环 = 1
        while 条件循环 == 1:  # 条件循环  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            帖子链接分列表 = []
            for 页面提取帖子链接 in self.页面提取帖子链接列表[0:100]:
                帖子链接分列表.append(页面提取帖子链接)

            if len(self.页面提取帖子链接列表) > 99:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                del self.页面提取帖子链接列表[0:100]
            else:  # 否则
                条件循环 = 998

            self.模具一一异步调度(帖子链接分列表)  # self.返回网页一链接组列表

            倒计数 = len(self.返回网页一链接组列表)
            if 倒计数 == 0:
                return  # 返回

            for 返回网页一链接组 in self.返回网页一链接组列表:
                倒计数 = 倒计数 - 1

                self.帖子内容 = 返回网页一链接组[0]
                self.各帖子链接 = 返回网页一链接组[1]


    async def 模具一一异步设置代理打开网页(self, url,代理IP):

        # conn = aiohttp.TCPConnector(limit=10)  # 默认100,0表示无限
        async with aiohttp.ClientSession(headers=self.头部信息, connector=aiohttp.TCPConnector(limit=50)) as 会话:

            try:  # 调用异常处理,应对易发生错误的位置
                async with 会话.request("GET", url, proxy=代理IP, timeout=20) as 内容:  # "GET" 是个重要的请求方法
                    返回网页 = await 内容.text(
                        encoding="utf-8")  # 或者直接await r.read()不encoding='UTF-8',直接读取,适合于图像等无法encoding='UTF-8'文件

            except:  # () as 异常
                # print('网络异常等待', 异常)
                print('测试代理,异常')
                # time.sleep(6)
            else:
                if '[200 OK]' in str(内容):
                    print('====代理测试正常======')
                    self.正常代理IP列表.append(代理IP)
                else:  # 否则
                    pass

    def 模具一一设置代理异步调度(self):

        事件循环 = asyncio.get_event_loop()

        此时数 = int(time.time())
        if 此时数 > self.换IP时间计数 + 60:
            self.模具一一换ip连接()
            self.模具一一换头部信息()

        任务列表 = []
        百度网址= 'https://www.baidu.com'

        for 代理IP in self.待检测代理类型IP端口列表:
            if str(代理IP) in self.异常代理IP:
                continue  # 跳过当前循环,继续进行下一轮循环
            任务 = asyncio.ensure_future(self.模具一一异步设置代理打开网页(百度网址,代理IP))
            任务列表.append(任务)

        print('任务列表数',len(任务列表))
        if len(任务列表)==0:
            print('任务列表为空')
            等待用户输入 = input("\n按下 enter 确认键后继续")
        results = 事件循环.run_until_complete(asyncio.wait(任务列表))  # 等待任务完成
        # 事件循环.close()

    def 模具一一异步调度(self, 网址列表):
        self.返回网页一链接组列表 = []
        self.重新无序单网址列表= []

        事件循环 = asyncio.get_event_loop()

        self.此时数 = int(time.time())
        if self.此时数 > self.换IP时间计数 + 60:
            self.模具一一换ip连接()
            self.模具一一换头部信息()

        任务列表 = []

        for 各帖子链接 in 网址列表:
            任务 = asyncio.ensure_future(self.模具一一异步打开网页(各帖子链接))

            任务列表.append(任务)

        results = 事件循环.run_until_complete(asyncio.wait(任务列表))  # 等待任务完成
        # 事件循环.close()
        if len(self.重新无序单网址列表)> 0:

            self.模具一一gr无序网址列表请求返回网页内容(self.重新无序单网址列表)

    async def 模具一一异步打开网页(self, url):

        # conn = aiohttp.TCPConnector(limit=10)  # 默认100,0表示无限
        async with aiohttp.ClientSession(headers=self.头部信息, connector=aiohttp.TCPConnector(limit=10)) as 会话:

            try:  # 调用异常处理,应对易发生错误的位置
                async with 会话.request("GET", url) as 内容:  # "GET" 是个重要的请求方法
                    返回网页 = await 内容.text(
                        encoding="utf-8")  # 或者直接await r.read()不encoding='UTF-8',直接读取,适合于图像等无法encoding='UTF-8'文件

            except:  # () as 异常
                # print('网络异常等待', 异常)
                print('倒数6秒再连接', '次')
                # time.sleep(3)
            else:
                if '[200 OK]' in str(内容):
                    返回网页一链接组 = []
                    返回网页一链接组.append(返回网页)
                    返回网页一链接组.append(url)
                    self.返回网页一链接组列表.append(返回网页一链接组)

                else:  # 否则

                    self.重新无序单网址列表.append(url)



    """============多线打开网页,下载种子=================="""


    def 模具一一gr无序单网址请求返回网页内容(self, 单网址):  # grequests.imap(任务列
        单网址列表 = []
        单网址列表.append(单网址)

        单网址列表 = 单网址列表 * 3

        任务列表 = []
        for 各帖子链接 in 单网址列表:

                # if 各帖子链接 in self.过滤帖子网址:
                # continue  # 跳过当前循环,继续进行下一轮循环
            任务 = grequests.get(各帖子链接, headers=self.头部信息)  # timeout=len(任务列表)//2,
            任务列表.append(任务)

        条件循环 = 1
        次数循环 = 0
        while 条件循环 == 1:


            try:  # 调用异常处理,应对易发生错误的位置
                返回网页内容集 = grequests.imap(任务列表, size=5)  # size=3 并发数 3  gtimeout超时时间
            except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout,
                    requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout,
                    requests.exceptions.ChunkedEncodingError, requests.exceptions.InvalidSchema) as 异常:
                print('网络异常等待', 异常)
                print('倒数6秒再连接', 次数循环, '次')
                # time.sleep(3)
            else:

                for 返回网页内容 in 返回网页内容集:
                    返回网页内容文本 = str(返回网页内容)
                    if '<Response [200]>' in 返回网页内容文本:
                        # print('返回网页内容', 返回网页内容)
                        返回网页内容.encoding = "UTF-8"

                        return 返回网页内容  # 返回

    def 模具一一gr无序网址列表请求返回网页内容(self, 网址列表):  # grequests.imap(任务列

        self.模具一一高位换头部信息()
        self.模具一一换ip连接二()
        开始时间计数 = int(time.time())

        初始网址列表数=len(网址列表)
        print('gr无序网址列表请求返回网页内容数',初始网址列表数)
        print('gr无序网址列表', 网址列表)



        条件循环 = 1
        次数循环 = 0

        有效返回网页内容集 = []
        while 条件循环 == 1:
            网址列表数=len(网址列表)
            任务列表 = []
            for 各帖子链接 in 网址列表:
                # if 各帖子链接 in self.过滤帖子网址:
                # continue  # 跳过当前循环,继续进行下一轮循环
                任务 = grequests.get(各帖子链接, headers=self.头部信息)  # timeout=len(任务列表)//2,
                任务列表.append(任务)

            try:  # 调用异常处理,应对易发生错误的位置
                返回网页内容集 = grequests.imap(任务列表, size=5)  # size=3 并发数 3  gtimeout超时时间
            except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout,
                    requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout,
                    requests.exceptions.ChunkedEncodingError, requests.exceptions.InvalidSchema) as 异常:
                print('网络异常等待', 异常)
                print('倒数6秒再连接', 次数循环, '次')
                time.sleep(3)
            else:
                计数器=0


                for 返回网页内容 in 返回网页内容集:
                    返回网页内容文本 = str(返回网页内容)

                    if '<Response [200]>' in 返回网页内容文本 :
                        # print('返回网页内容', 返回网页内容)
                        有效返回网页内容集.append(返回网页内容)
                        网址列表.remove(返回网页内容.url)  # 删除指定元素

                        计数器 = 计数器 + 1
                此时数 = int(time.time())
                if 计数器==网址列表数 :
                    print('网址列表数，全部完成:')

                    条件循环 = 998
                elif 此时数 > self.换IP时间计数 + 初始网址列表数*2:
                    print('时间超时:网址列表数，未完成')
                    print('有效返回网页内容集:', len(有效返回网页内容集))
                    print('未完成网址列表数:', 初始网址列表数 - len(有效返回网页内容集))

                    条件循环 = 998

        for 返回网页内容 in 有效返回网页内容集:
            返回网页内容.encoding = "UTF-8"
            返回网页 = 返回网页内容.text
            返回网页一链接组 = []
            返回网页一链接组.append(返回网页)
            返回网页一链接组.append(返回网页内容.url)
            self.返回网页一链接组列表.append(返回网页一链接组)





        结束时间计数 = int(time.time())
        print('gr无序 用时计数:', 结束时间计数 - 开始时间计数, '秒')

if __name__ == '__main__':
    开始时间计数 = int(time.time())

    类=类一一维护代理IP()

    结束时间计数 = int(time.time())
    print('用时计数:', 结束时间计数 - 开始时间计数,'秒')

