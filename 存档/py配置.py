import sqlite3

def 换ip连接():

    # coding:gbk
    print('宽带连接进行时.....')

    import os
    import time


    os.system(r"rasphone -h 宽带连接")  # xxx0是你的拨号名称，xp下默认是“宽带连接”。
    os.system(r"rasdial 宽带连接 02007044432@163.gd  77341859")  # xxx0同上，xxx1 拨号用户名 ，xxx2拨号密码。
    time.sleep(1)


def 换ip():
    def 换ip连接():

        # coding:gbk
        print('宽带连接进行时.....')

        import os
        import time

        os.system(r"rasphone -h 宽带连接")  # xxx0是你的拨号名称，xp下默认是“宽带连接”。
        os.system(r"rasdial 宽带连接 02007044432@163.gd  77341859")  # xxx0同上，xxx1 拨号用户名 ，xxx2拨号密码。
        time.sleep(1)
    import requests
    import time
    换ip连接()

    ua = 'gt'
    try:
        ua =换头部信息(ua)
        a = requests.get('http://www.btbtt.net', headers=ua, timeout=10)
    except requests.exceptions.ConnectTimeout:
        print('网络异常等待60秒')
        time.sleep(60)

        转备用换ip()

    except requests.exceptions.ReadTimeout:
        print('网络异常等待60秒')
        time.sleep(60)

        转备用换ip()

    except requests.exceptions.ConnectionError:
        print('网络异常等待60秒')
        time.sleep(60)

        转备用换ip()
    except requests.exceptions.ConnectTimeout:
        print('网络异常等待60秒')
        time.sleep(60)

        转备用换ip()

    print('换ip再连接完成')

def 获取某一天是星期几():
    import time
    import re

    import datetime

    发贴时间='2017-12-05'
    发贴时间列表 = 发贴时间.split("-")
    年=int(发贴时间列表[0])
    月=int(发贴时间列表[1])
    日=int(发贴时间列表[2])
    #a=(datetime.strptime(发贴时间, "%w")
    print (发贴时间列表)

    today=int(time.strftime("%w"))
    anyday=datetime.datetime(年,月,日).strftime("%w")

    print (anyday)

def 转备用换ip():
    import requests
    import time
    换ip连接()
    ua='gt'

    try:
        ua =换头部信息(ua)
        a = requests.post('http://www.btbtt.net', headers=ua, timeout=10)


    except requests.exceptions.ConnectTimeout:
        print('网络异常等待60秒')
        time.sleep(60)
        换ip()

    except requests.exceptions.ReadTimeout:


        print('网络异常等待60秒')
        time.sleep(60)

        换ip()

    except requests.exceptions.ConnectionError:
        print('网络异常等待60秒')
        time.sleep(60)
        换ip()
    except requests.exceptions.ConnectTimeout:
        print('网络异常等待60秒')
        time.sleep(60)

        换ip()


def 移除字符串头尾指定的字符(默认为空格):
    str = "87, 15, 49,"
    print (str.strip( ',' ))
def 批量字符串的字典映射替换():
    a = 'abc'

    dict = {'abc': 456}
    dict['School'] = "菜鸟教程" # 添加信息
    if a in dict:
        a = dict[a]
    print(a)

def 按照字符进行划分读取内容文件:
    f = open(r'test.txt', 'r')  # 打开所保存的cookies内容文件
    cookies = {}  # 初始化cookies字典变量
    for line in f.read().split(';'):  # 按照字符：进行划分读取
        # 其设置为1就会把字符串拆分成2份
        name, value = line.strip().split('=', 1)
        cookies[name] = value  # 为字典cookies添加内容


def 换IP时间计数():
    import time
    换IP时间计数 = int(time.time())

    time.sleep(5)

    换IP时间计数b = int(time.time())
    if (换IP时间计数 + 60) > 换IP时间计数b:
        print('ok')

    else:
        print('on')


