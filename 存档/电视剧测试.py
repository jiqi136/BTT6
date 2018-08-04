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
        self.总提取帖子链接列表1 = cursor.fetchall()
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
            if 此时数 > self.换IP时间计数 + 120:
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
              '！','|',
              '\\n', '\n', '>', '<', '%']
        for 符号 in 列表:
            原文 = str(原文).replace(符号, '')
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
        一楼内容 =str(一楼内容列表[0])
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
              "\\n","<script type=\"text/javascript\"","src=\"http://cbjs.baidu.com/js/o.js\">", "链接"]
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
        self.正文 =self.模具_网站图片网址清洗转换(正文)


    def 模具_提取一楼种子名进行过滤(self):
        规则 = '//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[1]/td[1]/text()'
        规则 = str(规则).replace("/tbody", "")
        个附件文本 = self.帖子内容html.xpath(规则)
        if '个附件' in str(个附件文本):
            规则 ='//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[*]/td[1]/a/text()'
            规则 = str(规则).replace("/tbody", "")
            一楼种子名列表文本 = str(self.帖子内容html.xpath(规则))

            过滤列表=['謦灵风软','.风软' , 'www.', '.com', '.net']
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


        if '第' in str(self.短标题):
            if '季' in str(self.短标题):
                规则 = '第.{1,}'
                self.短标题 = re.sub(规则, '', str(self.短标题), count=0)

    def 模具_长标题(self):
        #长标题规则 = '(?<=\]\[).{1,}'
        #print('self.帖子标题1:', self.帖子标题)
        #长标题列表 = re.findall(长标题规则, str(self.帖子标题))
        #print('长标题列表:', 长标题列表)
        #self.长标题=长标题列表[0]
        长标题=self.帖子标题

        if '更' in str(长标题):
            if '集' in str(长标题):
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
        返回种子内容 = self.返回网页内容
        if '第' in str(self.中短标题):
            if '季' in str(self.中短标题):
                短标题规则 = '.{1,}(?=第)'
                季度名 = re.sub(短标题规则, '', self.中短标题)
                季度名 = self.模具_符号清洗(季度名)
                种子目录 = str(self.种子目录).replace("剧名", str(self.短标题))
                种子目录 = str(种子目录).replace("季度", 季度名)
            else:
                种子目录 = str(self.种子目录).replace("剧名/季度", str(self.短标题))
        else:
            种子目录 = str(self.种子目录).replace("剧名/季度", str(self.短标题))
        创建种子目录 = str(种子目录).strip('/')



        for 三次循环创建种子目录 in 'ger':  # 条件循环  post
            try:
                os.makedirs(创建种子目录)  # makedirs 创建多级目录文件夹,mkdir创建一个文件夹
            except (FileNotFoundError,OSError) as 异常:
                if os.path.exists(创建种子目录):  # 必有条件选择,否则出错
                    break  # 结束循环
                print('创建种子目录的异常', 异常)
                创建种子目录 = str(创建种子目录).replace(' ', '')
                创建种子目录 = str(创建种子目录).rstrip()  # 指定删除的字符串末尾的字符（默认为空格）
                种子目录 = str(种子目录).replace(' ', '')
                种子目录= str(种子目录).rstrip()# 指定删除的字符串末尾的字符（默认为空格）
            else:
                break  # 结束循环

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

