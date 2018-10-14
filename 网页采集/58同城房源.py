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
import xlwt  # 写入Excel文件

import win32api  # 操作本地文件

"""


"""


class 类一一公共库:  # 调用 类的模具 self.模具一一数据库()
    def __init__(self):

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
        self.头部信息 = 头部信息

        print('更换浏览器信息', self.头部信息['User-Agent'])

    def 模具一一换ip连接(self):
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
                返回网页内容 = requests.get('https://www.163.com/', headers=self.头部信息, timeout=3)
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

                    print('等待60秒')

                    time.sleep(60)

    """============异步打开网页================"""

    def 模具一一gr无序网址列表请求返回网页内容(self, 网址列表, 分流数=100):  # grequests.imap(任务列

        初始网址列表数 = len(网址列表)

        条件循环 = 1
        次数循环 = 0
        返回网页一链接组列表 = []

        有效返回网页内容集 = []
        while 条件循环 == 1:
            time.sleep(2)  # 等待
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
                返回网页内容集 = grequests.imap(任务列表, size=3)  # size=3 并发数 3  gtimeout超时时间
            except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout,
                    requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout,
                    requests.exceptions.ChunkedEncodingError, requests.exceptions.InvalidSchema) as 异常:

                print('倒数6秒再连接', 次数循环, '次')
                time.sleep(3)
            else:
                计数器 = 0
                for 返回网页内容 in 返回网页内容集:
                    网页内容文本 = str(返回网页内容)

                    if '<Response [200]>' in 网页内容文本 and "访问过于频繁" not in 返回网页内容.text:
                        # print('返回网页内容', 返回网页内容)
                        有效返回网页内容集.append(返回网页内容)
                        print('成功采集网页：', 返回网页内容.url)
                        # 返回网页内容.url= 返回网页内容.url.strip('/')  # 默认则是去除空格

                        # 网址列表.remove(返回网页内容.url)  # 删除指定元素

                        计数器 = 计数器 + 1
                    else:  # 否则
                        网址列表.append(返回网页内容.url)

                此时数 = int(time.time())
                if len(网址列表) == 0:

                    条件循环 = 998
                elif 此时数 > self.换IP时间计数 + 初始网址列表数 * 3:

                    条件循环 = 998

        for 返回网页内容 in 有效返回网页内容集:
            返回网页内容.encoding = "UTF-8"

            返回网页一链接组 = []
            返回网页一链接组.append(返回网页内容)
            返回网页一链接组.append(返回网页内容.url)
            返回网页一链接组列表.append(返回网页一链接组)

        return 返回网页一链接组列表  # 返回

    """============测试库================"""