def 模具_符号清洗(原文):
    列表 = ["[", "]", "\'", "\"", ":", "*", "/", "\\", "#", "\"", "?", ".", "\'", "'", "\'", "'", '', '，', '！', '\\n',
          '\n', '>', '<']
    for 符号 in 列表:
        if 符号 in 原文:
            原文 = str(原文).replace(符号, '')

    原文 = str(原文).replace("[", '')
    原文 = str(原文).replace("]", '')
    原文 = str(原文).replace("\'", '')
    原文 = str(原文).replace("\"", '')
    原文 = str(原文).replace(":", '')
    原文 = str(原文).replace("*", '')
    原文 = str(原文).replace("/", '')
    原文 = str(原文).replace("\\", '')
    原文 = str(原文).replace("#", '')
    原文 = str(原文).replace("\"", '')
    原文 = str(原文).replace("?", '')
    原文 = str(原文).replace(".", '')
    原文 = str(原文).replace("\'", '')
    原文 = str(原文).replace("'", '')
    原文 = str(原文).replace("\'", '')
    原文 = str(原文).replace("'", '')
    原文 = str(原文).replace(' ', '')
    原文 = str(原文).replace('，', '')
    原文 = str(原文).replace('！', '')
    原文 = str(原文).replace('\\n', '')
    原文 = str(原文).replace('\n', '')
    原文 = str(原文).replace('>', '')
    原文 = str(原文).replace('<', '')
    return 原文


