# -*- coding:utf-8
from selenium import webdriver  # 浏览的驱动


import re  # 正则式
import time  # 时间


import random  # 随机




class 类一一公共库:  # 调用 类的模具 self.模具一一数据库()
    def __init__(self):

        self.模具一一换头部信息()

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
        self.头部信息=头部信息
        print(头部信息)

    def 模具一一打开的网址请求返回网页内容(self, 网址):  # self.返回网页内容
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

    def 模具一一gr无序单网址请求返回网页内容(self, 单网址):  # grequests.imap(任务列
        单网址列表 = []
        单网址列表.append(单网址)

        单网址列表 = 单网址列表 * 3
        规则 = '.{1,}hread'
        任务列表 = []
        for 各帖子链接 in 单网址列表:
            if 'thread' in 各帖子链接:
                各帖子链接 = re.sub(规则, 'http://91btbtt.com/?thread', 各帖子链接)  # 替换
                # if 各帖子链接 in self.过滤帖子网址:
                # continue  # 跳过当前循环,继续进行下一轮循环
            任务 = grequests.get(各帖子链接, headers=头部信息)  # timeout=len(任务列表)//2,
            任务列表.append(任务)

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
                print('倒数6秒再连接', 次数循环, '次')
                # time.sleep(3)
            else:

                for 返回网页内容 in 返回网页内容集:
                    返回网页内容文本 = str(返回网页内容)
                    if '<Response [200]>' in 返回网页内容文本:
                        # print('返回网页内容', 返回网页内容)
                        返回网页内容.encoding = "UTF-8"

                        return 返回网页内容  # 返回

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
                        # continue  # 跳过当前循环,继续进行下一轮循环
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

    """============异步打开网页================"""

    async def 模具一一异步打开网页(self, url):

        # conn = aiohttp.TCPConnector(limit=10)  # 默认100,0表示无限
        async with aiohttp.ClientSession(headers=头部信息, connector=aiohttp.TCPConnector(limit=10)) as 会话:

            try:  # 调用异常处理,应对易发生错误的位置
                async with 会话.request("GET", url) as 内容:  # "GET" 是个重要的请求方法
                    返回网页 = await 内容.text(
                        encoding="utf-8")  # 或者直接await r.read()不encoding='UTF-8',直接读取,适合于图像等无法encoding='UTF-8'文件

            except:  # () as 异常
                # print('网络异常等待', 异常)
                print('倒数6秒再连接', '次')
                # time.sleep(3)
            else:
                if '[200 OK]' in str(内容):
                    pass
                else:  # 否则
                    内容 = self.模具一一gr无序单网址请求返回网页内容(url)
                    返回网页 = 内容.text
                    print('重新修正内容', 内容)
                返回网页一链接组 = []
                返回网页一链接组.append(返回网页)
                返回网页一链接组.append(url)
                self.返回网页一链接组列表.append(返回网页一链接组)

    def 模具一一异步调度(self, 网址列表):
        此时数 = int(time.time())
        if 此时数 > 换IP时间计数 + 60:
            self.模具一一换ip连接()
            self.模具一一换头部信息()

        self.返回网页一链接组列表 = []
        任务列表 = []
        规则 = '.{1,}hread'
        for 各帖子链接 in 网址列表:
            if 'thread' in 各帖子链接:
                各帖子链接 = re.sub(规则, 'http://91btbtt.com/?thread', 各帖子链接)  # 替换
                # if 各帖子链接 in self.过滤帖子网址:
                # continue  # 跳过当前循环,继续进行下一轮循环
            print('各帖子链接', 各帖子链接)

            任务 = asyncio.ensure_future(self.模具一一异步打开网页(各帖子链接))
            任务列表.append(任务)

        event_loop = asyncio.get_event_loop()
        results = event_loop.run_until_complete(asyncio.wait(任务列表))  # 等待任务完成
        event_loop.close()

    def 模具一一异步返回网页一链接组列表(self):
        网址列表 = []

        self.模具一一异步调度(网址列表)  # self.返回网页一链接组列表
        for 返回网页一链接组 in self.返回网页一链接组列表:
            返回网页内容 = 返回网页一链接组[0]
            链接 = 返回网页一链接组[1]
            print('链接', 链接)
        print('返回网页内容', 返回网页内容)

    """============测试库================"""


