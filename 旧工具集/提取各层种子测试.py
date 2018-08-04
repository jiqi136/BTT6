

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

class 类一一种子名: #调用 类的模具 self.模具一一数据库()
    def __init__(self):
        self.模具_换头部信息()
        self.模具一一种子名()
        pass

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
                              {
                                  'User-Agent': 'Mozilla/4.0 (compatible; MSIE 随机1位数.0; Windows NT 随机11位数.1; The World)'},
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
    def 模具一一种子名(self):
        网址='http://91btbtt.com/thread-index-fid-950-tid-4377380.htm'
        self.模具_打开的网址请求返回网页内容(网址)
        网页文本=self.返回网页内容.text
        分层列表 = 网页文本.split("div class=\"grey mod\" pid=")
        for 分层 in 分层列表:
            if 'torrent.gif' in 分层 and '个附件' in 分层 and '金币' in 分层: #种子附件的过滤
                行列表 = 分层.split("\n")
                for 行 in 行列表:
                    if '</p></div>' in 行 and '◎' not in 行:
                        分层名=行
                        规则列表=['</p>.{1,}','<br.{1,}', '<.{1,}?>']
                        for 规则 in 规则列表:
                            分层名 = re.sub(规则, '', str(分层名))  # 替换   ,count=0,re.S|re.I
                        print('===========================:')
                        print('分层名:',分层名)
                    if 'torrent.gif' in 行 and 'attach-dialog-fid' in 行:  # 种子附件的过滤
                        种子行=行
                        规则='".{1,}?"'
                        文本列表 = re.findall(规则, str(种子行))  # 提取列表
                        种子链接 = 文本列表[0]
                        种子链接 = 种子链接.replace("\"", "") #替换   , 1) 次数 1
                        print('种子链接:', 种子链接)
                        规则 = '<.{1,}?>'
                        种子名 = re.sub(规则, '', str(种子行))  # 替换   ,count=0,re.S|re.I
                        print('种子名:', 种子名)



分层列表 = self.帖子内容.split("div class=\"grey mod\" pid=")
        for 分层 in 分层列表:
            if 'torrent.gif' in 分层 and '个附件' in 分层 and '金币' in 分层:  # 种子

if '◎' in 行 and '</p></div>' in 行:  # 第一层内容页的 种子附件
    self.种子目录 = 种子目录.replace("分层名/", "")  # 替换   , 1) 次数 1
    break  # 结束循环



规则 = '<.{1,}?>'
                        种子名 = re.sub(规则, '', str(种子行))  # 替换   ,count=0,re.S|re.I
                        print('种子名:', 种子名)

if self.影视类型 == '电视剧' or self.影视类型 == '动漫':
    self.模具一一提取一楼种子名进行过滤()
else:  # 否则
    self.模具一一电影过滤一楼种子名()
if self.跳过循环 == 0:
    self.模具一一保存最新影视剧过滤帖子网址()
    continue  # 跳过循环






类=类一一种子名()
