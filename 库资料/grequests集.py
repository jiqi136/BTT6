import grequests
import time
import ahttp
import random



def 模具一一换头部信息():  # 头部信息 def 函数模具内通行变量
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
def grequests顺序集():#grequests.map(任务列
    页数网址 = 'http://91btbtt.com/forum-index-fid-951-page-123.htm'#http://www.mzitu.com/page/3/
    任务列表=[]
    for 倒页数 in range(15,5,-1):
        各帖子链接 = str(页数网址).replace("123", str(倒页数))
        任务=grequests.get(各帖子链接)
        任务列表.append(任务)


    条件循环 = 1
    次数循环 = 0
    while 条件循环 == 1:
        try:  # 调用异常处理，应对易发生错误的位置
            返回网页内容集 = grequests.map(任务列表, size=5,gtimeout=len(任务列表)//2)  # size=3 并发数 3  gtimeout超时时间

        except (grequests.exceptions.ConnectTimeout, grequests.exceptions.ReadTimeout,
                grequests.exceptions.ConnectionError, grequests.exceptions.ConnectTimeout,
                grequests.exceptions.ChunkedEncodingError, grequests.exceptions.InvalidSchema) as 异常:
            print('网络异常等待', 异常)
            print('倒数9秒再连接', 次数循环, '次')
            # time.sleep(3)

        else:
            返回网页内容集文本=str(返回网页内容集)
            if '200' in 返回网页内容集文本 and 'None'not in 返回网页内容集文本 and  '40' not in 返回网页内容集文本:

                print('返回网页内容集', 返回网页内容集)
                条件循环 = 0
                #return  # 返回
            else:
                print('网站网络异常,状态码:',返回网页内容集)

    for 返回网页内容 in 返回网页内容集:
        print('返回网页内容url',返回网页内容.url)
        返回网页内容.encoding = "UTF-8"


    print('完成')

def grequests随机无序集(): # grequests.imap(任务列
    页数网址 = 'http://91btbtt.com/forum-index-fid-951-page-123.htm'#http://www.mzitu.com/page/3/
    任务列表=[]

    for 倒页数 in range(15,5,-1):
        各帖子链接 = str(页数网址).replace("123", str(倒页数))
        if len(任务列表) > 20:
            任务 = grequests.get(各帖子链接, timeout=len(任务列表) // 2, headers=头部信息)  # timeout=len(任务列表)//2,
        else:  # 否则
            任务 = grequests.get(各帖子链接, headers=头部信息)  # timeout=len(任务列表)//2,
        任务列表.append(任务)


    条件循环 = 1
    次数循环 = 0
    while 条件循环 == 1:
        计数器 = 0
        try:  # 调用异常处理，应对易发生错误的位置
            返回网页内容集 = grequests.imap(任务列表, size=5)  # size=3 并发数 3  gtimeout超时时间

        except (grequests.exceptions.ConnectTimeout, grequests.exceptions.ReadTimeout,
                grequests.exceptions.ConnectionError, grequests.exceptions.ConnectTimeout,
                grequests.exceptions.ChunkedEncodingError, grequests.exceptions.InvalidSchema) as 异常:
            print('网络异常等待', 异常)
            print('倒数9秒再连接', 次数循环, '次')
            # time.sleep(3)
        else:
            返回网页内容列表=[]
            for 返回网页内容 in 返回网页内容集:
                返回网页内容文本 = str(返回网页内容)
                if '200' in 返回网页内容文本 and 'None' not in 返回网页内容文本 and '40' not in 返回网页内容文本 :
                    #print('返回网页内容', 返回网页内容)
                    计数器 =计数器+1
                    返回网页内容列表.append(返回网页内容)
                    print('计数器', 计数器)

                if len(任务列表) ==计数器:
                    print('len(任务列表)',len(任务列表))
                    条件循环 =233
                    # return 返回网页内容集  # 返回

    for 返回网页内容 in 返回网页内容集:

        print('返回网页内容url',返回网页内容.url)

        返回网页内容.encoding = "UTF-8"
    for 返回网页内容 in 返回网页内容列表:

        print('返回网页url',返回网页内容.url)

        返回网页内容.encoding = "UTF-8"
    print('完成')


def ahttp随机无序集():#grequests.map(任务列


    会话 = ahttp.Session(headers = 头部信息)

    页数网址 = 'http://91btbtt.com/forum-index-fid-951-page-123.htm'#http://www.mzitu.com/page/3/
    任务列表=[]
    for 倒页数 in range(15,5,-1):
        各帖子链接 = str(页数网址).replace("123", str(倒页数))
        任务=会话.get(各帖子链接,pool=1,timeout=len(任务列表)//2,size=2)
        任务列表.append(任务)


    条件循环 = 1
    次数循环 = 0
    print('len(任务列表)//2',len(任务列表)//2)  # 异常
    while 条件循环 == 1:
        try:  # 调用异常处理，应对易发生错误的位置
            返回网页内容集 = ahttp.run(任务列表)  # size=3 并发数 3  gtimeout超时时间


        except:  # (re) as 异常
            print('网络异常等待')# 异常
            print('倒数9秒再连接', 次数循环, '次')
            # time.sleep(3)

        else:
            返回网页内容集文本=str(返回网页内容集)
            if '200' in 返回网页内容集文本 and 'None'not in 返回网页内容集文本 and  '40' not in 返回网页内容集文本:

                print('返回网页内容集', 返回网页内容集)
                条件循环 = 0
                #return  # 返回
            else:
                print('网站网络异常,状态码:',返回网页内容集)
                time.sleep(1)

    for 返回网页内容 in 返回网页内容集:
        print('返回网页内容url',返回网页内容.url)
        返回网页内容.encoding = "UTF-8"


    print('完成')

模具一一换头部信息()


#ahttp随机无序集()
grequests随机无序集()





