
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



class 类一一公共库: #调用 类的模具 self.模具一一数据库()
    def __init__(self):
        pass

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
                if '200' in str(self.返回网页内容) and 'None' not in str(self.返回网页内容) :
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


class 类一一提取正文(类一一公共库): #调用 类的模具 self.模具一一数据库()
    def __init__(self):
        self.模具一一换头部信息()
        self.网址='http://91btbtt.com/thread-index-fid-951-tid-3707480.htm'

        #self.模具一一帖子正文请求返回网页内容()
        self.模具一一帖子正文请求随机无序集()




    def 模具一一帖子正文请求返回网页内容(self):

        self.模具一一打开的网址请求返回网页内容(self.网址)
        self.帖子内容 = (self.返回网页内容.text)
        self.模具一一帖子正文字段清洗()

        print('正文:', self.正文)

    def 模具一一帖子正文请求随机无序集(self):
        网址列表 = []
        self.标题图列表 = []
        网址列表.append(self.网址)

        正文列表 = self.模具一一grequests打开网址随机无序集(网址列表)
        for 正文 in 正文列表:
            self.帖子内容=正文.text

            self.模具一一帖子正文列表清洗()

            print('正文:', self.正文)

    def 模具一一每一段落清洗(self):
        self.一楼合成内容 =''


        规则列表 = ["迅雷", 'href="http', 'http', 'text/javascript',"baidu","百度网盘", "网盘下载", "ed2k://", "ftp://", "本帖最后由", "上季",
                "<scripttype=", "BAIDU_CLB_SLOT_ID", '上季', '百度', '网盘', '本帖', 'magnet', '磁力', '种子', '电驴', '转贴', '本贴',
                "◎BT", "之家整理", "BT之家", "本帖编辑", "HQC小组", "所有压制整合作品", "链接"]
        for 每一段落 in self.段落列表:
            if self.计数器 != 0:
                每一段落 = self.换行字符 + 每一段落
            self.计数器 = self.计数器 + 1

            结束循环 = 123
            if '<img' in 每一段落 and 'src=' in 每一段落:
                self.标题图列表.append(每一段落)
                self.一楼合成内容 = self.一楼合成内容+ 每一段落
                continue  # 跳过当前循环,继续进行下一轮循环

            for 规则 in 规则列表:
                if 规则 in 每一段落 and 'douban' not in 每一段落:  # 不过滤◎豆瓣评分 douban
                    结束循环 = 0

                    print('过滤字符', 规则)
                    print('过滤段落', 每一段落)
                    if '</p>' in 每一段落:
                        每一段落 = '</p>'
                        self.一楼合成内容 = self.一楼合成内容 + 每一段落
                    break  # 结束循环 规则列表
            if 结束循环 == 0:
                continue  # 跳过当前循环,继续进行下一轮循环

            self.一楼合成内容 = self.一楼合成内容+ 每一段落

        self.一楼内容 =self.一楼合成内容
        print('self.一楼内容', self.一楼内容)


    def 模具一一帖子正文列表清洗(self):
        # 规则 = '(?<=648542).{1,}(?=BAIDU_CLB_SLOT_ID)'
        打印计数=0

        一楼内容 = str(self.帖子内容)
        规则 = '(?<=BAIDU_CLB_SLOT_ID).{1,}(?=BAIDU_CLB_SLOT_ID)'
        一楼内容列表 = re.findall(规则, str(一楼内容), re.S)

        一楼内容列表 = 一楼内容.split('BAIDU_CLB_SLOT_ID')
        一楼内容=一楼内容列表[2]


        print("打印计数", 打印计数)
        打印计数 = 打印计数 + 1
        print(一楼内容)

        行列表 = 一楼内容.split('\n')  # 以] 为界定 字符串变为 数个列表 数
        self.一楼内容 =''
        for 行 in 行列表:
            if 'script' not in 行:

                self.一楼内容 =self.一楼内容 + 行
                if '个附件' in 行:
                    break  # 结束循环
            else:  # 否则
                continue  # 跳过当前循环，继续进行下一轮循环



        print("打印计数",打印计数)
        打印计数 = 打印计数 + 1
        print(self.一楼内容)

        if '<p' in self.一楼内容 and '<br'in self.一楼内容: #  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            p段落列表 = self.一楼内容.split('<p')  #
            self.p段落一楼内容 = ''
            计数器=0
            for 段落 in p段落列表:
                if 计数器 !=0:
                    段落='<p'+段落
                计数器 =计数器+1
                self.段落列表 = 段落.split('<br')

                self.换行字符 = '<br'
                self.计数器=0
                self.模具一一每一段落清洗()

                self.p段落一楼内容 =self.p段落一楼内容 +self.一楼内容

            self.一楼内容=self.p段落一楼内容
            print("打印计数", 打印计数)
            打印计数 = 打印计数 + 1

            print('==', self.一楼内容)


        elif '<p' in self.一楼内容:# 其它条件
            self.段落列表 = self.一楼内容.split('<p')  ## .

            self.换行字符 = '<p'
            self.计数器 = 0
            self.模具一一每一段落清洗()
        elif '<br' in self.一楼内容:# 其它条件
            self.段落列表 = self.一楼内容.split('<br')  ##

            self.换行字符 = '<br'
            self.计数器 = 0
            self.模具一一每一段落清洗()

        else:# 否则
            print('正文清洗没有换行符: 路过循环')
            print(self.一楼内容)




        一楼内容 = self.一楼内容
        print("打印计数",打印计数)
        打印计数 = 打印计数 + 1

        print('=======一楼内容2333',一楼内容)

        规则列表 = ["</script>", "\'\";", "<ahrefa>", "</div>", "<div>", "\\u3000", "\\n"]
        for 规则 in 规则列表:
            一楼内容 = 一楼内容.replace(规则, "")
        一楼内容 = str(一楼内容).strip('\'')
        一楼内容 = str(一楼内容).replace("<div ", "<")
        一楼内容 = str(一楼内容).replace("< /div>", "<")
        if 'src=\"/upload' in 一楼内容:
            一楼内容 = str(一楼内容).replace("/upload", "http://91btbtt.com/upload")

        print("打印计数",打印计数)
        打印计数 = 打印计数 + 1

        print(一楼内容)

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

        print("打印计数",打印计数)
        打印计数 = 打印计数 + 1

        print(一楼内容)

        正文 = str(正文).strip('";')  # 文本前后截去特定字符串
        正文 = str(正文).strip('"')  # 文本前后截去特定字符串
        self.正文 = self.模具一一网站图片网址清洗转换(正文)

    def 模具一一帖子正文字段清洗(self):
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
        self.正文 = self.模具一一网站图片网址清洗转换(正文)


类=类一一提取正文()


            