class 类_电视剧下载(类_公共库): #调用 类的模具 self.模具_数据库()
    def __init__(self):
        self.模具_下载电视剧内容()

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
            帖子标题列表= re.findall(规则, str(self.帖子标题))
            if len(帖子标题列表)==0:
                规则 = '(?<=\[).+?(?=季\])'
                帖子标题列表 = re.findall(规则, str(self.帖子标题))

            self.帖子标题 = str(帖子标题列表[0])
            self.帖子标题 = str(self.帖子标题) + '季'
            return # 返回 空值,

        elif '][全' in str(self.帖子标题):

            规则 = '(?<=\]\[).+?(?=\]\[全)'
            帖子标题列表 = re.findall(规则, str(self.帖子标题))

            if len(帖子标题列表) == 0:
                规则 = '(?<=\[).+?(?=\]\[全)'
                帖子标题列表 = re.findall(规则, str(self.帖子标题))

            self.帖子标题 = str(帖子标题列表[0])


            return # 返回 空值,
        elif '][更' in str(self.帖子标题):

            规则 = '(?<=\]\[).+?(?=\]\[更)'
            帖子标题列表 = re.findall(规则, str(self.帖子标题))
            if len(帖子标题列表) == 0:
                规则 = '(?<=\[).+?(?=\]\[更)'
                帖子标题列表 = re.findall(规则, str(self.帖子标题))
            self.帖子标题 = str(帖子标题列表[0])
            return # 返回 空值,

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
            return # 返回 空值,
        elif '集]' in str(self.帖子标题):
            规则 = '(?<=\]\[).+?(?=集\])'
            帖子标题列表 = re.findall(规则, str(self.帖子标题))
            if len(帖子标题列表) == 0:
                规则 = '(?<=\[).+?(?=集\])'
                帖子标题列表 = re.findall(规则, str(self.帖子标题))

            self.帖子标题 = str(帖子标题列表[0])
            return # 返回 空值,
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

                return# 返回 空值,
            else:
                self.标题图 = 标题图集[1]
                if 'http' not in str(self.标题图):
                    self.标题图 = str(self.标题图).replace("/upload", "http://91btbtt.com/upload")

                return# 返回 空值,


    def 模具_提取电视剧一楼种子(self):
        if '个附件' in str(self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[1]/td[1]/text()')):
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
                self.种子目录 = 'F:/电影模板/下载种子目录2/电视剧/剧名/季度/'
                # =========== (模具)种子目录并下载================
                self.模具_种子目录并下载( 一楼种子下载地址)



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

                    # =========== 种子目录======F:/电影模板/下载种子目录2/电视剧/剧名/季度/分层名/==========
                    种子目录 = 'F:/电影模板/下载种子目录2/电视剧/剧名/季度/分层名/'
                    分层名目 = self.模具_符号清洗(分层名目)
                    self.种子目录 = str(种子目录).replace("分层名", 分层名目)
                    # =========== (模具)种子目录并下载================
                    self.模具_种子目录并下载(下载地址)
            else:
                continue  # (跳过当前循环)


    def 模具_电视剧过滤图片并且提取标题图(self):
        标题图集 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/p[*]/img/@src')
        if len(标题图集) == 0:
            if '人人' in str(self.帖子内容):
                标题图集 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/img/@src')
                if len(标题图集) > 0:
                    self.标题图 = 标题图集[0]
                    if 'http' not in str(self.标题图):
                        self.标题图 = str(self.标题图).replace("/upload", "http://91btbtt.com/upload")

                    return # 返回 空值,
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

                return # 返回 空值,
            else:
                self.标题图 = 标题图集[1]
                if 'http' not in str(self.标题图):
                    self.标题图 = str(self.标题图).replace("/upload", "http://91btbtt.com/upload")

                return # 返回 空值,
        else:
            self.标题图 = 标题图集[0]
            if 'http' not in str(self.标题图):
                self.标题图 = str(self.标题图).replace("/upload", "http://91btbtt.com/upload")

            return # 返回 空值,
        # ==========过滤无种子附件,跳过循环================================================
        if 'torrent.gif' not in str(self.帖子内容):
            print('无种子附件,跳过循环')
            print('=====================')
            self.模具_保存电影与合集过滤帖子网址()
            self.跳过循环 = 0
            return  # 返回 0 值,跳过循环

    def 模具_电视剧网站副栏目ID(self):
        # 全部合集时 载入'[连载] '60'':改为全集 '61',
        网站副栏目字典 = {'[连载]': '61', '[]': '',  '[美国]': '84' ,'[英国]': '84', '[大陆]': '85', '[香港]': '86', '[台湾]': '87', '[日本]': '88',
                   '[韩国]': '89',
                   '[法国]': '90', '[多国]': '90', '[印度]': '90', '[西剧]': '90', '[泰国]': '90', '[加剧]': '84', '[意剧]': '90',
                   '[澳剧]': '90', '[德国]': '90',
                   '[新马]': '90', '[剧情]': '91', '[喜剧]': '92', '[爱情]': '93', '[偶像]': '91', '[动作]': '94', '[奇幻]': '95',
                   '[科幻]': '96',
                   '[悬疑]': '97', '[罪案]': '97', '[刑侦]': '97', '[战争]': '98', '[谍战]': '97', '[军旅]': '98', '[历史]': '99',
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
        print('网站副栏目ID',self.网站副栏目ID)

    def 模具_电视剧各链接网址处理(self):
        总提取帖子链接列表 = []

        for 倒页数 in range(self.倒页总数, 0, -1):
            页数网址 = 'http://91btbtt.com/forum-index-fid-950-page-312.htm'
            self.页数网址 = str(页数网址).replace("312", str(倒页数))
            # ===========self.打开的网址请求self.返回网页内容======================================
            self.模具_打开的网址请求返回网页内容(self.页数网址)

            帖子列表 = self.返回网页内容
            # ====================================================
            帖子列表html = html.fromstring(帖子列表.text)
            提取帖子链接列表 = 帖子列表html.xpath('//*[@id="threadlist"]/table[*]/tr/td[1]/a[1]/@href')

            for 各帖子链接 in 提取帖子链接列表:
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
        print('===========帖子链接总数============', len(总提取帖子链接列表))

        计数器 = 0
       
        for 各帖子链接 in 总提取帖子链接列表:
            倒计数=len(总提取帖子链接列表)-int(计数器)
            print('========倒计数================',倒计数)
            计数器 = 计数器+1

            各帖子链接 = str(各帖子链接)
            self.各帖子链接 = 各帖子链接.replace("thread", "http://91btbtt.com/thread")
            if self.各帖子链接 in self.过滤帖子网址:
                print('过滤帖子网址')
                continue  # 跳过循环
            print('各帖子链接', self.各帖子链接)
            # ============换IP时间计数===============
            # self.模具_换IP时间计数()

            # ============  self.打开的网址请求self.返回网页内容==============================================
            self.模具_打开的网址请求返回网页内容(self.各帖子链接)
            帖子内容 = self.返回网页内容

            # =====================
            self.帖子内容html = etree.HTML(帖子内容.text)
            self.帖子标题列表 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/h2/text()')
            self.标题前的栏目列表 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/h2/a/text()')

            # =========#过滤标题栏目=====================================================
            self.跳过循环 =1  # 设定初始值
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

            # ======中短标题与self.短标题的清洗==============================================================================================================================================
            帖子标题 = self.帖子标题列表[-1]
            self.帖子标题 = str(帖子标题)

            # ==========================================================

            self.模具_电视剧中短标题与短标题的清洗()
            if self.跳过循环 == 0:
                continue  # 跳过循环
           
            self.短标题 = self.帖子标题

            self.时间ID = int(time.strftime("%y%m%d%H%M%S", time.localtime()))
            if len(self.短标题) == 0:
                self.短标题 = str(self.时间ID)
            中短标题 =self.短标题
            # =================self.短标题的再次清洗=========================================
            self.模具_短标题的再次清洗()

            # 符号清洗
            self.短标题 = self.模具_符号清洗(self.短标题)
            self.中短标题 = self.模具_符号清洗(中短标题)
            if len(self.短标题) == 0:
                self.短标题 = str(self.时间ID)
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

            #self.模具_保存电影与合集已下载内容页网址()
            self.模具_保存电影与合集帖子内容至数据库()
            self.过滤帖子网址 = self.过滤帖子网址 + str(self.各帖子链接)
            #print('=倒页数==', 倒页数)


    def 模具_下载电视剧内容(self):
        self.影视类型 = '电视剧'
        self.倒页总数 =0
        self.换IP时间计数 = int(time.time())
        self.模具_换头部信息()
        self.模具_提取电影与合集数据库里的过滤网址一已下载内容网址一过滤种子网址()
        self.模具_提取电影与合集数据库里的总提取帖子链接列表()
        # self.模具_提取电影与合集数据库里的已下载内容网址()
        # self.模具_提取电影与合集数据库里的过滤种子网址()
    
        self.模具_电视剧各链接网址处理()

'''============类模具控制台======================================'''
#类=类_电影下载()
类=类_电视剧下载()
#类=类_动漫下载()
# 帖子标题2,先全部搜集再遍历,计数器,图片网址清洗,副ID 多国 []
#新的合集，风是 连载 全 略过