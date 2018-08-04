
import asyncio # import 异步框架
import aiomysql  # import 异步数据库
import aiohttp # import 异步浏览器

import requests #人性化的 浏览器
import re  #正则表达式
import time #时间
import os #处理电脑系统文件和目录
import pymysql #mysql数据库
import random #随机数
from lxml import etree   #解析与定位网页
import datetime  # 时间



class 类_调度任务: #调用 类的模具 self.模具_数据库()
    def __init__(self):
        global 换IP时间计数 #时间计数全局变量声明
        换IP时间计数 = int(time.time()) + 60

        self.模具_进入置顶类型帖子()




    def 模具_启动异步任务(self):
        sem = asyncio.Semaphore(5)  # 设置Semaphore为4,说明在抓取时最多并发发出4个请求
        loop = asyncio.get_event_loop()

        任务组 = []  # 设置任务为一个列表
        self.模具_每日更新页面进入每个帖子()  # 收集进入每个帖子列表
        self.模具_过滤网址查找数据库()
        self.模具_已下载内容页网址()
        self.模具_过滤种子网址查找数据库()

        self.进入每个帖子列表 = self.进入每个帖子列表[0:10]

        运行类 = 类_执行任务(self.已下载内容页网址,self.过滤种子网址,self.过滤帖子网址)

        for 每个帖子网址 in self.进入每个帖子列表:  # 范围 range
            # 用format替换初始网址产生页数网址,将要代入hello模具,从而包装成一个任务

            任务 = asyncio.ensure_future(运行类.模具_每个帖子提取内容(每个帖子网址))
            任务组.append(任务)  # 每个任务都加入列表

        loop.run_until_complete(asyncio.wait(任务组))

    def 模具_换头部信息(self):  # 头部信息 def 函数模具内通行变量
        # nonlocal 头部信息  # def 函数模具内通行变量
        # global 头部信息  # def 函数模具内通行变量

        # {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'}  被BT网站墙了
        self.头部信息 = random.choice([{'User-Agent': 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'},
                              {
                                  'User-Agent': 'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},
                              {
                                  'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.9Safari/536.5'},
                              {
                                  'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.9Safari/536.5'},
                              {
                                  'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/535.24(KHTML,likeGecko)Chrome/19.0.1055.1Safari/535.24'},
                              {
                                  'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/535.24(KHTML,likeGecko)Chrome/19.0.1055.1Safari/535.24'},
                              {
                                  'User-Agent': 'Mozilla/5.0(X11;CrOSi6862268.111.0)AppleWebKit/536.11(KHTML,likeGecko)Chrome/20.0.1132.57Safari/536.11'},
                              {
                                  'User-Agent': 'Mozilla/5.0(X11;CrOSi6862268.111.0)AppleWebKit/536.11(KHTML,likeGecko)Chrome/20.0.1132.57Safari/536.11'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2;WOW64)AppleWebKit/537.1(KHTML,likeGecko)Chrome/19.77.34.5Safari/537.1'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2;WOW64)AppleWebKit/537.1(KHTML,likeGecko)Chrome/19.77.34.5Safari/537.1'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2;WOW64)AppleWebKit/535.24(KHTML,likeGecko)Chrome/19.0.1055.1Safari/535.24'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.6(KHTML,likeGecko)Chrome/20.0.1090.0Safari/536.6'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.6(KHTML,likeGecko)Chrome/20.0.1090.0Safari/536.6'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1062.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1062.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.1(KHTML,likeGecko)Chrome/22.0.1207.1Safari/537.1'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.1(KHTML,likeGecko)Chrome/22.0.1207.1Safari/537.1'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.6(KHTML,likeGecko)Chrome/20.0.1092.0Safari/536.6'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.6(KHTML,likeGecko)Chrome/20.0.1092.0Safari/536.6'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1063.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1063.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1062.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1062.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.0)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.36Safari/536.5'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.0)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.36Safari/536.5'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT5.1)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1063.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(Macintosh;IntelMacOSX10_8_0)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1063.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(Macintosh;IntelMacOSX10_8_0)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1063.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
                              {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
                              {
                                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko'},
                              {
                                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'},
                              {
                                  'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
                              {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'},
                              {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'},
                              {
                                  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},
                              {
                                  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
                              {
                                  'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)'},
                              {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)'},
                              {
                                  'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)'},
                              {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)'},
                              {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)'},
                              {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'},
                              {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'},
                              {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'}])
        print(self.头部信息)

    def 模具_进入置顶类型帖子(self):
        self.模具_换头部信息()
        打开的网址 = 'http://www.btbtt.net/index-index-page-1.htm'
        返回网页内容 = requests.post(打开的网址, headers=self.头部信息, timeout=3)
        帖子内容html = etree.HTML(返回网页内容.text)


        # for 帖子位置数 in range(2,6):  # 范围
        for 帖子位置数 in range(2, 3):
            规则 = "//*[@id=\"threadlist\"]/table[{}]/tbody/tr/td[1]/a[5]/@href".format(帖子位置数)  # 不换行 end=""
            规则 = str(规则).replace("/tbody", "")
            置顶类型帖子 = 帖子内容html.xpath(规则)
            self.置顶类型帖子网址 = 'http://www.btbtt.net/' + 置顶类型帖子[0]
            print('置顶类型帖子', 置顶类型帖子)
            self.模具_启动异步任务()


        # 美剧 = 剧集.类_剧集(置顶类型帖子列表[0])
        # 日韩剧 = 剧集.类_剧集(置顶类型帖子列表[1])
        # 国剧 = 剧集.类_剧集(置顶类型帖子列表[2])
        # 动漫= 剧集.类_动漫(置顶类型帖子列表[3])


    def 模具_打开的网址请求返回网页内容(self,网址):

        循环 = 0
        次数循环 = 0
        self.模具_换头部信息()
        while 循环 == 0:  # 条件循环
            if 次数循环==60: #  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                self.模具_换头部信息()
                self.模具_换ip连接()
                次数循环 = 0
            try:
                self.返回网页内容 = requests.post(网址, headers=self.头部信息, timeout=3)

            except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout,
                    requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout) as 异常:
                次数循环 += 1
                print('网络异常等待', 异常)
                print('倒数1秒再连接', 循环,'次')
                time.sleep(1)
            else:
                self.返回网页内容.encoding = "UTF-8"  # 转换encoding='UTF-8' "gbk"
                return#返回

    def 模具_每日更新页面进入每个帖子(self):
        self.模具_打开的网址请求返回网页内容(self.置顶类型帖子网址)

        帖子内容html = etree.HTML(self.返回网页内容.text)
        规则 = "//*[@id=\"body\"]/div/table[2]/tbody/tr[1]/td[3]/div[1]/table[*]//@href"
        规则 = str(规则).replace("/tbody", "")

        self.进入每个帖子列表 = 帖子内容html.xpath(规则)

        # = set(进入每个帖子列表)#转换为集合

    def 模具_过滤网址查找数据库(self):
        db = pymysql.connect("localhost", "root", "", "综合影视剧", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句
        sql = """SELECT 过滤网址 FROM 过滤网址;"""  # 数值条件查找后选取
        # 执行sql语句
        cursor.execute(sql)
        # 获取所有记录列表

        self.过滤帖子网址 = cursor.fetchall()
        self.过滤帖子网址 = str(self.过滤帖子网址)

        # 关闭数据库连接
        db.close()

    def 模具_已下载内容页网址(self):
        db = pymysql.connect("localhost", "root", "", "综合影视剧", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句
        sql = """SELECT 帖子链接 FROM 剧集"""  # 数值条件查找后选取
        # 执行sql语句
        cursor.execute(sql)
        # 获取所有记录列表
        self.已下载内容页网址 = cursor.fetchall()
        # self.已下载内容页网址 = str(self.已下载内容页网址)
        print('self.已下载内容页网址:', self.已下载内容页网址)

        # 关闭数据库连接
        db.close()

    def 模具_过滤种子网址查找数据库(self):
        db = pymysql.connect("localhost", "root", "", "综合影视剧", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句
        sql = """SELECT*FROM 过滤种子网址"""  # 数值条件查找后选取
        # 执行sql语句
        cursor.execute(sql)
        # 获取所有记录列表

        self.过滤种子网址 = cursor.fetchall()
        self.过滤种子网址 = str(self.过滤种子网址)

        # 关闭数据库连接
        db.close()

    def 模具_换头部信息(self):  # 头部信息 def 函数模具内通行变量

        # {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'}  被BT网站墙了
        self.头部信息 = random.choice(
            [{'User-Agent': 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'},
             {
                 'User-Agent': 'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},
             {
                 'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.9Safari/536.5'},
             {
                 'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.9Safari/536.5'},
             {
                 'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/535.24(KHTML,likeGecko)Chrome/19.0.1055.1Safari/535.24'},
             {
                 'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/535.24(KHTML,likeGecko)Chrome/19.0.1055.1Safari/535.24'},
             {
                 'User-Agent': 'Mozilla/5.0(X11;CrOSi6862268.111.0)AppleWebKit/536.11(KHTML,likeGecko)Chrome/20.0.1132.57Safari/536.11'},
             {
                 'User-Agent': 'Mozilla/5.0(X11;CrOSi6862268.111.0)AppleWebKit/536.11(KHTML,likeGecko)Chrome/20.0.1132.57Safari/536.11'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.2;WOW64)AppleWebKit/537.1(KHTML,likeGecko)Chrome/19.77.34.5Safari/537.1'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.2;WOW64)AppleWebKit/537.1(KHTML,likeGecko)Chrome/19.77.34.5Safari/537.1'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.2;WOW64)AppleWebKit/535.24(KHTML,likeGecko)Chrome/19.0.1055.1Safari/535.24'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.6(KHTML,likeGecko)Chrome/20.0.1090.0Safari/536.6'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.6(KHTML,likeGecko)Chrome/20.0.1090.0Safari/536.6'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1062.0Safari/536.3'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1062.0Safari/536.3'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.0Safari/536.3'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.0Safari/536.3'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.1(KHTML,likeGecko)Chrome/22.0.1207.1Safari/537.1'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.1(KHTML,likeGecko)Chrome/22.0.1207.1Safari/537.1'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.6(KHTML,likeGecko)Chrome/20.0.1092.0Safari/536.6'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.6(KHTML,likeGecko)Chrome/20.0.1092.0Safari/536.6'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1063.0Safari/536.3'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1063.0Safari/536.3'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1062.0Safari/536.3'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1062.0Safari/536.3'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.1)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.1)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.0)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.36Safari/536.5'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.0)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.36Safari/536.5'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT5.1)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1063.0Safari/536.3'},
             {
                 'User-Agent': 'Mozilla/5.0(Macintosh;IntelMacOSX10_8_0)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1063.0Safari/536.3'},
             {
                 'User-Agent': 'Mozilla/5.0(Macintosh;IntelMacOSX10_8_0)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1063.0Safari/536.3'},
             {
                 'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
             {
                 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
             {
                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko'},
             {
                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'},
             {
                 'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
             {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'},
             {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'},
             {
                 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},
             {
                 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
             {
                 'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)'},
             {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)'},
             {
                 'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)'},
             {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)'},
             {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)'},
             {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'},
             {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'},
             {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'}])
        print(self.头部信息)

    def 模具_换ip连接(self):
        # coding:gbk
        print('宽带连接进行时.....')
        os.system(r"rasphone -h 宽带连接")  # xxx0是你的拨号名称,xp下默认是"宽带连接”.
        os.system(r"rasdial 宽带连接 02007044432@163.gd  77341859")  # xxx0同上,xxx1 拨号用户名 ,xxx2拨号密码.
        time.sleep(3)
        print('换ip再连接完成')


class 类_执行任务():  # 调用 类的模具 self.模具_数据库()
    def __init__(self,已下载内容页网址,过滤种子网址,过滤帖子网址):

        #self.网址 = 每日更新页面网址
        self.过滤种子网址=过滤种子网址
        self.已下载内容页网址=已下载内容页网址
        self.过滤帖子网址=过滤帖子网址
        self.模具_换头部信息()


        #self.模具_启动异步任务()

    def 模具_符号清洗(self ,原文):
        列表 = ["\\xa0","[", "]", "\'", "\"", ":", "*", "/", "\\", "#", "\"", "?", ".", "\'", "'", "\'", "'", '', ',', ':', ':',
              '！', '\\n', '\n', '>', '<', '%', '?', ':', '｜', '|', '！']# 英中字符
        for 符号 in 列表:
            原文 = str(原文).replace(符号, '')
        原文 = "".join(原文.split())
        return 原文  # 返回


    def 模具_正文清洗(self):
        # ===========先去掉相同换行的字符=====================
        正文 =self.正文
        正文 = str(正文).replace("\'\\n-->\\n\\n\',", "")
        正文 = str(正文).replace("\\n", "")
        正文 = str(正文).replace("\\u3000", "")
        # ===========正文杂乱字符至行尾的整行处理===============
        规则列表 =['(?<=◎BT).{10,30}(?=\', \')', '(?<=上季).{1,}(?=\', \')', '(?<=迅雷).{1,}(?=\', \')', '(?<=百度网盘).{1,}(?=\', \')' ,'(?<=网盘下载).{1,}(?=\', \')', '(?<=http://pan.baidu.com).{1,}(?=\', \')',
                '(?<=https: /pan.baidu.com).{1,}(?=\', \')','(?<=ed2k:// ).{1,}(?=\', \')'
            , '(?<=https://yunpan.cn).{1,}(?=\', \')', '(?<=http://yunpan.cn).{1,}(?=\', \')',
                '(?<=ftp://).{1,}(?=\', \')','(?<=http:// www.bt).{1,}(?=\', \')'
            ,'(?<=magnet) .{1,}(?=\', \')', '(?<=磁力).{1,}(?=\', \')',
                '(?<=本帖最后由).{10}(?=\', \')', '(?<=迅雷).{1,}(?=\', \')']

        for 规则 in 规则列表:  # 范围 range

            正文 = re.sub(规则, '', str(正文))
        # ===========替换行尾,进行换行=====================
        正文 = str(正文).replace("\', \'", "\n")
        # ===========正文杂乱字符的处理===============
        杂乱字符列表=["◎BT","上季" , "迅雷","百 度网盘", "网盘下载 ","http ://pan. baidu.com","https://pan .baidu.com","ed2k://",
                  "https://yunpan.cn","http://yunp an.cn","ftp://","ht tp://www. bt","磁力","magnet ","本帖 最后由","\\x a0",
                "\'","\"", \
                  " \\","\"", "ufe ff",]

        for 字符 in 杂乱字符列表:  # 范围 range

            正文 = str(正文).replace(字符, "")

        self.正文 = str(正文)

    def 模具_种子名清洗(self):
        种子名规则 = '\[bt.{1,}\]'
        种子名 = re.sub(种子名规则, '', str(self.各链接名))
        种子名规则 = '\.bt.{1,}torrent'
        种子名 = re.sub(种子名规则, '.torrent', str(种子名))
        列表 = ["\\xa0", "\'", "\"", ":", "*", "/", "\\", "#", "\"", "?",':', '?', ':', '｜', '|', '！']
        for 符号 in 列表:
            种子名 = str(种子名).replace(符号, '')

        self. 种子名=种子名

    def 模具_帖子正文清洗(self):
        # 规则 = '(?<=648542).{1,}(?=BAIDU_CLB_SLOT_ID)'

        一楼内容 = str(self.帖子内容)
        规则 = '(?<=643755).{1,}(?=648546)'
        一楼内容列表 = re.findall(规则, str(一楼内容), re.S)
        一楼内容=一楼内容列表[0]
        规则列表 = ['(?<=◎BT).{1,300}(?=a>)', '(?<=上季).{1,}(?=</p>)', '(?<=<a href).{1,}(?=a>)',
                '(?<=</script>).{1,}(?=</script>)', '(?<=迅雷).{1,}(?=</p>)', '(?<=百度网盘).{1,}(?=</p>)',
                '(?<=百度网盘).{1,}(?=</p>)',
                '(?<=网盘下载).{1,}(?=</p>)', '(?<=http://pan.baidu.com).{1,}(?=</p>)',
                '(?<=https://pan.baidu.com).{1,}(?=</p>)',
                '(?<=ed2k://).{1,}(?=</p>)', '(?<=https://yunpan.cn).{1,}(?=</p>)',
                '(?<=http://yunpan.cn).{1,}(?=</p>)', '(?<=ftp://).{1,}(?=</p>)',
                '(?<=本帖).{1,50}(?=编辑)', '(?<=<i>).{1,}(?=i>)', '(?<=magnet).{1,}(?=</p>)',
                '(?<=磁力).{1,}(?=</p>)', '(?<=本帖最后由).{10}(?=</p>)', '(?<=迅雷).{1,}(?=</p>)', '(?<=链接).{1,300}(?=</p>)']
        for 规则 in 规则列表:
            一楼内容 = re.sub(规则, '', str(一楼内容))

        # ========字符替换=========
        列表 = ["迅雷", "百度网盘", "网盘下载", "http://pan.baidu.com", "https://pan.baidu.com", "ed2k://", "https://yunpan.cn",
              "http://yunpan.cn", "ftp://", "本帖最后由", "上季", "<scripttype=\"text/javascript\">BAIDU_CLB_SLOT_ID=\"",
              "<script type=\"text/javascript\">BAIDU_CLB_SLOT_ID = ",
              "◎BT", "之家整理", "</script>", "\'\";", "<ahrefa>", "a>", "BT之家", "本帖编辑", "<i>i>", "\\u3000", "\\n", "链接"]
        for 符号 in 列表:
            一楼内容 = str(一楼内容).replace(符号, '')
        一楼内容 = str(一楼内容).strip('\'')
        if 'src=\"/upload' in 一楼内容:
            一楼内容 = str(一楼内容).replace("/upload", "http://btbtt.co/upload")
        if 'HQC' in 一楼内容:
            次数 = 一楼内容.count('src=')
            if int(次数) > 1:
                规则 = '(?<=<img).{1,}(?=<img)'
                一楼内容 = re.sub(规则, '', str(一楼内容), count=1)
                一楼内容 = str(一楼内容).replace("<img", "")
                一楼内容 = str(一楼内容).replace("src", "<img src")
                一楼内容 = str(一楼内容).replace("HQC小组", "")
                一楼内容 = str(一楼内容).replace("[]的所有压制整合作品,均为小组成员合力精心制作.欢迎转载,但禁止私自取消小组的专用印记,需注明出处.", "")
        一楼内容 = str(一楼内容).replace("\'", "")
        self.帖子内容=str(一楼内容)

    def 模具_提取一楼种子名进行过滤(self):
        if '个附件' in str(self.帖子内容html).xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[1]/td[1]/text()'):
            一楼种子名列表 = str(self.帖子内容html).xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[*]/td[1]/a/text()')
            种子名列表文本 = str(一楼种子名列表)

            标记其它网站符号列表=['謦灵风软','风软','www.','.com','.net']
            for 字符 in 标记其它网站符号列表:  # 范围 range
                if 字符 in 种子名列表文本:
                    print('标记其它网站,跳过循环')
                    print('=====================')
                    self.模具_保存过滤帖子网址()
                    self.循环结束=0
                    return  # 返回None空值,跳过循环
        # 电影的过滤
        # 謦灵风软www.|.com|先版|鲜版|鲜版|删减版|TS|TC|抢先|清晰|公映版|网盘下载|电驴|迅雷|[email /span

    def 模具_短标题的再次清洗(self):
        短标题 = str(self.短标题).replace("] ", ']')
        if '][' in str(短标题):
            规则 = '(?<=\]\[).{1,}'
            短标题列表 = re.findall(规则, str(短标题))
            短标题 = 短标题列表[0]
        if '/' in str(短标题):
            # 规则5 = '(?<=/).{1,}'
            # 短标题4 = re.sub(规则4, '', str(短标题3))
            规则 = '/{1}'
            短标题 = re.sub(规则, '%', str(短标题), count=1)
            规则 = '.{1,}(?=%)'
            短标题列表= re.findall(规则, str(短标题))
            短标题=短标题列表[0]
        if '.' in str(短标题):
            规则 = '(?<=\.).{0,}'
            帖子标题 = re.sub(规则, '', str(短标题))
            帖子标题 = str(帖子标题).replace(".", '')
        elif ' ' in str(短标题):
            # 规则4 = '.*(?=)'
            规则 = '\s{1}'
            短标题 = re.sub(规则, '%', str(短标题), count=1)
            规则 = '.{1,}(?=%)'
            短标题列表 = re.findall(规则, str(短标题))
            短标题 = 短标题列表[0]

        if '第' in str(短标题):
            if '季' in str(短标题):

                规则 = '.{1,}(?=第)'
                短标题列表 = re.findall(规则, str(短标题))
                短标题 = 短标题列表[0]
        self.短标题=短标题

    def 模具_长标题(self):
        长标题规则 = '(?<=\]\[).{1,}'
        长标题 = re.findall(长标题规则, str(self.帖子标题))
        长标题 = str(长标题).replace("\'", "")
        if '][更' in str(长标题):
            规则 = '更\d{1,}集'
            长标题 = re.sub(规则, '', str(长标题))
        # 符号清洗
        长标题 = self.模具_符号清洗(长标题)

        assert len(长标题) ==0 , '长标题为空'
        # 长标题 = str(self.短标题)
        print('长标题', 长标题)
        self.帖子标题=长标题

    def 模具_换头部信息(self):  # 头部信息 def 函数模具内通行变量

        # {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'}  被BT网站墙了
        self.头部信息 = random.choice(
            [{'User-Agent': 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'},
             {
                 'User-Agent': 'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},
             {
                 'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.9Safari/536.5'},
             {
                 'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.9Safari/536.5'},
             {
                 'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/535.24(KHTML,likeGecko)Chrome/19.0.1055.1Safari/535.24'},
             {
                 'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/535.24(KHTML,likeGecko)Chrome/19.0.1055.1Safari/535.24'},
             {
                 'User-Agent': 'Mozilla/5.0(X11;CrOSi6862268.111.0)AppleWebKit/536.11(KHTML,likeGecko)Chrome/20.0.1132.57Safari/536.11'},
             {
                 'User-Agent': 'Mozilla/5.0(X11;CrOSi6862268.111.0)AppleWebKit/536.11(KHTML,likeGecko)Chrome/20.0.1132.57Safari/536.11'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.2;WOW64)AppleWebKit/537.1(KHTML,likeGecko)Chrome/19.77.34.5Safari/537.1'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.2;WOW64)AppleWebKit/537.1(KHTML,likeGecko)Chrome/19.77.34.5Safari/537.1'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.2;WOW64)AppleWebKit/535.24(KHTML,likeGecko)Chrome/19.0.1055.1Safari/535.24'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.6(KHTML,likeGecko)Chrome/20.0.1090.0Safari/536.6'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.6(KHTML,likeGecko)Chrome/20.0.1090.0Safari/536.6'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1062.0Safari/536.3'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1062.0Safari/536.3'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.0Safari/536.3'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.0Safari/536.3'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.1(KHTML,likeGecko)Chrome/22.0.1207.1Safari/537.1'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.1(KHTML,likeGecko)Chrome/22.0.1207.1Safari/537.1'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.6(KHTML,likeGecko)Chrome/20.0.1092.0Safari/536.6'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.6(KHTML,likeGecko)Chrome/20.0.1092.0Safari/536.6'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1063.0Safari/536.3'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1063.0Safari/536.3'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1062.0Safari/536.3'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1062.0Safari/536.3'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.1)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.1)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.0)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.36Safari/536.5'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.0)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.36Safari/536.5'},
             {
                 'User-Agent': 'Mozilla/5.0(WindowsNT5.1)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1063.0Safari/536.3'},
             {
                 'User-Agent': 'Mozilla/5.0(Macintosh;IntelMacOSX10_8_0)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1063.0Safari/536.3'},
             {
                 'User-Agent': 'Mozilla/5.0(Macintosh;IntelMacOSX10_8_0)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1063.0Safari/536.3'},
             {
                 'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
             {
                 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
             {
                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko'},
             {
                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'},
             {
                 'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
             {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'},
             {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'},
             {
                 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},
             {
                 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
             {
                 'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)'},
             {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)'},
             {
                 'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)'},
             {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)'},
             {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)'},
             {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'},
             {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'},
             {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'}])
        print(self.头部信息)

    def 模具_换ip连接(self):
        # coding:gbk
        print('宽带连接进行时.....')
        os.system(r"rasphone -h 宽带连接")  # xxx0是你的拨号名称,xp下默认是"宽带连接”.
        os.system(r"rasdial 宽带连接 02007044432@163.gd  77341859")  # xxx0同上,xxx1 拨号用户名 ,xxx2拨号密码.
        time.sleep(3)
        print('换ip再连接完成')
    def 模具_打开的网址请求返回网页内容(self,网址):

        循环 = 0
        次数循环 = 0
        self.模具_换头部信息()
        while 循环 == 0:  # 条件循环
            if 次数循环==60: #  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                self.模具_换头部信息()
                self.模具_换ip连接()
                次数循环 = 0
            try:
                self.返回内容 = requests.post(网址, headers=self.头部信息, timeout=3)

            except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout,
                    requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout) as 异常:
                次数循环 += 1
                print('网络异常等待', 异常)
                print('倒数1秒再连接', 循环,'次')
                time.sleep(1)
            else:
                self.返回内容.encoding = "UTF-8"  # 转换encoding='UTF-8' "gbk"
                self.返回内容=self.返回内容.text
                return#返回
    async def 模具_请求返回下载内容(self):

        循环 = 0
        次数循环 = 0

        while 循环 == 0:  # 条件循环
            if 次数循环==60: #  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                self.模具_换头部信息()
                self.模具_换ip连接()
                次数循环 = 0
            try:
                self.返回下载内容 = requests.post(self.下载地址, headers=self.头部信息, timeout=3)

            except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout,
                    requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout) as 异常:
                次数循环 += 1
                print('网络异常等待', 异常)
                print('倒数1秒再连接', 次数循环,'次')
                time.sleep(1)
            else:
                return#返回


    async def 模具_异步请求网页内容(self, 打开网址):
        global 换IP时间计数 #时间计数全局变量声明
        conn = aiohttp.TCPConnector(limit=5)  # 同时最大进行连接的连接数为9
        循环 = 0
        while 循环 == 0:  # 条件循环
            此时数 = int(time.time())
            if 此时数 > 换IP时间计数:
                换IP时间计数 = int(time.time()) + 60
                self.模具_换ip连接()
                self.模具_换头部信息()


            try:
                async with aiohttp.ClientSession() as 会话:

                    async with 会话.post(打开网址, headers=self.头部信息, timeout=3) as 返回内容:
                        self.返回内容=await 返回内容.text()
                        print('打开网址',打开网址)
                        # self.返回内容.encoding = "UTF-8"  # 转换encoding='UTF-8' "gbk"

            except (asyncio.TimeoutError,aiohttp.client_exceptions.ServerDisconnectedError,aiohttp.client_exceptions.ClientConnectorError) as 异常:
                print('异常原因',异常)
                print('网络异常,等待1秒重试')
                time.sleep(1)#等待10秒
            else:
                return  # 返回
    async def 模具_异步请求网页下载内容(self):
        global 换IP时间计数 #时间计数全局变量声明

        conn = aiohttp.TCPConnector(limit=5)  # 同时最大进行连接的连接数为9
        time.sleep(0.3)  # 等待10秒
        循环 = 0
        次数 = 0

        while 循环 == 0:  # 条件循环

            此时数 = int(time.time())

            if 此时数 > 换IP时间计数:
                换IP时间计数 = int(time.time()) + 60
                self.模具_换ip连接()
                self.模具_换头部信息()


            try:
                async with aiohttp.ClientSession() as 会话:

                    async with 会话.get(self.下载地址, headers=self.头部信息, timeout=3) as 返回下载内容:

                        self.返回下载内容 =await 返回下载内容.read()

            except (asyncio.TimeoutError,aiohttp.client_exceptions.ServerDisconnectedError,aiohttp.client_exceptions.ClientConnectorError) as 异常:
                print('异常原因',异常)

                print('self.下载地址2', self.下载地址)

                次数 += 1
                print('网络异常,等待0.5秒重试',次数,'次')
                self.返回下载内容 =0
                time.sleep(3)  # 等待10秒
                return  # 返回
            else:
                print('self.返回下载内容：',self.返回下载内容)
                return #返回


    def 模具_提取标题与过滤(self):

        self.帖子内容html = etree.HTML(self.返回内容)

        影视类型 = self.帖子内容html.xpath('//*[@id="forum_link"]/text()')
        帖子标题列表 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/h2/text()')
        self.标题前的栏目列表 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/h2/a/text()')



        列表 = ['[单集]', '[讨论]', '[Resilio-Sync]']
        for 符号 in 列表:
            if 符号 in str(self.标题前的栏目列表):
                print(符号, '过滤的栏目跳过循环')
                print('=====================')
                self.模具_保存过滤帖子网址()
                self.循环结束 = 0
                return  # 返回 跳过循环


        if '动漫' in 影视类型:  # 其它条件.
            if '[猪猪]' in str(self.标题前的栏目列表):
                print(符号, '过滤的栏目跳过循环')
                print('=====================')
                self.模具_保存过滤帖子网址()
                self.循环结束 = 0
                return  # 返回 跳过循环

        elif '电影' in 影视类型:  # 其它条件.
            列表 = ['删节版', '删减版', 'TS', '抢先', '抢鲜', 'TC', '清晰', '大陆', '中国', 'BT之家整合', '版块公告', '版块专用', '[猪猪]',
                  '[Resilio-Sync]']
            帖子标题 = str(帖子标题列表) + str(self.标题前的栏目列表)
            版本表 = ['抢', '删', '鲜']

            if '版' in 帖子标题:
                for 版符号 in 版本表:
                    if 版符号 in 帖子标题:
                        print(版符号, '版,跳过循环')
                        print('=====================')

                        self.模具_保存过滤帖子网址()
                        self.循环结束 = 0
                        return  # 返回 跳过循环
            for 符号 in 列表:
                if 符号 in 帖子标题:
                    print(符号, '列表符号,跳过循环')
                    print('=====================')

                    self.模具_保存过滤帖子网址()
                    self.循环结束 = 0
                    return  # 返回 跳过循环



        if len(帖子标题列表) > 1:
            帖子标题 = 帖子标题列表[-1]

        elif len(帖子标题列表) == 0:
            print('帖子标题列表0# 跳过循环')
            print('==================')
            assert len(帖子标题列表) == 0
            # return  # 返回 跳过循环
        else:
            帖子标题 = 帖子标题列表[0]
        self.帖子标题 = str(帖子标题)
        self.帖子标题2 = str(帖子标题)

    def 模具_提取标题图与过滤(self):
        标题图集 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]//img/@src')

        # ==========过滤无种子附件,跳过循环================================================
        if 'torrent.gif' not in str(self.返回内容):
            print('无种子附件,跳过循环')
            print('=====================')
            self.模具_保存过滤帖子网址()
            self.循环结束 = 0
            return  # 返回None空值,跳过循环
        elif len(标题图集) == 0:
            print('无标题图,跳过循环')
            self.模具_保存过滤帖子网址()
            print('=====================')
            self.循环结束 = 0
            return  # 返回None空值,跳过循环

        列表 = ['tietuku', 'yupoo', 'imgsrc.baidu']
        for 符号 in 列表:
            if 符号 in str(self.返回内容):
                print(符号, '图片已破or标记其它网站,跳过循环')
                print('=====================')
                self.模具_保存过滤帖子网址()
                self.循环结束 = 0
                return  # 返回None空值,跳过循环

        if 'HQC' in self.返回内容:
            if len(标题图集) == 1:
                标题图 = 标题图集[0]
                if 'http' not in str(标题图):
                    self.标题图 = str(标题图).replace("/upload", "http://www.btbtt.co/upload")
                    return  # 返回None空值,跳过循环

            else:
                标题图 = 标题图集[1]
                if 'http' not in str(标题图):
                    self.标题图 = str(标题图).replace("/upload", "http://www.btbtt.co/upload")
                    return  # 返回None空值,跳过循环

        标题图 = 标题图集[0]
        if 'http' not in str(标题图):
            self.标题图 = str(标题图).replace("/upload", "http://www.btbtt.co/upload")

    def 模具_提取一楼种子名进行过滤(self):
                if '个附件' in self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[1]/td[1]/text()'):
                    种子名列表文本 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[*]/td[1]/a/text()')
                    #种子名列表文本 = 一楼种子名列表
                    if ['謦灵风软', 'www.', '.com', '.net'] in 种子名列表文本:
                        print('标记其它网站,跳过循环')
                        print('=====================')
                        self.模具_保存过滤帖子网址()
                        self.循环结束 = 0
                        return  # 返回None空值,跳过循环
                # 电影的过滤
                # 謦灵风软www.|.com|先版|鲜版|鲜版|删减版|TS|TC|抢先|清晰|公映版|网盘下载|电驴|迅雷|[email /span

    def 模具_提取电视剧帖子标题(self):

        帖子标题 = self.帖子标题

        if '季]' in str(帖子标题):  # 最后为 单边[
            规则 = '(?<=季)].{0,}'
            帖子标题 = re.sub(规则, '', str(帖子标题))

        elif '全]' in str(帖子标题):  # 最后为 单边[
            规则 = '全].{0,}'
            帖子标题 = re.sub(规则, '', str(帖子标题))
            # 去掉最后一个 [ ]
            规则 = r'.{0,}(?=])'  # .*(文本)  *号是贪婪的,放置在最前方会消耗尽可能多的字符.
            帖子标题列表 = re.findall(规则, str(帖子标题))  # 提取 前面
            帖子标题 = 帖子标题列表[0]


        elif '集]' in str(帖子标题):  # 最后为 单边[
            规则 = '集].{0,}'
            帖子标题 = re.sub(规则, '', str(帖子标题))
            # 去掉最后一个 [ ]
            规则 = r'.{0,}(?=])'  # .*(文本)  *号是贪婪的,放置在最前方会消耗尽可能多的字符.
            帖子标题列表 = re.findall(规则, str(帖子标题))  # 提取 前面
            帖子标题 = 帖子标题列表[0]
        elif '][更' in str(帖子标题):  # 最后为 单边[
            规则 = r']\[更.{0,}'
            帖子标题 = re.sub(规则, '', str(帖子标题))
        规则 = '.{0,}\['
        self.帖子标题 = re.sub(规则, '', str(帖子标题))

    def 模具_长中短标题的再次清洗(self):
        短标题 = str(self.帖子标题)
        self.时间ID = int(time.strftime("%y%m%d%H%M%S", time.localtime()))
        if len(短标题) == 0:
            短标题 = str(self.时间ID)
        中短标题 = 短标题

        # =================短标题的再次清洗=========================================

        短标题 = str(短标题).replace("] ", ']')
        if '][' in str(短标题):
            a_规则3 = '(?<=\]\[).{1,}'
            短标题 = re.findall(a_规则3, str(短标题))
        if '/' in str(短标题):
            规则 = '/.{0,}'
            短标题 = re.sub(规则, '', str(短标题))
        if '.' in str(短标题):
            规则 = '\..{0,}'
            短标题 = re.sub(规则, '', str(短标题))
        elif ' ' in str(短标题):
            规则 = '\s.{0,}'
            短标题 = re.sub(规则, '', str(短标题))
        if '第' and '季' in str(短标题):
            规则 = '第.{0,}'
            短标题 = re.sub(规则, ''.str(短标题))

        # 符号清洗
        self.短标题 = self.模具_符号清洗(短标题)
        self.中短标题 = self.模具_符号清洗(中短标题)
        self.长标题 = self.模具_符号清洗(self.帖子标题)
        print('短标题', self.短标题)

        self.标题前栏目字符串 = ''.join(self.标题前的栏目列表)
        self.摘要 = '<h2>资源下载:<a href="/uploads/html/{}/{}.html"target="_blank">{}.torrent</a></h2>'.format(self.类型拼音目录,
                                                                                                          self.短标题,
                                                                                                          self.长标题)  # 不换行 end=""
        print('摘要', self.摘要)
        print('标题前栏目字符', self.标题前栏目字符串)

    def 模具_提取影视类型(self):
        self.影视类型 = self.帖子内容html.xpath('//*[@id="forum_link"]/text()')
        self.影视类型 = self.模具_符号清洗(self.影视类型)

        发帖时间 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[2]/td[3]/div/b[1]/text()')
        规则 = '\s.{0,}'
        星期数 = re.sub(规则, '', str(发帖时间))  # 替换   ,count=0,re.S|re.I

        星期数=星期数.strip('[')
        星期数 = 星期数.strip('\'')


        发贴时间列表 = 星期数.split("-")

        年 = int(发贴时间列表[0])
        月 = int(发贴时间列表[1])
        日 = int(发贴时间列表[2])
        # a=(datetime.strptime(发贴时间, "%w"
        today = int(time.strftime("%w"))
        星期数 = datetime.datetime(年, 月, 日).strftime("%w")
        print('星期数',星期数)


        if '剧集' in self.影视类型: #  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            self.影视类型
            self.主栏目ID = '22'
            self.类型拼音目录 = 'dianshiju'

            # 全部合集时 不载入'[连载]': '60',
            网站副栏目字典 = {'[连载]': '60,', '[美国]': '84,', '[英国]': '84,', '[大陆]': '85,', '[香港]': '86,', '[台湾]': '87,',
                       '[日本]': '88,',
                       '[韩国]': '89,',
                       '[法国]': '90,', '[多国]': '90,', '[印度]': '90,', '[西剧]': '90,', '[泰国]': '90,', '[加剧]': '84,',
                       '[意剧]': '90,',
                       '[澳剧]': '90,', '[德国]': '90,',
                       '[新马]': '90,', '[剧情]': '91,', '[喜剧]': '92,', '[爱情]': '93,', '[偶像]': '91,', '[动作]': '94,',
                       '[奇幻]': '95,',
                       '[科幻]': '96,',
                       '[悬疑]': '97,', '[罪案]': '97,', '[刑侦]': '97,', '[战争]': '98,', '[谍战]': '97,', '[军旅]': '98,',
                       '[历史]': '99,',
                       '[古装]': '99,', '[惊悚]': '100,', '[恐怖]': '100,', '[真人]': '101,', '[时装]': '91,',
                       '[医务]': '91,', '[歌舞]': '91,', '[其他]': '91,', '[都市]': '91,', '[情感]': '91,',
                       '[家庭]': '91,',
                       '[武侠]': '94,', '[纪录]': '102,', '[经典]': '103,', '[合 集]': '61,',
                       '[全集]': '61,', '[打包]': '61,', '[单集]': '61,', '[合集]': '61,', '[断载]': '61,', '[2006]': '117,',
                       '[2007]': '116,', '[2008]': '115,', '[2009]': '114,', '[2010]': '113,', '[2011]': '112,',
                       '[2012]': '111,',
                       '[2013]': '110,', '[2014]': '109,', '[2015]': '108,', '[2016]': '107,', '[2017]': '106,',
                       '[2018]': '105,',
                       '[更 早]': '104,'}

            网站副栏目ID10= [网站副栏目字典[x] if x in 网站副栏目字典 else x for x in self.标题前的栏目列表]
            网站副栏目ID = str(网站副栏目ID10)


            星期数字典 = {'1': '141', '2': '142', '3': '143', '4': '144', '5': '145', '6': '146', '7': '147'}
             
            for 字符 in 星期数字典:  # 范围 range
                
                if 字符 in 星期数: #  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                    网站副栏目ID2=星期数字典[字符]
                    break  # 结束循环

            #网站副栏目ID =str(网站副栏目ID) .strip(',')

            # 符号清洗
            #网站副栏目ID = self.模具_符号清洗(网站副栏目ID)

            #网站副栏目ID = 网站副栏目ID.strip(',')
            网站副栏目ID文本=''
            for 栏目ID in 网站副栏目ID10:  # 范围 range

                网站副栏目ID文本 =网站副栏目ID文本+str(栏目ID)

            if '[动画]' in 网站副栏目ID文本:

                if '88' in 网站副栏目ID文本:
                    网站副栏目ID文本 = 网站副栏目ID文本.replace("[动画]","118,")

                elif '85' in 网站副栏目ID文本:
                    网站副栏目ID文本 = 网站副栏目ID文本.replace("[动画]","119,")
                elif '84' in 网站副栏目ID文本:
                    网站副栏目ID文本 = 网站副栏目ID文本.replace("[动画]","120,")
                elif '87' in 网站副栏目ID文本:
                    网站副栏目ID文本 = 网站副栏目ID文本.replace("[动画]","")
                else:
                    网站副栏目ID文本 = 网站副栏目ID文本.replace("[动画]", "90,")

            网站副栏目ID文本 = 网站副栏目ID文本 + str(网站副栏目ID2)
            if len(网站副栏目ID文本) == 0:
                网站副栏目ID文本 = 91



            print('网站副栏目ID文本', 网站副栏目ID文本)
            self.网站副栏目ID=网站副栏目ID文本


            
        elif '电影' in self.影视类型:# 其它条件.
            self.主栏目ID = '21'
            self.类型拼音目录 = 'dying'
            网站副栏目字典 = {'[欧美]': '25,', '[美国]': '25,', '[英国]': '25,', '[大陆]': '26,', '[香港]': '27,', '[台湾]': '28,',
                       '[日本]': '29,',
                       '[韩国]': '30,',
                       '[法国]': '31,', '[多国]': '31,', '[印度]': '31,', '[犯罪]': '40,', '[西剧]': '31,', '[泰国]': '31,',
                       '[加剧]': '31,', '[意剧]': '31,', '[澳剧]': '31,', '[德国]': '31,',
                       '[新马]': '31,', '[剧情]': '34,', '[喜剧]': '33,', '[爱情]': '34,', '[偶像]': '34,', '[动作]': '32,',
                       '[奇幻]': '37,',
                       '[科幻]': '35,',
                       '[悬疑]': '40,', '[罪案]': '40,', '[刑侦]': '40,', '[战争]': '38,', '[谍战]': '40,', '[军旅]': '38,',
                       '[历史]': '39,',
                       '[古装]': '39,', '[惊悚]': '43,', '[恐怖]': '43,', '[真人]': '34,', '[时装]': '34,',
                       '[医务]': '34,', '[歌舞]': '34,', '[其他]': '44,', '[都市]': '34,', '[情感]': '34,',
                       '[家庭]': '34,',
                       '[武侠]': '39,', '[纪录]': '42,', '[经典]': '42,', '[动画]': '41,',
                       '[微电影]': '44,', '[同性]': '44,', '[其他]': '44,', '[合集]': '140,', '[系列]': '140,', '[2006]': '58,',
                       '[2007]': '57,', '[2008]': '56,', '[2009]': '55,', '[2010]': '54,', '[2011]': '53,',
                       '[2012]': '52,',
                       '[2013]': '51,', '[2014]': '50,', '[2015]': '49,', '[2016]': '48,', '[2017]': '47,',
                       '[2018]': '46,',
                       '[更 早]': '45,', '[更早]': '45,'}
            网站副栏目ID10 = [网站副栏目字典[x] if x in 网站副栏目字典 else x for x in self.标题前的栏目列表]
            网站副栏目ID = str(网站副栏目ID10)
            if '41' in str(网站副栏目ID):
                if '25' in str(网站副栏目ID):
                    网站副栏目ID = str((网站副栏目ID)).replace("25", "25,120")
                elif '29' in str(网站副栏目ID):
                    网站副栏目ID = str((网站副栏目ID)).replace("29", "29,118")

            网站副栏目ID文本 = ''
            for 栏目ID in 网站副栏目ID10:  # 范围 range

                网站副栏目ID文本 = 网站副栏目ID文本 + str(栏目ID)

            if '[动画]' in 网站副栏目ID文本:

                if '88' in 网站副栏目ID文本:
                    网站副栏目ID文本 = 网站副栏目ID文本.replace("[动画]", "118,")

                elif '85' in 网站副栏目ID文本:
                    网站副栏目ID文本 = 网站副栏目ID文本.replace("[动画]", "119,")
                elif '84' in 网站副栏目ID文本:
                    网站副栏目ID文本 = 网站副栏目ID文本.replace("[动画]", "120,")
                elif '87' in 网站副栏目ID文本:
                    网站副栏目ID文本 = 网站副栏目ID文本.replace("[动画]", "")
                else:
                    网站副栏目ID文本 = 网站副栏目ID文本.replace("[动画]", "90,")
            if len(网站副栏目ID文本) == 0:
                网站副栏目ID文本 =34
            网站副栏目ID文本 = str(网站副栏目ID文本).strip(',')
            print('网站副栏目ID文本', 网站副栏目ID文本)
            self.网站副栏目ID = 网站副栏目ID文本

        elif '动漫' in self.影视类型:  # 其它条件.
            self.主栏目ID = '23'
            self.类型拼音目录 = 'dongman'

            网站副栏目字典 = {'[连载]': '123,', '[合集]': '124,', '[美国]': '120,', '[英国]': '120,', '[大陆]': '119,', '[香港]': '119,',
                       '[台湾]': '119,',
                       '[日本]': '118,',
                       '[法国]': '120,', '[加剧]': '120,',
                       '[合 集]': '124,',
                       '[全集]': '124,', '[打包]': '124,', '[断载]': '124,', '[2006]': '137,',
                       '[2007]': '136,', '[2008]': '135,', '[2009]': '134,', '[2010]': '133,', '[2011]': '132,',
                       '[2012]': '131,',
                       '[2013]': '130,', '[2014]': '129,', '[2015]': '128,', '[2016]': '127,', '[2017]': '126,',
                       '[2018]': '125,',
                       '[更 早]': '138,', '[新番]': '124,', '[火影]': '124,', '[海贼]': '124,', '[柯南]': '124,', '[敢达]': '124,',
                       '[死神]': '124,', '[银魂]': '124,', '[妖尾]': '124,', '[龙珠]': '124,', '[布袋戏]': '124,', '[完结]': '124,',
                       '[其他]': '124,', '[音乐]': '139,'}
            网站副栏目ID10 = [网站副栏目字典[x] if x in 网站副栏目字典 else x for x in self.标题前的栏目列表]
            网站副栏目ID = str(网站副栏目ID10)
            星期数字典 = {'1': '148', '2': '149', '3': '150', '4': '151', '5': '152', '6': '153', '7': '154'}

            for 字符 in 星期数字典:  # 范围 range

                if 字符 in 星期数:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                    网站副栏目ID2 = 星期数字典[字符]
                    break  # 结束循环

            网站副栏目ID = str(网站副栏目ID).strip(',')
            网站副栏目ID文本 = ''
            for 栏目ID in 网站副栏目ID10:  # 范围 range

                网站副栏目ID文本 = 网站副栏目ID文本 + str(栏目ID)

            网站副栏目ID文本 = 网站副栏目ID文本 + str(网站副栏目ID2)
            if len(网站副栏目ID文本) == 0:
                网站副栏目ID文本 = 124
            print('网站副栏目ID文本', 网站副栏目ID文本)
            self.网站副栏目ID = 网站副栏目ID文本



    def 模具_更新集数(self):
        帖子标题 = self.帖子标题2

        if '集]' in str(帖子标题):
            规则 = '(?<=集]).{0,}'
            帖子标题 = re.sub(规则, '', str(帖子标题))

            规则 = '.{0,}]\['
            更新集数 = re.sub(规则, '', str(帖子标题))
            更新集数 = str(更新集数).replace("]", "")  # 替换   , 1) 次数 1

            print('更新集数:%s'%(更新集数))

            if len(更新集数) == 0:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                更新集数 = '合集'
        else:  # 否则
            更新集数 = '合集'

        self.更新集数 = 更新集数

    def 模具_提取帖子正文与清洗(self):

        #self.帖子内容html = etree.HTML(self.返回内容)


        一楼内容 = str(self.返回内容)

        规则 = '(?<=643755).{1,}(?=648546)'
        一楼内容 = re.findall(规则, str(一楼内容), re.S)
        规则列表 = ['(?<=◎BT).{1,300}(?=a>)', '(?<=上季).{1,}(?=</p>)', '(?<=<a href).{1,}(?=a>)',
                '(?<=</script>).{1,}(?=</script>)', '(?<=迅雷).{1,}(?=</p>)', '(?<=百度网盘).{1,}(?=</p>)',
                '(?<=百度网盘).{1,}(?=</p>)',
                '(?<=网盘下载).{1,}(?=</p>)', '(?<=http://pan.baidu.com).{1,}(?=</p>)',
                '(?<=https://pan.baidu.com).{1,}(?=</p>)',
                '(?<=ed2k://).{1,}(?=</p>)', '(?<=https://yunpan.cn).{1,}(?=</p>)',
                '(?<=http://yunpan.cn).{1,}(?=</p>)', '(?<=ftp://).{1,}(?=</p>)',
                '(?<=本帖).{1,50}(?=编辑)', '(?<=<i>).{1,}(?=i>)', '(?<=magnet).{1,}(?=</p>)',
                '(?<=磁力).{1,}(?=</p>)', '(?<=本帖最后由).{10}(?=</p>)', '(?<=迅雷).{1,}(?=</p>)', '(?<=链接).{1,300}(?=</p>)']
        for 规则 in 规则列表:
            一楼内容 = re.sub(规则, '', str(一楼内容))

        # ========字符替换=========
        列表 = ["迅雷", "百度网盘", "网盘下载", "http://pan.baidu.com", "https://pan.baidu.com", "ed2k://", "https://yunpan.cn",
              "http://yunpan.cn", "ftp://", "本帖最后由", "上季", "<scripttype=\"text/javascript\">BAIDU_CLB_SLOT_ID=\"",
              "<script type=\"text/javascript\">BAIDU_CLB_SLOT_ID = ",
              "◎BT", "之家整理", "</script>", "\'\";", "<ahrefa>", "a>", "BT之家", "本帖编辑", "<i>i>", "\\u3000", "\\n", "链接"]
        for 符号 in 列表:
            一楼内容 = str(一楼内容).replace(符号, '')
        一楼内容 = str(一楼内容).strip('\'')
        if 'src=\"/upload' in 一楼内容:
            一楼内容 = str(一楼内容).replace("/upload", "http://btbtt.co/upload")
        if 'HQC' in 一楼内容:
            次数 = 一楼内容.count('src=')
            if int(次数) > 1:
                规则 = '(?<=<img).{1,}(?=<img)'
                一楼内容 = re.sub(规则, '', str(一楼内容), count=1)
                一楼内容 = str(一楼内容).replace("<img", "")
                一楼内容 = str(一楼内容).replace("src", "<img src")
                一楼内容 = str(一楼内容).replace("HQC小组", "")
                一楼内容 = str(一楼内容).replace("[]的所有压制整合作品,均为小组成员合力精心制作.欢迎转载,但禁止私自取消小组的专用印记,需注明出处.", "")
        一楼内容 = str(一楼内容).replace("\'", "")
        self.正文=一楼内容

    async def 模具_提取每层种子(self):
        规则 = "//*[@id=\"body\"]/div/table[*]/tr/td[3]/div"
        规则 = str(规则).replace("/tbody", "")
        各层内容列表 = self.帖子内容html.xpath(规则)
        # 置顶类型帖子列表.append(置顶类型帖子)
        for 各层内容 in 各层内容列表:  # 范围

            各层内容html = etree.tostring(各层内容, encoding="unicode", method='html')
            各层内容文本 = str(各层内容html)

            if '个附件' not in str(各层内容html):  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                continue  # 跳过当前循环,继续进行下一轮循环
            if '天天' in str(各层内容html):
                continue  # 跳过循环
            if '风软' in str(各层内容html):
                continue  # 跳过循环

            各层内容html = etree.HTML(各层内容html)

            规则 = "//div/div[2]/table/tr[*]/td[1]/a"
            各层链接列表 = 各层内容html.xpath(规则)


            规则 = "//div/div[1]/p//text()"
            规则 = str(规则).replace("/tbody", "")
            各层名 = 各层内容html.xpath(规则)

            self.各层名 = 各层名[0]
            self.各层名 = self.模具_符号清洗(self.各层名)
            print('self.各层名',self.各层名)

            # =========== 种子目录================


            # =========== (模具)种子目录并下载================

            if '#1楼' in 各层内容文本:  # 其它条件.
                self.种子目录 = 'F:/电影模板/下载种子目录2/{}/剧名/季度/'.format(self.影视类型)  # 不换行 end=""

            else:
                self.种子目录 = 'F:/电影模板/下载种子目录2/{}/剧名/季度/{}/'.format(self.影视类型,self.各层名)
            for 各链接 in 各层链接列表:  # 范围 range
                各链接内容 = etree.tostring(各链接, encoding="unicode", method='html')
                各链接内容html = etree.HTML(各链接内容)
                规则 = "//text()"
                各链接名 = 各链接内容html.xpath(规则)
                self.各链接名 = 各链接名[0]

                格式列表=['.jpg','.npg']
                for 格式 in 格式列表:  # 范围 range
                    if 格式 in str(各链接名):  # 其它条件.
                        print('跳过图片下载')
                        break # 结束循环,or '\.npg'

                规则 = "//@href"
                各链接 = 各链接内容html.xpath(规则)
                各链接 = 各链接[0]

                下载地址 = str(各链接).replace("attach", "http://www.btbtt.net/attach")
                self.下载地址 = str(下载地址).replace("dialog", "download")
                
                if self.下载地址 in self.过滤种子网址: #  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                    print('跳过已过滤的下载种子')
                    return  # 返回
                await self.模具_建立目录并下载种子()

    async def 模具_建立目录并下载种子(self):

        # =========== 种子目录================
        # 种子目录 = 'F:/电影模板/下载种子目录2/电视剧/电视剧名/季度/'
        # F:/电影模板/下载种子目录2/动漫/动漫名/季度/
        '#F:/电影模板/下载种子目录2/电视剧/剧名/季度/分层名/'
        if '第'  in str(self.中短标题):
            if '季' in str(self.中短标题):
                短标题规则 = '第.{1,}季'
                #季度名 = re.sub(短标题规则, '', self.中短标题)
                季度名列表 = re.findall(短标题规则, str(self.中短标题))  # 提取列表
                季度名 = 季度名列表[0]
                季度名 = self.模具_符号清洗(季度名)
                种子目录 = str(self.种子目录).replace("剧名", str(self.短标题))
                种子目录 = str(种子目录).replace("季度", 季度名)
            else:
                种子目录 = str(self.种子目录).replace("剧名/季度", str(self.短标题))

        else:
            种子目录= str(self.种子目录).replace("剧名/季度", str(self.短标题))

        创建种子目录 = str(种子目录).strip('/')
        if not os.path.exists(创建种子目录):  # 必有条件选择,否则出错
            try:
                os.makedirs(创建种子目录)  # makedirs 创建多级目录文件夹,mkdir创建一个文件夹
            except (FileNotFoundError,OSError) as 异常原因:
                print('异常原因',异常原因)

        # =========== 种子下载=====
        self.模具_种子名清洗()

        目录与种子名 = str(种子目录) + str(self.种子名)

        if os.path.exists(目录与种子名):  # 避免重复
            print('跳过已存在种子')
            return  # 返回

        await self.模具_请求返回下载内容()

        if self.返回下载内容==0:  # 避免重复
            print('返回空值下载内容,跳过下载')
            return  # 返回

        try:
            with open(目录与种子名, 'wb') as fout:  #async

                fout.write(self.返回下载内容.content)# await   .content
                fout.close()


        except (FileNotFoundError, OSError)as 异常原因:
                assert len(异常原因)> 0,print(异常原因)
        else:#必须放在所有的except子句之后.这个子句将在try子句没有发生任何异常的时候执行.
            self.已下载种子网址列表.append(self.下载地址)

            self.过滤种子网址 =self.过滤种子网址 + str(self.下载地址)
            print('完成下载', 目录与种子名)


    async def 模具_保存内容至数据库(self):
        # 连接数据库
        conn = await aiomysql.connect(host='localhost', port=3306,user='root', password='',db="最新影视剧", charset="utf8")
        # 获取游标
        cur =await conn.cursor()


        try:  #剧集
            # 定义执行SQL  语句 为协程

            async with conn.cursor() as cur:

                await cur.execute("""INSERT INTO 剧集(影视类型,时间ID,长标题,短标题,主栏目ID,副栏目ID,摘要,正文,标题图,主演之标题前栏目字符串,文章来源之更新集数,帖子链接)
                                       VALUES ('%s','%d','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""\
                                             %(self.影视类型, self.时间ID, self.长标题, self.短标题, self.主栏目ID, self.网站副栏目ID, self.摘要,self.正文, self.标题图, self.标题前栏目字符串, self.更新集数, self.每个帖子网址))    #%(self.影视类型)

                # 提交至数据库执行

                await conn.commit()

        except Warning as 异常:#异常处理
            print('异常',异常 )
        #关闭数据库连接
            conn.close()



        for 已下载种子网址 in self.已下载种子网址列表:  # 范围 range
            try:  # 已下载种子网址列表
                # 定义执行SQL  语句 为协程

                async with conn.cursor() as cur:

                        await cur.execute("""INSERT INTO 过滤种子网址(过滤种子网址)
                                                      VALUES ('%s')""" % (已下载种子网址))  #

                        # 提交至数据库执行

                        await conn.commit()

            except Warning as 异常:  # 异常处理
                print('异常:', 异常)
                # 关闭数据库连接
                conn.close()



        print('保存至数据库完成')
        conn.close()

    async def 模具_保存过滤帖子网址(self):
        # 连接数据库
        conn = await aiomysql.connect(host='localhost', port=3306, user='root', password='', db="最新影视剧", charset="utf8")
        # 获取游标
        cur = await conn.cursor()
        try:  # 过滤网址
            # 定义执行SQL  语句 为协程

            async with conn.cursor() as cur:

                await cur.execute("""INSERT INTO 过滤网址(过滤网址)
                               VALUES ('%s')""" % (self.每个帖子网址))  # %(self.影视类型)


                # 提交至数据库执行
                print('提交至数据库执行..')
                await conn.commit()

        except Warning as 异常:  # 异常处理
            print('异常', 异常)
            # 关闭数据库连接
            conn.close()

        print('保存过滤网址至数据库完成')
        conn.close()

    #async def 模具_提取标题图与过滤(self):

    async def 模具_每个帖子提取内容(self,每个帖子网址):
        self.循环结束 = 1
        self.已下载种子网址列表=[]
        self.每个帖子网址=每个帖子网址
        if self.每个帖子网址 in self.过滤帖子网址:
            print('过滤帖子网址')
            return  # 返回 跳过循环
        print('各帖子链接', self.每个帖子网址)
        self.模具_打开的网址请求返回网页内容(self.每个帖子网址)
        self.模具_提取标题与过滤()
        if self.循环结束 == 0:
            return  # 返回 跳过循环
        self.模具_提取标题图与过滤()
        print('self.标题图',self.标题图)
        if self.循环结束 == 0:
            return  # 返回 跳过循环
        self.模具_提取一楼种子名进行过滤()
        if self.循环结束 == 0:
            return  # 返回 跳过循环

        self.模具_提取影视类型()
        self.模具_提取电视剧帖子标题()
        self.模具_长中短标题的再次清洗()
        self.模具_更新集数()
        self.模具_提取帖子正文与清洗()
        await self.模具_提取每层种子()

        if self.每个帖子网址 in str(self.已下载内容页网址):
            print('已经存在于数据库')
        else:# 否则
            await self.模具_保存内容至数据库()
            
        #await self.模具_()


类=类_调度任务()