class 类一一58同城房源(类一一公共库):  # 调用 类的模具 self.模具一一数据库()
    def __init__(self):
        开始时间计数 = int(time.time())
        self.模具一一高位换头部信息()
        self.模具一一列表页面()
        self.模具一一提取各页面链接()
        self.模具一一提取页面详情各项内容()
        # self.模具一一列表页面()
        结束时间计数 = int(time.time())
        print('用时计数:', 结束时间计数 - 开始时间计数, '秒')

    def 模具一一列表页面(self):
        页数网址列表 = []
        for 页数 in range(1, 4):
            页数网址 = 'https://nj.58.com/ershoufang/0/pn{}'.format(str(页数))  # '代入 '{}'
            页数网址列表.append(页数网址)

        print('采集页数：', len(页数网址列表))
        self.各页面链接网页内容组列表 = self.模具一一gr无序网址列表请求返回网页内容(页数网址列表, 3)  # 返回 self.返回网页一链接组列表

    def 模具一一提取各页面链接(self):
        页面链接总列表 = []

        for 返回网页一链接组 in self.各页面链接网页内容组列表:
            返回网页内容 = 返回网页一链接组[0]

            帖子内容html = etree.HTML(返回网页内容.text)  #

            # ========页面链接
            规则 = '/html/body/div[5]/div[5]/div[1]/ul/li[*]/div[2]/h2/a/@href'
            页面链接列表 = 帖子内容html.xpath(规则)
            for 页面链接 in 页面链接列表:

                if 'https://nj.58.com/ershoufang' in 页面链接:
                    页面链接总列表.append(页面链接)

        页面链接总列表 = list(set(页面链接总列表))
        print('待采集页面数：', len(页面链接总列表))

        self.页面详情各项内容组列表 = self.模具一一gr无序网址列表请求返回网页内容(页面链接总列表)  # 返回 self.返回网页一链接组列表

    def 模具一一提取文本清洗(self, 文本列表):

        try:  # 调用异常处理,应对易发生错误的位置
            文本 = 文本列表[0]
        except (IndexError) as 异常原因:  # 异常处理
            文本 = str(文本列表)

        文本 = 文本.replace("\n", "")  # 替换   , 1) 次数 1
        文本 = 文本.replace("[]", "")  # 替换   , 1) 次数 1
        文本 = 文本.strip()  # 默认则是去除空格
        return 文本  # 返回

    def 模具一一提取页面详情各项内容(self):
        self.模具一一写入Excel文件字段名()
        self.行计数 = 0
        print('成功采集页内容数：', len(self.页面详情各项内容组列表))
        for 返回网页一链接组 in self.页面详情各项内容组列表:
            self.行计数 = self.行计数 + 1
            返回网页内容 = 返回网页一链接组[0]
            self.采集网址 = 返回网页一链接组[1]
            帖子内容html = etree.HTML(返回网页内容.text)  #

            # =========提取页面详情
            print('===============================================')
            print('采集序号:', self.行计数)

            # ========标题
            规则 = '/html/body/div[4]/div[1]/h1/text()'
            self.标题 = 帖子内容html.xpath(规则)
            self.标题 = self.模具一一提取文本清洗(self.标题)
            print('标题:', self.标题)

            # ========总价
            规则 = '/html/body/div[4]/div[2]/div[2]/p/span[1]/text()'
            self.总价 = 帖子内容html.xpath(规则)
            self.总价 = self.模具一一提取文本清洗(self.总价)
            print('总价:', self.总价)

            # ========单价
            规则 = '/html/body/div[4]/div[2]/div[2]/p/span[2]/text()'
            self.单价 = 帖子内容html.xpath(规则)
            self.单价 = self.模具一一提取文本清洗(self.单价)
            print('单价:', self.单价)

            # ========房本面积一平
            规则 = '/html/body/div[4]/div[2]/div[2]/div[1]/p[2]/span[1]/text()'
            self.房本面积一平 = 帖子内容html.xpath(规则)
            self.房本面积一平 = self.模具一一提取文本清洗(self.房本面积一平)
            print('房本面积一平:', self.房本面积一平)

            # ========小区
            规则 = '/html/body/div[4]/div[2]/div[2]/ul/li[1]/span[2]/text()'
            self.小区 = 帖子内容html.xpath(规则)
            self.小区 = self.模具一一提取文本清洗(self.小区)
            print('小区:', self.小区)

            # ========位置
            规则 = '/html/body/div[4]/div[2]/div[2]/ul/li[2]/span[2]/a[1]/text()'
            self.位置 = 帖子内容html.xpath(规则)
            self.位置 = self.模具一一提取文本清洗(self.位置)
            print('位置:', self.位置)

            # ================概况
            # ========房屋总价
            规则 = '//*[@id="generalSituation"]/div/ul[1]/li[1]/span[2]/text()'
            self.房屋总价 = 帖子内容html.xpath(规则)
            self.房屋总价 = self.模具一一提取文本清洗(self.房屋总价)
            print('房屋总价:', self.房屋总价)

            # ========所在楼层
            规则 = '//*[@id="generalSituation"]/div/ul[2]/li[1]/span[2]/text()'
            self.所在楼层 = 帖子内容html.xpath(规则)
            self.所在楼层 = self.模具一一提取文本清洗(self.所在楼层)
            print('所在楼层:', self.所在楼层)

            # ========房屋户型
            规则 = '//*[@id="generalSituation"]/div/ul[1]/li[2]/span[2]/text()'
            self.房屋户型 = 帖子内容html.xpath(规则)
            self.房屋户型 = self.模具一一提取文本清洗(self.房屋户型)
            print('房屋户型:', self.房屋户型)

            # ========装修情况
            规则 = '//*[@id="generalSituation"]/div/ul[2]/li[2]/span[2]/text()'
            self.装修情况 = 帖子内容html.xpath(规则)
            self.装修情况 = self.模具一一提取文本清洗(self.装修情况)
            print('装修情况:', self.装修情况)

            # ========房本面积一m
            规则 = '//*[@id="generalSituation"]/div/ul[1]/li[3]/span[2]/text()'
            self.房本面积一m = 帖子内容html.xpath(规则)
            self.房本面积一m = self.模具一一提取文本清洗(self.房本面积一m)
            print('房本面积一m:', self.房本面积一m)

            # ========产权年限
            规则 = '/html/body/div[4]/div[1]/h1/text()'
            self.产权年限 = 帖子内容html.xpath(规则)
            self.产权年限 = self.模具一一提取文本清洗(self.产权年限)
            print('产权年限:', self.产权年限)

            # ========房屋朝向
            规则 = '//*[@id="generalSituation"]/div/ul[1]/li[4]/span[2]/text()'
            self.房屋朝向 = 帖子内容html.xpath(规则)
            self.房屋朝向 = self.模具一一提取文本清洗(self.房屋朝向)
            print('房屋朝向:', self.房屋朝向)

            # ================描述
            # ========核心卖点
            规则 = '//*[@id="generalDesc"]/div/div/p/text()'
            self.核心卖点 = 帖子内容html.xpath(规则)
            self.核心卖点 = self.模具一一提取文本清洗(self.核心卖点)
            print('核心卖点:', self.核心卖点)

            # ================费用
            # ========费用一房屋总价
            规则 = '//*[@id="generalExpense"]/div/ul[1]/li[1]/span[2]/text()'
            self.费用一房屋总价 = 帖子内容html.xpath(规则)
            self.费用一房屋总价 = self.模具一一提取文本清洗(self.费用一房屋总价)
            print('费用一房屋总价:', self.费用一房屋总价)

            # ========参考首付
            规则 = '//*[@id="generalExpense"]/div/ul[2]/li/span[2]/text()'
            self.参考首付 = 帖子内容html.xpath(规则)
            self.参考首付 = self.模具一一提取文本清洗(self.参考首付)
            print('参考首付:', self.参考首付)

            # ========房屋类型
            规则 = '//*[@id="generalExpense"]/div/ul[1]/li[2]/span[2]/text()'
            self.房屋类型 = 帖子内容html.xpath(规则)
            self.房屋类型 = self.模具一一提取文本清洗(self.房屋类型)
            print('房屋类型:', self.房屋类型)

            # ========交易权属
            规则 = '//*[@id="generalExpense"]/div/ul[1]/li[3]/span[2]/text()'
            self.交易权属 = 帖子内容html.xpath(规则)
            self.交易权属 = self.模具一一提取文本清洗(self.交易权属)
            print('交易权属:', self.交易权属)

            # ========户型图
            self.户型图列表 = []
            规则 = '//div/ul/li[*]/img/@src'
            self.户型图列表 = 帖子内容html.xpath(规则)
            # print('户型图列表:', self.户型图列表)
            print('户型图列表数:', len(self.户型图列表))
            # self.户型图列表.append(行内容)

            # =====填充Exce
            self.模具一一填充Excel文件值()

        self.模具一一保存Excel文件()

    def 模具一一写入Excel文件字段名(self):

        # 创建 xls 文件对象  设置encoding='UTF-8'
        self.文件操作 = xlwt.Workbook(encoding='utf-8')
        # 新增一个表单
        self.表单操作 = self.文件操作.add_sheet('58同城房源工作表')
        # 写入excel

        # 参数对应 行, 列, 值
        self.表单操作.write(0, 0, label='标题')  # write 写入
        self.表单操作.write(0, 1, label='总价')  # write 写入
        self.表单操作.write(0, 2, label='单价')  # write 写入
        self.表单操作.write(0, 3, label='房本面积一平')  # write 写入
        self.表单操作.write(0, 4, label='小区')  # write 写入
        self.表单操作.write(0, 5, label='位置')  # write 写入

        self.表单操作.write(0, 6, label='房屋总价')  # write 写入
        self.表单操作.write(0, 7, label='所在楼层')  # write 写入
        self.表单操作.write(0, 8, label='房屋户型')  # write 写入
        self.表单操作.write(0, 9, label='装修情况')  # write 写入
        self.表单操作.write(0, 10, label='房本面积一m')  # write 写入
        self.表单操作.write(0, 11, label='产权年限')  # write 写入
        self.表单操作.write(0, 12, label='房屋朝向')  # write 写入
        self.表单操作.write(0, 13, label='核心卖点')  # write 写入
        self.表单操作.write(0, 14, label='费用一房屋总价')  # write 写入
        self.表单操作.write(0, 15, label='参考首付')  # write 写入
        self.表单操作.write(0, 16, label='房屋类型')  # write 写入
        self.表单操作.write(0, 17, label='交易权属')  # write 写入
        self.表单操作.write(0, 18, label='户型图列表')  # write 写入
        self.表单操作.write(0, 19, label='采集网址')  # write 写入

    def 模具一一填充Excel文件值(self):

        # 写入excel

        # 参数对应 行, 列, 值
        self.表单操作.write(self.行计数, 0, label=self.标题)  # write 写入
        self.表单操作.write(self.行计数, 1, label=self.总价)  # write 写入
        self.表单操作.write(self.行计数, 2, label=self.单价)  # write 写入
        self.表单操作.write(self.行计数, 3, label=self.房本面积一平)  # write 写入
        self.表单操作.write(self.行计数, 4, label=self.小区)  # write 写入
        self.表单操作.write(self.行计数, 5, label=self.位置)  # write 写入
        self.表单操作.write(self.行计数, 6, label=self.房屋总价)  # write 写入
        self.表单操作.write(self.行计数, 7, label=self.所在楼层)  # write 写入
        self.表单操作.write(self.行计数, 8, label=self.房屋户型)  # write 写入
        self.表单操作.write(self.行计数, 9, label=self.装修情况)  # write 写入
        self.表单操作.write(self.行计数, 10, label=self.房本面积一m)  # write 写入
        self.表单操作.write(self.行计数, 11, label=self.产权年限)  # write 写入
        self.表单操作.write(self.行计数, 12, label=self.房屋朝向)  # write 写入
        self.表单操作.write(self.行计数, 13, label=self.核心卖点)  # write 写入
        self.表单操作.write(self.行计数, 14, label=self.费用一房屋总价)  # write 写入
        self.表单操作.write(self.行计数, 15, label=self.参考首付)  # write 写入
        self.表单操作.write(self.行计数, 16, label=self.房屋类型)  # write 写入
        self.表单操作.write(self.行计数, 17, label=self.交易权属)  # write 写入
        self.表单操作.write(self.行计数, 18, label=self.户型图列表)  # write 写入
        self.表单操作.write(self.行计数, 19, label=self.采集网址)  # write 写入

    def 模具一一保存Excel文件(self):
        # 保存文件
        self.文件操作.save('58同城房源.xls')
        print('成功保存,58同城房源.xls')


if __name__ == '__main__':
    类 = 类一一58同城房源()