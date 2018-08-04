
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


class 类一一会话: #调用 类的模具 self.模具一一数据库()
    def __init__(self):
        self.模具一一换头部信息()
        self.模具一一会话()

    def 模具一一会话(self):
        self.模具一一导入cookie()
        url = 'http://3e38.com/image/article_add.php?channelid=17'
        self.会话 = grequests.Session()  # 创建全局会话
        self.会话.cookies.update(self.cookies)  # 格式化cookie,全网页才能共享登录cookie,

        返回网页内容 = self.会话.get(url)
        返回网页内容 = 返回网页内容.text
        if '看不清' in 返回网页内容:
            print('登录失效,正在启动浏览器.')
            self.模具一一浏览器输入验证码提取cookies()
        else:  # 否则
            print('======登录成功=========')

    def 模具一一会话打开网址随机无序集(self, 网址总列表):  # grequests.imap(任务列
        网址分列表 = []
        倒数 = len(网址总列表)
        内容总列表 = []
        规则 = '.{1,}hread'
        for 各帖子链接 in 网址总列表:
            网址分列表.append(各帖子链接)
            倒数 = 倒数 - 1
            if len(网址分列表) == 20 or 倒数 == 0:
                print('等待响应网页倒数', 倒数)
                任务列表 = []
                for 各帖子链接 in 网址分列表:
                    if 'thread' in 各帖子链接:
                        各帖子链接 = re.sub(规则, 'http://91btbtt.com/thread', 各帖子链接)  # 替换
                        # if 各帖子链接 in self.过滤帖子网址:
                        # continue  # 跳过当前循环，继续进行下一轮循环
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
        print('返回网页内容数', len(内容总列表))  # break # 结束循环
        return 内容总列表  # 返回



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
        帖子内容 = self.置顶类型帖子网页内容.text

        一楼内容列表 = 帖子内容.split('BAIDU_CLB_SLOT_ID')
        if len(一楼内容列表) < 2:
            print('一楼内容列表 小于2: 路过循环')
            self.正文清洗没有换行符 = 0
            return  # 结束函数
        一楼内容 = 一楼内容列表[2]

        行列表 = 一楼内容.split('\n')  # 以] 为界定 字符串变为 数个列表 数
        一楼内容 = ''
        for 行 in 行列表:
            if 'script' not in 行:
                一楼内容 = 一楼内容 + 行
        行列表 = 一楼内容.split('href="')  # 以] 为界定 字符串变为 数个列表 数
        链接列表 = []
        for 行 in 行列表:
            if '.htm"' in 行:
                规则 = '.htm".{1,}'
                链接 = re.sub(规则, '.htm', 行, re.S)  # 替换   ,count=0,re.S|re.I
                if '-page-' in 链接:
                    规则 = '-page-.{1,}'
                    链接 = re.sub(规则, '.htm', 行, re.S)  # 替换   ,count=0,re.S|re.I
                if 链接 in self.过滤帖子网址:
                    continue  # 跳过当前循环，继续进行下一轮循环
                链接列表.append(链接)
        self.页面提取帖子链接列表 = set(链接列表)  # 转换为集,去重复list()

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
                    复制合集目录与种子名 = str(复制合集目录与种子名).replace("上传网盘/最新", "下载保存")  # 替换   , 1) 次数 1
                    if '电视剧' in self.影视类型:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                        复制合集目录与种子名 = str(复制合集目录与种子名).replace("/电视剧/", "/旧剧集合集/")  #
                    elif '动漫' in self.影视类型:  # 其它条件.
                        复制合集目录与种子名 = str(复制合集目录与种子名).replace("/动漫/", "/旧动漫合集/")  #
                    else:  # 否则
                        复制合集目录与种子名 = str(复制合集目录与种子名).replace("/电影/", "/旧电影/")  #

                    复制合集目录与种子名二 = str(目录与种子名)
                    复制合集目录与种子名二 = str(复制合集目录与种子名二).replace("最新", "合集")  # 替换   , 1) 次数 1

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
        规则 = '.{1,}hread'
        for 各帖子链接 in 网址总列表:
            网址分列表.append(各帖子链接)
            倒数 = 倒数 - 1
            if len(网址分列表) == 20 or 倒数 == 0:
                print('等待响应网页倒数', 倒数)
                任务列表 = []
                for 各帖子链接 in 网址分列表:
                    if 'thread' in 各帖子链接:
                        各帖子链接 = re.sub(规则, 'http://91btbtt.com/thread', 各帖子链接)  # 替换
                        # if 各帖子链接 in self.过滤帖子网址:
                        # continue  # 跳过当前循环，继续进行下一轮循环
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
        print('返回网页内容数', len(内容总列表))  # break # 结束循环
        return 内容总列表  # 返回

类=类一一会话()
        
            