class 类一一测试库(类一一公共库):  # 调用 类的模具 self.模具一一数据库()
    def __init__(self):
        self.模具一一换头部信息()

        # self.模具一一gr无序单网址()
        self.模具一一浏览器访问并注册知乎()


    def 模具一一gr无序单网址(self):

        单网址 = 'http://91btbtt.com/?thread-4348648.htm'

        网址内容 = self.模具一一gr无序单网址请求返回网页内容(单网址)
        print('网址内容:', 网址内容.text)

    def 模具一一异步调度网址列表(self):
        网址列表 = []
        页数网址 = 'http://news.paidai.com/?page={}'  # {}

        for 倒页数 in range(18, 0, -1):
            各帖子链接 = 页数网址.format(str(倒页数))  # 不换行 end=""  request("GET"  pool=1, ,size=2 pool=1,timeout=len(任务列表)//2,
            print('各帖子链接', 各帖子链接)
            网址列表.append(各帖子链接)
        self.模具一一异步调度(网址列表)  # self.返回网页一链接组列表

        for 返回网页一链接组 in self.返回网页一链接组列表:
            返回网页内容 = 返回网页一链接组[0]
            链接 = 返回网页一链接组[1]
            print('链接', 链接)
        # print('网址内容:', 网址内容.text)

        print('返回网页内容', 返回网页内容)

    def 模具一一提炼Cookie(self):
        Cookie文本='tgw_l7_route=170010e948f1b2a2d4c7f3737c85e98c; _zap=ce1305a8-7d69-4551-b0c9-3cdf5d6e0b0c; _xsrf=pSfp9xAJvbYsJp1oUeeJVgGwSSWRFG79; q_c1=b2869836ad1545b89e2ca2fe599291f3|1534096133000|1534096133000; d_c0="ABBnPv7jCw6PTvReDG2SZyvJkmkHe8nDvT4=|1534096133"; capsion_ticket="2|1:0|10:1534096136|14:capsion_ticket|44:Mzg1YjZlMGFlOWY4NGE5MmI3M2IxOTA3MzQ3NjdhMTc=|3531eddc76e8d7935cbda485229e69ab672d0ab931d9139acb5a96cd8d1059e0"; z_c0="2|1:0|10:1534096157|4:z_c0|92:Mi4xTGlzSUFBQUFBQUFBRUdjLV91TUxEaVlBQUFCZ0FsVk5IY0ZkWEFBWHFOTTc5V0M5M19NUFMtbHYyaG1YU044MmNn|2163e2d4319ea00dfbc6fd180ec62e5a883da34d05477a0cec2806e10e49d870"'

        cookies = {}
        for 每句 in Cookie文本.split(';'): # 转为列表cookies['tgw_l7_route']
            字典键, 值 = 每句.strip().split('=', 1)  # 1代表只分割一次
            cookies[字典键] = 值
        self.cookies =cookies
        self.cookies浏览操作= {'domain': '.www.zhihu.com',
                        'name': 'tgw_l7_route',
                        'value': 'ec452307db92a7f0fdb158e41da8e5d8',
                       '_zap':cookies['_zap'],
                       '_xsrf':cookies['_xsrf'],
                       'capsion_ticket': cookies['capsion_ticket'],
                       'd_c0':cookies['d_c0'],
                       'z_c0':cookies['z_c0'],
                        'q_c1':cookies['q_c1'],
                        'expiry': None,
                        'path': '/',
                        'httpOnly': False,
                        'secure': False}
        self.cookies = cookies

    def 模具一一浏览器访问并注册知乎(self):
        self.模具一一换头部信息()
        self.模具一一提炼Cookie()

        头部信息 = str(self.头部信息).replace("'User-Agent':", "user-agent=")  # 替换   , 1) 次数 1
        头部信息 = 头部信息.replace("{", "")  # 替换   , 1) 次数 1
        头部信息 = 头部信息.replace("}", "")  # 替换   , 1) 次数 1
        后缀 = 'user-agent=Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'

        options = webdriver.ChromeOptions()  # 设置中文

        # options = Options()

        options.add_argument('disable-infobars')  # 加启动配置 去除正在受到自动软件的控制
        print('头部信息:', 头部信息)
        print('后缀t:', 后缀)
        options.add_argument(后缀)



        浏览器操作 = webdriver.Chrome(chrome_options=options)  # 打开chrome浏览器



        url = "https://www.zhihu.com"  # 注册页面  https://www.zhihu.com/signup?next=%2Fexplore
        浏览器操作.get(url)
        time.sleep(2)  # 等待
        主页cookies=浏览器操作.get_cookies()  # 打开主页后获取cookies
        print('登录前主页cookies',主页cookies)
        cookies浏览=主页cookies[0]


        浏览器操作.delete_all_cookies() # 删除第一次建立连接时的cookie

        time.sleep(100000)  # 等待

        for 键名 in self.cookies:

            cookies浏览操作 = {'domain': '.www.zhihu.com',
                           'name': 键名,
                           'value': self.cookies[键名],
                           'expiry':cookies浏览['expiry']+31536000,
                           'path': '/',
                           'httpOnly': False,
                           'secure': False}
            浏览器操作.add_cookie(cookie_dict=cookies浏览操作)


        # 浏览器操作.add_cookie(cookie_dict=self.cookies浏览操作)
        #浏览器操作.add_cookie(cookie_dict=cookies浏览)
        # 浏览器操作.add_cookie({'value': '61066e97b5b7b3b0daad1bff47134a22'})



        time.sleep(2)  # 等待
        主页cookies = 浏览器操作.get_cookies()  # 打开主页后获取cookies
        print('登录后主页cookies', 主页cookies)

        浏览器操作.refresh()  # 刷新当前页面

        time.sleep(20000)  # 等待


类 = 类一一测试库()