def 换头部信息(ua):
    import random

    ua='er'



    头部信息=random.choice([ {'User-Agent':'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'},
    {'User-Agent':'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},
    {'User-Agent':'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.9Safari/536.5'},
    {'User-Agent':'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.9Safari/536.5'},
    {'User-Agent':'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/535.24(KHTML,likeGecko)Chrome/19.0.1055.1Safari/535.24'},
    {'User-Agent':'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/535.24(KHTML,likeGecko)Chrome/19.0.1055.1Safari/535.24'},
    {'User-Agent':'Mozilla/5.0(X11;CrOSi6862268.111.0)AppleWebKit/536.11(KHTML,likeGecko)Chrome/20.0.1132.57Safari/536.11'},
    {'User-Agent':'Mozilla/5.0(X11;CrOSi6862268.111.0)AppleWebKit/536.11(KHTML,likeGecko)Chrome/20.0.1132.57Safari/536.11'},
    {'User-Agent':'Mozilla/5.0(WindowsNT6.2;WOW64)AppleWebKit/537.1(KHTML,likeGecko)Chrome/19.77.34.5Safari/537.1'},
    {'User-Agent':'Mozilla/5.0(WindowsNT6.2;WOW64)AppleWebKit/537.1(KHTML,likeGecko)Chrome/19.77.34.5Safari/537.1'},
    {'User-Agent':'Mozilla/5.0(WindowsNT6.2;WOW64)AppleWebKit/535.24(KHTML,likeGecko)Chrome/19.0.1055.1Safari/535.24'},
    {'User-Agent':'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.6(KHTML,likeGecko)Chrome/20.0.1090.0Safari/536.6'},
    {'User-Agent':'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.6(KHTML,likeGecko)Chrome/20.0.1090.0Safari/536.6'},
    {'User-Agent':'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1062.0Safari/536.3'},
    {'User-Agent':'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1062.0Safari/536.3'},
    {'User-Agent':'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3'},
    {'User-Agent':'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3'},
    {'User-Agent':'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.0Safari/536.3'},
    {'User-Agent':'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.0Safari/536.3'},
    {'User-Agent':'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.1(KHTML,likeGecko)Chrome/22.0.1207.1Safari/537.1'},
    {'User-Agent':'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.1(KHTML,likeGecko)Chrome/22.0.1207.1Safari/537.1'},
    {'User-Agent':'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.6(KHTML,likeGecko)Chrome/20.0.1092.0Safari/536.6'},
    {'User-Agent':'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.6(KHTML,likeGecko)Chrome/20.0.1092.0Safari/536.6'},
    {'User-Agent':'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1063.0Safari/536.3'},
    {'User-Agent':'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1063.0Safari/536.3'},
    {'User-Agent':'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1062.0Safari/536.3'},
    {'User-Agent':'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1062.0Safari/536.3'},
    {'User-Agent':'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3'},
    {'User-Agent':'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3'},
    {'User-Agent':'Mozilla/5.0(WindowsNT6.1)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3'},
    {'User-Agent':'Mozilla/5.0(WindowsNT6.1)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3'},
    {'User-Agent':'Mozilla/5.0(WindowsNT6.0)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.36Safari/536.5'},
    {'User-Agent':'Mozilla/5.0(WindowsNT6.0)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.36Safari/536.5'},
    {'User-Agent':'Mozilla/5.0(WindowsNT5.1)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1063.0Safari/536.3'},
    {'User-Agent':'Mozilla/5.0(Macintosh;IntelMacOSX10_8_0)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1063.0Safari/536.3'},
    {'User-Agent':'Mozilla/5.0(Macintosh;IntelMacOSX10_8_0)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1063.0Safari/536.3'},
    {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'},
    {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
    {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'},
    {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'},
    {'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'},
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
    {'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)'},
    {'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)'},
    {'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)'},
    {'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)'},
    {'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)'},
    {'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'},
    {'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'},
    {'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'}])



    return 头部信息


def 存入数据库():
    # !/usr/bin/python3

    import pymysql

    # 打开数据库连接
    db = pymysql.connect("localhost", "s2", "", "影视剧",charset="utf8")
    print("已连接 " )

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT VERSION()")

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()

    print("Database version : %s " % data)

    # 关闭数据库连接
    db.close()

def 创建表SQLsqlite():
    # !/usr/bin/python

    import sqlite3

    conn = sqlite3.connect('影视剧.db')
    print ("已连接数据库")
    c = conn.cursor()

    c.execute('''CREATE TABLE 电视剧
           (主栏目ID TEXT  PRIMARY KEY NOT NULL,
           副栏目ID TEXT NOT NULL,
           长标题 TEXT NOT NULL,
           短标题 TEXT NOT NULL,           
           摘要 TEXT NOT NULL,
           正文 TEXT NOT NULL,
           标题图  TEXT NOT NULL,
           标题前栏目字符串 TEXT NOT NULL);''')
    print("完成操作")
    conn.commit()
    conn.close()

#创建表SQLsqlite()

def 创建表2SQLsqlite():
    # !/usr/bin/python

    import sqlite3

    conn = sqlite3.connect('影视剧.db')
    print ("已连接数据库")
    c = conn.cursor()

    c.execute('CREATE TABLE 电视剧种子网址(种子网址 TEXT PRIMARY KEY NOT NULL);')


    print("完成操作")
    conn.commit()
    conn.close()


def 创建表3SQLsqlite():
    # !/usr/bin/python

    import sqlite3

    conn = sqlite3.connect('影视剧.db')
    print ("已连接数据库")
    c = conn.cursor()

    c.execute('CREATE TABLE 各帖子链接网址(各帖子链接 TEXT NOT NULL);')


    print("完成操作")
    conn.commit()
    conn.close()


#创建表3SQLsqlite()
def 电视剧种子网址():
    # !/usr/bin/python


    下载地址="9份"

    conn = sqlite3.connect('影视剧.db')
    print ("已连接数据库")
    c = conn.cursor()


    c.execute("INSERT INTO 电视剧种子网址(种子网址) \
          VALUES ('%s')"%(下载地址));

    conn.commit()
    conn.commit()


    print("完成操作")
    conn.close()





def SQLsqlite创建记录():
    # !/usr/bin/python

    import sqlite3

    conn = sqlite3.connect('影视剧.db')
    print ("已连接数据库")
    c = conn.cursor()


    c.execute("INSERT INTO 电视剧 (主栏目ID,副栏目ID,长标题,短标题,摘要,正文,标题图) \
          VALUES (主栏目ID,网站副栏目ID,长标题, 短标题2,摘要,正文,标题图,标题前栏目字符串)")


    conn.commit()
    print("完成操作")
    conn.close()

def 各帖子链接():
    # !/usr/bin/python

    import sqlite3

    conn = sqlite3.connect('影视剧.db')
    print ("已连接数据库")
    c = conn.cursor()


    c.execute("INSERT INTO 各帖子链接(各帖子链接) \
          VALUES (各帖子链接)")
    conn.commit()
    print("完成操作")
    conn.clos

def mysql存入数据():
    import pymysql

    下载地址='INSER'

    # 打开数据库连接
    db = pymysql.connect("localhost", "s2", "", "影视剧",charset="utf8")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 插入语句
    sql = """INSERT INTO 过滤已下载种子网址(种子网址)
             VALUES ('%s')"""%(下载地址)
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
    print('数据库保存')










