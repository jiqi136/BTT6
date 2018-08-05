# -*- coding:utf-8

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
import win32api  # 操作本地文件
from selenium import webdriver  # 浏览的驱动
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


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

    def 模具一一打开的网址请求返回网页内容(self,网址):  # self.返回网页内容
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
                返回网页内容 = requests.post(网址, headers=头部信息, timeout=10)
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
                if '200' in str(返回网页内容):
                    返回网页内容.encoding = "UTF-8"  # 转换encoding='UTF-8' "gbk"
                    return  返回网页内容 # 返回
                else:
                    print('网站网络异常,状态码:', 返回网页内容)
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




    """============测试库================"""


class 类一一测试库(类一一公共库):  # 调用 类的模具 self.模具一一数据库()
    def __init__(self):
        self.模具一一换头部信息()
        开始时间计数 = int(time.time())

        # self.模具一一易码短信平台()
        self.模具一一浏览器访问并注册知乎()

        结束时间计数 = int(time.time())
        用时 = 结束时间计数 - 开始时间计数
        print('易码短信:', 用时, '秒')

    def 模具一一易码短信平台账户信息(self):
        通信令牌token = '00285014c8a4ce850ee48bcfdd205a14751a49ed'

        令牌网址 = 'http://api.fxhyd.cn/UserInterface.aspx?action=getaccountinfo&token={}'.format(通信令牌token)  # 不换行 end=""

        网址内容 = self.模具一一打开的网址请求返回网页内容(令牌网址)
        账户信息 = 网址内容.text.replace("success|", "")  # 替换   , 1) 次数 1
        文本列表 = 账户信息.split("|")
        print('用户名:', 文本列表[0])
        print('账户状态:', 文本列表[1])
        print('账户等级:', 文本列表[2])
        print('账户余额:', 文本列表[3])
        print('冻结金额:', 文本列表[4])
        print('账户折扣:', 文本列表[5])
        print('获取号码最大数量:', 文本列表[6])
        print('=========================')

    def 模具一一获取接收的手机号码(self):
        self.通信令牌token = '00285014c8a4ce850ee48bcfdd205a14751a49ed'
        self.项目编号="891"
        排除号段=''
        获取手机号码接口网址 ="http://api.fxhyd.cn/UserInterface.aspx?action=getmobile&token={}&itemid={}&excludeno={}".format(self.通信令牌token,self.项目编号,排除号段)
        网址内容 = self.模具一一打开的网址请求返回网页内容(获取手机号码接口网址)

        self.手机号码 = 网址内容.text.replace("success|", "") #替换   , 1) 次数 1
        print('手机号码:', self.手机号码)



    def 模具一一获取短信(self):
        self.通信令牌token = '00285014c8a4ce850ee48bcfdd205a14751a49ed'
        self.项目编号 = "891"

        获取短信网址 = "http://api.fxhyd.cn/UserInterface.aspx?action=getsms&token={}&itemid={}&mobile={}".format(self.通信令牌token,
                                                                                                            self.项目编号, self.手机号码)
        """&release=1  自动释放号码标识符 若该参数值为1时,获取到短信的同时系统将自己释放该手机号码.若要继续使用该号码,请勿带入该参数."""

        for i in 'few':
            print('等待 10秒:')
            time.sleep(10)  # 等待

            网址内容 = self.模具一一打开的网址请求返回网页内容(获取短信网址)

            if 'success' in 网址内容.text:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                self.短信内容 = 网址内容.text.replace("success|", "")  # 替换   , 1) 次数 1
                print('短信内容:', self.短信内容)
                break  # 结束循环

            elif '3001' in 网址内容.text:  # 其它条件.
                print('短信尚未到达:3001,应继续调用取短信接口,直到超时为止.')

            else:  # 否则
                print('请求失败:', 网址内容.text)

        释放手机号码接口 = "http://api.fxhyd.cn/UserInterface.aspx?action=release&token={}&itemid={}&mobile={}".format(
            self.通信令牌token, self.项目编号, self.手机号码)
        释放手机号码网址内容 = self.模具一一打开的网址请求返回网页内容(释放手机号码接口)

    def 模具一一知乎短信内容清洗(self):
        规则 = '，.{1,}'
        文本 = re.sub(规则, '', self.短信内容)  # 替换   ,count=0,re.S|re.I
        规则 = '.{1,}是'
        文本 = re.sub(规则, '', 文本)  # 替换   ,count=0,re.S|re.I
        self.短信内容 = 文本.strip()  # 默认则是去除空格

    def 模具一一手机模式访问并注册知乎(self):
        头部信息="user - agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_5 like Mac OS X) AppleWebKit/612.1.60(KHTML, like Gecko) CriOS/66.0.2524.75 Mobile/15E5239e Safari/612.1'"

        #url = "http://www.sunchateau.com/free/UA.htm"#  浏览器UA头部信息 在线查询
        url = "https://www.zhihu.com/signin?next=https://www.zhihu.com/"
        #随机手机型号= random.choice(["iPhone 5","iPhone 6","iPhone 6 Plus","iPhone 7","iPhone 7 Plus","iPhone 8","iPhone 8 Plus","iPhone X"])

        随机手机型号 = random.choice(
            ["iPhone 5", "iPhone 6", "iPhone 6 Plus", "iPad Pro", "iPad"])

        随机手机型号 = "iPhone 6"
        print('随机手机型号', 随机手机型号)


        mobile_emulation = {"deviceName":随机手机型号}# 设置成手机模式
        options = Options()
        options = webdriver.ChromeOptions()  # 设置中文
        options.add_experimental_option("mobileEmulation",mobile_emulation)# 更改 浏览头部信息为手机模式
        #options.add_argument(头部信息)

        #options.add_argument('disable-infobars')# 加启动配置 去除正在受到自动软件的控制
        #options.add_argument('headless')  # 静默模式

        #prefs = {"profile.managed_default_content_settings.images": 2}#配置不加载图片
        #options.add_experimental_option("prefs", prefs)#配置不加载图片

        操作 = webdriver.Chrome(chrome_options=options) # 打开chrome浏览器
        #driver = webdriver.Chrome(chrome_options=options)

        # self.模具一一获取接收的手机号码()
        # self.手机号码='17131632268'


        操作.get(url)# 访问网址

        time.sleep(1000)  # 等待



        time.sleep(5)  # 等待
        # 操作.find_element_by_xpath("//*[@id=\"address\"]").send_keys(Keys.CONTROL,'DELETE') # 键盘按击或输入  请空输入框:clear()
        # 操作.find_element_by_xpath("//*[@id=\"address\"]").click()# 光标 点击.click()
        # 操作.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/header/div/div/div/a[2]").click()  # 光标 点击.click()



        #操作.find_element_by_name("username").send_keys(self.手机号码)  # 键盘按击或输入  请空输入框:clear()
        操作.find_element_by_xpath("//*[@id=\"root\"]/div/main/div/form/div[1]/div[1]/div[2]/div[1]/input").send_keys(self.手机号码)  # 键盘按击或输入  请空输入框:clear()
        time.sleep(1)  # 等待
        #操作.find_element_by_class_name("CountingDownButton").click() # 光标 点击.click()


        定位 = 操作.find_element_by_xpath('//*[@id="root"]/div/main/div/form/div[1]/div[2]/button')# 触摸事件 发送验证码 按扭
        TouchActions(操作).tap(定位).perform()
        time.sleep(1)  # 等待

        self.模具一一获取短信()
        self.模具一一知乎短信内容清洗()
        # self.短信内容='623516'
        操作.find_element_by_name("digits").send_keys(self.短信内容)  # 键盘按击或输入  请空输入框:clear()
        time.sleep(1)  # 等待

        定位 = 操作.find_element_by_xpath('//*[@id="root"]/div/main/div/form/button')  # 触摸事件 登录 按扭
        TouchActions(操作).tap(定位).perform()

        time.sleep(5)  # 等待

        保存cookie = [item["name"] + ":" + item["value"] for item in 操作.get_cookies()]
        print('保存cookie:\n',保存cookie)

        time.sleep(1000)  # 等待

        #操作.quit()  # 关闭浏览器

    def 模具一一浏览器访问并注册知乎(self):
        self.模具一一换头部信息()

        头部信息 = str(self.头部信息).replace("'User-Agent':", "user-agent=")  # 替换   , 1) 次数 1
        头部信息 = 头部信息.replace("{", "")  # 替换   , 1) 次数 1
        头部信息 = 头部信息.replace("}", "")  # 替换   , 1) 次数 1
        后缀='user-agent=Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'

        options = webdriver.ChromeOptions()  # 设置中文
        options = Options()
        options.add_argument('disable-infobars')  # 加启动配置 去除正在受到自动软件的控制
        print('头部信息:', 头部信息)
        print('后缀:', 后缀)
        options.add_argument(后缀)

        浏览器操作 = webdriver.Chrome(chrome_options=options)  # 打开chrome浏览器

        url = "http://www.zhihu.com"
        浏览器操作.get(url)
        time.sleep(500)  # 等待




类 = 类一一测试库()



