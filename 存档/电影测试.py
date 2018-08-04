from lxml import html
import requests
import re
import time
import os
import pymysql
import random
from lxml import etree


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

    def 模具_保存电影与合集总提取帖子链接列表(self,帖子链接):
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

    def 模具_保存电影与合集已下载内容页网址(self):
        db = pymysql.connect("localhost", "root", "", "电影与合集", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句
        sql = """INSERT INTO 已下载内容页网址(已下载内容页网址)
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
        过滤帖子网址 = list(过滤帖子网址)


        #=======SQL 查询语句 self.已下载内容网址======
        sql = "SELECT 帖子链接 FROM 网站文章内容"
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        过滤下载内容网址 = cursor.fetchall()
        for 各帖子链接 in 过滤下载内容网址:
            过滤帖子网址.append(各帖子链接)
        # SQL 查询语句   self.已下载内容网址
        sql = "SELECT 已下载内容页网址 FROM 已下载内容页网址"
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        过滤下载内容网址 = cursor.fetchall()
        for 各帖子链接 in 过滤下载内容网址:
            过滤帖子网址.append(各帖子链接)
        self.过滤帖子网址 = str(过滤帖子网址)


        # SQL 查询语句
        sql = "SELECT 过滤种子网址 FROM 过滤种子网址"
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        过滤种子网址 = cursor.fetchall()
        self.过滤种子网址 = str(过滤种子网址)
        # 关闭数据库连接
        db.close()


    def 模具_提取电影与合集数据库里的已下载内容网址(self):
        # 提取数据库里的过滤网址
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "", "电影与合集", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # SQL 查询语句   self.已下载内容网址
        sql = "SELECT 帖子链接 FROM 网站文章内容"
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        过滤下载内容网址 = cursor.fetchall()
        self.已下载内容网址 = str(过滤下载内容网址)
        # 关闭数据库连接
        db.close()

    def 模具_提取电影与合集数据库里的总提取帖子链接列表(self):
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
        self.总提取帖子链接列表2 = cursor.fetchall()
        # 关闭数据库连接
        db.close()


    def 模具_提取电影与合集数据库里的过滤种子网址(self):
        # 提取数据库里的self.过滤种子网址
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "", "电影与合集", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句
        sql = "SELECT 过滤种子网址 FROM 过滤种子网址"
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        过滤种子网址 = cursor.fetchall()
        # 关闭数据库连接
        db.close()
        self.过滤种子网址 = str(过滤种子网址)

    def 模具_提取电影与合集已更正文章内容网址(self):
        # 提取数据库里的self.过滤种子网址
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "", "电影与合集", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句
        sql = "SELECT 已更正文章内容网址 FROM 已更正文章内容网址"
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        已更正文章内容网址 = cursor.fetchall()
        # 关闭数据库连接
        db.close()
        self.已更正文章内容网址 = str(已更正文章内容网址)

    def 模具_保存电影与合集帖子内容至数据库(self):
        # 打开数据库连接
        self.摘要 = str(self.摘要).replace('\'', '')

        db = pymysql.connect("localhost", "root", "", "电影与合集", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句  (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""" %
        sql = """INSERT INTO 网站文章内容(影视类型,时间ID,长标题,短标题,主栏目ID,副栏目ID,摘要,正文,标题图,主演之标题前栏目字符串,文章来源之更新集数,帖子链接)
                      VALUES ('%s','%d','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" \
              % (self.影视类型, self.时间ID, self.长标题, self.短标题, self.主栏目ID, self.网站副栏目ID, self.摘要, self.正文, self.标题图,self.标题前栏目字符串, self.更新集数, self.各帖子链接)

        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()

        # 关闭数据库连接
        db.close()
        print('帖子内容保存完成')

    # =====================================模具集================================

    def 模具_换头部信息(self):  # 头部信息 def 函数模具内通行变量
        # nonlocal 头部信息  # def 函数模具内通行变量
        global 头部信息  # def 函数模具内通行变量

        # {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'}  被BT网站墙了
        头部信息 = random.choice([{'User-Agent': 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'},
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
        print(头部信息)

    def 模具_打开的网址请求返回网页内容(self, 网址):
        # global 换IP时间计数  # 时间计数全局变量声明

        循环 = 0
        次数循环 = 0

        while 循环 == 0:  # 条件循环  post
            此时数 = int(time.time())
            if 此时数 > self.换IP时间计数 + 60:
                self.换IP时间计数 = int(time.time())
                self.模具_换ip连接()
                self.模具_换头部信息()

            try:
                self.返回网页内容 = requests.post(网址, headers=头部信息, timeout=3)
                time.sleep(1)

            except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout,
                    requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout,
                    requests.exceptions.ChunkedEncodingError,requests.exceptions.InvalidSchema) as 异常:


                次数循环 += 1
                print('网络异常等待', 异常)
                print('倒数15秒再连接', 次数循环, '次')
                time.sleep(12)
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
              '！','|',
              '\\n', '\n', '>', '<', '%']
        for 符号 in 列表:
            原文 = str(原文).replace(符号, '')
        return 原文

    def 模具_正文清洗(self):
        # ===========先去掉相同换行的字符=====================
        正文 = str(self.正文).replace("\'\\n-->\\n\\n\',", "")
        正文 = str(正文).replace("\\n", "")
        # ===========self.正文杂乱字符至行尾的整行处理===============
        正文 = str(正文).replace("\\u3000", "")
        a_规则 = '(?<=◎BT).{10,30}(?=\', \')'
        正文 = re.sub(a_规则, '', str(正文))
        a_规则 = '(?<=上季).{1,}(?=\', \')'
        正文 = re.sub(a_规则, '', str(正文))
        a_规则 = '(?<=迅雷).{1,}(?=\', \')'
        正文 = re.sub(a_规则, '', str(正文))
        a_规则 = '(?<=百度网盘).{1,}(?=\', \')'
        正文 = re.sub(a_规则, '', str(正文))
        a_规则 = '(?<=网盘下载).{1,}(?=\', \')'
        正文 = re.sub(a_规则, '', str(正文))
        a_规则 = '(?<=http://pan.baidu.com).{1,}(?=\', \')'
        正文 = re.sub(a_规则, '', str(正文))
        a_规则 = '(?<=https://pan.baidu.com).{1,}(?=\', \')'
        正文 = re.sub(a_规则, '', str(正文))
        a_规则 = '(?<=ed2k://).{1,}(?=\', \')'
        正文 = re.sub(a_规则, '', str(正文))
        a_规则 = '(?<=https://yunpan.cn).{1,}(?=\', \')'
        正文 = re.sub(a_规则, '', str(正文))
        a_规则 = '(?<=http://yunpan.cn).{1,}(?=\', \')'
        正文 = re.sub(a_规则, '', str(正文))
        a_规则 = '(?<=ftp://).{1,}(?=\', \')'
        正文 = re.sub(a_规则, '', str(正文))
        a_规则 = '(?<=http://www.bt).{1,}(?=\', \')'
        正文 = re.sub(a_规则, '', str(正文))
        a_规则 = '(?<=magnet).{1,}(?=\', \')'
        正文 = re.sub(a_规则, '', str(正文))
        a_规则 = '(?<=磁力).{1,}(?=\', \')'
        正文 = re.sub(a_规则, '', str(正文))
        a_规则 = '(?<=本帖最后由).{10}(?=\', \')'
        正文 = re.sub(a_规则, '', str(正文))
        a_规则 = '(?<=迅雷).{1,}(?=\', \')'
        # ===========替换行尾,进行换行=====================
        正文 = str(正文).replace("\', \'", "\n")
        # ===========self.正文杂乱字符的处理===============
        正文 = str(正文).replace("◎BT", "")
        正文 = str(正文).replace("上季", "")
        正文 = str(正文).replace("迅雷", "")
        正文 = str(正文).replace("百度网盘", "")
        正文 = str(正文).replace("网盘下载", "")
        正文 = str(正文).replace("http://pan.baidu.com", "")
        正文 = str(正文).replace("https://pan.baidu.com", "")
        正文 = str(正文).replace("ed2k://", "")
        正文 = str(正文).replace("https://yunpan.cn", "")
        正文 = str(正文).replace("http://yunpan.cn", "")
        正文 = str(正文).replace("ftp://", "")
        正文 = str(正文).replace("http://www.bt", "")
        正文 = str(正文).replace("magnet", "")
        正文 = str(正文).replace("磁力", "")
        正文 = str(正文).replace("本帖最后由", "")
        正文 = str(正文).replace("\\xa0", "")
        正文 = str(正文).replace(")", "$")
        正文 = str(正文).replace("(", "$")
        正文 = str(正文).replace("\'", '')
        正文 = str(正文).replace("\"", '')
        正文 = str(正文).replace("\\", '')
        正文 = str(正文).replace("\"", '')
        self.正文 = str(正文).replace("ufeff", '')

    def 模具_种子名清洗(self, 种子名):
        种子名规则 = '\[bt.{1,}\]'
        种子名 = re.sub(种子名规则, '', str(种子名))
        种子名规则 = '\.bt.{1,}torrent'
        种子名 = re.sub(种子名规则, '.torrent', str(种子名))
        列表 = ["\'", "\"", ":", "*", "/", "\\", "#", "\"", "?"]

        for 符号 in 列表:
            种子名 = str(种子名).replace(符号, '')
        return 种子名

    def 模具_帖子正文清洗(self):
        # 规则 = '(?<=648542).{1,}(?=BAIDU_CLB_SLOT_ID)'

        一楼内容 = str(self.帖子内容)
        规则 = '(?<=643755).{1,}(?=648546)'
        一楼内容 = re.findall(规则, str(一楼内容), re.S)
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
              "◎BT", "之家整理", "</script>", "\'\";", "<ahrefa>", "a>", "BT之家", "本帖编辑", "<i>i>", "\\u3000", "\\n", "链接"]
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
        self.正文 =self.模具_网站图片网址清洗转换(正文)

    def 模具_提取一楼种子名进行过滤(self):
        if '个附件' in str(self.帖子内容html).xpath(
                '//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[1]/td[1]/text()'):
            一楼种子名列表 = str(self.帖子内容html).xpath(
                '//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[*]/td[1]/a/text()')
            种子名列表文本 = str(一楼种子名列表)
            if ['謦灵风软', 'www.', '.com', '.net'] in 种子名列表文本:
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
            a_规则3 = '(?<=\]\[).{1,}'
            self.短标题 = re.findall(a_规则3, str(self.短标题))
        if '/' in str(self.短标题):
            # a_规则5 = '(?<=/).{1,}'
            # self.短标题4 = re.sub(a_规则4, '', str(self.短标题3))
            a_规则4 = '/{1}'
            self.短标题 = re.sub(a_规则4, '%', str(self.短标题), count=1)
            a_规则 = '.{1,}(?=%)'
            self.短标题 = re.findall(a_规则, str(self.短标题))
        if '.' in str(self.短标题):
            规则 = '(?<=\.).{0,}'
            self.帖子标题 = re.sub(规则, '', str(self.短标题))
            self.短标题 = str(self.帖子标题).replace(".", '')  # 帖子标题修改为'self.短标题
        elif ' ' in str(self.短标题):
            # a_规则4 = '.*(?=)'
            a_规则4 = '\s{1}'
            self.短标题 = re.sub(a_规则4, '%', str(self.短标题), count=1)
            a_规则 = '.{1,}(?=%)'
            self.短标题 = re.findall(a_规则, str(self.短标题))

        if '第' in str(self.短标题):
            if '季' in str(self.短标题):
                a_规则 = '.{1,}(?=第)'
                self.短标题 = re.findall(a_规则, str(self.短标题))

    def 模具_长标题(self):
        self.长标题规则 = '(?<=\]\[).{1,}'
        self.长标题 = re.findall(self.长标题规则, str(self.帖子标题))
        self.长标题 = str(self.长标题).replace("\'", "")
        if '][更' in str(self.长标题):
            a_规则 = '更\d{1,}集'
            self.长标题 = re.sub(a_规则, '', str(self.长标题))
        # 符号清洗
        self.长标题 = self.模具_符号清洗(self.长标题)
        if len(self.长标题) == 0:
            self.长标题 = str(self.短标题)
        print('self.长标题', self.长标题)

    def 模具_种子目录并下载(self, 下载地址):
        # =========== 种子目录================
        # 种子目录 = 'F:/电影模板/下载种子目录2/电视剧/电视剧名/季度/'
        # F:/电影模板/下载种子目录2/动漫/动漫名/季度/
        '#F:/电影模板/下载种子目录2/电视剧/剧名/季度/分层名/'
        返回种子内容 = self.返回网页内容
        if '第' in str(self.中短标题):
            if '季' in str(self.中短标题):
                短标题规则 = '.{1,}(?=第)'
                季度名 = re.sub(短标题规则, '', self.中短标题)
                季度名 = self.模具_符号清洗(季度名)
                种子目录 = str(self.种子目录).replace("剧名", str(self.短标题))
                种子目录 = str(种子目录).replace("季度", 季度名)
            else:
                种子目录 = str(self.种子目录).replace("剧名\季度", str(self.短标题))
        else:
            种子目录 = str(self.种子目录).replace("剧名\季度", str(self.短标题))
        创建种子目录 = str(种子目录).strip('\\')

        if not os.path.exists(创建种子目录):  # 必有条件选择,否则出错
            try:
                os.makedirs(创建种子目录)  # makedirs 创建多级目录文件夹,mkdir创建一个文件夹
            except FileNotFoundError:
                创建种子目录 = str(创建种子目录).replace(' ', '')
                种子目录 = str(种子目录).replace(' ', '')
                创建种子目录 = str(创建种子目录).rstrip()  # 指定删除的字符串末尾的字符(默认为空格)
                创建种子目录 = str(创建种子目录).replace('\\n ', '')
                创建种子目录 = str(创建种子目录).replace('\n ', '')
                os.makedirs(创建种子目录)
            except OSError:
                创建种子目录 = str(创建种子目录).replace('\\n ', '')
                创建种子目录 = str(创建种子目录).replace('\n ', '')
                创建种子目录 = str(创建种子目录).rstrip()  # 指定删除的字符串末尾的字符(默认为空格)
                创建种子目录 = str(创建种子目录).replace(' ', '')
                种子目录 = str(种子目录).replace(' ', '')
                os.makedirs(创建种子目录)
        # =========== 种子下载=====
        目录与种子名 = str(种子目录) + str(self.种子名)
        try:
            with open(目录与种子名, 'wb') as fout:
                fout.write(返回种子内容.content)
                fout.close()

        except (FileNotFoundError, OSError):
            种子名 = str(self.种子名).replace('.', '')
            种子名 = str(种子名).replace(' ', '')
            种子名 = str(种子名).replace('torrent', '.torrent')

            # 种子目录 = str(种子目录).replace(' ', '')
            try:
                目录与种子名 = str(种子目录) + str(种子名)
                with open(目录与种子名, 'wb') as fout:
                    fout.write(返回种子内容.content)
                    fout.close()
            except (FileNotFoundError, OSError):
                print('找不到目录与种子名,出错跳出种子下载循环', 目录与种子名)
                self.过滤种子网址 = self.过滤种子网址 + str(下载地址)
                return  # 返回 空值,

        print('完成下载', 目录与种子名)

        self.过滤种子网址 = self.过滤种子网址 + str(下载地址)
        print('===========================')
    def 模具_网站图片网址清洗转换(self, 图片网址文本):
        列表 = ["http://www.btbtt.co/", "http://btbtt.co/", "http://www.btbtt.net/", "http://www.btbtt.me/", "http://www.btbtt.com/", "http://www.btbtt.pw/",
              "http://btbtt.net/", "http://btbtt.me/", "http://btbtt.com/", "http://btbtt.pw/"]

        for 符号 in 列表:
            图片网址文本 = str(图片网址文本).replace(符号, 'http://91btbtt.com/')
        return 图片网址文本

class 类_电影下载(类_公共库): #调用 类的模具 self.模具_数据库()
    def __init__(self):
        self.模具_下载电影内容()

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
        if '/view/image/filetype/torrent.gif' not in str(self.帖子内容):
            print('无种子附件,跳过循环')
            print('=====================')

            self.模具_保存电影与合集过滤帖子网址()
            self.跳过循环 =0

            return  # 返回 0 值,跳过循环

        if '◎' not in str(self.帖子内容):
            print('无◎,规范的self.帖子内容,跳过循环')
            print('=====================')

            self.模具_保存电影与合集过滤帖子网址()
            self.跳过循环 =0

            return  # 返回 0 值,跳过循环

        if 'HQC' in self.帖子内容:
            if len(标题图集) == 1:
                self.标题图 = 标题图集[0]
                if 'http' not in str(self.标题图):
                    self.标题图 = str(self.标题图).replace("/upload", "http://91btbtt.com/upload")
                    标题图集 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/img/@img')
                return # 返回
            else:
                self.标题图 = 标题图集[1]
                if 'http' not in str(self.标题图):
                    self.标题图 = str(self.标题图).replace("/upload", "http://91btbtt.com/upload")
                return # 返回

        if 'Non' in str(标题图集文本):
            print('无标题图,跳过循环')
            print('=====================')
            self.模具_保存电影与合集过滤帖子网址()
            self.跳过循环 =0
            return  # 返回 0 值,跳过循环
        print('self.标题图1')
        if len(标题图集) == 0:
            print('无self.标题图,跳过循环')
            print('=====================')
            self.模具_保存电影与合集过滤帖子网址()
            self.跳过循环 =0
            return  # 返回 0 值,跳过循环
        else:
            self.标题图 = 标题图集[0]
            print('self.标题图2')
            if 'http' not in str(self.标题图):
                self.标题图 = str(self.标题图).replace("/upload", "http://91btbtt.com/upload")
            print('self.标题图',self.标题图)
            return # 返回

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
            self.帖子标题 =帖子标题

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
        self.短标题= 短标题
        print('self.短标题',self.短标题)


    def 模具_电影长标题符号清洗(self):
        列表 = ["\'", "\"", ":", "*", "/", "#", "\"", "?", ".", "\'", "'", "\'", "'", '', ',', '！', '\\n',
              '\n', '>', '<']
        原文 = str(self.长标题)
        for 符号 in 列表:
            原文 = 原文.replace(符号, '')
        self.长标题=原文

    def 模具_提取电影一楼种子(self):
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
            self.种子名=self.模具_种子名清洗(种子名)

            # =========== (模具)换IP时间计数============

            # =========== (模具)保存过滤已下载种子网址============

            self.模具_保存电影与合集过滤已下载种子网址(一楼种子下载地址)
            # =========== (模具)返回种子内容============
            一楼种子下载地址 = str(一楼种子下载地址).replace("attach", "http://91btbtt.com/attach")
            一楼种子下载地址 = str(一楼种子下载地址).replace("dialog", "download")
            self.模具_打开的网址请求返回网页内容(一楼种子下载地址)

            # =========== 种子目录=====F:/电影模板/下载种子目录2/电影/剧名/季度/===========
            self.种子目录 = 'F:\\电影模板\\下载种子目录2\\电影\\剧名\\季度\\'
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
                    if 下载地址 in str(self.过滤种子网址):
                        print('过滤种子网址')
                        continue  # 跳过循环
                    # =========== (模具)下载种子网址================
                    self.种子名 = self.模具_种子名清洗(种子名)
                    # =========== (模具)换IP时间计数================

                    # =========== (模具)保存过滤已下载种子网址================
                    self.模具_保存电影与合集过滤已下载种子网址(下载地址)
                    # =========== (模具)下载种子网址================
                    下载地址 = str(下载地址).replace("attach", "http://91btbtt.com/attach")
                    下载地址 = str(下载地址).replace("dialog", "download")
                    self.模具_打开的网址请求返回网页内容(下载地址)

                    # =========== 种子目录================
                    种子目录 = 'F:\\电影模板\\下载种子目录2\\电影\\剧名\\季度\\分层名\\'
                    分层名目 = self.模具_符号清洗(分层名目)
                    self.种子目录 = str(种子目录).replace("分层名", 分层名目)
                    # =========== (模具)种子目录并下载================
                    self.模具_种子目录并下载(下载地址)
            else:

                continue  # (跳过当前循环)

    def 模具_电影网站副栏目ID(self):

        网站副栏目字典 = {'[]': '','[纯净版]': '','[欧美]': '25', '[美国]': '25', '[英国]': '25', '[大陆]': '26', '[香港]': '27', '[台湾]': '28', '[日本]': '29',
                   '[韩国]': '30',
                   '[法国]': '31', '[西剧]': '31', '[泰国]': '31', '[加剧]': '31', '[意剧]': '31', '[澳剧]': '31', '[德国]': '31',
                   '[新马]': '31', '[多国]': '31','[剧情]': '34', '[喜剧]': '33', '[爱情]': '34', '[偶像]': '34', '[动作]': '32', '[奇幻]': '37',
                   '[科幻]': '35', '[印度]': '31',
                   '[悬疑]': '40', '[罪案]': '40','[犯罪]': '40', '[刑侦]': '40', '[战争]': '38', '[灾难]': '38','[谍战]': '40', '[军旅]': '38', '[历史]': '39',
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


    def 模具_电影各链接网址处理(self):
        总提取帖子链接列表=[]

        for 倒页数 in range(self.倒页总数, 0, -1):
            页数网址 = 'http://91btbtt.com/forum-index-fid-951-page-2150.htm'
            self.页数网址 = str(页数网址).replace("2150", str(倒页数))
            # ===========self.打开的网址请求self.返回网页内容======================================
            self.模具_打开的网址请求返回网页内容(self.页数网址)
            time.sleep(5)
            帖子列表 = self.返回网页内容
            # ====================================================
            帖子列表html = html.fromstring(帖子列表.text)
            提取帖子链接列表 = 帖子列表html.xpath('//*[@id="threadlist"]/table[*]/tr/td[1]/a[1]/@href')

            for 各帖子链接 in 提取帖子链接列表:
                各帖子链接 = 各帖子链接.replace("thread", "http://91btbtt.com/thread")

                if 各帖子链接 in self.过滤帖子网址:
                    print('过滤帖子网址')
                    continue  # 跳过循环
                self.模具_保存电影与合集总提取帖子链接列表(各帖子链接)
                总提取帖子链接列表.append(各帖子链接)
            print('======倒页数============', 倒页数)
            # ============self.各帖子链接============================================================

        for 各帖子链接 in self.总提取帖子链接列表2:
            各帖子链接 = 各帖子链接[0]
            总提取帖子链接列表.append(各帖子链接)
        print('====================帖子链接总数=================', len(总提取帖子链接列表))

        计数器=0
        for 各帖子链接 in 总提取帖子链接列表:


            倒计数=len(总提取帖子链接列表)-int(计数器)
            print('========倒计数================',倒计数)
            计数器 = 计数器+1

            self.各帖子链接 = str(各帖子链接)

            if self.各帖子链接 in self.过滤帖子网址:
                print('过滤帖子网址')
                continue  # 跳过循环
            print('各帖子链接', self.各帖子链接)

            # ============换IP时间计数===============
            self.跳过循环=1
            # self.模具_换IP时间计数()

            # ============  self.打开的网址请求self.返回网页内容==============================================
            self.模具_打开的网址请求返回网页内容(self.各帖子链接)
            帖子内容 = self.返回网页内容

            # =====================
            self.帖子内容html = etree.HTML(帖子内容.text)
            self.帖子标题列表 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/h2/text()')
            self.标题前的栏目列表 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/h2/a/text()')

            # =========#过滤标题栏目=====================================================
            if len(self.帖子标题列表) > 1:
                self.帖子标题 = self.帖子标题列表[-1]
            elif len(self.帖子标题列表) == 0:
                print('帖子标题列表0# 跳过循环')
                print('==================')
                continue  # 跳过循环
            else:
                self.帖子标题 = self.帖子标题列表[0]
            self.帖子标题 = str(self.帖子标题)


            # ==============

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
                self.短标题 = str(self.时间ID)
            self.短标题 = str(self.帖子标题)
            中短标题 = self.短标题
            print('=self.短标题3=', self.短标题)

            # =================self.短标题的再次清洗=========================================
            self.模具_电影短标题的再次清洗()

            # 符号清洗
            self.短标题 = self.模具_符号清洗(self.短标题)

            if len(self.短标题) == 0:
                self.短标题 = str(self.时间ID)
            self.中短标题 = self.模具_符号清洗(中短标题)
            if len(self.短标题) == 0:
                self.短标题 = str(self.时间ID)
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
            print('标题前栏目字符', self.标题前栏目字符串)

            self.更新集数 = '合集'
            # ===========self.网站副栏目ID============================================================================

            self.模具_电影网站副栏目ID()
            # =========(模具)self.正文清洗=====================================================

            self.模具_帖子正文清洗()

            # ===========保存self.帖子内容至数据库==================================================================

            # =========== 提取一楼种子列表==================================================================
            if '个附件' in str(
                    self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[1]/td[1]/text()')):
                self.模具_提取电影一楼种子()


            # =========== 提取各分层页种子列表=================================================================
            self.模具_提取电影各分层页种子列表()

            # ===========# 保存已下载网址至数据库=================================================================
            self.模具_保存电影与合集帖子内容至数据库()
            #self.模具_保存电影与合集已下载内容页网址()
            self.过滤帖子网址 = self.过滤帖子网址 + str(self.各帖子链接)
            #print('=倒页数==', 倒页数)


    def 模具_下载电影内容(self):
        self.影视类型='电影'
        self.倒页总数 = 0
        self.换IP时间计数 = int(time.time())
        self.模具_换头部信息()
        self.模具_提取电影与合集数据库里的过滤网址一已下载内容网址一过滤种子网址()
        self.模具_提取电影与合集数据库里的总提取帖子链接列表()
        #self.模具_提取电影与合集数据库里的已下载内容网址()
        #self.模具_提取电影与合集数据库里的过滤种子网址()

        self.模具_电影各链接网址处理()

'''============类模具控制台======================================'''
类=类_电影下载()
#类=类_电视剧下载()
#类=类_动漫下载()
# 帖子标题2，先全部搜集再遍历，计数器，图片网址清洗，副ID 多国 []  [纯净版]