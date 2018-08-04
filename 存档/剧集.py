

import asyncio # import 异步框架
import aiomysql  # import 异步数据库
import aiohttp # import 异步浏览器

import requests #人性化的 浏览器
import re  #正则表达式
import time #时间
import os #处理电脑系统文件和目录
import pymysql #mysql数据库
import random #随机数
from lxml import etree#解析与定位网页
import datetime  # 时间
import 影视剧共库

class 类_剧集(影视剧共库.类_共用库): #调用 类的模具 self.模具_数据库()
    def __init__(self,每日更新页面网址):

        self.网址=每日更新页面网址
        self.换IP时间计数 = int(time.time()) + 60
        self.模具_每日更新页面进入每个帖子()


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
        self.模具_换头部信息()
        while 循环 == 0:  # 条件循环
            try:
                self.返回网页内容 = requests.post(网址,headers=self.头部信息,timeout=3)

            except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout,
                    requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout):
                print('网络异常等待')
                for 倒数 in range(60, 0, -10):
                    print('倒数', 倒数, '秒')
                    time.sleep(10)
                self.模具_换头部信息()
                self.模具_换ip连接()
            else:
                self.返回网页内容.encoding = "UTF-8"  # 转换encoding='UTF-8' "gbk"
                循环 = 1
    def 模具_每日更新页面进入每个帖子(self):
        self.模具_打开的网址请求返回网页内容(self.网址)


        帖子内容html = etree.HTML(self.返回网页内容.text)
        规则 = "//*[@id=\"body\"]/div/table[2]/tbody/tr[1]/td[3]/div[1]/table[*]//@href"
        规则 = str(规则).replace("/tbody", "")

        进入每个帖子列表 = 帖子内容html.xpath(规则)

        self.进入每个帖子列表 = set(进入每个帖子列表)

    
    def 模具_启动异步任务(self):
        sem = asyncio.Semaphore(10)  # 设置Semaphore为4,说明在抓取时最多并发发出4个请求
        loop = asyncio.get_event_loop()

        任务组 = []  # 设置任务为一个列表


        for 每个帖子网址 in self.进入每个帖子列表:  # 遍历页数
            # 用format替换初始网址产生页数网址,将要代入hello模具,从而包装成一个任务
            任务 = asyncio.ensure_future(self.模具_每个帖子提取内容(每个帖子网址))
            任务组.append(任务)  # 每个任务都加入列表

        loop.run_until_complete(asyncio.wait(任务组))


    async def 模具_异步请求网页内容(self,打开网址):
        此时数=int(time.time())
        
        if 此时数 > self.换IP时间计数:
            self.模具_换ip连接()
            self.换IP时间计数 = int(time.time()) + 60
        循环 = 0
        self.模具_换头部信息()
        while 循环 == 0:  # 条件循环
            try:

                async with aiohttp.get(打开网址, headers=self.头部信息, timeout=3) as 返回网页内容:
                    返回网页内容=await 返回网页内容.text()

            except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout,
                    requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout):
                print('网络异常等待')
                for 倒数 in range(60, 0, -10):
                    print('倒数', 倒数, '秒')
                    time.sleep(10)
                self.模具_换头部信息()
                self.模具_换ip连接()
            else:
                返回网页内容.encoding = "UTF-8"  # 转换encoding='UTF-8' "gbk"
                self.返回网页内容=返回网页内容
                self.帖子内容html = etree.HTML(返回网页内容)
                循环 = 1

    async def 模具_提取标题与过滤(self):
        帖子标题列表 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/h2/text()')
        self.标题前的栏目列表 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/h2/a/text()')

        列表 = ['[单集]', '[讨论]', '[Resilio-Sync]']
        for 符号 in 列表:
            if 符号 in str(self.标题前的栏目列表):
                print(符号, '过滤的栏目跳过循环')
                print('=====================')
                self.模具_保存过滤帖子网址(self.每个帖子网址)
                self.循环结束 =0
                break  # 结束符号列表循环
        if len(帖子标题列表) > 1:
            帖子标题 = 帖子标题列表[-1]

        elif len(帖子标题列表) == 0:
            print('帖子标题列表0# 跳过循环')
            print('==================')
            assert len(帖子标题列表) == 0
            #return  # 返回 跳过循环
        else:
            帖子标题 = 帖子标题列表[0]
        self.帖子标题 = str(帖子标题)

    async def 模具_提取标题图与过滤(self):
        标题图集 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]//img/@src')
        # ==========过滤无种子附件,跳过循环================================================
        if 'torrent.gif' not in str(self.帖子内容):
            print('无种子附件,跳过循环')
            print('=====================')
            self.模具_保存过滤帖子网址(self.每个帖子网址)
            self.循环结束 = 0
            return  # 返回None空值,跳过循环
        elif len(标题图集) == 0:
            print('无标题图,跳过循环')
            self.模具_保存过滤帖子网址(self.每个帖子网址)
            print('=====================')
            self.循环结束 = 0
            return  # 返回None空值,跳过循环

        列表 = ['tietuku', 'yupoo', 'imgsrc.baidu', '謦灵风软']
        for 符号 in 列表:
            if 符号 in str(self.帖子内容):
                print(符号, '图片已破or标记其它网站,跳过循环')
                print('=====================')
                self.模具_保存过滤帖子网址(self.每个帖子网址)
                self.循环结束 = 0
                return  # 返回None空值,跳过循环

        if 'HQC' in self.帖子内容:
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

    async def 模具_提取一楼种子名进行过滤(self):
        if '个附件' in str(self.帖子内容html).xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[1]/td[1]/text()'):
            一楼种子名列表 = str(self.帖子内容html).xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[*]/td[1]/a/text()')
            种子名列表文本 = str(一楼种子名列表)
            if ['謦灵风软', 'www.', '.com', '.net'] in 种子名列表文本:
                print('标记其它网站,跳过循环')
                print('=====================')
                self.模具_保存过滤帖子网址(self.每个帖子网址)
                self.循环结束 = 0
                return  # 返回None空值,跳过循环
        # 电影的过滤
        # 謦灵风软www.|.com|先版|鲜版|鲜版|删减版|TS|TC|抢先|清晰|公映版|网盘下载|电驴|迅雷|[email /span
    async def 模具_提取电视剧帖子标题(self):

        帖子标题=self.帖子标题

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
    async def 模具_长中短标题的再次清洗(self):
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
        if '第'and  '季' in str(短标题):
            规则 = '第.{0,}'
            短标题 = re.sub(规则,''.str(短标题))

        # 符号清洗
        self.短标题 =self.模具_符号清洗(短标题)
        self.中短标题 =self.模具_符号清洗(中短标题)
        self.长标题 = self.模具_符号清洗(self.帖子标题)
        print('短标题',self.短标题)


        self.标题前栏目字符串 = ''.join(self.标题前的栏目列表)
        self.摘要 = '<h2>资源下载:<a href="/uploads/html/{}/{}.html"target="_blank">{}.torrent</a></h2>'.format(self.类型拼音目录,self.短标题,self.长标题)  # 不换行 end=""
        print('摘要', self.摘要)
        print('标题前栏目字符', self.标题前栏目字符串)

    async def 模具_提取影视类型(self):
        self.影视类型 = self.帖子内容html.xpath('//*[@id="forum_link"]/text()')
        类型字典 ={'电影':'21','剧集':'22','动漫':'23'}
        类型拼音目录字典 = {'电影': 'dying', '剧集': 'dianshiju', '动漫': 'dongman'}
         
        for 字符 in 类型字典:  # 范围 range
            if self.影视类型 in 字符: #  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                self.主栏目ID = 类型字典[字符]
        for 字符 in 类型拼音目录字典:  # 范围 range
            if self.影视类型 in 字符: #  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                self.类型拼音目录 = 类型拼音目录字典[字符]



    async def 模具_更新集数(self):
        帖子标题=self.帖子标题
        if '集]' in str(帖子标题):
            规则 = '(?<=集]).{0,}'
            帖子标题 = re.sub(规则, '', str(帖子标题))
            规则 = '.{0,}]\['
            更新集数 = re.sub(规则, '', str(帖子标题))
            更新集数 = str(更新集数).replace("]", "")  # 替换   , 1) 次数 1
            
            if len(更新集数)==0: #  break # 结束循环 continue # 跳过当前循环，继续进行下一轮循环
                更新集数 = '合集'

        self.更新集数 = 更新集数

    async def 模具_提取标题图与过滤(self):
    async def 模具_提取标题图与过滤(self):



    async def 模具_每个帖子提取内容(self,每个帖子网址):
        self.循环结束=1
        if self.每个帖子网址 in self.过滤帖子网址:
            print('过滤帖子网址')
            return # 返回 跳过循环
        print('各帖子链接', self.每个帖子网址)

        await self.模具_异步请求网页内容(self.每个帖子网址)
        await self.模具_提取影视类型()
        await self.模具_提取标题与过滤()
        if self.循环结束 ==0:
            return  # 返回 跳过循环
        await self.模具_提取标题图与过滤()
        if self.循环结束 ==0:
            return  # 返回 跳过循环
        await self.模具_提取一楼种子名进行过滤()
        if self.循环结束 ==0:
            return  # 返回 跳过循环
        await self.模具_提取电视剧帖子标题()
        await self.模具_长中短标题的再次清洗()
        await self.模具_更新集数()
        await self.模具_()
        await self.模具_()
        await self.模具_()
        await self.模具_()
        await self.模具_()
        await self.模具_()












        