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


class 类一一公共库:  # 调用 类的模具 self.模具一一数据库()
    def __init__(self):
        选取列中唯一不同的值 = 'SELECT DISTINCT A列 FROM 中文表;'  # 在表中,一个列可能会包含多个重复值,
        # 有时您也许希望仅仅列出不同(distinct)的值.DISTINCT 关键词用于返回唯一不同的值.

    """==========最新影视剧数据库=========================="""
    def 模具一一提取电影与合集数据库里的过滤网址一已下载内容网址一过滤种子网址(self):
        # 提取数据库里的过滤网址
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "", "电影与合集", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # SQL 查询语句
        sql = "SELECT 过滤网址 FROM 过滤网址"
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        过滤帖子网址 = cursor.fetchall()
        过滤帖子网址 = str(过滤帖子网址)

        # SQL 查询语句
        sql = "SELECT `帖子链接` FROM `网站文章内容` WHERE 影视类型='%s'" % (self.影视类型)
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        帖子链接 = cursor.fetchall()
        self.过滤帖子网址 = 过滤帖子网址 + str(帖子链接)




    def 模具一一提取最新影视剧数据库里的过滤网址(self):
        # 提取数据库里的过滤网址
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "", "最新影视剧", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句
        sql = "SELECT 过滤网址 FROM 过滤网址"
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        过滤帖子网址 = cursor.fetchall()
        self.过滤帖子网址二 = str(过滤帖子网址)
        # 关闭数据库连接
        db.close()

    def 模具一一保存电影与合集过滤帖子网址(self):
        # 打开数据库连接,保存已下载网址
        db = pymysql.connect("localhost", "root", "", "电影与合集", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句
        sql = """INSERT INTO 过滤网址(过滤网址)
                   VALUES ('%s')""" % (self.各帖子链接)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            db.rollback()
        # 关闭数据库连接
        db.close()

    def 模具一一保存电影与合集总提取帖子链接列表(self,帖子链接):
        # 打开数据库连接,保存已下载网址
        db = pymysql.connect("localhost", "root", "", "电影与合集", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句
        sql = """INSERT INTO 总提取帖子链接列表(影视类型,总提取帖子链接列表)
                   VALUES ('%s','%s')""" % (self.影视类型,帖子链接)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            db.rollback()
        # 关闭数据库连接
        db.close()


    def 模具一一提取电影与合集数据库里的总提取帖子链接列表(self):
        # 提取数据库里的过滤网址
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "", "电影与合集", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # SQL 查询语句   self.已下载内容网址
        sql = "SELECT 总提取帖子链接列表 FROM 总提取帖子链接列表 WHERE 影视类型='%s'"%(self.影视类型)
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        self.总提取帖子数据库链接组列表 = cursor.fetchall()
        # 关闭数据库连接
        db.close()


    def 模具一一保存电影与合集帖子内容至数据库(self):
        # 打开数据库连接
        self.摘要 = str(self.摘要).replace('\'', '')
        发布= '否'
        db = pymysql.connect("localhost", "root", "", "电影与合集", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句  (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""" %
        sql = """INSERT INTO 网站文章内容(影视类型,时间ID,长标题,短标题,主栏目ID,副栏目ID,摘要,正文,标题图,主演之标题前栏目字符串,文章来源之更新集数,帖子链接,发布)
                      VALUES ('%s','%d','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" \
              % (self.影视类型, self.时间ID, self.长标题, self.短标题, self.主栏目ID, self.网站副栏目ID, self.摘要, self.正文, self.标题图,self.标题前栏目字符串, self.更新集数, self.各帖子链接,发布)

        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()

        # 关闭数据库连接
        db.close()
        print('帖子内容保存完成')






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

    def 模具一一打开的网址请求返回网页内容(self, 网址):
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
                self.返回网页内容 = requests.post(网址, headers=头部信息, timeout=1)
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

    def 模具一一提炼类型帖子最新各剧集链接(self):
        规则 = "//*[@id=\"body\"]/div/table[2]/tbody/tr[1]/td[3]/div[1]/table[*]//@href"  # text()format 代入{}内,不换行 end=""
        规则 = str(规则).replace("/tbody", "")
        类型帖子最新各剧集链接 = self.类型帖子内容html.xpath(规则)
        页面提取帖子链接列表 = set(类型帖子最新各剧集链接)  # 转换为集,去重复list()
        for 页面提取帖子链接 in 页面提取帖子链接列表:
            if '-page' in 页面提取帖子链接:
                规则='-page.{1,}'
                页面提取帖子链接 =re.sub(规则, '.htm', str(页面提取帖子链接))#替换   ,count=0,re.S|re.I
            规则 = '.{1,}thread'
            页面提取帖子链接 = re.sub(规则, 'http://91btbtt.com/thread', str(页面提取帖子链接))  # 替换
            self.页面提取帖子链接列表文本 = self.页面提取帖子链接列表文本+str(页面提取帖子链接列表)

    def 模具一一种子目录并下载(self, 下载地址):
        # =========== 种子目录================
        #  电影 种子目录 = 'F:/下载种子目录/上传网盘/最新/电影/剧名/季度/'
        if '第' in str(self.长标题) and '季' in str(self.长标题):
            短标题规则 = '.{1,}(?=第)'
            季度名 = re.sub(短标题规则, '', self.长标题)
            季度名 = self.模具一一符号清洗(季度名)
            种子目录 = str(self.种子目录).replace("剧名", str(self.短标题))
            种子目录 = str(种子目录).replace("季度", 季度名)
        else:
            种子目录 = str(self.种子目录).replace("剧名/季度", str(self.短标题))
        创建种子目录 = str(种子目录).strip('/')
        if not os.path.exists(创建种子目录):  # 探测 目录 是否 存在
            os.makedirs(创建种子目录)  # makedirs 创建多级目录文件夹,mkdir创建一个文件夹
        # =========== 种子下载=====
        种子名 = str(self.种子名)
        for 三次循环创建种子目录 in 'ge3':  # 条件循环  post
            try:
                目录与种子名 = str(种子目录) + str(种子名)
                if not os.path.exists(目录与种子名):  # 探测 文件 是否 存在
                    #  F:\下载种子目录\上传网盘\最新\电视剧
                    #  F:\下载种子目录\下载保存\旧剧集合集
                    # 种子目录 = 'F:/下载种子目录/上传网盘/最新/电视剧/剧名/季度/'
                    复制合集目录与种子名 = str(目录与种子名)
                    复制合集目录与种子名 = str(复制合集目录与种子名).replace("上传网盘/合集", "下载保存")  # 替换   , 1) 次数 1
                    if '电视剧' in self.影视类型:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                        复制合集目录与种子名 = str(复制合集目录与种子名).replace("/电视剧/", "/旧剧集合集/")  #
                    elif '动漫' in self.影视类型:  # 其它条件.
                        复制合集目录与种子名 = str(复制合集目录与种子名).replace("/动漫/", "/旧动漫合集/")  #
                    else:  # 否则
                        复制合集目录与种子名 = str(复制合集目录与种子名).replace("/电影/", "/旧电影/")  #

                    复制合集目录与种子名二 = str(目录与种子名)
                    复制合集目录与种子名二= str(复制合集目录与种子名二).replace("合集", "最新")  # 替换   , 1) 次数 1

                    if os.path.exists(复制合集目录与种子名):  # 探测 文件 是否 存在
                        shutil.copy(复制合集目录与种子名, 种子目录)
                        print(复制合集目录与种子名)
                        print('复制文件:', 种子目录)
                        return  # 返回

                    

                    elif os.path.exists(复制合集目录与种子名二):  # 探测 文件 是否 存在
                        shutil.copy(复制合集目录与种子名二, 种子目录)
                        print(复制合集目录与种子名二)
                        print('复制文件:', 种子目录)
                        return  # 返回

                    else:  # 否则
                        目录与种子名一下载地址组 = []
                        目录与种子名一下载地址组.append(目录与种子名)
                        目录与种子名一下载地址组.append(下载地址)
                        self.种子下载地址列表.append(下载地址)
                        self.目录与种子名一下载地址组列表.append(目录与种子名一下载地址组)
                else:  # 否则
                    self.跳过循环3 = 0
                    return  # 返回
            except (FileNotFoundError, OSError):
                种子名 = str(种子名).replace('.', '')
                种子名 = str(种子名).replace('torrent', '.torrent')
                if '3' in 三次循环创建种子目录:
                    print('找不到目录与种子名,出错跳出种子下载循环', 目录与种子名)
                    return  # 返回 空值,
            else:
                break  # 结束循环

    def 模具一一浏览器输入验证码提取cookies(self):
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        driver = webdriver.Chrome(chrome_options=option)
        driver.get("http://3e38.com/image/login.php?gotopage=%2Fimage%2Findex.php")
        # 参数是像素点宽,高
        driver.set_window_size(800, 800)
        # driver.maximize_window() 浏览器全屏显示,不带参数
        driver.implicitly_wait(10)  # 设置 隐式等待.单位是秒(s),
        driver.find_element_by_xpath('//*[@id="login-box"]/div[2]/form/dl/dd[1]/input').send_keys(
            "ad38min")  # 定位用户名
        driver.find_element_by_xpath('//*[@id="login-box"]/div[2]/form/dl/dd[2]/input').send_keys(
            "qq962962")  # 定位密码
        print('输入验证码')
        input("\n\n登录成功后,按下 确认键enter 键后继续.")
        print('提取保存cookie')
        保存cookie = [item["name"] + ":" + item["value"] for item in driver.get_cookies()]
        # cookiestr = ';'.join(item for item in 保存cookie)
        规则 = r"[\'\[\]]{1}"
        保存cookie = re.sub(规则, '', str(保存cookie))
        保存cookie = str(保存cookie).replace(",", ";")
        保存cookie = str(保存cookie).replace(":", "=")
        保存cookie = str(保存cookie)
        f = open("E:\PY学习文件\PyCharm文件\BT影视剧\de3ede38.txt", "w")  # 保存cookie 文件
        f.write(保存cookie)
        f.close()
        driver.quit()
        print('关闭浏览器')

    def 模具一一测试cookies存活(self):
        self.模具一一导入cookie()
        self.url = 'http://3e38.com/image/article_add.php?channelid=17'
        self.s = requests.Session()  # 创建全局会话
        self.s.cookies.update(self.cookies)  # 格式化cookie,全网页才能共享登录cookie,
        返回网页内容 = self.s.get(self.url)
        返回网页内容 = 返回网页内容.text
        if '看不清' in 返回网页内容:
            print('登录失效,正在启动浏览器.')
            self.模具一一浏览器输入验证码提取cookies()
        else:  # 否则
            print('======登录成功=========')

    def 模具一一导入cookie(self):
        with open('E:\PY学习文件\PyCharm文件\BT影视剧\de3ede38.txt', 'r') as f:
            self.cookies = {}
            for line in f.read().split(';'):
                name, value = line.strip().split('=', 1)  # 1代表只分割一次
                self.cookies[name] = value

    """============多线打开网页,下载种子=================="""

    def 模具一一grequests打开网址随机无序集(self, 网址总列表):  # grequests.imap(任务列
        网址分列表 = []
        倒数 = len(网址总列表)
        内容总列表 = []
        规则 = '.{1,}thread'
        for 各帖子链接 in 网址总列表:
            网址分列表.append(各帖子链接)
            倒数 = 倒数 - 1
            if len(网址分列表) == 20 or 倒数 == 0:
                print('等待响应网页倒数', 倒数)
                任务列表 = []
                for 各帖子链接 in 网址分列表:
                    if 'thread' in 各帖子链接:
                        各帖子链接 = re.sub(规则, 'http://91btbtt.com/thread', 各帖子链接)  # 替换
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
                                # break # 结束循环
        return 内容总列表  # 返回

    def 模具一一下载并保存种子(self):
        if len(self.目录与种子名一下载地址组列表) == 0:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            print('下载任务数为 0,跳过')
            return  # 返回
        print('===============等待================')
        print('下载任务数为', len(self.种子下载地址列表))
        种子字节流内容列表 = self.模具一一grequests打开网址随机无序集(self.种子下载地址列表)
        for 种子字节流内容 in 种子字节流内容列表:
            for 目录与种子名一下载地址组 in self.目录与种子名一下载地址组列表:
                if 种子字节流内容.url == 目录与种子名一下载地址组[1]:
                    目录与种子名 = 目录与种子名一下载地址组[0]
                    with open(目录与种子名, 'wb') as fout:
                        fout.write(种子字节流内容.content)
                        fout.close()
                        print('下载完成', 目录与种子名)
                        print('===========================')

    def 模具一一提取一楼种子(self):
        帖子内容html文本 = str(
            self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[1]/td[1]/text()'))
        if '个附件' in 帖子内容html文本:
            提取一楼种子下载地址列表 = self.帖子内容html.xpath(
                '//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[*]/td[1]/a/@href')
            种子名列表 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[*]/td[1]/a/text()')
            # =========== 种子目录================
            if '电视剧' in self.影视类型:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                self.种子目录 = 'F:/下载种子目录/上传网盘/合集/电视剧/剧名/季度/'
            elif '动漫' in self.影视类型:  # 其它条件.
                self.种子目录 = 'F:/下载种子目录/上传网盘/合集/动漫/剧名/季度/'
            else:  # 否则
                self.种子目录 = 'F:/下载种子目录/上传网盘/合集/电影/剧名/季度/'
            # =========== (模具)种子目录并下载================
            for (一楼种子下载地址, 种子名) in zip(提取一楼种子下载地址列表, 种子名列表):
                # =========(模具)种子名过滤与清洗============
                if '.jpg' in str(种子名) or '.png' in str(种子名):
                    print('跳过下载图片')
                    continue  # 跳过循环
                # =========== (模具)种子名清洗=========
                self.种子名 = self.模具一一种子名清洗(种子名)
                # =========== (模具)返回种子内容============
                一楼种子下载地址 = str(一楼种子下载地址).replace("attach", "http://91btbtt.com/attach")
                一楼种子下载地址 = str(一楼种子下载地址).replace("dialog", "download")
                self.跳过循环3 = 3
                self.模具一一种子目录并下载(一楼种子下载地址)
                if self.跳过循环3 == 0:
                    print('种子文件已存在,跳过循环')
                    print('=====================')
                    continue  # 跳过循环

    def 模具一一提取各分层页种子列表(self):
        # =========== 种子目录======F:/电影模板/下载种子目录2/电视剧/剧名/季度/分层名/==========
        if '电视剧' in self.影视类型:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            种子目录 = 'F:/下载种子目录/上传网盘/合集/电视剧/剧名/季度/分层名/'
        elif '动漫' in self.影视类型:  # 其它条件.
            种子目录 = 'F:/下载种子目录/上传网盘/合集/动漫/剧名/季度/分层名/'
        else:  # 否则
            种子目录 = 'F:/下载种子目录/上传网盘/合集/电影/剧名/季度/分层名/'
        # =========== 种子目录======F:/电影
        提取各分层 = self.帖子内容html.xpath('//*[@id="body"]/div/table[*]/tr/td[3]/div')
        层数 = (len(提取各分层))
        for 分层 in range(层数):
            查看附件规则 = ('//*[@id="body"]/div/table[' + str(分层) + ']/tr/td[3]/div/div[2]/table/tr[1]/td[1]/text()')
            分层名目规则 = ('//*[@id="body"]/div/table[' + str(
                分层) + ']/tr/td[3]/div/div/p[1]/text()|//*[@id="body"]/div/table[' + str(
                分层) + ']/tr/td[3]/div/div/p[1]/span/text()')
            if '动漫' in self.影视类型 or '电影' in self.影视类型:
                分层名目规则 = ('//*[@id="body"]/div/table[' + str(
                    分层) + ']/tr/td[3]/div/div/p[1]//text()|//*[@id="body"]/div/table[' + str(
                    分层) + ']/tr/td[3]/div/div/p[1]/span/text()//*[@id="body"]/div/table[' + str(
                    分层) + ']/tr/td[3]/div/div/p[1]/strong/text()')
            分层种子列表规则 = ('//*[@id="body"]/div/table[' + str(分层) + ']/tr/td[3]/div/div[2]/table/tr[*]/td[1]/a/@href')
            分层种子名列表规则 = ('//*[@id="body"]/div/table[' + str(分层) + ']/tr/td[3]/div/div[2]/table/tr[*]/td[1]/a/text()')
            查看附件 = self.帖子内容html.xpath(查看附件规则)
            分层名目 = self.帖子内容html.xpath(分层名目规则)
            分层名目 = ''.join(分层名目)
            if '天天' in str(分层名目) or '风软' in str(分层名目):
                print('过滤分层种子下载链接')
                continue  # 跳过循环
            if '个附件' in str(查看附件):
                分层种子列表 = self.帖子内容html.xpath(分层种子列表规则)
                分层种子名列表 = self.帖子内容html.xpath(分层种子名列表规则)
                分层名目 = self.模具一一符号清洗(分层名目)
                self.种子目录 = str(种子目录).replace("分层名", 分层名目)
                for (下载地址, 种子名) in zip(分层种子列表, 分层种子名列表):
                    # =========== (模具)下载种子网址================
                    self.种子名 = self.模具一一种子名清洗(种子名)
                    # =========== (模具)下载种子网址================
                    下载地址 = str(下载地址).replace("attach", "http://91btbtt.com/attach")
                    下载地址 = str(下载地址).replace("dialog", "download")
                    # =========== (模具)种子目录并下载================
                    self.跳过循环3 = 3
                    self.模具一一种子目录并下载(下载地址)
                    if self.跳过循环3 == 0:
                        print('种子文件已存在,跳过循环')
                        print('=====================')
                        continue  # 跳过循环
            else:
                continue  # (跳过当前循环)

    """============过滤网址================"""



    def 模具一一过滤图片已破与标记其它网站(self):
        列表 = ['tietuku', 'yupoo', 'imgsrc.baidu', '謦灵风软', '风软']
        for 符号 in 列表:
            if 符号 in str(self.帖子内容):
                print(符号, '图片已破or标记其它网站,跳过循环')
                print('=====================')
                self.跳过循环 = 0
                return  # 返回 0 值,跳过循环
            else:
                return  # 返回



    def 模具一一提取一楼种子名进行过滤(self):
        规则 = '//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[1]/td[1]/text()'
        规则 = str(规则).replace("/tbody", "")
        个附件文本 = self.帖子内容html.xpath(规则)
        if '个附件' in str(个附件文本):
            规则 = '//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[*]/td[1]/a/text()'
            规则 = str(规则).replace("/tbody", "")
            一楼种子名列表文本 = str(self.帖子内容html.xpath(规则))
            过滤列表 = ['謦灵风软', '.风软', 'www.', '.com', '.net']
            for 过滤名 in 过滤列表:
                if 过滤名 in 一楼种子名列表文本:
                    print('标记其它网站,跳过循环')
                    print('=====================')
                    self.模具一一保存电影与合集过滤帖子网址()
                    self.跳过循环 = 0
                    return  # 返回 0 值,跳过循环
        # 电影的过滤
        # 謦灵风软www.|.com|先版|鲜版|鲜版|删减版|TS|TC|抢先|清晰|公映版|网盘下载|电驴|迅雷|[email /span

    """===============内容页整理============================"""

    def 模具一一提取帖子标题(self):
        字数列表 = []
        for 帖子标题 in self.帖子标题列表:
            if len(帖子标题) == 0:
                continue  # 跳过当前循环,继续进行下一轮循环
            字数列表.append(len(帖子标题))
        for 帖子标题 in self.帖子标题列表:
            if len(帖子标题) == max(字数列表):
                self.帖子标题 = 帖子标题
                原版标题 = self.帖子标题
                self.原版标题 = self.模具一一符号清洗(原版标题)
                return  # 返回 空值,

    def 模具一一提取长标题(self):
        def 模具一每框内容清洗(每框内容):
            清洗字列表 = ['BT', '网盘', '下载', '迅雷', '种子', '百度', 'MKV', '更至', '全集', '中字', '英语', '国语',
                     '日语', '中英', '字幕', 'MP4', 'MKV', '0P', '多版', '双语', '无水印', '打包', '[全', 'HQC', '片源', 'BD', 'RMVB',
                     '韩语', '无字','更新','TVB','集]','连载','HD-','双字','WEB',
                     'WEBRip', 'GB']  # ,'WEB','','','','','','','','','','','','','',''
            for 清洗字 in 清洗字列表:

                if 清洗字 in 每框内容:
                    每框内容 = ''
                    return 每框内容  # 返回
            return 每框内容  # 返回
        if ']' not in self.帖子标题:
            print('不规整的标题帖子,跳过循环')
            print('=====================')
            self.跳过循环 = 0
            return  # 返回 0 值,跳过循环
        列表 = self.帖子标题.split(']')  #
        字数列表 = []
        清洗后列表 = []
        for 每框内容 in 列表[0:2]:
            每框内容 = 每框内容 + ']'
            每框内容 = 模具一每框内容清洗(每框内容)
            if len(每框内容) == 0 or '[' not in 每框内容:
                continue  # 跳过当前循环,继续进行下一轮循环
            字数列表.append(len(每框内容))
            清洗后列表.append(每框内容)
        for 内容 in 清洗后列表:
            if len(内容) == max(字数列表):
                self.多名长标题 = 内容

        长标题=self.多名长标题
        if '更' in 长标题 and '集' in 长标题:
            规则 = '更.{1,}集'
            长标题 = re.sub(规则, '', 长标题)
            # 符号清洗
        self.符号清洗不过滤空格 = 1
        self.长标题 = self.模具一一符号清洗(长标题)
        if len(self.长标题) == 0:
            self.长标题 = self.多名长标题

    def 模具一一提取短标题(self):
        短标题 = self.多名长标题
        符号列表 = ['/', '.', ' ']
        for 符号 in 符号列表:
            if 符号 in 短标题:
                if 符号 == ' ':
                    符号 = '\s'
                规则 = '{}'.format(符号) + '.{1,}'  # 不换行 end=""
                短标题 = re.sub(规则, '', 短标题, count=0)
        self.短标题 = self.模具一一符号清洗(短标题)

    def 模具一一提取标题图(self):
        标题图列表 = self.标题图列表
        if len(标题图列表) == 0:
            print('无标题图,跳过循环')
            print('=====================')
            self.跳过循环 = 0
            return  # 返回 0 值,跳过循环
        标题图 = 标题图列表[0]
        if "http" in 标题图 and "btbtt" not in 标题图 and "人人" not in 标题图:
            print('非bt网站标题图,跳过循环')
            print('=====================')
            self.跳过循环 = 0
            return  # 返回 0 值,跳过循环
        if "/upload/attach" not in 标题图 and "人人" not in 标题图:
            print('非bt网站标题图,跳过循环')
            print('=====================')
            self.跳过循环 = 0
            return  # 返回 0 值,跳过循环
        if 'HQC' in self.帖子内容:
            if len(标题图列表) == 1:
                标题图 = 标题图列表[0]
            else:
                标题图 = 标题图列表[1]
        规则 = '.{1,}src="'
        标题图 = re.sub(规则, '', str(标题图))  # 替换   ,count=0,re.S|re.I
        规则 = '".{1,}'
        标题图 = re.sub(规则, '', str(标题图))  # 替换   ,count=0,re.S|re.I
        if "http" not in 标题图:
            标题图 = 标题图.replace("/upload", "http://91btbtt.com/upload")
        self.标题图 = 标题图

    def 模具一一种子名清洗(self, 种子名):
        种子名规则 = '\[bt.{1,}\]'
        种子名 = re.sub(种子名规则, '', str(种子名))
        种子名规则 = '\.bt.{1,}torrent'
        种子名 = re.sub(种子名规则, '.torrent', str(种子名))
        列表 = ["\'", "\"", ":", ' ', ' ', '`', '|', '\\n', '\n', '>', '<', '%', "*", "`", "\'", "\"", "`", ":", "*", "/",
              "\\", "#", "\"", "?", "\'", "'", "\'", "'", '', ',', ':', ':', "-", '@',
              '！', "/", "\\", "#", "\"", "@TsKscncom", '菜牙电影网', ',', '?'
            , "www.517ww.com", "www.117hm.com", "www.15bx.com", "www.hanmi520.com", "www.hanmi.cc", '@TsKscn.com', "?"]
        for 符号 in 列表:
            种子名 = str(种子名).replace(符号, '')
        # 替换不同字符间的符号
        if '[' in 种子名 or ']' in 种子名:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            种子名 = 种子名.replace("[", "【")  # 替换   , 1) 次数 1
            种子名 = 种子名.replace("]", "】")  # 替换   , 1) 次数 1
        if '(' in 种子名 or ')' in 种子名:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            种子名 = 种子名.replace("(", "（")  # 替换   , 1) 次数 1
            种子名 = 种子名.replace(")", "）")  # 替换   , 1) 次数 1
        if '..torrent' in 种子名:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            种子名 = 种子名.replace("..torrent", ".torrent")  # 替换   , 1) 次数 1

        if '(' in 种子名 or ')' in 种子名:
            print('( 括号又改变了，等待：500秒')
            time.sleep(50000)  # 等待
        return 种子名

    def 模具一一每一段落清洗(self):
        self.一楼合成内容 = ''

        规则列表 = ["迅雷", 'href="http', 'http', 'text/javascript', "baidu", "百度网盘", "网盘下载", "ed2k://", "ftp://", "本帖最后由",
                "上季", "ftp:", "做种", "在线观看", "ADSL",
                "<scripttype=", "BAIDU_CLB_SLOT_ID", '上季', '下载', '百度', '网盘', '本帖', '发帖', '上传', 'magnet', '磁力', '种子',
                '电驴', '转贴', '本贴',
                "◎BT", "之家整理", "BT之家", "本帖编辑", "HQC小组", "所有压制整合作品", "链接"]
        for 每一段落 in self.段落列表:
            if self.首段落 != 0:
                每一段落 = self.换行字符 + 每一段落
            self.首段落 = 125

            结束循环 = 123
            if '<img' in 每一段落 and 'src=' in 每一段落 and '.gif' not in 每一段落:
                self.标题图列表.append(每一段落)
                self.一楼合成内容 = self.一楼合成内容 + 每一段落
                continue  # 跳过当前循环,继续进行下一轮循环

            for 规则 in 规则列表:
                if 规则 in 每一段落 and 'douban' not in 每一段落:  # 不过滤◎豆瓣评分 douban
                    结束循环 = 0
                    if '</p>' in 每一段落:
                        每一段落 = '</p>'
                        self.一楼合成内容 = self.一楼合成内容 + 每一段落

                    break  # 结束循环 规则列表
            if 结束循环 == 0:
                continue  # 跳过当前循环,继续进行下一轮循环

            self.一楼合成内容 = self.一楼合成内容 + 每一段落

        self.一楼内容 = self.一楼合成内容

    def 模具一一帖子正文清洗(self):

        # 规则 = '(?<=648542).{1,}(?=BAIDU_CLB_SLOT_ID)'
        一楼内容 = str(self.帖子内容)

        一楼内容列表 = 一楼内容.split('BAIDU_CLB_SLOT_ID')
        if len(一楼内容列表) < 2:
            print('一楼内容列表 小于2: 路过循环')
            self.正文清洗没有换行符 = 0
            return  # 结束函数
        一楼内容 = 一楼内容列表[2]

        行列表 = 一楼内容.split('\n')  # 以] 为界定 字符串变为 数个列表 数
        self.一楼内容 = ''
        for 行 in 行列表:
            if 'script' not in 行:

                self.一楼内容 = self.一楼内容 + 行
                if '个附件' in 行:
                    break  # 结束循环
            else:  # 否则
                continue  # 跳过当前循环，继续进行下一轮循环

        if '<p' in self.一楼内容 and '<br' in self.一楼内容:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            p段落列表 = self.一楼内容.split('<p')  #
            self.p段落一楼内容 = ''
            首段落 = 0
            for 段落 in p段落列表:
                if 首段落 != 0:
                    段落 = '<p' + 段落
                首段落 = 123
                self.段落列表 = 段落.split('<br')
                self.换行字符 = '<br'
                self.首段落 = 0
                self.模具一一每一段落清洗()
                self.p段落一楼内容 = self.p段落一楼内容 + self.一楼内容
            self.一楼内容 = self.p段落一楼内容
        elif '<p' in self.一楼内容:  # 其它条件
            self.段落列表 = self.一楼内容.split('<p')  ## .
            self.换行字符 = '<p'
            self.首段落 = 0
            self.模具一一每一段落清洗()
        elif '<br' in self.一楼内容:  # 其它条件
            self.段落列表 = self.一楼内容.split('<br')  ##
            self.换行字符 = '<br'
            self.首段落 = 0
            self.模具一一每一段落清洗()
        else:  # 否则
            print('正文清洗没有换行符: 路过循环')
            self.正文清洗没有换行符 = 0
            return  # 结束函数

        一楼内容 = self.一楼内容
        规则列表 = ["</script>", "\'\";", "<ahrefa>", "</div>", "<div>", "\\u3000", "\\n"]
        for 规则 in 规则列表:
            一楼内容 = 一楼内容.replace(规则, "")
        一楼内容 = str(一楼内容).strip('\'')
        一楼内容 = str(一楼内容).replace("<div ", "<")
        一楼内容 = str(一楼内容).replace("< /div>", "<")
        if 'src=\"/upload' in 一楼内容:
            一楼内容 = str(一楼内容).replace("/upload", "http://91btbtt.com/upload")

        if 'HQC' in 一楼内容:
            次数 = 一楼内容.count('src=')
            if int(次数) > 1:
                规则 = '(?<=<img).{1,}(?=<img)'
                一楼内容 = re.sub(规则, '', str(一楼内容), count=1)
                一楼内容 = str(一楼内容).replace("<img", "")
                一楼内容 = str(一楼内容).replace("src", "<img src")
                一楼内容 = str(一楼内容).replace("HQC小组", "")
                一楼内容 = str(一楼内容).replace("[]的所有压制整合作品,均为小组成员合力精心制作.欢迎转载,但禁止私自取消小组的专用印记,需注明出处.", "")

        正文 = str(一楼内容).replace("\'", "")

        正文 = str(正文).strip('";')  # 文本前后截去特定字符串
        正文 = str(正文).strip('"')  # 文本前后截去特定字符串
        self.正文 = self.模具一一网站图片网址清洗转换(正文)

    def 模具一一符号清洗(self, 原文):
        列表 = ["[", "]", "(", ")", "\'", "\"", "`", ":", "*", "/", "\\", "#", "\"", "?", ".", "\'", "'", "\'", "'", '',
              ',', ':', ':',
              '！', '[', ']', ' ', '`', '|',
              '\\n', '\n', '>', '<', '%']
        for 符号 in 列表:
            原文 = str(原文).replace(符号, '')
        if self.符号清洗不过滤空格 == 1:
            self.符号清洗不过滤空格 = 0
            return 原文
        原文 = str(原文).replace(' ', '')
        return 原文

    def 模具一一网站图片网址清洗转换(self, 图片网址文本):
        列表 = ["http://www.btbtt.co/", "http://btbtt.co/", "http://www.btbtt.net/", "http://www.btbtt.me/",
              "http://www.btbtt.com/", "http://www.btbtt.pw/",
              "http://btbtt.net/", "http://btbtt.me/", "http://btbtt.com/", "http://btbtt.pw/"]
        for 符号 in 列表:
            图片网址文本 = str(图片网址文本).replace(符号, 'http://91btbtt.com/')
        if 'htm' in 图片网址文本:
            规则 = '-page-.{1,}htm'
            图片网址文本 = re.sub(规则, '-page-1.htm', str(图片网址文本))  # 替换   ,count=0,re.S|re.I
        return 图片网址文本

    """====================="""


class 类一一后台发布(类一一公共库):
    def __init__(self):
        self.模具一一测试cookies存活()
        # self.新旧剧集 = '电影与合集'
        # self.模具一一调度控制()
        self.新旧剧集 = '最新影视剧'
        self.模具一一调度控制()
        # print('等待:500秒')
        # time.sleep(500)  # 等待

    def 模具一一调度控制(self):
        影视类型列表 = ['电影', '电视剧', '动漫']
        for self.影视类型 in 影视类型列表:
            print('上传类型:', self.影视类型)
            self.模具一一读取内容数据库()
            self.模具一一数据表反向过滤短标题()
            self.模具一一发布文章()
        self.模具一一模具一一明天日期更新剧集的全部更新()
        self.模具一一更新数据库里剧集发布状态()

    def 模具一一打开的网址请求返回网页内容(self, 网址, 文章内容):
        # global 换IP时间计数  # 时间计数全局变量声明
        循环 = 0
        缓冲时间 = 0
        次数循环 = 0
        while 循环 == 0:  # 条件循环  post
            头部信息 = {'User-Agent': 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'}
            try:
                此时数2 = int(time.time())
                if 缓冲时间 > 此时数2:
                    time.sleep(1)
                返回网页内容 = self.s.post(网址, data=文章内容, headers=头部信息, timeout=1)
                缓冲时间 = int(time.time()) + 1
            except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout,
                    requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout,
                    requests.exceptions.ChunkedEncodingError, requests.exceptions.InvalidSchema) as 异常:
                次数循环 += 1
                print('网络异常等待', 异常)
                print('倒数6秒再连接', 次数循环, '次')
                time.sleep(3)
                if 'None, 10053,' in str(异常):
                    pass
            else:
                if '200' in str(返回网页内容):
                    返回网页内容.encoding = "UTF-8"  # 转换encoding='UTF-8' "gbk"
                    返回网页内容 = 返回网页内容.text
                    if '成功' in (返回网页内容):
                        print('成功发布', self.长标题)
                        break  # 结束循环
                else:
                    print('网站网络异常,状态码:', 返回网页内容)
                    print('等待10秒')
                    time.sleep(10)

    def 模具一一模具一一明天日期更新剧集的全部更新(self):
        print('正在更新....')
        url = 'http://3e38.com/image/makehtml_all.php?action=make&uptype=time&starttime=2018-01-29&startid=0&Submit=%E5%BC%80%E5%A7%8B%E6%9B%B4%E6%96%B0'
        今天时间加八小时 = (datetime.datetime.now() + datetime.timedelta(hours=8)).strftime("%Y-%m-%d")
        url = str(url).replace('2018-01-29', 今天时间加八小时)
        req3 = self.s.post(url)
        url列表 = ['http://3e38.com/image/makehtml_all.php?action=make&step=2&uptype=time&mkvalue=1517068800',
                 'http://3e38.com/image/makehtml_archives_action.php?endid=0&startid=-1&typeid=0&totalnum=31&startdd=20&pagesize=20&seltime=0&sstime=1517101367&stime=&etime=&uptype=time&mkvalue=1517068800&isremote=0&serviterm=',
                 'http://3e38.com/image/makehtml_all.php?action=make&step=3&uptype=time&mkvalue=1517068800',
                 'http://3e38.com/image/makehtml_all.php?action=make&step=4&uptype=time&mkvalue=1517068800',
                 'http://3e38.com/image/makehtml_list_action.php?gotype=mkall',
                 'http://3e38.com/image/makehtml_all.php?action=make&step=10']
        for url in url列表:
            req3 = self.s.post(url)
        print('生成今日的全部更新')

    def 模具一一数据表反向过滤短标题(self):
        # 关闭数据库连接
        数据表 = list(self.数据表)  # 转换为列表
        数据表.reverse()  # 反向排序 列表
        短标题列表 = []
        self.反向过滤数据表 = []
        for 每行数据 in 数据表:
            短标题 = 每行数据[2]
            长标题 = 每行数据[1]
            if 短标题 in 短标题列表:
                if len(短标题) == 0:
                    self.反向过滤数据表.append(每行数据)
                    # self.时间ID列表.append(每行数据[0])  # 每个时间ID都加入列表
                    continue  # 跳过当前循环,继续进行下一轮循环
                print('过滤的短标题', 短标题)
                continue  # 跳过当前循环,继续进行下一轮循环
            elif 长标题 in 短标题列表:
                if len(长标题) == 0:
                    self.反向过滤数据表.append(每行数据)
                    # self.时间ID列表.append(每行数据[0])  # 每个时间ID都加入列表
                    continue  # 跳过当前循环,继续进行下一轮循环
                print('过滤的长标题........', 长标题)
                continue  # 跳过当前循环,继续进行下一轮循环
            self.反向过滤数据表.append(每行数据)
            短标题列表.append(短标题)
            短标题列表.append(长标题)
        self.反向过滤数据表.reverse()  # 反向排序 列表
        短标题列表 = []

    def 模具一一更新数据库里剧集发布状态(self):
        # 连接数据库
        # 连接数据库
        print('连接数据库....')
        db = pymysql.connect("localhost", "root", "", self.新旧剧集, charset="utf8")
        cursor = db.cursor()
        # SQL 查询语句   已下载内容网址
        # 获取游标
        sql = "UPDATE `网站文章内容` SET `发布`='是' WHERE `发布`='否'"
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        # 关闭数据库连接
        db.close()
        print('更新数据库...成功.')

    def 模具一一读取内容数据库(self):
        # 连接数据库
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "", self.新旧剧集, charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句   已下载内容网址
        sql = "SELECT  `影视类型`, `长标题`, `短标题`, `主栏目ID`, `副栏目ID`, `摘要`, `正文`, `标题图`, `主演之标题前栏目字符串`, `文章来源之更新集数`, `帖子链接` FROM `网站文章内容` WHERE `发布`='否'  and `影视类型`=('%s') " % (
            self.影视类型)  # 不换行 end=""
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        self.数据表 = cursor.fetchall()
        # 关闭数据库连接
        db.close()

    def 模具一一发布文章(self):
        for 单条文章内容 in self.反向过滤数据表:
            #  `影视类型`, `长标题`, `短标题`, `主栏目ID`, `副栏目ID`,
            # `摘要`, `正文`, `标题图`,
            # `主演之标题前栏目字符串`, `文章来源之更新集数`, `帖子链接
            影视类型 = 单条文章内容[0]
            长标题 = 单条文章内容[1]
            if len(长标题) == 0:
                长标题 = '空标题' + str(random.randrange(1, 100000))
            短标题 = 单条文章内容[2]
            主栏目ID = 单条文章内容[3]
            网站副栏目ID = 单条文章内容[4]
            摘要 = 单条文章内容[5]
            正文 = 单条文章内容[6]
            标题图 = 单条文章内容[7]
            文章来源标题前栏目字符串 = 单条文章内容[8]
            更新集数 = 单条文章内容[9]
            self.帖子链接 = 单条文章内容[10]
            更新时间 = time.strftime("%Y-%m-%d ", time.localtime())
            随机浏览数 = random.randrange(10001, 1000000)
            网站副栏目ID = str(网站副栏目ID).replace(" ", "")
            网站副栏目ID = str(网站副栏目ID).replace(",,", ",")
            网站副栏目ID = str(网站副栏目ID).strip(',')
            正文 = 正文.strip('[')
            正文 = 正文.strip(']')
            正文 = 正文.strip('";')  # 文本前后截去特定字符串
            正文 = 正文.strip('"')  # 文本前后截去特定字符串
            文章内容 = {"channelid": 17,
                    "dopost": "save",
                    "title": 长标题,
                    "shorttitle": 短标题,
                    "redirecturl": "",
                    "tags": "",
                    "weight": 26185,
                    "picname": 标题图,
                    '"litpic"; filename=""': "Content-Type: application/octet-stream",
                    "source": 更新集数,
                    "writer": "",
                    "typeid": 主栏目ID,
                    "typeid2": 网站副栏目ID,
                    "keywords": "",
                    "autokey": 1,
                    "description": 摘要,
                    "authors": 文章来源标题前栏目字符串,
                    "areas": "",
                    "murls": "",
                    "dede_addonfields": "authors,multitext;areas,text;murls,multitext",
                    "needwatermark": 1,
                    "sptype": 'hand',
                    "spsize": 5000,
                    "body": 正文,
                    "voteid": "",
                    "notpost": 0,
                    "click": 随机浏览数,
                    "sortup": 0,
                    "color": "",
                    "arcrank": 0,
                    "money": 0,
                    "pubdate": 更新时间,
                    "ishtml": 1, "filename": "",
                    "templet": "",
                    "imageField.x": 33,
                    "imageField.y": 9}
            后台提交网址 = 'http://3e38.com/image/article_add.php?channelid=17'
            self.长标题 = 长标题
            self.模具一一打开的网址请求返回网页内容(后台提交网址, 文章内容)


class 类一一综合影视类型(类一一公共库):  # 调用 类的模具 self.模具一一数据库()
    def __init__(self):
        self.模具一一测试cookies存活()
        self.模具一一换头部信息()

        self.页面提取帖子链接列表文本 = ''
        self.模具一一置顶帖子剧集动漫类型()  # 电视剧集动漫


        今天天数 = datetime.datetime.now()
        三月前时间 = 今天天数 + datetime.timedelta(days=-90)
        规则 = '\s.{0,}'
        三月前时间 = re.sub(规则, '', str(三月前时间))  # 除掉后面的时间分数 替换   ,count=0,re.S|re.I
        self.三月前时间 = int(str(三月前时间).replace("-", ""))  # 替换   , 1) 次数 1


        影视类型列表=['电影','电视剧','动漫']
        for 影视类型 in 影视类型列表:
            self.影视类型 =影视类型

            self.模具一一提取电影与合集数据库里的过滤网址一已下载内容网址一过滤种子网址()
            self.模具一一提取最新影视剧数据库里的过滤网址()

            self.过滤帖子网址 = self.过滤帖子网址 + self.过滤帖子网址二 +self.页面提取帖子链接列表文本
            if '电视剧' in self.影视类型:
                self.倒页总数 = 100
                self.页数网址 = 'http://91btbtt.com/forum-index-fid-950-page-123.htm'

            elif '动漫' in self.影视类型:  # 其它条件.
                self.倒页总数 = 50
                self.页数网址 = 'http://91btbtt.com/forum-index-fid-981-page-123.htm'

            else:  # 否则
                self.倒页总数 = 0 # 电影
                self.页数网址 = 'http://91btbtt.com/forum-index-fid-951-page-123.htm'



            self.模具一一总提取帖子链接列表()
            self.模具一一综合影视各链接网址处理()

    def 模具一一综合影视各链接网址处理(self):
        self.目录与种子名一下载地址组列表 = []  # 初始设定
        self.种子下载地址列表 = []  # 初始设定


        self.模具一一换头部信息()
        print('========================等待==============================')

        内容页列表 = self.模具一一grequests打开网址随机无序集(self.页面提取帖子链接列表)
        倒计数 = len(内容页列表)
        for 内容页 in 内容页列表:
            倒计数 = 倒计数 - 1
            self.跳过循环 = 1  # 设定初始值
            self.符号清洗不过滤空格 = 0  # 设定初始值
            print('========倒计数=========', 倒计数)
            # ======================
            self.帖子内容 = 内容页.text
            self.各帖子链接 = 内容页.url
            self.帖子内容html = etree.HTML(内容页.text)
            print('==================:')
            print('网址:', self.各帖子链接)
            # =====================
           
            # ===========发贴时间半年前比较=========================
            if self.影视类型 == '电影':
                self.模具一一判断发贴时间三月前或内()
            if self.跳过循环 == 0:
                continue  # 跳过循环
            # ====================================
            self.帖子标题列表 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/h2/text()')
            self.标题前的栏目列表 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/h2/a/text()')


            # ===========帖子标题列表清洗===========================================
            self.模具一一提取帖子标题()


            # =========#过滤标题栏目=====================================================
            if self.影视类型 == '电视剧' or self.影视类型 == '动漫':
                self.模具一一剧集过滤标题栏目()
            else:  # 否则
                self.模具一一电影过滤标题栏目()
            if self.跳过循环 == 0:
                self.模具一一保存电影与合集过滤帖子网址()
                continue  # 跳过循环
            # ========过滤图片已破与标记其它网站,跳过循环=================================================================
            self.模具一一过滤图片已破与标记其它网站()
            if self.跳过循环 == 0:
                self.模具一一保存电影与合集过滤帖子网址()
                continue  # 跳过循环
            # ========提取一楼种子名进行过滤=============================================================
            if self.影视类型 == '电视剧' or self.影视类型 == '动漫':
                self.模具一一提取一楼种子名进行过滤()
            else:  # 否则
                self.模具一一电影过滤一楼种子名()
            if self.跳过循环 == 0:
                self.模具一一保存电影与合集过滤帖子网址()
                continue  # 跳过循环

            # ===================提取长标题===============================
            self.模具一一提取长标题()
            if self.跳过循环 == 0:
                self.模具一一保存电影与合集过滤帖子网址()
                continue  # 跳过循环
            print('长标题:', self.长标题)
            # 符号清洗
            # ==============短标题的清洗============================
            self.模具一一提取短标题()
            if len(self.短标题) == 0:
                self.短标题 = self.原版标题
            print('短标题', self.短标题)
            # ==============摘要===========================
            if '电视剧' in self.影视类型:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                self.摘要 = '<h2>资源下载:<a href="/uploads/3html/dianshiju/{}.html"target="_blank">{}.torrent</a></h2>'.format(
                    self.短标题, self.长标题)  # 代入 .不换行 end=""
            elif '动漫' in self.影视类型:  # 其它条件.
                self.摘要 = '<h2>资源下载:<a href="/uploads/3html/dongman/{}.html"target="_blank">{}.torrent</a></h2>'.format(
                    self.短标题, self.长标题)  # 代入 .不换行 end=""
            else:  # 否则
                self.摘要 = '<h2>资源下载:<a href="/uploads/3html/dying/{}.html"target="_blank">{}.torrent</a></h2>'.format(
                    self.短标题, self.长标题)  # 代入 .不换行 end=""
            print('摘要', self.摘要)
            # ===========self.主栏目ID、self.标题前栏目字符串==============================================================================================
            self.标题前栏目字符串 = ''.join(self.标题前的栏目列表)
            self.时间ID = int(time.strftime("%y%m%d%H%M%S", time.localtime()))
            self.更新集数='合集'
            print('标题前栏目字符', self.标题前栏目字符串)
            # ===========self.网站副栏目ID============================================================================
            if '电视剧' in self.影视类型:
                self.模具一一电视剧网站副栏目ID()
            elif '动漫' in self.影视类型:  # 其它条件.
                self.模具一一动漫网站副栏目ID()
            else:  # 否则
                self.模具一一电影网站副栏目ID()

            # =========(模具)self.正文清洗=====================================================
            self.标题图列表 = []
            self.模具一一帖子正文清洗()
            # =========(模具)标题图===============================================
            self.模具一一提取标题图()
            if self.跳过循环 == 0:
                self.模具一一保存电影与合集过滤帖子网址()
                continue  # 跳过循环
            self.标题图 = self.模具一一网站图片网址清洗转换(self.标题图)
            # =========== 提取一楼种子列表==================================================================
            self.模具一一提取一楼种子()
            # =========== 提取各分层页种子列表=================================================================
            self.模具一一提取各分层页种子列表()
            # self.模具一一保存最新影视剧已下载内容页网址()
            if self.各帖子链接 in self.过滤帖子网址:
                print('网站内容页已经存在,跳过保存')
            else:  # 否则
                self.模具一一保存电影与合集帖子内容至数据库()

                self.过滤帖子网址 = self.过滤帖子网址 + str(self.各帖子链接)
        self.模具一一下载并保存种子()
    """======================="""

    def 模具一一置顶帖子剧集动漫类型(self):

        网址列表 = []
        打开的网址 = 'http://91btbtt.com'
        网址列表.append(打开的网址)
        首页网页内容列表 = self.模具一一grequests打开网址随机无序集(网址列表)
        # self.模具一一打开的网址请求返回网页内容(打开的网址)
        帖子内容html = etree.HTML(首页网页内容列表[0].text)
        # ==================置顶类型帖子网址列表================================
        # for 帖子位置数 in range(2,6):  # 范围
        置顶类型帖子网址列表 = []
        for self.帖子位置数 in range(2, 6):
            规则 = "//*[@id=\"threadlist\"]/table[{}]/tbody/tr/td[1]/a[5]/@href".format(
                self.帖子位置数)  # text()format 代入{}内,不换行 end=""
            规则 = str(规则).replace("/tbody", "")
            置顶类型帖子 = 帖子内容html.xpath(规则)
            置顶类型帖子网址 = 'http://91btbtt.com/' + str(置顶类型帖子[0])
            置顶类型帖子网址列表.append(置顶类型帖子网址)
        # =================置顶类型帖子网页内容===============================
        置顶类型帖子网页内容列表 = self.模具一一grequests打开网址随机无序集(置顶类型帖子网址列表)
        for 置顶类型帖子网页内容 in 置顶类型帖子网页内容列表:
            self.类型帖子内容html = etree.HTML(置顶类型帖子网页内容.text)

            self.模具一一提炼类型帖子最新各剧集链接()


    def 模具一一总提取帖子链接列表(self):
        self.模具一一提取电影与合集数据库里的总提取帖子链接列表()


        总提取帖子链接列表 = []

        if self.倒页总数 == 0:
            pass
        else:  # 否则
            总倒页链接 = []
            for 倒页数 in range(self.倒页总数, 0, -1):
                print('倒页数', 倒页数)
                各帖子链接 = str(self.页数网址).replace("123", str(倒页数))
                print(self.影视类型,'各页数链接', 各帖子链接)
                # =========请求各帖子链接网页内容======================
                各帖子链接 = self.模具一一网站图片网址清洗转换(各帖子链接)
                总倒页链接.append(各帖子链接)
            页数链接列表网页内容列表 = self.模具一一grequests打开网址随机无序集(总倒页链接)
            计数器=0
            for 页数链接列表网页内容 in 页数链接列表网页内容列表:
                # ====================================================
                帖子列表html = etree.HTML(页数链接列表网页内容.text)
                提取帖子链接列表 = 帖子列表html.xpath('//*[@id="threadlist"]/table[*]/tr/td[1]/a[1]/@href')
                for 各帖子链接 in 提取帖子链接列表:
                    if '-page' in 各帖子链接:
                        规则 = '-page.{1,}'
                        各帖子链接 = re.sub(规则, '.htm', str(各帖子链接))  # 替换   ,count=0,re.S|re.I
                    规则 = '.{1,}thread'
                    各帖子链接 = re.sub(规则, 'http://91btbtt.com/thread', str(各帖子链接))  # 替换
                    if 各帖子链接 in self.过滤帖子网址:
                        continue  # 跳过循环
                    self.模具一一保存电影与合集总提取帖子链接列表(各帖子链接)
                    总提取帖子链接列表.append(各帖子链接)
                    print('提取帖子链接数', 计数器)
                    计数器=计数器+1

        for 各帖子链接组 in self.总提取帖子数据库链接组列表:
            各帖子链接 = 各帖子链接组[0]
            if 各帖子链接 in self.过滤帖子网址:
                print('过滤帖子网址二,跳过采集')
                continue  # 跳过循环
            总提取帖子链接列表.append(各帖子链接)
        print('===帖子链接总数:=====', len(总提取帖子链接列表))
        总提取帖子链接列表 = set(总提取帖子链接列表)
        self.页面提取帖子链接列表 = list(总提取帖子链接列表)
        self.电视剧类型 = "最新电影"
        print('====================帖子链接总数去重复后:=================', len(self.页面提取帖子链接列表))

    """==========各类型模具============="""

    def 模具一一剧集过滤标题栏目(self):
        列表 = ['[单集]', '[讨论]', '[Resilio-Sync]', '猪猪', '音乐', '动漫']
        for 符号 in 列表:
            if self.影视类型 == '电视剧' and 符号 == '猪猪':
                continue  # 跳过当前循环,继续进行下一轮循环
            if 符号 in str(self.标题前的栏目列表):
                print(符号, '过滤的栏目跳过循环')
                print('=====================')
                self.模具一一保存电影与合集过滤帖子网址()
                self.跳过循环 = 0
                return  # 返回 0 值,跳过循环
        if 'torrent.gif' not in self.帖子内容 and '个附件' not in self.帖子内容:
            print('无种子附件,跳过循环')
            print('=====================')
            self.模具一一保存电影与合集过滤帖子网址()
            self.跳过循环 = 0
            return  # 返回 0 值,跳过循环

    def 模具一一电影过滤标题栏目(self):
        列表 = ['删节版', '删减版', 'TS', '抢先', '抢鲜', 'TC', '清晰', '大陆', '中国', 'BT之家整合', '版块公告', '版块专用', '[猪猪]',
              '[Resilio-Sync]', '有水印', '有广告']
        帖子标题 = str(self.帖子标题) + str(self.标题前的栏目列表)
        版本表 = ['抢', '删', '鲜']
        for 版符号 in 版本表:
            if 版符号 in 帖子标题 and '版' in 帖子标题:
                print(版符号, '版,跳过循环')
                print('=====================')
                self.模具一一保存电影与合集过滤帖子网址()
                self.跳过循环 = 0
                return  # 返回 0 值,跳过循环
        for 符号 in 列表:
            if 符号 in 帖子标题:
                print(符号, '列表符号,跳过循环')
                print('=====================')
                self.模具一一保存电影与合集过滤帖子网址()
                self.跳过循环 = 0
                return  # 返回 0 值,跳过循环

    def 模具一一判断发贴时间三月前或内(self):
        发帖时间列表 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[2]/td[3]/div/b[1]/text()')
        发帖时间 = 发帖时间列表[0]
        规则 = '\s.{0,}'
        发帖时间天数 = re.sub(规则, '', str(发帖时间))  # 除掉后面的时间分数 替换   ,count=0,re.S|re.I
        发帖时间天数 = int(str(发帖时间天数).replace("-", ""))  # 替换   , 1) 次数 1
        if self.三月前时间 > 发帖时间天数:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            
            print('发贴时间为三月前:')
        else:  # 否则
            self.跳过循环 == 0

            print('发贴时间为三月内最新电影,跳过循环:')

    def 模具一一发贴时间半年前过滤(self):
        发帖时间列表 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[2]/td[3]/div/b[1]/text()')
        self.发帖时间 = 发帖时间列表[0]
        规则 = '\s.{0,}'
        发帖时间天数 = re.sub(规则, '', str(self.发帖时间))  # 除掉后面的时间分数 替换   ,count=0,re.S|re.I
        发帖时间天数 = int(str(发帖时间天数).replace("-", ""))  # 替换   , 1) 次数 1
        if 发帖时间天数 < self.半年前时间 and '4378529' not in str(self.各帖子链接):  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            self.跳过循环 = 0
            print('发贴时间为半年前,跳过循环:')
            return  # 返回

    def 模具一一动漫网站副栏目ID(self):
        # 全部合集时 载入'[连载]更改为,'[合集]': '124',
        网站副栏目字典 = {'[合集]': '124', '[连载]': '124', '[美国]': '120', '[英国]': '120', '[多国]': '120', '[大陆]': '119',
                   '[香港]': '119', '[台湾]': '119',
                   '[日本]': '118',
                   '[法国]': '120', '[加剧]': '120',
                   '[合 集]': '124',
                   '[全集]': '124', '[打包]': '124', '[断载]': '124', '[2006]': '137',
                   '[2007]': '136', '[2008]': '135', '[2009]': '134', '[2010]': '133', '[2011]': '132', '[2012]': '131',
                   '[2013]': '130', '[2014]': '129', '[2015]': '128', '[2016]': '127', '[2017]': '126', '[2018]': '125',
                   '[更 早]': '138', '[新番]': '124', '[火影]': '124', '[海贼]': '124', '[柯南]': '124', '[敢达]': '124',
                   '[死神]': '124',
                   '[银魂]': '124', '[妖尾]': '124', '[龙珠]': '124', '[布袋戏]': '124', '[完结]': '124', '[其他]': '124',
                   '[音乐]': '139', '[]': '', '单集': '', '[纯净版]': ''}
        网站副栏目ID = [网站副栏目字典[x] if x in 网站副栏目字典 else x for x in self.标题前的栏目列表]
        网站副栏目ID = str(网站副栏目ID)
        # 符号清洗
        self.符号清洗不过滤空格 = 1  # 符号清洗不过滤 空格
        网站副栏目ID = self.模具一一符号清洗(网站副栏目ID)
        网站副栏目ID = 网站副栏目ID.strip()
        if len(网站副栏目ID) == 0:
            网站副栏目ID = '124'
        网站副栏目ID = str(网站副栏目ID).replace(" ", ",")
        网站副栏目ID = 网站副栏目ID.replace("124,124,124", "124")
        self.网站副栏目ID = 网站副栏目ID.replace("124,124", "124")

        if '118' in 网站副栏目ID:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            self.主栏目ID = '118'
        else:  # 否则
            self.主栏目ID = '23'

        print('网站副栏目ID', self.网站副栏目ID)

    def 模具一一电影网站副栏目ID(self):
        网站副栏目字典 = {'[]': '', '[纯净版]': '', '[欧美]': '25', '[美国]': '25', '[英国]': '25', '[大陆]': '26', '[香港]': '27',
                   '[台湾]': '28', '[日本]': '29',
                   '[韩国]': '30',
                   '[法国]': '31', '[西剧]': '31', '[泰国]': '31', '[加剧]': '31', '[意剧]': '31', '[澳剧]': '31', '[德国]': '31',
                   '[新马]': '31', '[多国]': '31', '[剧情]': '34', '[喜剧]': '33', '[爱情]': '34', '[偶像]': '34', '[动作]': '32',
                   '[奇幻]': '37',
                   '[科幻]': '35', '[印度]': '31',
                   '[悬疑]': '40', '[罪案]': '40', '[犯罪]': '40', '[刑侦]': '40', '[战争]': '38', '[灾难]': '38', '[谍战]': '40',
                   '[军旅]': '38', '[历史]': '39',
                   '[古装]': '39', '[惊悚]': '43', '[恐怖]': '43', '[真人]': '34', '[时装]': '34',
                   '[医务]': '34', '[歌舞]': '34', '[其他]': '44', '[都市]': '34', '[情感]': '34',
                   '[家庭]': '34',
                   '[武侠]': '39', '[纪录]': '42', '[经典]': '42', '[动画]': '41',
                   '[微电影]': '44', '[同性]': '44', '[其他]': '44', '[合集]': '140', '[系列]': '140', '[2006]': '58',
                   '[2007]': '57', '[2008]': '56', '[2009]': '55', '[2010]': '54', '[2011]': '53', '[2012]': '52',
                   '[2013]': '51', '[2014]': '50', '[2015]': '49', '[2016]': '48', '[2017]': '47', '[2018]': '46',
                   '[更 早]': '45', '[更早]': '45'}
        网站副栏目ID = [网站副栏目字典[x] if x in 网站副栏目字典 else x for x in self.标题前的栏目列表]
        网站副栏目ID = str(网站副栏目ID)
        if '41' in str(网站副栏目ID):
            if '25' in str(网站副栏目ID):
                网站副栏目ID = str((网站副栏目ID)).replace("25", "25 120")
            elif '29' in str(网站副栏目ID):
                网站副栏目ID = str((网站副栏目ID)).replace("29", "29 118")
        # 符号清洗
        self.符号清洗不过滤空格 = 1  # 符号清洗不过滤 空格
        网站副栏目ID = self.模具一一符号清洗(网站副栏目ID)
        网站副栏目ID = 网站副栏目ID.strip()
        if len(网站副栏目ID) == 0:
            网站副栏目ID = '34'
        self.网站副栏目ID = str(网站副栏目ID).replace(" ", ",")
        if '25' in self.网站副栏目ID:
            self.主栏目ID = '25'
        else:  # 否则
            self.主栏目ID = '21'
        print('.主栏目ID', self.主栏目ID)
        print('网站副栏目ID', self.网站副栏目ID)

    def 模具一一电视剧网站副栏目ID(self):
        # 全部合集时 载入'[连载] '60'':改为全集 '61',
        网站副栏目字典 = {'[连载]': '61', '[]': '', '[美国]': '84', '[英国]': '84', '[大陆]': '85', '[香港]': '86', '[台湾]': '87',
                   '[日本]': '88',
                   '[韩国]': '89',
                   '[法国]': '90', '[多国]': '90', '[印度]': '90', '[西剧]': '90', '[泰国]': '90', '[加剧]': '84', '[意剧]': '90',
                   '[澳剧]': '90', '[德国]': '90',
                   '[新马]': '90', '[剧情]': '91', '[喜剧]': '92', '[爱情]': '93', '[偶像]': '91', '[动作]': '94', '[奇幻]': '95',
                   '[科幻]': '96',
                   '[悬疑]': '97', '[罪案]': '97', '[灾难]': '97', '[刑侦]': '97', '[战争]': '98', '[谍战]': '97', '[军旅]': '98',
                   '[历史]': '99',
                   '[古装]': '99', '[惊悚]': '100', '[恐怖]': '100', '[真人]': '101', '[时装]': '91',
                   '[医务]': '91', '[歌舞]': '91', '[其他]': '91', '[都市]': '91', '[情感]': '91',
                   '[家庭]': '91',
                   '[武侠]': '94', '[纪录]': '102', '[经典]': '103', '[合 集]': '61',
                   '[全集]': '61', '[打包]': '61', '[单集]': '61', '[合集]': '61', '[断载]': '61', '[2006]': '117',
                   '[2007]': '116', '[2008]': '115', '[2009]': '114', '[2010]': '113', '[2011]': '112', '[2012]': '111',
                   '[2013]': '110', '[2014]': '109', '[2015]': '108', '[2016]': '107', '[2017]': '106', '[2018]': '105',
                   '[更 早]': '104', '[星期一]': '141', '[情感]': '91', '[情感]': '91', '[情感]': '91', '[情感]': '91', '[情感]': '91',
                   '[情感]': '91'}
        网站副栏目ID = [网站副栏目字典[x] if x in 网站副栏目字典 else x for x in self.标题前的栏目列表]
        网站副栏目ID = str(网站副栏目ID)
        if '[动画]' in str(网站副栏目ID):
            if '88' in str(网站副栏目ID):
                网站副栏目ID = str((网站副栏目ID)).replace("[动画]", "118")
            elif '85' in str(网站副栏目ID):
                网站副栏目ID = str((网站副栏目ID)).replace("[动画]", "119")
            elif '84' in str(网站副栏目ID):
                网站副栏目ID = str((网站副栏目ID)).replace("[动画]", "120")
            elif '87' in str(网站副栏目ID):
                网站副栏目ID = str((网站副栏目ID)).replace("[动画]", "")
            else:
                网站副栏目ID = str((网站副栏目ID)).replace("[动画]", "90")
        # 符号清洗
        self.符号清洗不过滤空格 = 1  # 符号清洗不过滤 空格
        网站副栏目ID = self.模具一一符号清洗(网站副栏目ID)
        if len(网站副栏目ID) == 0:
            网站副栏目ID = '91'
        self.网站副栏目ID = str(网站副栏目ID).replace(" ", ",")

        if '84' in self.网站副栏目ID:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            self.主栏目ID ='84'
        else:  # 否则
            self.主栏目ID = '22'

        print('网站副栏目ID', self.网站副栏目ID)

    def 模具一一电视剧副栏目一星期数ID(self):
        规则 = '\s.{0,}'
        星期数 = re.sub(规则, '', str(self.发帖时间))  # 替换   ,count=0,re.S|re.I
        星期数 = 星期数.strip('[')
        星期数 = 星期数.strip('\'')
        发贴时间列表 = 星期数.split("-")
        年 = int(发贴时间列表[0])
        月 = int(发贴时间列表[1])
        日 = int(发贴时间列表[2])
        # a=(datetime.strptime(发贴时间, "%w"
        today = int(time.strftime("%w"))
        星期数 = datetime.datetime(年, 月, 日).strftime("%w")
        星期数字典 = {'0': '141', '1': '141', '2': '142', '3': '143', '4': '144', '5': '145', '6': '146', '7': '147'}
        for 字符 in 星期数字典:  # 范围 range
            if 字符 in 星期数:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                self.网站副栏目一星期数ID = 星期数字典[字符]
                print('网站副栏目一星期数ID', self.网站副栏目一星期数ID)
                break  # 结束循环

    def 模具一一动漫副栏目一星期数ID(self):
        规则 = '\s.{0,}'
        星期数 = re.sub(规则, '', str(self.发帖时间))  # 替换   ,count=0,re.S|re.I
        星期数 = 星期数.strip('[')
        星期数 = 星期数.strip('\'')
        发贴时间列表 = 星期数.split("-")
        年 = int(发贴时间列表[0])
        月 = int(发贴时间列表[1])
        日 = int(发贴时间列表[2])
        # a=(datetime.strptime(发贴时间, "%w"
        today = int(time.strftime("%w"))
        星期数 = datetime.datetime(年, 月, 日).strftime("%w")
        星期数字典 = {'1': '148', '2': '149', '3': '150', '4': '151', '5': '152', '6': '153', '7': '154'}
        for 字符 in 星期数字典:  # 范围 range
            if 字符 in 星期数:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                self.网站副栏目一星期数ID = 星期数字典[字符]
                break  # 结束循环

    def 模具一一电影过滤一楼种子名(self):
        种子名列表 = self.帖子内容html.xpath(
            '//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[*]/td[1]/a/text()|//*[@id="body"]/div/table[2]/tr[1]/td[3]/font/b/div[1]/table/tr[3]/td[1]/a/text()')
        种子名列表 = str(种子名列表)
        版本表 = ['抢', '删', '鲜']
        for 版符号 in 版本表:
            if 版符号 in 种子名列表 and '版' in 种子名列表:
                print(版符号, '版,跳过循环,一楼种子名')
                print('=====================')
                self.模具一一保存电影与合集过滤帖子网址()
                self.跳过循环 = 0
                return  # 返回 0 值,跳过循环
        列表 = ('删节版', '删减版', 'TS', '抢先', 'TC', '清晰', '大陆', '中国', 'www.', '.com', '.net')
        for 符号 in 列表:
            if 符号 in 种子名列表:
                print(符号, '列表符号,跳过循环,一楼种子名')
                print('=====================')
                self.模具一一保存电影与合集过滤帖子网址()
                self.跳过循环 = 0
                return  # 返回 0 值,跳过循环

    """=========数据库=============="""




开始时间计数 = int(time.time())
类 = 类一一综合影视类型()  # 电视剧、动漫
类c = 类一一后台发布()
结束时间计数 = int(time.time())
用时 = 结束时间计数 - 开始时间计数
取整除分数 = int(用时) // 60
除的余数的秒数 = int(用时) % 60
print('用时计数:', 取整除分数, '分:', 除的余数的秒数, '秒')
