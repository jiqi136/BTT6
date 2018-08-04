from lxml import html
import requests
import re
import time
import os
import pymysql
import random
from lxml import etree
import shutil


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

    def 模具_更正数据库空标题(self):
        # 打开数据库连接
        self.摘要 = str(self.摘要).replace('\'', '')

        db = pymysql.connect("localhost", "root", "", "电影与合集", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句  (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""" %
        sql = """UPDATE `网站文章内容` SET `长标题`=('%s'),`短标题`=('%s'),`摘要`=('%s') WHERE `帖子链接`=('%s')""" \
              % (self.长标题, self.短标题, self.摘要,self.各帖子链接)
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()

        # 关闭数据库连接
        db.close()
        print('帖子内容保存完成')

    def 模具_删除数据库空标题的跳过(self):
        db = pymysql.connect("localhost", "root", "", "电影与合集", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句  (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""" %
        sql = """DELETE FROM `网站文章内容` WHERE `帖子链接`=('%s')""" \
              % ( self.各帖子链接)
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()

        # 关闭数据库连接
        db.close()
        print('帖子删除完成')



    # =====================================模具集================================

    def 模具_换头部信息(self):  # 头部信息 def 函数模具内通行变量
        # nonlocal 头部信息  # def 函数模具内通行变量
        global 头部信息  # def 函数模具内通行变量

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
                              {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 随机1位数.0; Windows NT 随机11位数.1; Maxthon 2.0)'},
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
            if 此时数 > self.换IP时间计数 + 120:
                self.换IP时间计数 = int(time.time())
                self.模具_换ip连接()
                self.模具_换头部信息()

            try:
                此时数2 = int(time.time())
                if 缓冲时间 > 此时数2:
                    time.sleep(1)
                self.返回网页内容 = requests.post(网址, headers=头部信息, timeout=3)

                缓冲时间 = int(time.time()) + 1

            except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout,
                    requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout,
                    requests.exceptions.ChunkedEncodingError, requests.exceptions.InvalidSchema) as 异常:

                次数循环 += 1
                print('网络异常等待', 异常)
                print('倒数6秒再连接', 次数循环, '次')
                time.sleep(3)
                if 'None, 10053,' in str(异常):
                    self.模具_换头部信息()
            else:
                if '200' in str(self.返回网页内容):
                    self.返回网页内容.encoding = "UTF-8"  # 转换encoding='UTF-8' "gbk"
                    return  # 返回
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
        列表 = ["[", "]", "\'", "\"", ":", "*", "/", "\\", "#", "\"", "?", ".", "\'", "'", "\'", "'", '', ',', ':', ':',
              '！', '|',
              '\\n', '\n', '>', '<', '%']
        for 符号 in 列表:
            原文 = str(原文).replace(符号, '')
        原文 = 原文.strip() # 默认则是去除空格
        return 原文

    def 模具_种子名清洗(self, 种子名):
        种子名规则 = '\[bt.{1,}\]'
        种子名 = re.sub(种子名规则, '', str(种子名))
        种子名规则 = '\.bt.{1,}torrent'
        种子名 = re.sub(种子名规则, '.torrent', str(种子名))
        列表 = ["\'", "\"", ":", "*", "/", "\\", "#", "\""
            , "www.517ww.com", "www.117hm.com", "www.15bx.com", "www.hanmi520.com", "www.hanmi.cc", "?"]

        for 符号 in 列表:
            种子名 = str(种子名).replace(符号, '')
        return 种子名

    def 模具_帖子正文清洗(self):
        # 规则 = '(?<=648542).{1,}(?=BAIDU_CLB_SLOT_ID)'

        一楼内容 = str(self.帖子内容)
        规则 = '(?<=643755).{1,}(?=648546)'
        一楼内容列表 = re.findall(规则, str(一楼内容), re.S)
        一楼内容 = str(一楼内容列表[0])
        规则列表 = ['(?<=◎BT).{1,300}(?=a>)', '(?<=上季).{1,}(?=</p>)', '(?<=<a href).{1,}(?=a>)',
                '(?<=</script>).{1,}(?=</script>)', '(?<=迅雷).{1,}(?=</p>)', '(?<=百度网盘).{1,}(?=</p>)',
                '(?<=百度网盘).{1,}(?=</p>)',
                '(?<=网盘下载).{1,}(?=</p>)', '(?<=http://pan.baidu.com).{1,}(?=</p>)',
                '(?<=https://pan.baidu.com).{1,}(?=</p>)',
                '(?<=ed2k://).{1,}(?=</p>)', '(?<=https://yunpan.cn).{1,}(?=</p>)',
                '(?<=http://yunpan.cn).{1,}(?=</p>)',
                '(?<=ftp://).{1,}(?=</p>)',
                '(?<=本帖).{1,50}(?=编辑)', '(?<=<i>).{1,}(?=i>)', '(?<=magnet).{1,}(?=</p>)',
                '(?<=磁力).{1,}(?=</p>)', '(?<=本帖最后由).{10}(?=</p>)', '(?<=迅雷).{1,}(?=</p>)', '(?<=链接).{1,300}(?=</p>)']
        for 规则 in 规则列表:
            一楼内容 = re.sub(规则, '', str(一楼内容))

        # ========字符替换=========
        列表 = ["迅雷", "百度网盘", "网盘下载", "http://pan.baidu.com", "https://pan.baidu.com", "ed2k://", "https://yunpan.cn",
              "http://yunpan.cn", "ftp://", "本帖最后由", "上季", "<scripttype=\"text/javascript\">BAIDU_CLB_SLOT_ID=\"",
              "<script type=\"text/javascript\">BAIDU_CLB_SLOT_ID = ",
              "◎BT", "之家整理", "</script>", "\'\";", "<ahrefa>", "a>", "BT之家", "本帖编辑", "<i>i>", "\\u3000",
              "\\n", "<script type=\"text/javascript\"", "src=\"http://cbjs.baidu.com/js/o.js\">", "链接"]
        for 符号 in 列表:
            一楼内容 = str(一楼内容).replace(符号, '')

        一楼内容 = str(一楼内容).strip('\'')
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
    def 模具_置顶类型帖子分类(self):
        self.换IP时间计数 = int(time.time())
        self.模具_换头部信息()

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

            if '剧集下载' in 置顶各帖子类型文本:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                self.模具_每日更新页面提取每个帖子链接()

            elif '动漫下载' in 置顶各帖子类型文本:  # 其它条件.
                self.模具_每日更新页面提取每个帖子链接()

            else:  # 否则
                continue  # 跳过当前循环,继续进行下一轮循环
        '''============类模具控制台======================================'''

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

    def 模具_模具_每日更新页面提取每个帖子链接(self):
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
        self.页面提取帖子链接列表文本=self.页面提取帖子链接列表文本+str(self.页面提取帖子链接列表)

    def 模具_帖子标题列表清洗(self):
        print('帖子标题列表', self.帖子标题列表)
        if len(self.帖子标题列表) == 0:

            self.跳过循环 = 0
            return#返回

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


class 类_电影下载(类_公共库):  # 调用 类的模具 self.模具_数据库()
    def __init__(self,类型短标题链接组):
        类型短标题链接组 = 类型短标题链接组
        self.换IP时间计数 = int(time.time())

        self.影视类型 = 类型短标题链接组[0]
        self.数据库短标题 = 类型短标题链接组[1]
        self.帖子链接 = 类型短标题链接组[2]
        print('影视类型:', self.影视类型)
        print('数据库数字短标题:', self.数据库短标题)
        print('帖子链接:', self.帖子链接)
        self.模具_电影各链接网址处理()

    def 模具_电影各链接网址处理(self):
        for e in 'f':

            self.各帖子链接 = self.帖子链接


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
            if self.跳过循环 == 0:
                print('# 跳过循环.短标题:', self.各帖子链接)
                self.模具_删除数据库空标题的跳过()
                continue  # 跳过循环
            if len(self.帖子标题)==0:
                print('self.帖子标题为空# 跳过循环.短标题:', self.各帖子链接)
                self.模具_删除数据库空标题的跳过()
                continue  # 跳过循环
            self.原版短标题 = self.模具_符号清洗(self.帖子标题)


            # =========#过滤标题栏目=====================================================
            self.模具_电影过滤标题栏目()
            if self.跳过循环 == 0:
                print('# 跳过循环.短标题:', self.各帖子链接)
                self.模具_删除数据库空标题的跳过()
                continue  # 跳过循环

            # ===============过滤图片并且提取self.标题图与self.正文图集==========================================

            self.帖子内容 = (帖子内容.text)
            self.模具_电影过滤图片并且提取标题图()

            if self.跳过循环 == 0:
                print('# 跳过循环.短标题:', self.各帖子链接)
                self.模具_删除数据库空标题的跳过()
                continue  # 跳过循环
            self.标题图 = self.模具_网站图片网址清洗转换(self.标题图)
            # ========过滤图片已破与标记其它网站,跳过循环=================================================================

            self.模具_电影过滤图片已破与标记其它网站()

            if self.跳过循环 == 0:
                print('# 跳过循环.短标题:', self.各帖子链接)
                self.模具_删除数据库空标题的跳过()
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
                print('# 跳过循环.短标题:', self.各帖子链接)
                self.模具_删除数据库空标题的跳过()
                continue  # 跳过循环
            self.短标题 = str(self.帖子标题)
            # ==================================

            self.时间ID = int(time.strftime("%y%m%d%H%M%S", time.localtime()))
            if len(self.短标题) == 0:
                self.短标题 = self.原版短标题
            self.短标题 = str(self.帖子标题)
            中短标题 = self.短标题


            # =================self.短标题的再次清洗=========================================
            self.模具_电影短标题的再次清洗()

            # 符号清洗
            self.短标题 = self.模具_符号清洗(self.短标题)

            if len(self.短标题) == 0:
                self.短标题 = self.原版短标题
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

            摘要 = '<h2>资源下载:<a href="/uploads/html/dying/参数1.html"target="_blank">参数2.torrent</a></h2>'


            摘要 = str(摘要).replace("参数1", str(self.短标题))
            self.摘要 = str(摘要).replace("参数2", str(self.长标题))
            print('摘要', self.摘要)

            # ====================重命名文件夹==================
            文件夹 = 'F:/电影模板/下载种子目录3/电影/酒鬼妹子'
            数字文件夹 = str(文件夹).replace("酒鬼妹子", self.数据库短标题)  # 替换   , 1) 次数 1
            修改后文件夹 = str(文件夹).replace("酒鬼妹子", self.短标题)  # 替换   , 1) 次数 1

            if os.path.exists(数字文件夹):  # 探测文件夹的存在
                try:  # 调用异常处理,应对易发生错误的位置
                    shutil.move(数字文件夹, 修改后文件夹)
                except (thr, htr)as 异常原因:  # 异常处理
                    print(异常原因)
                else:  # 必须放在所有的except子句之后.这个子句将在try子句没有发生任何异常的时候执行.
                    print(数字文件夹, '成功修改为:', 修改后文件夹)
            else:  # 否则
                print(数字文件夹, '数字文件夹不存在:')

            self.模具_更正数据库空标题()



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

                # =========== (模具)换IP时间计数============

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
                    # =========== (模具)换IP时间计数================

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
    def __init__(self,类型短标题链接组):
        类型短标题链接组= 类型短标题链接组

        self.影视类型 = 类型短标题链接组[0]
        self.数据库短标题 = 类型短标题链接组[1]
        self.帖子链接 = 类型短标题链接组[2]
        print('影视类型:', self.影视类型)
        print('短标题:', self.数据库短标题)
        print('帖子链接:', self.帖子链接)
        self.模具_动漫各链接网址处理()



    def 模具_动漫各链接网址处理(self):
        for e in 'f':
            self.各帖子链接 =self.帖子链接

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
                print('# 跳过循环.短标题:', self.各帖子链接)
                continue  # 跳过循环
            # ===============过滤图片并且提取self.标题图与self.正文图集==========================================

            self.帖子内容 = (帖子内容.text)
            self.模具_动漫过滤图片并且提取标题图()
            if self.跳过循环 == 0:
                print('# 跳过循环.短标题:',self.各帖子链接)
                continue  # 跳过循环
            self.标题图 = self.模具_网站图片网址清洗转换(self.标题图)
            # ========过滤图片已破与标记其它网站,跳过循环=================================================================

            self.模具_动漫过滤图片已破与标记其它网站()
            if self.跳过循环 == 0:
                print('# 跳过循环.短标题:', self.各帖子链接)
                continue  # 跳过循环
            # ========提取一楼种子名进行过滤=============================================================

            self.模具_提取一楼种子名进行过滤()
            if self.跳过循环 == 0:
                print('# 跳过循环.短标题:', self.各帖子链接)
                continue  # 跳过循环

            # ===========帖子标题列表清洗===========================================
            self.模具_帖子标题列表清洗()
            self.原版短标题=self.模具_符号清洗(self.帖子标题)
            # ======中短标题与self.短标题的清洗==============================================================================================================================================

            self.模具_动漫中短标题与短标题的清洗()
            if self.跳过循环 == 0:
                print('# 跳过循环.短标题:', self.各帖子链接)
                continue  # 跳过循环

            self.短标题 = self.帖子标题

            self.时间ID = int(time.strftime("%y%m%d%H%M%S", time.localtime()))
            if len(self.短标题) == 0:
                self.短标题 = self.原版短标题
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


            # ====================重命名文件夹==================
            文件夹='F:/电影模板/下载种子目录4/动漫/酒鬼妹子'
            数字文件夹 = str(文件夹).replace("酒鬼妹子", self.数据库短标题) #替换   , 1) 次数 1
            修改后文件夹 = str(文件夹).replace("酒鬼妹子", self.短标题 )  # 替换   , 1) 次数 1

            if os.path.exists(数字文件夹):  # 探测文件夹的存在
                try:  #调用异常处理,应对易发生错误的位置
                    shutil.move(数字文件夹,修改后文件夹)
                except (thr,htr)as 异常原因 :#异常处理
                    print(异常原因 )
                else:#必须放在所有的except子句之后.这个子句将在try子句没有发生任何异常的时候执行.
                    print(数字文件夹,'成功修改为:',修改后文件夹)
            else:# 否则
                print(数字文件夹, '数字文件夹不存在:')

            # ====================重命名压缩下载种子===============
            压缩下载种子文件夹 = 'F:/电影模板/压缩-下载种子/动漫/酒鬼妹子'
            压缩下载种子数字文件夹 = str(压缩下载种子文件夹).replace("酒鬼妹子", self.数据库短标题)  # 替换   , 1) 次数 1
            压缩下载种子修改后文件夹 = str(压缩下载种子文件夹).replace("酒鬼妹子", self.短标题)  # 替换   , 1) 次数 1

            if os.path.exists(压缩下载种子数字文件夹):  # 探测文件夹的存在
                try:  # 调用异常处理,应对易发生错误的位置
                    shutil.move(压缩下载种子数字文件夹, 压缩下载种子修改后文件夹)
                except (thr, htr)as 异常原因:  # 异常处理
                    print(异常原因)
                else:  # 必须放在所有的except子句之后.这个子句将在try子句没有发生任何异常的时候执行.
                    print(压缩下载种子数字文件夹, '成功修改为:', 压缩下载种子修改后文件夹)
            else:  # 否则
                print(压缩下载种子数字文件夹, '压缩下载种子数字文件夹不存在:')

            self.模具_更正数据库空标题()


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

                # =========== (模具)换IP时间计数============

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
                    # =========== (模具)换IP时间计数================

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






class 类_提取数据库的空标题链接(类_公共库): #调用 类的模具 self.模具_数据库()
    def __init__(self):

        self.模具_换头部信息()

        self.模具一一提取数据库的空标题链接()
        self.模具一一分解空标题链接()

    def 模具一一提取数据库的空标题链接(self):
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "", "电影与合集", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # SQL 查询语句   self.已下载内容网址
        sql = "SELECT `影视类型`, `短标题`,`帖子链接` FROM `网站文章内容` WHERE `短标题` LIKE '%180%%' "
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        self.总提取空标题链接列表 = cursor.fetchall()
        # 关闭数据库连接
        db.close()

    def 模具一一分解空标题链接(self):
        print('总提取空标题链接列表总数',len(self.总提取空标题链接列表))
        for 类型短标题链接组 in self.总提取空标题链接列表:

            if '电影' in str(类型短标题链接组[0]):  # 其它条件.
                类 = 类_电影下载(类型短标题链接组)
                    



            
'''============类模具控制台======================================'''


类 =类_提取数据库的空标题链接()
#类 = 类_电影下载()
#类 = 类_电视剧下载()
#类 = 类_动漫下载()

