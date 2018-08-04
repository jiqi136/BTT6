from lxml import html
import requests
import re
import time
import os
import pymysql
import random
# =====================================模具集================================
def 换头部信息(ua):
    #import random
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
def 换ip连接():
    # coding:gbk
    print('宽带连接进行时.....')
    import os
    import time
    os.system(r"rasphone -h 宽带连接")  # xxx0是你的拨号名称，xp下默认是“宽带连接”。
    os.system(r"rasdial 宽带连接 02007044432@163.gd  77341859")  # xxx0同上，xxx1 拨号用户名 ，xxx2拨号密码。
    time.sleep(1)
def 换ip():
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
def 提取数据库里的过滤网址(过滤帖子网址):
    # 提取数据库里的过滤网址
    # 打开数据库连接
    db = pymysql.connect("localhost", "s2", "", "影视剧", charset="utf8")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT 过滤网址 FROM 过滤网址"
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    过滤帖子网址 = cursor.fetchall()
    # 关闭数据库连接
    db.close()
    过滤帖子网址=str(过滤帖子网址)
    return 过滤帖子网址
def 提取数据库里的已下载内容网址(过滤下载内容网址):
    # 提取数据库里的过滤网址
    # 打开数据库连接
    db = pymysql.connect("localhost", "s2", "", "影视剧", charset="utf8")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句   已下载内容网址
    sql = "SELECT 已下载内容页网址 FROM 已下载内容页网址"
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    过滤下载内容网址 = cursor.fetchall()
    # 关闭数据库连接
    db.close()
    过滤下载内容网址=str(过滤下载内容网址)
    return 过滤下载内容网址
def 提取数据库里的过滤种子网址(过滤种子网址):
    # 提取数据库里的过滤种子网址
    # 打开数据库连接
    db = pymysql.connect("localhost", "s2", "", "影视剧", charset="utf8")
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
    过滤种子网址 = str(过滤种子网址)
    return 过滤种子网址
def 保存过滤帖子网址(各帖子链接):
    # 打开数据库连接，保存已下载网址
    db = pymysql.connect("localhost", "s2", "", "影视剧", charset="utf8")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 插入语句
    sql = """INSERT INTO 过滤网址(过滤网址)
               VALUES ('%s')""" % (各帖子链接)
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
def 打开的网址请求返回网页内容(打开的网址,ua,换IP时间计数a):
    try:
        返回网页内容 = requests.post(打开的网址, headers=ua, timeout=10)
        return 返回网页内容,ua,换IP时间计数a
    except requests.exceptions.InvalidHeader:
        print(ua)
        ua = 换头部信息(ua)
        返回网页内容 = requests.post(打开的网址, headers=ua, timeout=3)
        换IP时间计数a = int(time.time())
        return 返回网页内容, ua,换IP时间计数a
    except requests.exceptions.ConnectTimeout:
        print('网络异常等待60秒')
        ua = 'r'
        time.sleep(60)
        换ip()
        ua =换头部信息(ua)
        返回网页内容 = requests.post(打开的网址, headers=ua, timeout=3)
        换IP时间计数a = int(time.time())
        return 返回网页内容,ua,换IP时间计数a
    except requests.exceptions.ReadTimeout:
        print('网络异常等待60秒')
        time.sleep(60)
        ua = 'r'
        换ip()
        ua = 换头部信息(ua)
        返回网页内容 = requests.post(打开的网址, headers=ua, timeout=3)
        换IP时间计数a = int(time.time())
        return 返回网页内容,ua,换IP时间计数a
    except requests.exceptions.ConnectionError:
        print('网络异常等待60秒')
        time.sleep(60)
        ua = 'r'
        换ip()
        ua = 换头部信息(ua)
        返回网页内容 = requests.post(打开的网址, headers=ua, timeout=3)
        换IP时间计数a = int(time.time())
        return 返回网页内容,ua,换IP时间计数a
    except requests.exceptions.ChunkedEncodingError:
        print('网络异常等待60秒')
        time.sleep(60)
        ua = 'r'
        换ip()
        ua = 换头部信息(ua)
        返回网页内容 = requests.post(打开的网址, headers=ua, timeout=3)
        换IP时间计数a = int(time.time())
        return 返回网页内容, ua,换IP时间计数a
