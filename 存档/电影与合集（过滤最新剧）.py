from lxml import html
import requests
import re
import time
import datetime  # 时间
import os
import pymysql
import random
from lxml import etree
import shutil
from selenium import webdriver# 浏览的驱动



class 类_公共库:  # 调用 类的模具 self.模具_数据库()
    def __init__(self, data):
        data = data

    # ==========电影与合集数据库==========================
    def 模具_保存电影与合集过滤帖子网址(self):
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

    def 模具_保存电影与合集总提取帖子链接列表(self, 帖子链接):
        # 打开数据库连接,保存已下载网址
        db = pymysql.connect("localhost", "root", "", "电影与合集", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()


        if self.清空数据库==0:
            # SQL 插入语句
            sql ="TRUNCATE `电影与合集`"#清空数据库
            try:
                # 执行sql语句
                cursor.execute(sql)
                # 提交到数据库执行
                db.commit()
            except:
                # 如果发生错误则回滚
                db.rollback()
            self.清空数据库 = 1

        # SQL 插入语句
        sql = """INSERT INTO 总提取帖子链接列表(影视类型,总提取帖子链接列表)
                   VALUES ('%s','%s')""" % (self.影视类型, 帖子链接)
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

    def 模具_保存电影与合集过滤已下载种子网址(self, 种子下载地址):
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "", "电影与合集", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句
        sql = """INSERT INTO 过滤种子网址(过滤种子网址)
                                VALUES ('%s')""" % (种子下载地址)
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

    def 模具_提取电影与合集数据库里的过滤网址一已下载内容网址一过滤种子网址(self):
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
        sql = "SELECT `帖子链接` FROM `网站文章内容`;"
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        帖子链接 = cursor.fetchall()
        self.过滤帖子网址 = 过滤帖子网址 + str(帖子链接)



        # SQL 查询语句
        sql = "SELECT 过滤种子网址 FROM 过滤种子网址"
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        过滤种子网址 = cursor.fetchall()
        self.过滤种子网址 = str(过滤种子网址)
        # 关闭数据库连接
        db.close()

    def 模具_提取电影与合集数据库里的总提取帖子链接列表(self):
        # 提取数据库里的过滤网址
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "", "电影与合集", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # SQL 查询语句   self.已下载内容网址
        sql = "SELECT 总提取帖子链接列表 FROM 总提取帖子链接列表 WHERE 影视类型='%s'" % (self.影视类型)
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        self.总提取帖子链接列表1 = cursor.fetchall()
        # 关闭数据库连接
        db.close()

    def 模具_保存电影与合集帖子内容至数据库(self):
        # 打开数据库连接
        self.摘要 = str(self.摘要).replace('\'', '')
        发布 = '否'
        db = pymysql.connect("localhost", "root", "", "电影与合集", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句  (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""" %
        sql = """INSERT INTO 网站文章内容(影视类型,时间ID,长标题,短标题,主栏目ID,副栏目ID,摘要,正文,标题图,主演之标题前栏目字符串,文章来源之更新集数,帖子链接,发布)
                      VALUES ('%s','%d','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" \
              % (self.影视类型, self.时间ID, self.长标题, self.短标题, self.主栏目ID, self.网站副栏目ID, self.摘要, self.正文, self.标题图,
                 self.标题前栏目字符串, self.更新集数, self.各帖子链接, 发布)

        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()

        # 关闭数据库连接
        db.close()
        print('帖子内容保存完成')

    def 模具_保存最新影视剧帖子内容至数据库(self):
        # 打开数据库连接
        self.摘要 = str(self.摘要).replace('\'', '')
        发布 = '否'
        db = pymysql.connect("localhost", "root", "", "最新影视剧", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句  (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""" %
        sql = """INSERT INTO 网站文章内容(影视类型,时间ID,长标题,短标题,主栏目ID,副栏目ID,摘要,正文,标题图,主演之标题前栏目字符串,文章来源之更新集数,帖子链接,发布)
                         VALUES ('%s','%d','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" \
              % (self.影视类型, self.时间ID, self.长标题, self.短标题, self.主栏目ID, self.网站副栏目ID, self.摘要, self.正文, self.标题图,
                 self.标题前栏目字符串, self.更新集数, self.各帖子链接, 发布)

        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()

        # 关闭数据库连接
        db.close()
        print('帖子内容保存完成')
    def 模具_保存电影与合集种子存放目录(self):
        种子存放目录=self.影视类型+'/'+self.短标题

        # 打开数据库连接,保存已下载网址
        db = pymysql.connect("localhost", "root", "", "电影与合集", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句
        sql = """INSERT INTO 种子存放目录(种子存放目录)
                           VALUES ('%s','%s')""" % (种子存放目录,self.时间ID)
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

    def 模具_提取最新影视剧数据库里的过滤网址(self):
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
        self.过滤帖子网址2 = str(过滤帖子网址)

        # SQL 查询语句
        sql = "SELECT `帖子链接` FROM `网站文章内容`;"
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        帖子链接 = cursor.fetchall()
        self.最新文章内容帖子网址 = str(帖子链接)

        # 关闭数据库连接
        db.close()
    def 模具_保存最新影视剧种子存放目录(self):
        种子存放目录=self.影视类型+'/'+self.短标题

        # 打开数据库连接,保存已下载网址
        db = pymysql.connect("localhost", "root", "", "最新影视剧", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句
        sql = """INSERT INTO 种子存放目录(种子存放目录)
                                  VALUES ('%s','%s')""" % (种子存放目录, self.时间ID)
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

    # ==========最新影视剧数据库的小更新=========

    # =================清洗模具集==========================================

    def 模具_换头部信息(self):  # 头部信息 def 函数模具内通行变量
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

    def 模具_打开的网址请求返回网页内容(self, 网址):
        # global 换IP时间计数  # 时间计数全局变量声明

        循环 = 0
        次数循环 = 0
        缓冲时间 = 0
        while 循环 == 0:  # 条件循环  post
            此时数 = int(time.time())
            if 此时数 > 换IP时间计数 + 200:
                self.模具_换ip连接()
                self.模具_换头部信息()

            try:
                此时数2 = int(time.time())
                if 缓冲时间 > 此时数2:
                    time.sleep(0.5)
                    print('缓冲时间 多加 0.5秒')
                self.返回网页内容 = requests.post(网址, headers=头部信息, timeout=3)

                缓冲时间 = int(time.time()) + 0.5

            except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout,
                    requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout,
                    requests.exceptions.ChunkedEncodingError, requests.exceptions.InvalidSchema) as 异常:

                次数循环 += 1
                print('网络异常等待', 异常)
                print('倒数9秒再连接', 次数循环, '次')
                time.sleep(3)

                if 'None, 10053,' in str(异常):
                    self.模具_换头部信息()
            else:
                if '200' in str(self.返回网页内容):
                    self.返回网页内容.encoding = "UTF-8"  # 转换encoding='UTF-8' "gbk"
                    return  # 返回
                else:
                    print('网站网络异常,状态码:', self.返回网页内容)
                    print('等待10秒')
                    time.sleep(10)

    def 模具_换ip连接(self):
        # coding:gbk
        print('宽带连接进行时.....')
        os.system(r"rasphone -h 宽带连接")  # xxx0是你的拨号名称,xp下默认是"宽带连接”.
        os.system(r"rasdial 宽带连接 02007044432@163.gd  77341859")  # xxx0同上,xxx1 拨号用户名 ,xxx2拨号密码.
        time.sleep(3)
        print('换ip再连接完成')

        # ============内容页过滤与提取===================================================

    def 模具_符号清洗(self, 原文):
        列表 = ["[", "]", "(", ")", "\'", "\"", "`", ":", "*", "/", "\\", "#", "\"", "?", ".", "\'", "'", "\'", "'", '',
              ',', ':', ':',
              '！', '[', ']', ' ', '`', '|',
              '\\n', '\n', '>', '<', '%']
        for 符号 in 列表:
            原文 = str(原文).replace(符号, '')
        if self.长标题清洗 == 1:
            self.长标题清洗 = 0
            return 原文
        原文 = str(原文).replace(' ', '')
        return 原文

    def 模具_种子名清洗(self, 种子名):
        种子名规则 = '\[bt.{1,}\]'
        种子名 = re.sub(种子名规则, '', str(种子名))
        种子名规则 = '\.bt.{1,}torrent'
        种子名 = re.sub(种子名规则, '.torrent', str(种子名))
        列表 = ["\'", "\"", ":", ' ', ' ', '`', '|', '\\n', '\n', '>', '<', '%', "*", "`", "\'", "\"", "`", ":", "*", "/",
              "\\", "#", "\"", "?", ".", "\'", "'", "\'", "'", '', ',', ':', ':',
              '！', "/", "\\", "#", "\""
            , "www.517ww.com", "www.117hm.com", "www.15bx.com", "www.hanmi520.com", "www.hanmi.cc", "?"]

        for 符号 in 列表:
            种子名 = str(种子名).replace(符号, '')

        # 替换不同字符间的符号
        if '[' in 种子名 or ']' in 种子名:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            种子名 = 种子名.replace("[", "[")  # 替换   , 1) 次数 1
            种子名 = 种子名.replace("]", "]")  # 替换   , 1) 次数 1
        if '(' in 种子名 or ')' in 种子名:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            种子名 = 种子名.replace("(", "（")  # 替换   , 1) 次数 1
            种子名 = 种子名.replace(")", "）")  # 替换   , 1) 次数 1
        return 种子名

    def 模具_帖子正文清洗(self):
        # 规则 = '(?<=648542).{1,}(?=BAIDU_CLB_SLOT_ID)'
        def 模具_每一段落清洗(每一段落):
            规则列表 = ["迅雷",'href="http','text/javascript', "百度网盘", "网盘下载",   "ed2k://", "ftp://", "本帖最后由", "上季",
                    "<scripttype=","BAIDU_CLB_SLOT_ID",'上季','百度','网盘','本帖','magnet','磁力','种子','电驴','转贴','本贴',
                    "◎BT", "之家整理", "BT之家", "本帖编辑", "HQC小组","所有压制整合作品","链接"]
            for 规则 in 规则列表:
                if 规则 in 每一段落 and 'douban' not in 每一段落:
                    每一段落 ='>'
                    return 每一段落  # 返回
            return 每一段落  # 返回


        一楼内容 = str(self.帖子内容)
        规则 = '(?<=643755).{1,}(?=648546)'
        一楼内容列表 = re.findall(规则, str(一楼内容), re.S)
        一楼内容 = str(一楼内容列表[0])
        合成一楼内容=''

        if '<p' in 一楼内容 and '<br' in 一楼内容:  # <p>  代码为 段落
            列表 = 一楼内容.split('<p')  #
            for 每一段落 in 列表:
                if '<br' in 每一段落:  # <p>  代码为 段落
                    列表B = 每一段落.split('<br')  # #<br>  代码为 新的一行 <br>
                    for 每一段落B in 列表B:
                        每一段落B=模具_每一段落清洗(每一段落B)
                        合成一楼内容 = 合成一楼内容 + '<br' + 每一段落B
                else:  # 否则
                    每一段落 = 模具_每一段落清洗(每一段落)
                    合成一楼内容 = 合成一楼内容+'<p' +每一段落
        else:  # 否则
            if '<p' in 一楼内容:  # <p>  代码为 段落
                列表 = 一楼内容.split('<p')  #
                for 每一段落 in 列表:
                    每一段落 = 模具_每一段落清洗(每一段落)
                    合成一楼内容 = 合成一楼内容 + '<p' + 每一段落
            elif '<br' in 一楼内容:  # <p>  代码为 段落
                列表 = 一楼内容.split('<br')  # #<br>  代码为 新的一行
                for 每一段落 in 列表:
                    每一段落 = 模具_每一段落清洗(每一段落)
                    合成一楼内容 = 合成一楼内容 + '<br' + 每一段落

        print('合成一楼内容', 合成一楼内容)
        一楼内容 =合成一楼内容
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
        self.正文 = self.模具_网站图片网址清洗转换(正文)

    def 模具_提取一楼种子名进行过滤(self):
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
                    self.模具_保存电影与合集过滤帖子网址()
                    self.跳过循环 = 0
                    return  # 返回 0 值,跳过循环

        # 电影的过滤
        # 謦灵风软www.|.com|先版|鲜版|鲜版|删减版|TS|TC|抢先|清晰|公映版|网盘下载|电驴|迅雷|[email /span

    def 模具_短标题的再次清洗(self):
        self.短标题 = str(self.短标题).replace("] ", ']')
        if '][' in str(self.短标题):
            规则3 = '(?<=\]\[).{1,}'
            短标题列表 = re.findall(规则3, str(self.短标题))
            self.短标题 = str(短标题列表[0])
        if '/' in str(self.短标题):
            规则 = '/.{1,}'
            self.短标题 = re.sub(规则, '', str(self.短标题), count=0)
        if '.' in str(self.短标题):
            规则 = '\..{1,}'
            self.短标题 = re.sub(规则, '', str(self.短标题), count=0)
        elif ' ' in str(self.短标题):
            规则 = '\s.{1,}'
            self.短标题 = re.sub(规则, '', str(self.短标题), count=0)


        #新-电影与合集-目录有季 不用删除第与季
            #if '第' in str(self.短标题):
            #if '季' in str(self.短标题):
            #规则 = '第.{1,}'
        #self.短标题 = re.sub(规则, '', str(self.短标题), count=0)

    def 模具_长标题(self):
        # 长标题规则 = '(?<=\]\[).{1,}'
        # print('self.帖子标题1:', self.帖子标题)
        # 长标题列表 = re.findall(长标题规则, str(self.帖子标题))
        # print('长标题列表:', 长标题列表)
        # self.长标题=长标题列表[0]
        长标题 = self.帖子标题

        if '更' in str(长标题) and '集' in str(长标题):

            规则 = '更.{1,}集'
            长标题 = re.sub(规则, '', str(长标题))
        # 符号清洗
        self.长标题 = self.模具_符号清洗(长标题)
        if len(self.长标题) == 0:
            self.长标题 = str(self.短标题)
        print('self.长标题', self.长标题)

    def 模具_种子目录并下载(self, 下载地址):
        # =========== 种子目录================
        # 种子目录 = 'F:/电影模板/下载种子目录2/电视剧/电视剧名/季度/'
        # F:/电影模板/下载种子目录2/动漫/动漫名/季度/
        '#F:/电影模板/下载种子目录2/电视剧/剧名/季度/分层名/'

        if '第' in str(self.中短标题) and '季' in str(self.中短标题):

            短标题规则 = '.{1,}(?=第)'
            季度名 = re.sub(短标题规则, '', self.中短标题)
            季度名 = self.模具_符号清洗(季度名)
            种子目录 = str(self.种子目录).replace("剧名", str(self.短标题))
            种子目录 = str(种子目录).replace("季度", 季度名)

        else:
            种子目录 = str(self.种子目录).replace("剧名/季度", str(self.短标题))
        创建种子目录 = str(种子目录).strip('/')

        for 三次循环创建种子目录 in 'ger':  # 条件循环  post
            try:
                os.makedirs(创建种子目录)  # makedirs 创建多级目录文件夹,mkdir创建一个文件夹
            except (FileNotFoundError, OSError) as 异常:
                if os.path.exists(创建种子目录):  # 必有条件选择,否则出错
                    break  # 结束循环
                print('创建种子目录的异常', 异常)
                创建种子目录 = str(创建种子目录).replace(' ', '')
                创建种子目录 = str(创建种子目录).rstrip()  # 指定删除的字符串末尾的字符(默认为空格)
                种子目录 = str(种子目录).replace(' ', '')
                种子目录 = str(种子目录).rstrip()  # 指定删除的字符串末尾的字符(默认为空格)
            else:
                break  # 结束循环

        # =========== 种子下载=====
        种子名 = str(self.种子名)
        for 三次循环创建种子目录 in 'ge3':  # 条件循环  post
            try:

                目录与种子名 = str(种子目录) + str(种子名)

                if not os.path.exists(目录与种子名):  # 探测目录或文件是否存在

                    复制合集目录与种子名 = str(目录与种子名).replace("下载种子目录2", "下载种子目录3") #替换   , 1) 次数 1
                    if os.path.exists(复制合集目录与种子名): # 探测目录或文件是否存在
                        shutil.copy(复制合集目录与种子名,种子目录)
                        print(复制合集目录与种子名)
                        print('复制文件:', 种子目录)
                        return  # 返回
                    else:  # 否则
                        self.模具_打开的网址请求返回网页内容(下载地址)
                        with open(目录与种子名, 'wb') as fout:
                            fout.write(self.返回网页内容.content)
                            fout.close()
                else:  # 否则

                    self.跳过循环3 = 0
                    return #返回

            except (FileNotFoundError, OSError):
                种子名 = str(种子名).replace('.', '')
                种子名 = str(种子名).replace(' ', '')
                if '.torrent' not in str(种子名):
                    种子名 = str(种子名).replace('torrent', '.torrent')
                if '3' in 三次循环创建种子目录:
                    print('找不到目录与种子名,出错跳出种子下载循环', 目录与种子名)
                    return  # 返回 空值,
            else:
                self.过滤种子网址 = self.过滤种子网址 + str(下载地址)
                break  # 结束循环

                # 种子目录 = str(种子目录).replace(' ', '')
        print('完成下载', 目录与种子名)
        print('===========================')

    def 模具_网站图片网址清洗转换(self, 图片网址文本):
        列表 = ["http://www.btbtt.co/", "http://btbtt.co/", "http://www.btbtt.net/", "http://www.btbtt.me/",
              "http://www.btbtt.com/", "http://www.btbtt.pw/",
              "http://btbtt.net/", "http://btbtt.me/", "http://btbtt.com/", "http://btbtt.pw/"]

        for 符号 in 列表:
            图片网址文本 = str(图片网址文本).replace(符号, 'http://91btbtt.com/')
        return 图片网址文本

    # =================合集网址过滤模具集====================

    def 模具_总提取帖子链接列表(self):
        self.清空数据库 = 0
        总提取帖子链接列表 = []
        for 倒页数 in range(self.倒页总数, 0, -1):

            self.页数网址 = str(self.页数网址).replace("123", str(倒页数))
            # ===========self.打开的网址请求self.返回网页内容======================================
            self.模具_打开的网址请求返回网页内容(self.页数网址)
            # time.sleep(5)
            帖子列表 = self.返回网页内容
            # ====================================================
            帖子列表html = html.fromstring(帖子列表.text)
            提取帖子链接列表 = 帖子列表html.xpath('//*[@id="threadlist"]/table[*]/tr/td[1]/a[1]/@href')

            for 各帖子链接 in 提取帖子链接列表:
                各帖子链接 = 各帖子链接.replace("thread", "http://91btbtt.com/thread")
                if 各帖子链接 in self.页面提取帖子链接列表文本:
                    print('最新剧集链接在====', 倒页数, '=======页')
                    continue  # 跳过循环

                if 各帖子链接 in self.过滤帖子网址:
                    print('过滤帖子网址')
                    continue  # 跳过循环
                self.模具_保存电影与合集总提取帖子链接列表(各帖子链接)
                总提取帖子链接列表.append(各帖子链接)
            print('======倒页数============', 倒页数)
            # ============self.各帖子链接============================================================

        for 各帖子链接 in self.总提取帖子链接列表1:
            各帖子链接 = 各帖子链接[0]
            总提取帖子链接列表.append(各帖子链接)
        print('====================帖子链接总数=================', len(总提取帖子链接列表))

        self.总提取帖子链接列表 = set(总提取帖子链接列表)
        print('====================帖子链接总数去重复后:=================', len(self.总提取帖子链接列表))
   

    def 模具_帖子标题列表清洗(self):
        print('帖子标题列表', self.帖子标题列表)
        for 帖子标题 in self.帖子标题列表:
            if len(帖子标题) > 60:
                self.帖子标题 = str(帖子标题)
                return  # 返回
            elif len(帖子标题) > 40:
                self.帖子标题 = str(帖子标题)
                return  # 返回
            elif len(帖子标题) > 20:
                self.帖子标题 = str(帖子标题)
                return  # 返回
            elif len(帖子标题) > 6:
                self.帖子标题 = str(帖子标题)
                return  # 返回

    def 模具_浏览器输入验证码提取cookies(self):
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

    def 模具_测试cookies存活(self):

        self.模具_导入cookie()

        self.url = 'http://3e38.com/image/article_add.php?channelid=17'
        self.s = requests.Session()  # 创建全局会话
        self.s.cookies.update(self.cookies)  # 格式化cookie,全网页才能共享登录cookie,

        返回网页内容 = self.s.get(self.url)

        返回网页内容 = 返回网页内容.text

        if '看不清' in 返回网页内容:
            print('登录失效,正在启动浏览器.')
            self.模具_浏览器输入验证码提取cookies()
        else:  # 否则
            print('======登录成功=========')

    def 模具_导入cookie(self):
        with open('E:\PY学习文件\PyCharm文件\BT影视剧\de3ede38.txt', 'r') as f:
            self.cookies = {}
            for line in f.read().split(';'):
                name, value = line.strip().split('=', 1)  # 1代表只分割一次
                self.cookies[name] = value


class 类_电影下载(类_公共库):  # 调用 类的模具 self.模具_数据库()
    def __init__(self,过滤置顶类型最新影视网址):

        global 三月前时间  # def 函数模具内通行变量
        今天天数 = datetime.datetime.now()
        三月前时间 = 今天天数 + datetime.timedelta(days=-90)
        规则 = '\s.{0,}'
        三月前时间 = re.sub(规则, '', str(三月前时间))  # 除掉后面的时间分数 替换   ,count=0,re.S|re.I
        三月前时间 = int(str(三月前时间).replace("-", ""))  # 替换   , 1) 次数 1


        self.影视类型 = '电影'
        self.倒页总数 = 150
        self.过滤置顶类型最新影视网址=过滤置顶类型最新影视网址


        self.模具_提取电影与合集数据库里的过滤网址一已下载内容网址一过滤种子网址()#最新电影不过滤网址,不跳过
        self.模具_提取电影与合集数据库里的总提取帖子链接列表()
        self.模具_提取最新影视剧数据库里的过滤网址()
        self.页数网址 = 'http://91btbtt.com/forum-index-fid-951-page-123.htm'
        self.模具_总提取帖子链接列表()

        self.模具_电影各链接网址处理()

    def 模具_电影各链接网址处理(self):
        self.电影倒计数 = 500
        for 各帖子链接 in self.总提取帖子链接列表:

            print(self.影视类型,'========电影倒计数================', self.电影倒计数)


            if self.电影倒计数 > 500:
                break # 结束循环

            if len(各帖子链接) == 0:
                print('==帖子链接链接为空=== # 跳过当前循环')
                continue  # 跳过当前循环,继续进行下一轮循环

            self.各帖子链接 = str(各帖子链接)


            if self.各帖子链接 in self.过滤帖子网址:
                print('过滤 电影倒计数 > 500 帖子网址')
                continue  # 跳过循环

            if self.各帖子链接 in self.过滤帖子网址2:
                print('过滤帖子网址')
                continue  # 跳过循环

            if self.各帖子链接 in self.最新文章内容帖子网址:
                print('帖子内容已经存在,跳过')
                self.电影倒计数 = self.电影倒计数 - 1
                continue  # 跳过循环


            print('各帖子链接', self.各帖子链接)

            # ============换IP时间计数===============
            self.跳过循环 = 1
            # self.模具_换IP时间计数()

            # ============  self.打开的网址请求self.返回网页内容==============================================
            self.模具_打开的网址请求返回网页内容(self.各帖子链接)
            帖子内容 = self.返回网页内容

            # =====================
            self.帖子内容html = etree.HTML(帖子内容.text)
            self.帖子标题列表 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/h2/text()')
            self.标题前的栏目列表 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/h2/a/text()')


            # ===========帖子标题列表清洗===========================================
            self.模具_帖子标题列表清洗()
            self.原版短标题 = self.模具_符号清洗(self.帖子标题)

            # =========#过滤标题栏目=====================================================
            self.模具_电影过滤标题栏目()
            if self.跳过循环 == 0:
                continue  # 跳过循环

            # ===============过滤图片并且提取self.标题图与self.正文图集==========================================

            self.帖子内容 = (帖子内容.text)
            self.模具_电影过滤图片并且提取标题图()

            if self.跳过循环 == 0:
                continue  # 跳过循环
            self.标题图 = self.模具_网站图片网址清洗转换(self.标题图)
            # ========过滤图片已破与标记其它网站,跳过循环=================================================================

            self.模具_电影过滤图片已破与标记其它网站()

            if self.跳过循环 == 0:
                continue  # 跳过循环

            # ========提取一楼种子名进行过滤=============================================================

            self.模具_电影过滤一楼种子名()

            if self.跳过循环 == 0:
                continue  # 跳过循环

            # ======中短标题与self.短标题的清洗==============================================================================================================================================

            # ==========================================================
            self.模具_电影中短标题与短标题的清洗()
            if self.跳过循环 == 0:
                print('中短标题与短标题的清洗,跳过循环')
                continue  # 跳过循环
            self.短标题 = str(self.帖子标题)
            # ==================================

            self.时间ID = int(time.strftime("%y%m%d%H%M%S", time.localtime()))
            if len(self.短标题) == 0:
                self.短标题 =self.原版短标题
            self.短标题 = str(self.帖子标题)
            中短标题 = self.短标题
            print('=self.短标题3=', self.短标题)

            # =================self.短标题的再次清洗=========================================
            self.模具_电影短标题的再次清洗()

            # 符号清洗
            self.短标题 = self.模具_符号清洗(self.短标题)

            if len(self.短标题) == 0:
                self.短标题 =self.原版短标题
            self.中短标题 = self.模具_符号清洗(中短标题)
            if len(self.短标题) == 0:
                self.短标题 = self.原版短标题
            print('短标题', self.短标题)
            # ===========self.长标题=====================================================================================================================
            self.长标题 = self.中短标题 + str(self.长标题后缀)
            self.模具_电影长标题符号清洗()
            # ===========self.主栏目ID、self.标题前栏目字符串==============================================================================================
            标题前栏目字符串 = ''.join(self.标题前的栏目列表)
            self.标题前栏目字符串 = str(标题前栏目字符串).replace('[]', '')
            self.标题前栏目字符串 = str(标题前栏目字符串).replace('[纯净版]', '')
            self.主栏目ID = 21

            if self.电影倒计数 > 500:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                摘要 = '<h2>资源下载:<a href="/uploads/html/dying/参数1.html"target="_blank">参数2.torrent</a></h2>'

            else:  # 否则
                摘要 = '<h2>资源下载:<a href="/uploads/2html/dying/参数1.html"target="_blank">参数2.torrent</a></h2>'


            摘要 = str(摘要).replace("参数1", str(self.短标题))
            self.摘要 = str(摘要).replace("参数2", str(self.长标题))
            print('摘要', self.摘要)
            print('标题前栏目字符', self.标题前栏目字符串)

            self.更新集数 = '合集'
            # ===========self.网站副栏目ID============================================================================

            self.模具_电影网站副栏目ID()
            # =========(模具)self.正文清洗=====================================================

            self.模具_帖子正文清洗()

            # ===========保存self.帖子内容至数据库==================================================================

            # =========== 提取一楼种子列表==================================================================

            self.模具_提取电影一楼种子()

            # =========== 提取各分层页种子列表=================================================================
            self.模具_提取电影各分层页种子列表()

            # ===========# 保存已下载网址至数据库=================================================================
            if self.电影倒计数 > 500:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                self.模具_保存电影与合集帖子内容至数据库()
                self.模具_保存电影与合集种子存放目录()

            else:  # 否则
                self.电影倒计数 = self.电影倒计数 - 1
                self.模具_保存最新影视剧帖子内容至数据库()
                self.模具_保存最新影视剧种子存放目录()

            # self.模具_保存电影与合集已下载内容页网址()
            self.过滤帖子网址 = self.过滤帖子网址 + str(self.各帖子链接)
            # print('=倒页数==', 倒页数)






    def 模具_电影过滤图片已破与标记其它网站(self):
        列表 = ['tietuku', 'yupoo', 'imgsrc.baidu', '謦灵风软']
        for 符号 in 列表:
            if 符号 in str(self.帖子内容):
                print(符号, '图片已破or标记其它网站,跳过循环')
                print('=====================')
                self.模具_保存电影与合集过滤帖子网址()
                self.跳过循环 = 0
                return  # 返回 0 值,跳过循环

    def 模具_电影过滤标题栏目(self):

        列表 = ['删节版', '删减版', 'TS', '抢先', '抢鲜', 'TC', '清晰', '大陆', '中国', 'BT之家整合', '版块公告', '版块专用', '[猪猪]',
              '[Resilio-Sync]', '有水印', '有广告']
        帖子标题 = str(self.帖子标题) + str(self.标题前的栏目列表)
        版本表 = ['抢', '删', '鲜']

        if '版' in 帖子标题:
            for 版符号 in 版本表:
                if 版符号 in 帖子标题:
                    print(版符号, '版,跳过循环')
                    print('=====================')
                    self.模具_保存电影与合集过滤帖子网址()
                    self.跳过循环 = 0
                    return  # 返回 0 值,跳过循环

        for 符号 in 列表:
            if 符号 in 帖子标题:
                print(符号, '列表符号,跳过循环')
                print('=====================')
                self.模具_保存电影与合集过滤帖子网址()
                self.跳过循环 = 0
                return  # 返回 0 值,跳过循环

    def 模具_电影过滤图片并且提取标题图(self):
        标题图集 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]//@src')
        for 次数 in range(标题图集.count('http://cbjs.baidu.com/js/o.js')):  # count() 方法用于统计某个元素在列表中出现的次数.
            标题图集.remove('http://cbjs.baidu.com/js/o.js')  # 移除列表中某个值的第一个匹配项

        标题图集文本 = str(标题图集)
        print('self.标题图0')

        # ==========过滤无种子附件,跳过循环======================================================
        if 'torrent.gif' not in str(self.帖子内容) and '个附件' not in str(self.帖子内容):
            print('无种子附件,跳过循环')
            print('=====================')

            self.模具_保存电影与合集过滤帖子网址()
            self.跳过循环 = 0

            return  # 返回 0 值,跳过循环

        if '◎' not in str(self.帖子内容):
            print('无◎,规范的self.帖子内容,跳过循环')
            print('=====================')

            self.模具_保存电影与合集过滤帖子网址()
            self.跳过循环 = 0

            return  # 返回 0 值,跳过循环

        if 'HQC' in self.帖子内容:
            if len(标题图集) == 1:
                self.标题图 = 标题图集[0]
                if 'http' not in str(self.标题图):
                    self.标题图 = str(self.标题图).replace("/upload", "http://91btbtt.com/upload")
                    标题图集 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/img/@img')
                return  # 返回
            else:
                self.标题图 = 标题图集[1]
                if 'http' not in str(self.标题图):
                    self.标题图 = str(self.标题图).replace("/upload", "http://91btbtt.com/upload")
                return  # 返回

        if 'Non' in str(标题图集文本):
            print('无标题图,跳过循环')
            print('=====================')
            self.模具_保存电影与合集过滤帖子网址()
            self.跳过循环 = 0
            return  # 返回 0 值,跳过循环
        print('self.标题图1')
        if len(标题图集) == 0:
            print('无self.标题图,跳过循环')
            print('=====================')
            self.模具_保存电影与合集过滤帖子网址()
            self.跳过循环 = 0
            return  # 返回 0 值,跳过循环
        else:
            self.标题图 = 标题图集[0]
            print('self.标题图2')
            if 'http' not in str(self.标题图):
                self.标题图 = str(self.标题图).replace("/upload", "http://91btbtt.com/upload")
            print('self.标题图', self.标题图)
            return  # 返回

    def 模具_电影过滤一楼种子名(self):
        种子名列表 = self.帖子内容html.xpath(
            '//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[*]/td[1]/a/text()|//*[@id="body"]/div/table[2]/tr[1]/td[3]/font/b/div[1]/table/tr[3]/td[1]/a/text()')
        种子名列表 = str(种子名列表)

        版本表 = ['抢', '删', '鲜']

        if '版' in 种子名列表:
            for 版符号 in 版本表:
                if 版符号 in 种子名列表:
                    print(版符号, '版,跳过循环,一楼种子名')
                    print('=====================')
                    self.模具_保存电影与合集过滤帖子网址()
                    self.跳过循环 = 0
                    return  # 返回 0 值,跳过循环

        列表 = ('删节版', '删减版', 'TS', '抢先', 'TC', '清晰', '大陆', '中国', 'www.', '.com', '.net')
        for 符号 in 列表:
            if 符号 in 种子名列表:
                print(符号, '列表符号,跳过循环,一楼种子名')
                print('=====================')
                self.模具_保存电影与合集过滤帖子网址()
                self.跳过循环 = 0
                return  # 返回 0 值,跳过循环

    def 模具_电影中短标题与短标题的清洗(self):
        帖子标题 = str(self.帖子标题)

        if ']' in str(帖子标题):
            帖子标题 = str(帖子标题).replace("]", ']')

        if ']' not in str(帖子标题):
            print('不规整的标题帖子,跳过循环')

            self.模具_保存电影与合集过滤帖子网址()
            print('=====================')
            self.跳过循环 = 0
            return  # 返回 0 值,跳过循环

        for i in range(1):
            前缀下载列表 = ['下载', 'BT', '迅雷', '网盘', '电骡', '百度云', '种子', '云盘', '磁力链', 'FTP', '电驴']
            循环结束 = 0

            for 前缀 in 前缀下载列表:
                if 前缀 in 帖子标题:
                    帖子标题 = str(帖子标题).replace("]", '%%', 1)  # 次数
                    规则 = '.{0,}%%'
                    帖子标题 = re.sub(规则, '', str(帖子标题))

                    循环结束 = 1

                    break  # 结束循环
            if 循环结束 == 1:
                break  # 结束循环
            列表 = ('美国][', '英国][', '大陆][', '香港][', '台湾][', '日本][',
                  '韩国][', '法国][', '西剧][', '泰国][', '加剧][', '意剧][', '澳剧][', '德国][', '新马][',
                  '剧情][', '喜剧][', '爱情][', '偶像][', '动作][', '奇幻][', '科幻][', '悬疑][', '罪案][', '刑侦][',
                  '战争][', '谍战][', '军旅][', '历史][', '古装][', '惊悚][', '恐怖][', '真人][', '时装][', '医务][',
                  '歌舞][', '其他][', '都市][', '情感][', '家庭][', '武侠][', '纪录][', '经典][', '其它][', '动画][')
            for 字符值 in 列表:
                if 字符值 in str(帖子标题):
                    帖子标题 = str(帖子标题).replace(字符值, '%%', 1)  # 次数
                    规则 = '.{0,}%%'
                    帖子标题 = re.sub(规则, '', str(帖子标题))

        if '][' in str(帖子标题):
            帖子标题 = str(帖子标题).replace("][", '%%', 1)  # 次数
            规则 = '.{0,}%%'
            self.长标题后缀 = re.sub(规则, '', str(帖子标题))

            规则 = '%%.{0,}'
            self.帖子标题 = re.sub(规则, '', str(帖子标题))

        else:
            self.长标题后缀 = str(帖子标题)
            self.帖子标题 = 帖子标题

    def 模具_电影短标题的再次清洗(self):
        短标题 = str(self.短标题).replace("] ", ']')

        符号列表 = ['/', '.', ' ', '第']
        for 符号 in 符号列表:
            if 符号 in str(短标题):
                if '季' in str(短标题):
                    短标题 = str(短标题).replace(符号, '%%', 1)
                    规则 = '%%.{1,}'
                    短标题 = re.sub(规则, '', str(短标题))
                短标题 = str(短标题).replace(符号, '%%', 1)
                规则 = '%%.{1,}'
                短标题 = re.sub(规则, '', str(短标题))
                print('短标题0', 短标题)
        self.短标题 = 短标题
        print('self.短标题', self.短标题)

    def 模具_电影长标题符号清洗(self):
        列表 = ["\'", "\"", ":", "*", "/", "#", "\"", "?", ".", "\'", "'", "\'", "'", '', ',', '！', '\\n',
              '\n', '>', '<']
        原文 = str(self.长标题)
        for 符号 in 列表:
            原文 = 原文.replace(符号, '')
        self.长标题 = 原文

    def 模具_提取电影一楼种子(self):
        帖子内容html文本 =str(self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[1]/td[1]/text()'))
        if '个附件' in 帖子内容html文本:

            提取一楼种子下载地址列表 = self.帖子内容html.xpath(
                '//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[*]/td[1]/a/@href|//*[@id="body"]/div/table[2]/tr[1]/td[3]/font/b/div[1]/table/tr[*]/td[1]/a/@href')
            种子名列表 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[*]/td[1]/a/text()')
            for (一楼种子下载地址, 种子名) in zip(提取一楼种子下载地址列表, 种子名列表):
                # =========== 提self.过滤种子网址# 跳过循环============
                if 一楼种子下载地址 in str(self.过滤种子网址):
                    print('过滤种子网址')
                    print('=====================')
                    continue  # 跳过循环
                # =========(模具)种子名过滤与清洗============
                if '.jpg' in str(种子名):
                    print('跳过下载图片')
                    continue  # 跳过循环
                elif '.png' in str(种子名):
                    print('跳过下载图片')
                    continue  # 跳过循环
                # =========== (模具)种子名清洗=========
                self.种子名 = self.模具_种子名清洗(种子名)



                # =========== (模具)保存过滤已下载种子网址============

                self.模具_保存电影与合集过滤已下载种子网址(一楼种子下载地址)
                # =========== (模具)返回种子内容============
                一楼种子下载地址 = str(一楼种子下载地址).replace("attach", "http://91btbtt.com/attach")
                一楼种子下载地址 = str(一楼种子下载地址).replace("dialog", "download")
                self.模具_打开的网址请求返回网页内容(一楼种子下载地址)

                # =========== 种子目录=====F:/电影模板/下载种子目录2/电影/剧名/季度/===========
                if self.电影倒计数 > 500:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                    self.种子目录 = 'F:/下载种子目录/下载保存/旧电影/剧名/季度/'

                else:  # 否则
                    self.种子目录 = 'F:/电影模板/下载种子目录2/电影/剧名/季度/'

                # =========== (模具)种子目录并下载================

                self.模具_种子目录并下载(一楼种子下载地址)

    def 模具_提取电影各分层页种子列表(self):
        提取各分层 = self.帖子内容html.xpath('//*[@id="body"]/div/table[*]/tr/td[3]/div')
        层数 = (len(提取各分层))
        for 分层 in range(层数):
            查看附件规则 = ('//*[@id="body"]/div/table[' + str(分层) + ']/tr/td[3]/div/div[2]/table/tr[1]/td[1]/text()')
            分层名目规则 = ('//*[@id="body"]/div/table[' + str(
                分层) + ']/tr/td[3]/div/div/p[1]//text()|//*[@id="body"]/div/table[' + str(
                分层) + ']/tr/td[3]/div/div/p[1]/span/text()//*[@id="body"]/div/table[' + str(
                分层) + ']/tr/td[3]/div/div/p[1]/strong/text()')
            分层种子列表规则 = ('//*[@id="body"]/div/table[' + str(分层) + ']/tr/td[3]/div/div[2]/table/tr[*]/td[1]/a/@href')
            分层种子名列表规则 = ('//*[@id="body"]/div/table[' + str(分层) + ']/tr/td[3]/div/div[2]/table/tr[*]/td[1]/a/text()')
            查看附件 = self.帖子内容html.xpath(查看附件规则)
            分层名目 = self.帖子内容html.xpath(分层名目规则)
            分层名目 = ''.join(分层名目)  # 连接字符串数组.将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
            if '天天' in str(分层名目):
                continue  # 跳过循环
            if '个附件' in str(查看附件):
                分层种子列表 = self.帖子内容html.xpath(分层种子列表规则)
                分层种子名列表 = self.帖子内容html.xpath(分层种子名列表规则)
                for (下载地址, 种子名) in zip(分层种子列表, 分层种子名列表):

                    # =========== (模具)下载种子网址================
                    self.种子名 = self.模具_种子名清洗(种子名)

                    # =========== (模具)保存过滤已下载种子网址================
                    self.模具_保存电影与合集过滤已下载种子网址(下载地址)
                    # =========== (模具)下载种子网址================
                    下载地址 = str(下载地址).replace("attach", "http://91btbtt.com/attach")
                    下载地址 = str(下载地址).replace("dialog", "download")


                    # =========== 种子目录================

                    if self.电影倒计数 > 500:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                        种子目录 = 'F:/下载种子目录/下载保存/旧电影/剧名/季度/分层名/'

                    else:  # 否则
                        种子目录 = 'F:/电影模板/下载种子目录2/电影/剧名/季度/分层名/'
                    分层名目 = self.模具_符号清洗(分层名目)
                    self.种子目录 = str(种子目录).replace("分层名", 分层名目)
                    # =========== (模具)种子目录并下载================
                    self.跳过循环3 = 3
                    self.模具_种子目录并下载(下载地址)
                    if self.跳过循环3 == 0:
                        print('==种子文件已存在,跳过循环=====')

                        continue  # 跳过循环
            else:

                continue  # (跳过当前循环)

    def 模具_电影网站副栏目ID(self):

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
        网站副栏目ID = self.模具_符号清洗(网站副栏目ID)
        网站副栏目ID = 网站副栏目ID.strip()

        if len(网站副栏目ID) == 0:
            网站副栏目ID = '34'
        self.网站副栏目ID = str(网站副栏目ID).replace(" ", ",")
        print('网站副栏目ID', self.网站副栏目ID)




class 类_动漫下载(类_公共库):  # 调用 类的模具 self.模具_数据库()
    def __init__(self):
        self.影视类型 = '动漫'
        self.倒页总数 =20
        self.模具_置顶类型帖子分类()#提取最新影视链接 进行网址过滤
        self.模具_提取电影与合集数据库里的过滤网址一已下载内容网址一过滤种子网址()
        self.模具_提取电影与合集数据库里的总提取帖子链接列表()
        self.页数网址 = 'http://91btbtt.com/forum-index-fid-981-page-123.htm'
        self.模具_总提取帖子链接列表()
        self.模具_动漫各链接网址处理()



    def 模具_动漫各链接网址处理(self):

        倒计数 = len(self.总提取帖子链接列表)
        for 各帖子链接 in self.总提取帖子链接列表:

            print(self.影视类型,'========倒计数===========', 倒计数)
            倒计数 = 倒计数 - 1

            if len(各帖子链接) == 0:
                print('==帖子链接链接为空=== # 跳过当前循环')
                continue  # 跳过当前循环,继续进行下一轮循环

            self.各帖子链接 = str(各帖子链接)

            if self.各帖子链接 in self.过滤帖子网址:
                print('过滤帖子网址')
                continue  # 跳过循环
            print('各帖子链接', self.各帖子链接)


            # ============  self.打开的网址请求self.返回网页内容==============================================
            self.模具_打开的网址请求返回网页内容(self.各帖子链接)
            帖子内容 = self.返回网页内容

            # =====================
            self.帖子内容html = etree.HTML(帖子内容.text)
            self.帖子标题列表 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/h2/text()')
            self.标题前的栏目列表 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/h2/a/text()')

            # =========#过滤标题栏目=====================================================
            self.跳过循环 = 1  # 设定初始值
            self.模具_动漫过滤标题栏目()
            if self.跳过循环 == 0:
                continue  # 跳过循环
            # ===============过滤图片并且提取self.标题图与self.正文图集==========================================

            self.帖子内容 = (帖子内容.text)
            self.模具_动漫过滤图片并且提取标题图()
            if self.跳过循环 == 0:
                continue  # 跳过循环
            self.标题图 = self.模具_网站图片网址清洗转换(self.标题图)
            # ========过滤图片已破与标记其它网站,跳过循环=================================================================

            self.模具_动漫过滤图片已破与标记其它网站()
            if self.跳过循环 == 0:
                continue  # 跳过循环
            # ========提取一楼种子名进行过滤=============================================================

            self.模具_提取一楼种子名进行过滤()
            if self.跳过循环 == 0:
                continue  # 跳过循环

            # ===========帖子标题列表清洗===========================================
            self.模具_帖子标题列表清洗()
            self.原版短标题 = self.模具_符号清洗(self.帖子标题)
            # ======中短标题与self.短标题的清洗==============================================================================================================================================

            self.模具_动漫中短标题与短标题的清洗()
            if self.跳过循环 == 0:
                continue  # 跳过循环

            self.短标题 = self.帖子标题

            self.时间ID = int(time.strftime("%y%m%d%H%M%S", time.localtime()))
            if len(self.短标题) == 0:
                self.短标题 =self.原版短标题
            中短标题 = self.短标题

            # =================self.短标题的再次清洗=========================================
            self.模具_短标题的再次清洗()
            # 符号清洗
            短标题 = self.短标题
            self.短标题 = self.模具_符号清洗(短标题)
            self.中短标题 = self.模具_符号清洗(中短标题)
            if len(self.短标题) == 0:
                self.短标题 = self.原版短标题
            print('self.短标题', self.短标题)
            # ===========self.长标题=====================================================================================================================
            self.模具_长标题()
            # ===========self.主栏目ID、self.标题前栏目字符串==============================================================================================
            self.标题前栏目字符串 = ''.join(self.标题前的栏目列表)
            self.主栏目ID = 23
            摘要 = '<h2>资源下载:<a href="/uploads/html/dongman/参数1.html"target="_blank">参数2.torrent</a></h2>'
            摘要 = str(摘要).replace("参数1", str(self.短标题))
            self.摘要 = str(摘要).replace("参数2", str(self.长标题))
            print('.摘要', self.摘要)
            print('标题前栏目字符', self.标题前栏目字符串)

            self.更新集数 = '合集'
            # ===========self.网站副栏目ID============================================================================
            self.模具_动漫网站副栏目ID()
            # =========(模具)self.正文清洗=====================================================
            self.模具_帖子正文清洗()
            # ===========保存self.帖子内容至数据库==================================================================

            # =========== 提取一楼种子列表==================================================================

            self.模具_提取动漫一楼种子()

            # =========== 提取各分层页种子列表=================================================================
            self.模具_提取动漫各分层页种子列表()

            # ===========# 保存已下载网址至数据库=================================================================

            # self.模具_保存电影与合集已下载内容页网址()
            self.模具_保存电影与合集帖子内容至数据库()
            self.模具_保存电影与合集种子存放目录()
            self.过滤帖子网址 = self.过滤帖子网址 + str(self.各帖子链接)
            # print('=倒页数==', 倒页数)

    def 模具_动漫过滤图片已破与标记其它网站(self):
        列表 = ['tietuku', 'yupoo', 'imgsrc.baidu', '謦灵风软']
        for 符号 in 列表:
            if 符号 in str(self.帖子内容):
                print(符号, '图片已破or标记其它网站,跳过循环')
                print('=====================')
                self.模具_保存电影与合集过滤帖子网址()
                self.跳过循环 = 0
                return  # 返回 0 值,跳过循环

            else:
                return  # 返回 0 值,跳过循环

    def 模具_动漫过滤标题栏目(self):
        if '[单集]' in self.标题前的栏目列表:
            print('[单集]的栏目跳过循环')
            print('=====================')
            self.模具_保存电影与合集过滤帖子网址()
            self.跳过循环 = 0
            return  # 返回 0 值,跳过循环
        if '[讨论]' in self.标题前的栏目列表:
            print('[讨论]的栏目跳过循环')
            print('=====================')
            self.模具_保存电影与合集过滤帖子网址()
            self.跳过循环 = 0
            return  # 返回 0 值,跳过循环
        if '[猪猪]' in self.标题前的栏目列表:
            print('过滤栏目跳过循环')
            print('=====================')
            self.模具_保存电影与合集过滤帖子网址()
            self.跳过循环 = 0
            return  # 返回 0 值,跳过循环
        if '[Resilio-Sync]' in self.标题前的栏目列表:
            print('Sync的栏目跳过循环')
            print('=====================')
            self.模具_保存电影与合集过滤帖子网址()
            self.跳过循环 = 0
            return  # 返回 0 值,跳过循环

    def 模具_动漫中短标题与短标题的清洗(self):
        帖子标题 = self.帖子标题
        帖子标题 = str(帖子标题).replace("[", "[")
        帖子标题 = str(帖子标题).replace("]", "]")
        if '季]' in str(self.帖子标题):
            规则 = '(?<=\]\[).+?(?=季\])'
            帖子标题列表 = re.findall(规则, str(帖子标题))
            if len(帖子标题列表) == 0:
                规则 = '(?<=\[).+?(?=季\])'
                帖子标题列表 = re.findall(规则, str(帖子标题))
            帖子标题 = str(帖子标题列表[0])
            self.帖子标题 = str(帖子标题) + '季'
            return  # 返回 空值,
        elif '][全' in str(帖子标题):
            规则 = '(?<=\]\[).+?(?=\]\[全)'
            帖子标题列表 = re.findall(规则, str(帖子标题))
            if len(帖子标题列表) == 0:
                规则 = '(?<=\[).+?(?=\]\[全)'
                帖子标题列表 = re.findall(规则, str(帖子标题))
            self.帖子标题 = str(帖子标题列表[0])
            return  # 返回 空值,
        elif '][更' in str(帖子标题):
            规则 = '(?<=\]\[).+?(?=\]\[更)'
            帖子标题列表 = re.findall(规则, str(帖子标题))
            if len(帖子标题列表) == 0:
                规则 = '(?<=\[).+?(?=\]\[更)'
                帖子标题列表 = re.findall(规则, str(帖子标题))
            self.帖子标题 = str(帖子标题列表[0])
            return  # 返回 空值,
        elif '全][' in str(帖子标题):
            规则 = '(?<=\]\[).+?(?=全\]\[)'
            帖子标题列表 = re.findall(规则, str(帖子标题))
            if len(帖子标题列表) == 0:
                规则 = '(?<=\[).+?(?=全\]\[)'
                帖子标题列表 = re.findall(规则, str(帖子标题))
            self.帖子标题 = str(帖子标题列表[0])
            if '集' in str(self.帖子标题):
                规则2 = '.{1,}(?=\]\[)'
                帖子标题列表 = re.findall(规则2, str(self.帖子标题))
                if len(帖子标题列表) == 0:
                    return  # 返回 空值,
                self.帖子标题 = str(帖子标题列表[0])

                if '][' in str(self.帖子标题):
                    规则3 = '(?<=\]\[).{1,}'
                    帖子标题列表 = re.findall(规则3, str(self.帖子标题))
                    if len(帖子标题列表) == 0:
                        return  # 返回 空值,
                    self.帖子标题 = str(帖子标题列表[0])
            if '话' in str(帖子标题):
                规则 = '.{1,}(?=\]\[)'
                帖子标题列表 = re.findall(规则, str(self.帖子标题))
                if len(帖子标题列表) == 0:
                    return  # 返回 空值,
                self.帖子标题 = str(帖子标题列表[0])

                if '][' in str(self.帖子标题):
                    规则3 = '(?<=\]\[).{1,}'
                    帖子标题列表 = re.findall(规则3, str(self.帖子标题))
                    if len(帖子标题列表) == 0:
                        return  # 返回 空值,
                    self.帖子标题 = str(帖子标题列表[0])

        elif '集]' in str(帖子标题):
            规则 = '(?<=\]\[).+?(?=集\])'
            帖子标题列表 = re.findall(规则, str(帖子标题))
            self.帖子标题 = str(帖子标题列表[0])
            return  # 返回 空值,
        elif '剧场版' in str(帖子标题):
            self.帖子标题 = 帖子标题
            return  # 返回 空值,
        elif '劇場版' in str(帖子标题):
            self.帖子标题 = 帖子标题
            return  # 返回 空值,
        elif 'OVA' in str(帖子标题):
            self.帖子标题 = 帖子标题
            return  # 返回 空值,
        elif 'TV' in str(帖子标题):
            self.帖子标题 = 帖子标题
            return  # 返回 空值,
        elif ']' in str(帖子标题):
            print(' 帖子标题')
            print('不规整的标题帖子,跳过循环')
            print('=====================')
            self.模具_保存电影与合集过滤帖子网址()
            self.跳过循环 = 0
            return  # 返回 0 值,跳过循环

    def 模具_动漫过滤图片并且提取标题图(self):
        标题图集 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/p[*]/img/@src')
        # del 标题图集['http://cbjs.baidu.com/js/o.js']
        # ==========过滤无种子附件,跳过循环======================================================
        if 'torrent.gif' not in str(self.帖子内容) and '个附件' not in str(self.帖子内容):
            print('无种子附件,跳过循环')
            print('=====================')
            self.模具_保存电影与合集过滤帖子网址()
            self.跳过循环 = 0
            return  # 返回 0 值,跳过循环
        if len(标题图集) == 0:
            print('无标题图,跳过循环')
            print('=====================')
            self.模具_保存电影与合集过滤帖子网址()
            self.跳过循环 = 0
            return  # 返回 0 值,跳过循环

        if 'HQC' in self.帖子内容:
            if len(标题图集) == 1:
                标题图 = 标题图集[0]
                if 'http' not in str(标题图):
                    self.标题图 = str(标题图).replace("/upload", "http://91btbtt.com/upload")
                    标题图集 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/img/@img')

                return  # 返回 空值,
            else:
                标题图 = 标题图集[1]
                if 'http' not in str(标题图):
                    self.标题图 = str(标题图).replace("/upload", "http://91btbtt.com/upload")

                return  # 返回 空值,

        标题图 = 标题图集[0]
        if 'http' not in str(标题图):
            标题图 = str(标题图).replace("/upload", "http://91btbtt.com/upload")
        self.标题图 = 标题图

    def 模具_提取动漫一楼种子(self):
        帖子内容html文本 =str(self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[1]/td[1]/text()'))
        if '个附件' in 帖子内容html文本:

            提取一楼种子下载地址列表 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[*]/td[1]/a/@href')
            种子名列表 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[*]/td[1]/a/text()')
            for (一楼种子下载地址, 种子名) in zip(提取一楼种子下载地址列表, 种子名列表):
                # =========== 提self.过滤种子网址# 跳过循环============
                if 一楼种子下载地址 in str(self.过滤种子网址):
                    print('过滤种子网址')
                    print('=====================')
                    continue  # 跳过循环
                # =========(模具)种子名过滤与清洗============
                if '.jpg' in str(种子名):
                    print('跳过下载图片')
                    continue  # 跳过循环
                elif '.png' in str(种子名):
                    print('跳过下载图片')
                    continue  # 跳过循环
                # =========== (模具)种子名清洗=========
                self.种子名 = self.模具_种子名清洗(种子名)



                # =========== (模具)保存过滤已下载种子网址============
                self.模具_保存电影与合集过滤已下载种子网址(一楼种子下载地址)
                # =========== (模具)返回种子内容============
                一楼种子下载地址 = str(一楼种子下载地址).replace("attach", "http://91btbtt.com/attach")
                一楼种子下载地址 = str(一楼种子下载地址).replace("dialog", "download")
                self.模具_打开的网址请求返回网页内容(一楼种子下载地址)

                # =========== 种子目录================
                self.种子目录 = 'F:/电影模板/下载种子目录2/动漫/剧名/季度/'
                # =========== (模具)种子目录并下载================
                self.模具_种子目录并下载(一楼种子下载地址)

    def 模具_提取动漫各分层页种子列表(self):
        提取各分层 = self.帖子内容html.xpath('//*[@id="body"]/div/table[*]/tr/td[3]/div')
        层数 = (len(提取各分层))
        for 分层 in range(层数):
            查看附件规则 = ('//*[@id="body"]/div/table[' + str(分层) + ']/tr/td[3]/div/div[2]/table/tr[1]/td[1]/text()')
            分层名目规则 = ('//*[@id="body"]/div/table[' + str(
                分层) + ']/tr/td[3]/div/div/p[1]//text()|//*[@id="body"]/div/table[' + str(
                分层) + ']/tr/td[3]/div/div/p[1]/span/text()//*[@id="body"]/div/table[' + str(
                分层) + ']/tr/td[3]/div/div/p[1]/strong/text()')
            分层种子列表规则 = ('//*[@id="body"]/div/table[' + str(分层) + ']/tr/td[3]/div/div[2]/table/tr[*]/td[1]/a/@href')
            分层种子名列表规则 = ('//*[@id="body"]/div/table[' + str(分层) + ']/tr/td[3]/div/div[2]/table/tr[*]/td[1]/a/text()')
            查看附件 = self.帖子内容html.xpath(查看附件规则)
            分层名目 = self.帖子内容html.xpath(分层名目规则)
            分层名目 = ''.join(分层名目)  # 连接字符串数组.将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
            if '天天' in str(分层名目):
                continue  # 跳过循环
            if '个附件' in str(查看附件):
                分层种子列表 = self.帖子内容html.xpath(分层种子列表规则)
                分层种子名列表 = self.帖子内容html.xpath(分层种子名列表规则)
                for (下载地址, 种子名) in zip(分层种子列表, 分层种子名列表):

                    # =========== (模具)下载种子网址================
                    self.种子名 = self.模具_种子名清洗(种子名)


                    # =========== (模具)保存过滤已下载种子网址================
                    self.模具_保存电影与合集过滤已下载种子网址(下载地址)
                    # =========== (模具)下载种子网址================
                    下载地址 = str(下载地址).replace("attach", "http://91btbtt.com/attach")
                    下载地址 = str(下载地址).replace("dialog", "download")


                    # =========== 种子目录================
                    种子目录 = 'F:/电影模板/下载种子目录2/动漫/剧名/季度/分层名/'
                    分层名目 = self.模具_符号清洗(分层名目)
                    self.种子目录 = str(种子目录).replace("分层名", 分层名目)
                    # =========== (模具)种子目录并下载================
                    self.跳过循环3 = 3
                    self.模具_种子目录并下载(下载地址)
                    if self.跳过循环3 == 0:
                        print('==种子文件已存在,跳过循环=====')

                        continue  # 跳过循环
            else:

                continue  # (跳过当前循环)

    def 模具_动漫网站副栏目ID(self):
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
                   '[音乐]': '139', '[]': '', '[纯净版]': ''}
        网站副栏目ID = [网站副栏目字典[x] if x in 网站副栏目字典 else x for x in self.标题前的栏目列表]
        网站副栏目ID = str(网站副栏目ID)

        # 符号清洗
        网站副栏目ID = self.模具_符号清洗(网站副栏目ID)
        网站副栏目ID = 网站副栏目ID.strip()
        if len(网站副栏目ID) == 0:
            网站副栏目ID = '124'
        网站副栏目ID = str(网站副栏目ID).replace(" ", ",")
        网站副栏目ID = 网站副栏目ID.replace("124,124,124", "124")
        self.网站副栏目ID = 网站副栏目ID.replace("124,124", "124")
        print('网站副栏目ID', self.网站副栏目ID)

class 类_电视剧下载(类_公共库):  # 调用 类的模具 self.模具_数据库()
    def __init__(self):
        self.影视类型 = '电视剧'
        self.倒页总数 = 20
        self.模具_置顶类型帖子分类()#提取最新影视链接 进行网址过滤
        self.模具_提取电影与合集数据库里的过滤网址一已下载内容网址一过滤种子网址()
        self.模具_提取电影与合集数据库里的总提取帖子链接列表()
        self.页数网址 = 'http://91btbtt.com/forum-index-fid-950-page-123.htm'
        self.模具_总提取帖子链接列表()
        self.模具_电视剧各链接网址处理()


    def 模具_电视剧各链接网址处理(self):

        倒计数 = len(self.总提取帖子链接列表)
        for 各帖子链接 in self.总提取帖子链接列表:

            print(self.影视类型 ,'========倒计数=========', 倒计数)
            倒计数 = 倒计数 - 1

            if len(各帖子链接) == 0:
                print('==帖子链接链接为空=== # 跳过当前循环')
                continue  # 跳过当前循环,继续进行下一轮循环

            各帖子链接 = str(各帖子链接)
            self.各帖子链接 = 各帖子链接.replace("thread", "http://91btbtt.com/thread")
            if self.各帖子链接 in self.过滤帖子网址:
                print('过滤帖子网址')
                continue  # 跳过循环
            print('各帖子链接', self.各帖子链接)


            # ============  self.打开的网址请求self.返回网页内容==============================================
            self.模具_打开的网址请求返回网页内容(self.各帖子链接)
            帖子内容 = self.返回网页内容

            # =====================
            self.帖子内容html = etree.HTML(帖子内容.text)
            self.帖子标题列表 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/h2/text()')
            self.标题前的栏目列表 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/h2/a/text()')

            # =========#过滤标题栏目=====================================================
            self.跳过循环 = 1  # 设定初始值
            self.模具_电视剧过滤标题栏目()
            if self.跳过循环 == 0:
                continue  # 跳过循环
            # ===============过滤图片并且提取self.标题图与self.正文图集==========================================

            self.帖子内容 = (帖子内容.text)
            self.模具_电视剧过滤图片并且提取标题图()
            if self.跳过循环 == 0:
                continue  # 跳过循环
            self.标题图 = self.模具_网站图片网址清洗转换(self.标题图)
            # ========过滤图片已破与标记其它网站,跳过循环=================================================================

            self.模具_电视剧过滤图片已破与标记其它网站()
            if self.跳过循环 == 0:
                continue  # 跳过循环

            # ========提取一楼种子名进行过滤=============================================================

            self.模具_提取一楼种子名进行过滤()
            if self.跳过循环 == 0:
                continue  # 跳过循环

            # ===========帖子标题列表清洗===========================================
            self.模具_帖子标题列表清洗()
            self.原版短标题 = self.模具_符号清洗(self.帖子标题)
            # ======中短标题与self.短标题的清洗==============================================================================================================================================


            self.模具_电视剧中短标题与短标题的清洗()
            if self.跳过循环 == 0:
                continue  # 跳过循环

            self.短标题 = self.帖子标题

            self.时间ID = int(time.strftime("%y%m%d%H%M%S", time.localtime()))
            if len(self.短标题) == 0:
                self.短标题 =self.原版短标题
            中短标题 = self.短标题
            # =================self.短标题的再次清洗=========================================
            self.模具_短标题的再次清洗()

            # 符号清洗
            self.短标题 = self.模具_符号清洗(self.短标题)
            self.中短标题 = self.模具_符号清洗(中短标题)
            if len(self.短标题) == 0:
                self.短标题 = self.原版短标题
            print('短标题', self.短标题)
            # ===========self.长标题=====================================================================================================================
            self.模具_长标题()
            # ===========self.主栏目ID、self.标题前栏目字符串==============================================================================================
            self.标题前栏目字符串 = ''.join(self.标题前的栏目列表)

            self.主栏目ID = 22
            摘要 = '<h2>资源下载:<a href="/uploads/html/dianshiju/参数1.html"target="_blank">参数2.torrent</a></h2>'
            摘要 = str(摘要).replace("参数1", str(self.短标题))
            self.摘要 = str(摘要).replace("参数2", str(self.长标题))
            print('摘要', self.摘要)
            print('标题前栏目字符', self.标题前栏目字符串)

            self.更新集数 = '合集'
            # ===========self.网站副栏目ID============================================================================
            self.模具_电视剧网站副栏目ID()
            # =========(模具)self.正文清洗=====================================================
            self.模具_帖子正文清洗()

            # =========== 提取一楼种子列表==================================================================
            self.模具_提取电视剧一楼种子()

            # =========== 提取各分层页种子列表=================================================================
            self.模具_提取电视剧各分层页种子列表()

            # ===========保存self.帖子内容至数据库==================================================================
            # ===========# 保存已下载网址至数据库=================================================================

            # self.模具_保存电影与合集已下载内容页网址()
            self.模具_保存电影与合集帖子内容至数据库()
            self.模具_保存电影与合集种子存放目录()
            self.过滤帖子网址 = self.过滤帖子网址 + str(self.各帖子链接)
            # print('=倒页数==', 倒页数)




    def 模具_电视剧过滤图片已破与标记其它网站(self):
        列表 = ['tietuku', 'yupoo', 'imgsrc.baidu', '謦灵风软', '风软']
        for 符号 in 列表:
            if 符号 in str(self.帖子内容):
                print(符号, '图片已破or标记其它网站,跳过循环')
                print('=====================')
                self.模具_保存电影与合集过滤帖子网址()
                self.跳过循环 = 0
                return  # 返回 0 值,跳过循环
            else:
                return  # 返回

    def 模具_电视剧过滤标题栏目(self):
        列表 = ['[单集]', '[讨论]', '[Resilio-Sync]']
        for 符号 in 列表:
            if 符号 in str(self.标题前的栏目列表):
                print(符号, '过滤的栏目跳过循环')
                print('=====================')
                self.模具_保存电影与合集过滤帖子网址()
                self.跳过循环 = 0
                return  # 返回 0 值,跳过循环

    def 模具_电视剧中短标题与短标题的清洗(self):
        if '季]' in str(self.帖子标题):

            规则 = '(?<=\]\[).+?(?=季\])'
            帖子标题列表 = re.findall(规则, str(self.帖子标题))
            if len(帖子标题列表) == 0:
                规则 = '(?<=\[).+?(?=季\])'
                帖子标题列表 = re.findall(规则, str(self.帖子标题))

            self.帖子标题 = str(帖子标题列表[0])
            self.帖子标题 = str(self.帖子标题) + '季'
            return  # 返回 空值,

        elif '][全' in str(self.帖子标题):

            规则 = '(?<=\]\[).+?(?=\]\[全)'
            帖子标题列表 = re.findall(规则, str(self.帖子标题))

            if len(帖子标题列表) == 0:
                规则 = '(?<=\[).+?(?=\]\[全)'
                帖子标题列表 = re.findall(规则, str(self.帖子标题))

            self.帖子标题 = str(帖子标题列表[0])

            return  # 返回 空值,
        elif '][更' in str(self.帖子标题):

            规则 = '(?<=\]\[).+?(?=\]\[更)'
            帖子标题列表 = re.findall(规则, str(self.帖子标题))
            if len(帖子标题列表) == 0:
                规则 = '(?<=\[).+?(?=\]\[更)'
                帖子标题列表 = re.findall(规则, str(self.帖子标题))
            self.帖子标题 = str(帖子标题列表[0])
            return  # 返回 空值,

        elif '全][' in str(self.帖子标题):
            规则 = '(?<=\]\[).+?(?=全\]\[)'
            帖子标题列表 = re.findall(规则, str(self.帖子标题))
            if len(帖子标题列表) == 0:
                规则 = '(?<=\[).+?(?=全\]\[)'
                帖子标题列表 = re.findall(规则, str(self.帖子标题))

            self.帖子标题 = str(帖子标题列表[0])
            if '集' in str(self.帖子标题):
                规则 = '.{1,}(?=\]\[)'
                帖子标题列表 = re.findall(规则, str(self.帖子标题))
                if len(帖子标题列表) == 0:
                    return  # 返回 空值,

                self.帖子标题 = str(帖子标题列表[0])
            if '][' in str(self.帖子标题):
                规则 = '(?<=\]\[).{1,}'
                帖子标题列表 = re.findall(规则, str(self.帖子标题))
                if len(帖子标题列表) == 0:
                    return  # 返回 空值,

                self.帖子标题 = str(帖子标题列表[0])
            return  # 返回 空值,
        elif '集]' in str(self.帖子标题):
            规则 = '(?<=\]\[).+?(?=集\])'
            帖子标题列表 = re.findall(规则, str(self.帖子标题))
            if len(帖子标题列表) == 0:
                规则 = '(?<=\[).+?(?=集\])'
                帖子标题列表 = re.findall(规则, str(self.帖子标题))

            self.帖子标题 = str(帖子标题列表[0])
            return  # 返回 空值,
        elif ']' in str(self.帖子标题):
            print('不规整的标题帖子,跳过循环')
            print('=====================')
            self.模具_保存电影与合集过滤帖子网址()
            self.跳过循环 = 0
            return  # 返回 0 值,跳过循环

    def 模具_电视剧过滤图片并且提取标题图一一备用(self):
        标题图集 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]//img/@src')
        # ==========过滤无种子附件,跳过循环================================================
        if 'torrent.gif' not in str(self.帖子内容):
            print('无种子附件,跳过循环')
            print('=====================')
            self.模具_保存电影与合集过滤帖子网址()
            self.跳过循环 = 0
            return  # 返回 0 值,跳过循环
        if len(标题图集) == 0:
            print('无self.标题图,跳过循环')
            print('=====================')
            self.模具_保存电影与合集过滤帖子网址()
            self.跳过循环 = 0
            return  # 返回 0 值,跳过循环
        else:
            self.标题图 = 标题图集[0]
            if 'http' not in str(self.标题图):
                self.标题图 = str(self.标题图).replace("/upload", "http://91btbtt.com/upload")

        if 'HQC' in self.帖子内容:
            if len(标题图集) == 1:
                self.标题图 = 标题图集[0]
                if 'http' not in str(self.标题图):
                    self.标题图 = str(self.标题图).replace("/upload", "http://91btbtt.com/upload")
                    标题图集 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/img/@img')

                return  # 返回 空值,
            else:
                self.标题图 = 标题图集[1]
                if 'http' not in str(self.标题图):
                    self.标题图 = str(self.标题图).replace("/upload", "http://91btbtt.com/upload")

                return  # 返回 空值,

    def 模具_提取电视剧一楼种子(self):
        帖子内容html文本=str(self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[1]/td[1]/text()'))
        if '个附件' in 帖子内容html文本:
            提取一楼种子下载地址列表 = self.帖子内容html.xpath(
                '//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[*]/td[1]/a/@href')
            种子名列表 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[*]/td[1]/a/text()')
            for (一楼种子下载地址, 种子名) in zip(提取一楼种子下载地址列表, 种子名列表):
                # =========== 提self.过滤种子网址# 跳过循环============
                if 一楼种子下载地址 in str(self.过滤种子网址):
                    print('过滤种子网址')
                    print('=====================')
                    continue  # 跳过循环
                # =========(模具)种子名过滤与清洗============
                if '.jpg' in str(种子名):
                    print('跳过下载图片')
                    continue  # 跳过循环
                elif '.png' in str(种子名):
                    print('跳过下载图片')
                    continue  # 跳过循环
                # =========== (模具)种子名清洗=========
                self.种子名 = self.模具_种子名清洗(种子名)


                # =========== (模具)保存过滤已下载种子网址============
                self.模具_保存电影与合集过滤已下载种子网址(一楼种子下载地址)
                # =========== (模具)返回种子内容============
                一楼种子下载地址 = str(一楼种子下载地址).replace("attach", "http://91btbtt.com/attach")
                一楼种子下载地址 = str(一楼种子下载地址).replace("dialog", "download")
                self.模具_打开的网址请求返回网页内容(一楼种子下载地址)

                # =========== 种子目录================
                self.种子目录 = 'F:/电影模板/下载种子目录2/电视剧/剧名/季度/'
                # =========== (模具)种子目录并下载================
                self.模具_种子目录并下载(一楼种子下载地址)


    def 模具_提取电视剧各分层页种子列表(self):
        提取各分层 = self.帖子内容html.xpath('//*[@id="body"]/div/table[*]/tr/td[3]/div')
        层数 = (len(提取各分层))
        for 分层 in range(层数):
            查看附件规则 = ('//*[@id="body"]/div/table[' + str(分层) + ']/tr/td[3]/div/div[2]/table/tr[1]/td[1]/text()')
            分层名目规则 = ('//*[@id="body"]/div/table[' + str(
                分层) + ']/tr/td[3]/div/div/p[1]/text()|//*[@id="body"]/div/table[' + str(
                分层) + ']/tr/td[3]/div/div/p[1]/span/text()')

            分层种子列表规则 = ('//*[@id="body"]/div/table[' + str(分层) + ']/tr/td[3]/div/div[2]/table/tr[*]/td[1]/a/@href')
            分层种子名列表规则 = ('//*[@id="body"]/div/table[' + str(分层) + ']/tr/td[3]/div/div[2]/table/tr[*]/td[1]/a/text()')
            查看附件 = self.帖子内容html.xpath(查看附件规则)
            分层名目 = self.帖子内容html.xpath(分层名目规则)
            分层名目 = ''.join(分层名目)
            if '天天' in str(分层名目):
                continue  # 跳过循环
            if '风软' in str(分层名目):
                continue  # 跳过循环
            if '个附件' in str(查看附件):
                分层种子列表 = self.帖子内容html.xpath(分层种子列表规则)
                分层种子名列表 = self.帖子内容html.xpath(分层种子名列表规则)
                for (下载地址, 种子名) in zip(分层种子列表, 分层种子名列表):

                    # =========== (模具)下载种子网址================
                    self.种子名 = self.模具_种子名清洗(种子名)


                    # =========== (模具)保存过滤已下载种子网址================
                    self.模具_保存电影与合集过滤已下载种子网址(下载地址)
                    # =========== (模具)下载种子网址================
                    下载地址 = str(下载地址).replace("attach", "http://91btbtt.com/attach")
                    下载地址 = str(下载地址).replace("dialog", "download")


                    # =========== 种子目录======F:/电影模板/下载种子目录2/电视剧/剧名/季度/分层名/==========
                    种子目录 = 'F:/电影模板/下载种子目录2/电视剧/剧名/季度/分层名/'
                    分层名目 = self.模具_符号清洗(分层名目)
                    self.种子目录 = str(种子目录).replace("分层名", 分层名目)
                    # =========== (模具)种子目录并下载================
                    self.跳过循环3 = 3
                    self.模具_种子目录并下载(下载地址)

                    if self.跳过循环3 == 0:
                        print('==种子文件已存在,跳过循环=====')

                        continue  # 跳过循环
            else:
                continue  # (跳过当前循环)

    def 模具_电视剧过滤图片并且提取标题图(self):
        if 'torrent.gif' not in str(self.帖子内容) and '个附件' not in str(self.帖子内容):
            print('无种子附件,跳过循环')
            print('=====================')
            self.模具_保存电影与合集过滤帖子网址()
            self.跳过循环 = 0
            return  # 返回 0 值,跳过循环

        标题图集 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/p[*]/img/@src')
        if len(标题图集) == 0:
            if '人人' in str(self.帖子内容):
                标题图集 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/img/@src')
                if len(标题图集) > 0:
                    self.标题图 = 标题图集[0]
                    if 'http' not in str(self.标题图):
                        self.标题图 = str(self.标题图).replace("/upload", "http://91btbtt.com/upload")

                    return  # 返回 空值,
                else:
                    print('无标题图,跳过循环')
                    print('=====================')
                    self.模具_保存电影与合集过滤帖子网址()
                    self.跳过循环 = 0
                    return  # 返回 0 值,跳过循环
            else:
                print('无self.标题图,跳过循环')
                print('=====================')
                self.模具_保存电影与合集过滤帖子网址()
                self.跳过循环 = 0
                return  # 返回 0 值,跳过循环
        if 'HQC' in self.帖子内容:
            if len(标题图集) == 1:
                self.标题图 = 标题图集[0]
                if 'http' not in str(self.标题图):
                    self.标题图 = str(self.标题图).replace("/upload", "http://91btbtt.com/upload")
                    标题图集 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/img/@img')

                return  # 返回 空值,
            else:
                self.标题图 = 标题图集[1]
                if 'http' not in str(self.标题图):
                    self.标题图 = str(self.标题图).replace("/upload", "http://91btbtt.com/upload")

                return  # 返回 空值,
        else:
            self.标题图 = 标题图集[0]
            if 'http' not in str(self.标题图):
                self.标题图 = str(self.标题图).replace("/upload", "http://91btbtt.com/upload")

            return  # 返回 空值,
        # ==========过滤无种子附件,跳过循环================================================


    def 模具_电视剧网站副栏目ID(self):
        # 全部合集时 载入'[连载] '60'':改为全集 '61',
        网站副栏目字典 = {'[连载]': '61', '[]': '', '[美国]': '84', '[英国]': '84', '[大陆]': '85', '[香港]': '86', '[台湾]': '87',
                   '[日本]': '88',
                   '[韩国]': '89',
                   '[法国]': '90', '[多国]': '90', '[印度]': '90', '[西剧]': '90', '[泰国]': '90', '[加剧]': '84', '[意剧]': '90',
                   '[澳剧]': '90', '[德国]': '90',
                   '[新马]': '90', '[剧情]': '91', '[喜剧]': '92', '[爱情]': '93', '[偶像]': '91', '[动作]': '94', '[奇幻]': '95',
                   '[科幻]': '96',
                   '[悬疑]': '97', '[罪案]': '97', '[刑侦]': '97','[灾难]': '97', '[战争]': '98', '[谍战]': '97', '[军旅]': '98', '[历史]': '99',
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
        网站副栏目ID = self.模具_符号清洗(网站副栏目ID)
        网站副栏目ID = 网站副栏目ID.strip()
        if len(网站副栏目ID) == 0:
            网站副栏目ID = '91'
        self.网站副栏目ID = str(网站副栏目ID).replace(" ", ",")
        print('网站副栏目ID', self.网站副栏目ID)

class 类_后台发布(类_公共库):
    def __init__(self):
        self.模具_测试cookies存活()
        self.新旧剧集 = '电影与合集'
        self.模具_调度控制()
        #self.新旧剧集 = '最新影视剧'
        #self.模具_调度控制()

        # print('等待:500秒')
        # time.sleep(500)  # 等待

    def 模具_调度控制(self):
        影视类型列表 = ['电影', '电视剧', '动漫']
        for self.影视类型 in 影视类型列表:
            print('上传类型:', self.影视类型)
            self.模具_读取内容数据库()
            self.模具_数据表反向过滤短标题()

            self.模具_发布文章()
        #self.模具_模具_明天日期更新剧集的全部更新()
        self.模具_更新数据库里剧集发布状态()

    def 模具_打开的网址请求返回网页内容(self, 网址, 文章内容):
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
                返回网页内容 = self.s.post(网址, data=文章内容, headers=头部信息, timeout=3)
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

    def 模具_模具_明天日期更新剧集的全部更新(self):
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







    def 模具_数据表反向过滤短标题(self):
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

    def 模具_更新数据库里剧集发布状态(self):
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

    def 模具_读取内容数据库(self):

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

    def 模具_发布文章(self):
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
            self.模具_打开的网址请求返回网页内容(后台提交网址, 文章内容)

class 类_置顶类型帖子分类(类_公共库):  # 调用 类的模具 self.模具_数据库()
    def __init__(self):
        self.模具_测试cookies存活()
        self.模具_换头部信息()
        self.置顶类型帖子分类()
        self.过滤置顶类型最新影视网址=self.页面提取帖子链接列表文本

        类 = 类_电影下载(self.过滤置顶类型最新影视网址)
        # 类 = 类_电视剧下载(self.过滤置顶类型最新影视网址)
        # 类 = 类_动漫下载(self.过滤置顶类型最新影视网址)


    def 模具_置顶类型帖子分类(self):

        打开的网址 = 'http://91btbtt.com'
        self.模具_打开的网址请求返回网页内容(打开的网址)

        self.帖子内容html = etree.HTML(self.返回网页内容.text)

        # for 帖子位置数 in range(2,6):  # 范围
        for self.帖子位置数 in range(2, 6):
            规则 = "//*[@id=\"threadlist\"]/table[{}]/tbody/tr/td[1]/a[5]/text()".format(
                self.帖子位置数)  # format 代入{}内,不换行 end=""
            规则 = str(规则).replace("/tbody", "")
            置顶各帖子类型文本 = str(self.帖子内容html.xpath(规则))

            self.页面提取帖子链接列表文本 = ""

            if '剧集下载' in 置顶各帖子类型文本 :  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                self.模具_每日更新页面提取每个帖子链接()

            elif '动漫下载' in 置顶各帖子类型文本:  # 其它条件.
                self.模具_每日更新页面提取每个帖子链接()

            else:  # 否则
                continue  # 跳过当前循环,继续进行下一轮循环

    def 模具_每日更新页面提取每个帖子链接(self):
        规则 = "//*[@id=\"threadlist\"]/table[{}]/tbody/tr/td[1]/a[5]/@href".format(
            self.帖子位置数)  # text()format 代入{}内,不换行 end=""
        规则 = str(规则).replace("/tbody", "")
        置顶类型帖子 = self.帖子内容html.xpath(规则)
        self.置顶类型帖子网址 = 'http://91btbtt.com/' + str(置顶类型帖子[0])
        print('置顶类型帖子:', self.置顶类型帖子网址)

        self.模具_打开的网址请求返回网页内容(self.置顶类型帖子网址)
        帖子内容html = etree.HTML(self.返回网页内容.text)

        规则 = "//*[@id=\"body\"]/div/table[2]/tbody/tr[1]/td[3]/div[1]/table[*]//@href"  # text()format 代入{}内,不换行 end=""
        规则 = str(规则).replace("/tbody", "")
        页面提取帖子链接列表 = 帖子内容html.xpath(规则)

        self.页面提取帖子链接列表 = set(页面提取帖子链接列表)  # 转换为集,去重复list()
        self.页面提取帖子链接列表文本 = self.页面提取帖子链接列表文本 + str(self.页面提取帖子链接列表)



'''============类模具控制台======================================'''

循环 = 1
while 循环 == 1:  # 条件循环  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
    开始时间计数 = int(time.time())
    类 = 类_置顶类型帖子分类()
    后台发布=类_后台发布()
    结束时间计数 = int(time.time())
    用时 = 结束时间计数 - 开始时间计数
    取整除分数 = int(用时) // 60
    除的余数的秒数 = int(用时) % 60
    print('用时计数:', 取整除分数, '分:', 除的余数的秒数, '秒')