def 换IP时间计数(换IP时间计数a,ua):
    换IP时间计数b = int(time.time())
    换IP时间计数a=int(换IP时间计数a)
    if (换IP时间计数a +80) < 换IP时间计数b:
        换ip()
        ua = 'r'
        ua = 换头部信息(ua)
        换IP时间计数a = int(time.time())
        print(ua)
        return 换IP时间计数a,ua
    else:
        return 换IP时间计数a,ua
def 符号清洗(原文):
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



    return 原文
def 正文清洗(正文):
    正文 = str(正文).replace("\'\\n-->\\n\\n\',", "")
    正文 = str(正文).replace("\'\\n\',", "")
    正文 = str(正文).replace("\\u3000", "")
    a_规则 = '(?<=◎BT).{10}(?=\', \')'
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
    正文 = str(正文).replace("\\n", "")
    正文 = str(正文).replace("\', \'", "")
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
    正文 = str(正文).replace("ufeff", '')
    return 正文
def 保存帖子内容至数据库(时间ID,长标题,短标题,主栏目ID,网站副栏目ID,摘要,正文,标题图,标题前栏目字符串):
    # 打开数据库连接
    db = pymysql.connect("localhost", "s2", "", "影视剧", charset="utf8")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 插入语句
    sql = """INSERT INTO 电视剧集(时间ID,长标题,短标题,主栏目ID,副栏目ID,摘要,正文,标题图, 文章来源标题前栏目字符串)
                 VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (
    时间ID, 长标题, 短标题, 主栏目ID, 网站副栏目ID, 摘要, 正文, 标题图, 标题前栏目字符串)
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
    print('帖子内容保存完成')
def 保存已下载内容网址(各帖子链接):
    db = pymysql.connect("localhost", "s2", "", "影视剧", charset="utf8")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 插入语句
    sql = """INSERT INTO 已下载内容页网址(已下载内容页网址)
               VALUES ('%s')""" % (各帖子链接)
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
def 保存过滤已下载种子网址(种子下载地址):
    # 打开数据库连接
    db = pymysql.connect("localhost", "s2", "", "影视剧", charset="utf8")
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
def 种子名清洗(种子名):
    种子名规则 = '\[bt.{1,}\]'
    种子名 = re.sub(种子名规则, '', str(种子名))
    种子名 = str(种子名).replace("\'", '')
    种子名 = str(种子名).replace("\"", '')
    种子名 = str(种子名).replace(":", '')
    种子名 = str(种子名).replace("*", '')
    种子名 = str(种子名).replace("/", '')
    种子名 = str(种子名).replace("\\", '')
    种子名 = str(种子名).replace("#", '')
    种子名 = str(种子名).replace("\"", '')
    种子名 = str(种子名).replace("?", '')
    return 种子名
def 电视剧种子目录并下载(电视剧种子目录, 中短标题, 短标题, 种子名, 返回种子内容, 下载地址,过滤种子网址):

    # =========== 电视剧种子目录================
    # 电视剧种子目录 = 'F:/电影模板/下载种子目录2/电视剧/电视剧名/季度/'
    if '第' in str(中短标题):
        if '季' in str(中短标题):
            短标题规则 = '.{1,}(?=第)'
            季度名 = re.sub(短标题规则, '', 中短标题)
            季度名 = 符号清洗(季度名)
            电视剧种子目录 = str(电视剧种子目录).replace("电视剧名", str(短标题))
            电视剧种子目录 = str(电视剧种子目录).replace("季度", 季度名)
    else:
        电视剧种子目录 = str(电视剧种子目录).replace("电视剧名/季度",str(短标题))

    创建电视剧种子目录=str(电视剧种子目录).strip( '/' )
    if not os.path.exists(创建电视剧种子目录): # 必有条件选择，否则出错
        try:

            os.makedirs(创建电视剧种子目录)  # makedirs 创建多级目录文件夹，mkdir创建一个文件夹
        except FileNotFoundError:
            创建电视剧种子目录 = str(创建电视剧种子目录).replace(' ', '')
            创建电视剧种子目录 = str(创建电视剧种子目录).replace('\\n ', '')
            创建电视剧种子目录 = str(创建电视剧种子目录).replace('\n ', '')
            os.makedirs(创建电视剧种子目录)
        except OSError:
            创建电视剧种子目录 = str(创建电视剧种子目录).replace('\\n ', '')
            创建电视剧种子目录 = str(创建电视剧种子目录).replace('\n ', '')

            os.makedirs(创建电视剧种子目录)


    # =========== 种子下载=====
    目录与种子名 = str(电视剧种子目录) + str(种子名)
    with open(目录与种子名, 'wb') as fout:

        fout.write(返回种子内容.content)
        fout.close()
        print('完成下载', 目录与种子名)
    过滤种子网址 = 过滤种子网址 + str(下载地址)
    print('===========================')
    return 过滤种子网址
#===============================================================

# ============ =（模具）电视剧下载=================================================================
def 电视剧(倒页总数):
    # http://www.btbtt.net/forum-index-fid-950-page-648.htm
    # ===========# 电视剧下载=================================================================
    过滤种子网址 = 'htm'
    过滤帖子网址 = 'httm'
    过滤下载内容网址 = 'nt'
    过滤种子网址 = 提取数据库里的过滤种子网址(过滤种子网址)
    过滤帖子网址 = 提取数据库里的过滤网址(过滤帖子网址)
    过滤下载内容网址 = 提取数据库里的已下载内容网址(过滤下载内容网址)
    过滤帖子网址 = str(过滤帖子网址) + str(过滤下载内容网址)
    for 倒页数 in range(倒页总数, 0, -1):
        页数网址 = 'http://www.btbtt.net/forum-index-fid-950-page-648.htm'
        页数网址 = str(页数网址).replace("648", str(倒页数))
        换IP时间计数a = int(time.time())
        print('==============倒页数==============================================================================', 倒页数)
        ua='ewg'
        ua = 换头部信息(ua)
       # ===========打开的网址请求返回网页内容======================================
        返回值 =打开的网址请求返回网页内容(页数网址,ua,换IP时间计数a)
        帖子列表 = 返回值[0]
        ua = 返回值[1]
        换IP时间计数a = 返回值[2]
        #换IP时间计数a = int(time.time())
        # ====================================================
        帖子列表html = html.fromstring(帖子列表.text)
        提取帖子链接列表 = 帖子列表html.xpath('//*[@id="threadlist"]/table[*]/tr/td[1]/a[1]/@href')
        # ============各帖子链接============================================================
        for 各帖子链接 in 提取帖子链接列表:
            各帖子链接=str(各帖子链接)
            各帖子链接=各帖子链接.replace("thread", "http://www.btbtt.net/thread")
            if 各帖子链接 in 过滤帖子网址:
                print('过滤帖子网址')
                continue  # 跳过循环
            print('各帖子链接',各帖子链接)
            # ============换IP时间计数===============
            返回值 = 换IP时间计数(换IP时间计数a,ua)
            换IP时间计数a = 返回值[0]
            ua = 返回值[1]
            # ============  打开的网址请求返回网页内容==============================================
            返回值 =打开的网址请求返回网页内容(各帖子链接,ua,换IP时间计数a)
            帖子内容 = 返回值[0]
            ua = 返回值[1]
            换IP时间计数a = 返回值[2]
            # =====================
            帖子内容html = html.fromstring(帖子内容.text)
            帖子标题列表 = 帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/h2/text()')
            标题前的栏目列表= 帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/h2/a/text()')
            # =========#过滤标题栏目=====================================================
            if '[单集]' in 标题前的栏目列表:
                print('[单集]的栏目跳过循环')
                print('=====================')
                保存过滤帖子网址(各帖子链接)
                continue  # 跳过循环
            if '[Resilio-Sync]' in 标题前的栏目列表:
                print('Sync的栏目跳过循环')
                保存过滤帖子网址(各帖子链接)
                print('=====================')
                continue  # 跳过循环
            # ===============过滤图片==========================================
            帖子内容 = (帖子内容.text)
            标题图集 = 帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/p[*]/img/@src')
            if len(标题图集) == 0:
                if '人人' in str(帖子内容):
                    标题图集 = 帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/img/@src')
                    if len(标题图集) > 0:
                        标题图 = 标题图集[0]
                        if 'http' not in str(标题图):
                            标题图 = str(标题图).replace("/upload", "http://www.btbtt.co/upload")
                    else:
                        print('无标题图，跳过循环')
                        保存过滤帖子网址(各帖子链接)
                        print('=====================')
                        continue  # 跳过循环
                else:
                    print('无标题图，跳过循环')
                    保存过滤帖子网址(各帖子链接)
                    print('=====================')
                    continue  # 跳过循环
            elif len(标题图集) == 1:
                标题图 = 标题图集[0]
                if 'http' not in str(标题图):
                    标题图 = str(标题图).replace("/upload", "http://www.btbtt.co/upload")
            else:
                标题图 = 标题图集[1]
                if 'http' not in str(标题图):
                    标题图 = str(标题图).replace("/upload", "http://www.btbtt.co/upload")
            # ==========过滤无种子附件，跳过循环================================================
            if 'torrent.gif' not in str(帖子内容):
                print('无种子附件，跳过循环')
                print('=====================')
                保存过滤帖子网址(各帖子链接)
                continue  # 跳过循环
            # ========过滤图片已破，跳过循环=================================================================
            if 'tietuku' in str(帖子内容):
                print('图片已破，跳过循环')
                print('=====================')
                保存过滤帖子网址(各帖子链接)
                continue  # 跳过循环
            elif 'yupoo' in str(帖子内容):
                print('图片已破，跳过循环')
                print('=====================')
                保存过滤帖子网址(各帖子链接)
                continue  # 跳过循环
            elif 'imgsrc.baidu' in str(帖子内容):
                print('图片已破，跳过循环')
                print('=====================')
                保存过滤帖子网址(各帖子链接)
                continue  # 跳过循环
            elif '謦灵风软' in str(帖子内容):
                print('标记其它网站，跳过循环')
                print('=====================')
                保存过滤帖子网址(各帖子链接)
                continue  # 跳过循环
            # ========提取1楼种子名列表=============================================================
            if '个附件' in str(帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[1]/td[1]/text()')):
                楼种子名列表= 帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[*]/td[1]/a/text()')
                种子名列表文本=str(楼种子名列表)
                if '謦灵风软' in 种子名列表文本:
                    print('标记其它网站，跳过循环')
                    print('=====================')
                    保存过滤帖子网址(各帖子链接)
                    continue  # 跳过循环
                elif 'www.' in 种子名列表文本:
                    print('标记其它网站，跳过循环')
                    print('=====================')
                    保存过滤帖子网址(各帖子链接)
                    continue  # 跳过循环
                elif '.com' in 种子名列表文本:
                    print('标记其它网站，跳过循环')
                    print('=====================')
                    保存过滤帖子网址(各帖子链接)
                    continue  # 跳过循环
                elif '.net' in 种子名列表文本:
                    print('标记其它网站，跳过循环')
                    print('=====================')
                    保存过滤帖子网址(各帖子链接)
                    continue  # 跳过循环
             #电影的过滤
            # 謦灵风软www.|.com|先版|鲜版|鲜版|删减版|TS|TC|抢先|清晰|公映版|网盘下载|电驴|迅雷|[email /span
            # ======中短标题、短标题的清洗==============================================================================================================================================
            帖子标题=帖子标题列表[-1]
            帖子标题 =str(帖子标题)
            if '季]' in str(帖子标题):
                a_规则 = '(?<=\]\[).+?(?=季\])'
                帖子标题 = re.findall(a_规则, str(帖子标题))
                帖子标题 = str(帖子标题) + '季'
            elif '][全' in str(帖子标题):
                a_规则 = '(?<=\]\[).+?(?=\]\[全)'
                帖子标题 = re.findall(a_规则, str(帖子标题))
            elif '][更' in str(帖子标题):
                a_规则 = '(?<=\]\[).+?(?=\]\[更)'
                帖子标题 = re.findall(a_规则, str(帖子标题))
            elif '全][' in str(帖子标题):
                a_规则 = '(?<=\]\[).+?(?=全\]\[)'
                帖子标题 = re.findall(a_规则, str(帖子标题))
                if '集' in str(帖子标题):
                    a_规则2 = '.{1,}(?=\]\[)'
                    帖子标题 = re.findall(a_规则2,str(帖子标题))
                if '][' in str(帖子标题):
                    a_规则3 = '(?<=\]\[).{1,}'
                    帖子标题= re.findall(a_规则3, str(帖子标题))
            elif '集]' in str(帖子标题):
                a_规则 = '(?<=\]\[).+?(?=集\])'
                帖子标题 = re.findall(a_规则, str(帖子标题))
            elif ']' in str(帖子标题):
                print(' 帖子标题')
                print('不规整的标题帖子，跳过循环')
                保存过滤帖子网址(各帖子链接)
                print('=====================')
                continue  # 跳过循环
            # ===========
            短标题 = str(帖子标题)
            中短标题 =短标题
            # ===========
            if '][' in str(短标题):
                a_规则3 = '(?<=\]\[).{1,}'
                短标题 = re.findall(a_规则3, str(短标题))
            if '/' in str(短标题):
                # a_规则5 = '(?<=/).{1,}'
                # 短标题4 = re.sub(a_规则4, '', str(短标题3))
                a_规则4 = '/{1}'
                短标题 = re.sub(a_规则4, '%', str(短标题),  count=1)
                a_规则 = '.{1,}(?=%)'
                短标题 = re.findall(a_规则, str(短标题))
            elif ' ' in str(短标题):
                # a_规则4 = '.*(?=)'
                a_规则4 = '\s{1}'
                短标题 = re.sub(a_规则4, '%',str(短标题), count=1)
                a_规则 = '.{1,}(?=%)'
                短标题 = re.findall(a_规则, str(短标题))
            if '第' in str(短标题):
                if '季' in str(短标题):
                    a_规则 = '.{1,}(?=第)'
                    短标题 = re.findall(a_规则, str(短标题))
            # 符号清洗
            短标题 = 符号清洗(短标题)
            中短标题 =符号清洗(中短标题)
            print('短标题', 短标题)
            # ===========长标题=====================================================================================================================
            长标题规则 = '(?<=\]\[).{1,}'
            长标题 = re.findall(长标题规则, str(帖子标题))
            长标题 = str(长标题).replace("\'", "")
            if '][更' in str(长标题):
                a_规则 = '更\d{1,}集'
                长标题 = re.sub(a_规则, '',str(长标题))
            # 符号清洗
            长标题= 符号清洗(长标题)
            if len(长标题)==0:
                长标题=短标题
            print('长标题', 长标题)
            # ===========主栏目ID、标题前栏目字符串、网站副栏目==============================================================================================
            标题前栏目字符串=''.join(标题前的栏目列表)
            主栏目ID=10
            摘要='<h2>资源下载：<a href="/uploads/dianshiju/参数1.html"target="_blank">参数2.torrent</a></h2>'
            摘要 = str(摘要).replace("参数1", str(短标题))
            摘要 = str(摘要).replace("参数2", str(长标题))
            print('摘要', 摘要)
            网站副栏目字典 = {'[美国]': '15', '[英国]': '15', '[大陆]': '11', '[香港]': '13', '[台湾]': '39', '[日本]': '12', '[韩国]': '40',
                       '[法国]': '16', '[西剧]': '16', '[泰国]': '16', '[加剧]': '15', '[意剧]': '16', '[澳剧]': '16', '[德国]': '16',
                       '[新马]': '16', '[剧情]': '43', '[喜剧]': '44', '[爱情]': '45', '[偶像]': '45','[动作]': '46', '[奇幻]': '47', '[科幻]': '48',
                       '[悬疑]': '49', '[罪案]': '49', '[刑侦]': '49', '[战争]': '50', '[谍战]': '50', '[军旅]': '50', '[历史]': '51',
                       '[古装]': '51', '[惊悚]': '52', '[恐怖]': '52', '[动画]': '53', '[真人]': '54', '[剧情]': '43', '[时装]': '43',
                       '[医务]': '43', '[歌舞]': '43', '[时装]': '43', '[其他]': '43', '[喜剧]': '44', '[都市]': '45', '[情感]': '45',
                       '[家庭]': '43', '[动作]': '46', '[奇幻]': '47', '[科幻]': '48', '[悬疑]': '49', '[战争]': '50', '[军旅]': '50',
                       '[武侠]': '51', '[惊悚]': '52', '[动画]': '53', '[真人]': '54', '[纪录]': '55', '[经典]': '56',  '[合 集]': '', '[连载]': '', '[经典]': '', '[全集]': '', '[打包]': '', '[单集]': '', '[合集]': '','[断载]': '','[2006]': '92',
                       '[2007]': '91', '[2008]': '90', '[2009]': '89', '[2010]': '88', '[2011]': '87', '[2012]': '86',
                       '[2013]': '85', '[2014]': '84', '[2015]': '83', '[2016]': '82', '[2017]': '81', '[2018]': '80',
                       '[更 早]': '93'}
            网站副栏目ID = [网站副栏目字典[x] if x in 网站副栏目字典 else x for x in 标题前的栏目列表]
            网站副栏目ID =str(网站副栏目ID)
            # 符号清洗
            网站副栏目ID = 符号清洗(网站副栏目ID)
            if len(网站副栏目ID)==0:
                网站副栏目ID =43
            print('网站副栏目ID', 网站副栏目ID)
            print('标题前栏目字符', 标题前栏目字符串)
            时间ID = time.strftime("%y%m%d%H%M%S", time.localtime())
            # =========（模具）正文清洗=====================================================
            正文 = 帖子内容html.xpath(
                '//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/p/text()|//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/p[*]/span/text()|//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/p[*]/span/span/text()|//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/p[*]/span/span/span/text()|//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/p[*]/span/span/span/span/text()|//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/text()|//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/div[*]/font/*/text()|//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/div[*]/text()|//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/ul/li[*]/p/text()')
            正文 = str(正文)
            正文=正文清洗(正文)
            # ===========保存帖子内容至数据库==================================================================
            保存帖子内容至数据库(时间ID, 长标题, 短标题, 主栏目ID, 网站副栏目ID, 摘要, 正文, 标题图, 标题前栏目字符串)
            长标题 = '空标题'
            过滤帖子网址 = 过滤帖子网址 + str(各帖子链接)
            # =========== 提取1楼种子列表==================================================================
            if '个附件' in str(帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[1]/td[1]/text()')):
                提取首楼种子下载地址列表 = 帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[*]/td[1]/a/@href')
                种子名列表= 帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[*]/td[1]/a/text()')
                for (楼种子下载地址, 种子名) in zip(提取首楼种子下载地址列表, 种子名列表):
                    # =========== 提过滤种子网址# 跳过循环============
                    if 楼种子下载地址 in str(过滤种子网址):
                        print('过滤种子网址')
                        print('=====================')
                        continue  # 跳过循环
                    # =========（模具）种子名过滤与清洗============
                    if '.jpg' in str(种子名):
                        print('跳过下载图片')
                        continue  # 跳过循环
                    elif '.png' in str(种子名):
                        print('跳过下载图片')
                        continue  # 跳过循环
                    # =========== （模具）种子名清洗=========
                    种子名 = 种子名清洗(种子名)
                    # =========== （模具）换IP时间计数============
                    返回值 = 换IP时间计数(换IP时间计数a, ua)
                    换IP时间计数a = 返回值[0]
                    ua = 返回值[1]
                    # =========== （模具）保存过滤已下载种子网址============
                    保存过滤已下载种子网址(楼种子下载地址)
                    # =========== （模具）返回种子内容============
                    楼种子下载地址 = str(楼种子下载地址).replace("attach", "http://www.btbtt.net/attach")
                    楼种子下载地址 = str(楼种子下载地址).replace("dialog", "download")
                    返回值 =打开的网址请求返回网页内容(楼种子下载地址, ua,换IP时间计数a)
                    返回种子内容 = 返回值[0]
                    ua = 返回值[1]
                    换IP时间计数a = 返回值[2]
                    # =========== 电视剧种子目录================
                    电视剧种子目录 = 'F:/电影模板/下载种子目录2/电视剧/电视剧名/季度/'
                    # =========== （模具）电视剧种子目录并下载================
                    过滤种子网址 = 电视剧种子目录并下载(电视剧种子目录, 中短标题, 短标题, 种子名, 返回种子内容,楼种子下载地址, 过滤种子网址)
            # =========== 提取各分层页种子列表=================================================================
            提取各分层 = 帖子内容html.xpath('//*[@id="body"]/div/table[*]/tr/td[3]/div')
            层数 = (len(提取各分层))
            for 分层 in range(层数):
                查看附件规则 = ('//*[@id="body"]/div/table[' + str(分层) + ']/tr/td[3]/div/div[2]/table/tr[1]/td[1]/text()')
                分层名目规则 = ('//*[@id="body"]/div/table[' + str(分层) + ']/tr/td[3]/div/div/p[1]/text()|//*[@id="body"]/div/table[' + str(
                    分层) + ']/tr/td[3]/div/div/p[1]/span/text()')
                分层种子列表规则 = ('//*[@id="body"]/div/table[' + str(分层) + ']/tr/td[3]/div/div[2]/table/tr[*]/td[1]/a/@href')
                分层种子名列表规则 = ('//*[@id="body"]/div/table[' + str(分层) + ']/tr/td[3]/div/div[2]/table/tr[*]/td[1]/a/text()')
                查看附件 = 帖子内容html.xpath(查看附件规则)
                分层名目= 帖子内容html.xpath(分层名目规则)
                分层名目=''.join(分层名目)
                if '天天' in str(分层名目):
                    continue  # 跳过循环
                if '个附件' in str(查看附件):
                    分层种子列表 = 帖子内容html.xpath(分层种子列表规则)
                    分层种子名列表= 帖子内容html.xpath(分层种子名列表规则)
                    for (下载地址, 种子名) in zip(分层种子列表, 分层种子名列表):
                        if 下载地址 in str(过滤种子网址):
                            print('过滤种子网址')
                            continue  # 跳过循环
                        # =========== （模具）下载种子网址================
                        种子名=种子名清洗(种子名)
                        # =========== （模具）换IP时间计数================
                        返回值 = 换IP时间计数(换IP时间计数a, ua)
                        换IP时间计数a = 返回值[0]
                        ua = 返回值[1]
                        # =========== （模具）保存过滤已下载种子网址================
                        保存过滤已下载种子网址(下载地址)
                        # =========== （模具）下载种子网址================
                        下载地址 = str(下载地址).replace("attach", "http://www.btbtt.net/attach")
                        下载地址 = str(下载地址).replace("dialog", "download")
                        返回值 =打开的网址请求返回网页内容(下载地址, ua,换IP时间计数a)
                        返回种子内容 = 返回值[0]
                        ua = 返回值[1]
                        换IP时间计数a = 返回值[2]
                        # =========== 电视剧种子目录================
                        电视剧种子目录 = 'F:/电影模板/下载种子目录2/电视剧/电视剧名/季度/分层名/'
                        分层名目 =符号清洗(分层名目)
                        电视剧种子目录 = str(电视剧种子目录).replace("分层名", 分层名目)
                        # =========== （模具）电视剧种子目录并下载================
                        过滤种子网址=电视剧种子目录并下载(电视剧种子目录, 中短标题, 短标题, 种子名, 返回种子内容, 下载地址, 过滤种子网址)
                else:
                    continue  # （跳过当前循环）
            # ===========# 保存已下载网址至数据库=================================================================
            保存已下载内容网址(各帖子链接)
# =========================================
  # 帖子内容页(页数网址,过滤种子网址,过滤帖子网址,换IP时间计数a)
倒页总数=120
电视剧(倒页总数)
# =========================================================================
