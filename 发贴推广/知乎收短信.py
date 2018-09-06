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
import win32clipboard as w# 提取剪切板内容
import win32con#提取剪切板内容
from selenium import webdriver  # 浏览的驱动
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui as pag
import pyautogui
import json #json格式化


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
                              {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 随机1位数.0; Windows NT 6.1)'},
                              {
                                  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/随机3位数.11 (KHTML, like Gecko) Chrome/随机2位数.0.963.56 Safari/535.11'},
                              {
                                  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/201随机3位数01 Firefox/随机2位数.0.1'},
                              {
                                  'User-Agent': 'Mozilla/4.0 (compatible; MSIE 随机1位数.0; Windows NT 5.1; Trident/随机2位数.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.随机2位数727; SE 2.X MetaSr 1.0)'},
                              {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 随机1位数.0; Windows NT 6.0; The World)'},
                              {
                                  'User-Agent': 'Mozilla/4.0 (compatible; MSIE 随机1位数.0; Windows NT 6.2; TencentTraveler 4.0)'},
                              {
                                  'User-Agent': 'Mozilla/4.0 (compatible; MSIE 随机1位数.0; Windows NT 6.1; Maxthon 2.0)'},
                              {
                                  'User-Agent': 'Mozilla/4.0 (compatible; MSIE 随机1位数.0; Windows NT 6.2; Avant Browser)'},
                              {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 随机1位数.0; Windows NT 6.0; 360SE)'},
                              {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 随机1位数.0; Windows NT 6.1)'},
                              {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 随机1位数.0; Windows NT 10.1)'}
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
    def 模具一一换ip连接二(self):
        # coding:gbk
        循环 = 0
        次数循环 = 0

        while 循环 == 0:  # 条件循环  post
            print('宽带连接进行时.....')
            os.system(r"rasphone -h 宽带连接")  # xxx0是你的拨号名称,xp下默认是"宽带连接”.
            os.system(r"rasdial 宽带连接 02007044432@163.gd  77341859")  # xxx0同上,xxx1 拨号用户名 ,xxx2拨号密码.
            time.sleep(3)
            print('换ip再连接完成')

            try:
                返回网页内容 = requests.post('https://www.baidu.com/', headers=头部信息, timeout=3)
            except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout,
                    requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout,
                    requests.exceptions.ChunkedEncodingError, requests.exceptions.InvalidSchema) as 异常:
                次数循环 += 1
                print('网络异常等待', 异常)
                print('倒数60秒再连接', 次数循环, '次')
                time.sleep(60)
                if 'None, 10053,' in str(异常):
                    pass
            else:
                if '200' in str(返回网页内容):
                    break  # 结束循环
                else:
                    print('网站网络异常,状态码:', 返回网页内容)
                    print('等待60秒')
                    time.sleep(60)

    """============短信平台================"""

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
        self.项目编号 = "891"
        排除号段 = ''
        获取手机号码接口网址 = "http://api.fxhyd.cn/UserInterface.aspx?action=getmobile&token={}&itemid={}&excludeno={}".format(
            self.通信令牌token, self.项目编号, 排除号段)
        网址内容 = self.模具一一打开的网址请求返回网页内容(获取手机号码接口网址)

        self.手机号码 = 网址内容.text.replace("success|", "")  # 替换   , 1) 次数 1
        print('手机号码:', self.手机号码)

    def 模具一一获取短信(self):

        pag.hotkey('altleft', 'tab')  # press()一次完整的击键.hotkey('ctrl','c'):热键函数 .keyDown()按下某个键.keyUp()松开某个键.


        self.通信令牌token = '00285014c8a4ce850ee48bcfdd205a14751a49ed'
        self.项目编号 = "891"

        获取短信网址 = "http://api.fxhyd.cn/UserInterface.aspx?action=getsms&token={}&itemid={}&mobile={}".format(
            self.通信令牌token,
            self.项目编号, self.手机号码)
        """&release=1  自动释放号码标识符 若该参数值为1时,获取到短信的同时系统将自己释放该手机号码.若要继续使用该号码,请勿带入该参数."""


        条件循环 =0
        while 条件循环 < 3:  # 条件循环  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            self.短信内容 = ''

            for i in 'few52676t':
                print('等待 15秒:')
                time.sleep(14)  # 等待
                网址内容 = self.模具一一打开的网址请求返回网页内容(获取短信网址)
                if 'success' in 网址内容.text:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                    self.短信内容 = 网址内容.text.replace("success|", "")  # 替换   , 1) 次数 1
                    print('短信内容:', self.短信内容)
                    条件循环 = 998

                    return#返回
                elif '3001' in 网址内容.text:  # 其它条件.
                    print('短信尚未到达:3001,应继续调用取短信接口,直到超时为止.')

                else:  # 否则
                    print('请求失败:', 网址内容.text)
            条件循环 =条件循环+1
            self.模具一一重新激活浏览器窗口()
            pag.PAUSE = 5  # 增加延迟
            pag.moveTo(740, 456)  # 鼠标移动X.Y 方位  发送验证码 按钮
            pag.rightClick()  # 右击pag.rightClick()
            self.开始计时数 = int(time.time())



        释放手机号码接口 = "http://api.fxhyd.cn/UserInterface.aspx?action=release&token={}&itemid={}&mobile={}".format(
            self.通信令牌token, self.项目编号, self.手机号码)
        释放手机号码网址内容 = self.模具一一打开的网址请求返回网页内容(释放手机号码接口)

    """===========共用库================"""

    def 模具一一启动浏览器Chrome68(self):
        win32api.ShellExecute(0, 'open', r'E:\Ean\Google Chrome68\Chrome.exe', '', '', 1)  # 主页已经设置为 注册知乎页

        time.sleep(8)



    def 模具一一随机取女名(self):
        内容 = """柔蓉安蓝春语彤晴语菱霜紫莲翠烟南寻慕蕊雪海沛宛晓菡巧
        听卉靖枫梓晨丽丹佩惠月玉婉晓玲倩瑞静颖棋芹萍幻露灵含雅薇瑶丹丽云亿仪伊伶佳依俞俪倩偲兰冰凝凡凤叆呤
        爱姿惠娇媛妩萱娈瑷悠源赫晗贻楚梦琪忆柳桃慕兰岚香沛菡珊曼菱寒薇忆旋芷蕾代
        芙盼蝶筠瑶珍谷荷画嘉囡女如妃妍妙妮妹姐姑姗姝姞姣梅梦楠檀欢欣歆毓水洁涵淑清滟滢漪漫澜灵煜燕
        玉玥玫环玲珂珊珍珠姬娅娆娇娉娜娟娣娥娴婉婕婧婵婷媚媛嫔嫣嫱安宛宜宝容巧希彤彩心忆念怀怜思怡情惠
        慧敏旭春晴曼月琦琪琬琰琳琴琼瑗瑛瑜瑶瑾璇璐璟白盈盼碧秀筠红绮美翠艳芃芊芝芬芮芯芳芷芸苑若苹茗茜茵茹荔荭
        荷莉莎莲莹菁菡菲萍萱蓉蓓蔓蕊蕾薇诗语贞采钰银雅雨雪雯霏霖霜霞露青靖静音韵颖颜香馨黛"""

        内容 = 内容.replace("\n", "")
        内容 = 内容.replace(" ", "")
        合名 = ''

        随机取名个位数 = int(random.choice('55667'))
        for 字符 in range(1, 随机取名个位数):  # 范围 range
            名 = random.choice(内容)
            合名 = 合名 + 名




        self.取女名=合名
        self.模具一一写入剪切板内容(self.取女名)
        print('随机取女名', self.取女名)

    def 模具一一随机职业名(self):

        职业列表=['作者','作家','资料登录员','壮工','主管','主编','钟表匠','置景工','职员','执行官',
              '园丁','宇航员','渔夫','油漆匠','邮政工人','银行经理','银行出纳员','医生','业务经理','药剂师','演员',
              '学生','心理学者','鞋店鞋匠','小学生','消防人员','洗碗机','舞蹈演员','维修工程师','外科医生','土木工程师',
              '屠宰商','小贩','统计员','速记打字员','私人司机','司仪','司机','水手长','水手','水管工人','兽医','售货员','收票员','摄影师',
              '摄影记者','上班一族','仆人','女演员','女侍者','服务生','女仆','内科医师助理','内科医师','奶妈','牧羊人','牧师','木匠',
              '模特儿','面包师','秘书','美容师','律师','旅行团的服务员','旅行社','临时照顾幼儿者','理发师','老师','垃圾清洁工','矿工',
              '客机服务员','科学家','看管者','卡车司机','酒店业主','酒吧招待','酒吧侍者','精神病医师','节目主持人','接待员','教授','技师','记者',
              '计划员','计程车司机','机械工','机车司机','会计','换工住宿的女孩','护士','航海家','行政助理','行李管理者','焊接工','海员','雇员',
              '顾问','公交司机','工程师','歌手','副驾驶员','服务员','飞行员','房地产经纪人','翻译者','发型师','发报员','儿科医师','店员',
              '电影制片人','电台的音乐节目主持人','电工','导演','导师','档案管理者','大厨','打扫房屋者','船长','厨师','出租车司机',
              '产科医师','叉式升降机操作员','测量技师','餐厅侍者助手','餐馆老板','裁缝师','宝石商']
        职业名 = random.choice(职业列表)
        print('职业名', 职业名)
        self.模具一一写入剪切板内容(职业名)



    def 模具一一获取剪切板内容(self):# 获取剪切板内容
        w.OpenClipboard()
        t = w.GetClipboardData(win32con.CF_TEXT)
        w.CloseClipboard()

        t = t.decode('gbk')  # 解码为 编程的中文

        return t


    def 模具一一写入剪切板内容(self,内容): # 写入剪切板内容
        内容 = str(内容).encode('gbk')  # encoding='UTF-8'为 WIN7 系统 的中文
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_TEXT, 内容)
        w.CloseClipboard()

    def 模具一一提取登录界面的cookie(self):
        cookie=''

        pag.hotkey('ctrlleft', '2')  # 鼠标移动X.Y 方位  cookie插件布置 页面
        pag.PAUSE = 1  # 增加延迟
        if self.清除全部 == 0:


            pag.moveTo(736, 113)  # 鼠标移动X.Y 方位  导出到剪切板 按钮
            pag.rightClick()  # 右击


            pag.PAUSE = 2  # 增加延迟
            self.cookie =self.模具一一获取剪切板内容()
            # self.cookie = json.loads(self.cookie)  # 解码为字符串
            # print('cookie\n', cookie)
            self.cookie = json.dumps(self.cookie,indent =4)  # 编码为json
            # self.cookie = str(self.cookie).replace("'", '单号')  # 替换   , 1) 次数 1

            print('cookie2\n',self.cookie)

        pag.PAUSE = 0.5  # 增加延迟
        pag.moveTo(418, 120)  # 鼠标移动X.Y 方位  清除全部cookie    按钮
        pag.rightClick()  # 右击


    def 模具一一测试页面属性(self,页面关键词):
        time.sleep(3)  # 等待

        for i in '123':
            pag.PAUSE = 0.5  # 增加延迟
            pag.hotkey('ctrlleft', 'a')  # press()一次完整的击键.hotkey('ctrl','c'):复制内容
            # pag.mouseDown(x=498, y=336, button='right')  # 按下 选择的右键
            pag.PAUSE = 0.5  # 增加延迟
            # pag.moveTo(643, 396)  # 鼠标移动X.Y 方位
            pag.hotkey('ctrlleft', 'c')  # press()一次完整的击键.hotkey('ctrl','c'):复制内容
            # pag.mouseUp(x=589, y=336, button='right')#  松开 选择的右键
            页面属性 = self.模具一一获取剪切板内容()
            if 页面关键词 in 页面属性:
                print('通过', 页面关键词, '页面')
                return  # 返回
            else:  # 否则
                time.sleep(10)  # 等待

        pag.hotkey('ctrlleft', 'r')  # 刷新页面
        pag.PAUSE = 2  # 增加延迟
        # pag.moveTo(77, 46)  # 鼠标移动X.Y 方位  刷新页面
        # pag.rightClick()  # 右击pag.rightClick()

        self.模具一一测试页面属性(页面关键词)

    """==========电脑操作==============="""

    def 模具一一清除浏览器历史缓存(self):
        print('清除浏览器历史缓存')

        pag.hotkey('ctrlleft', '4')  # 鼠标移动X.Y 方位  cookie插件布置 页面
        pag.PAUSE = 0.5  # 增加延迟
        pag.moveTo(90, 82)  # 鼠标移动X.Y 方位  清除历史缓存 按钮
        pag.rightClick()  # 右击

        pag.PAUSE = 4  # 增加延迟 等待清除新窗口
        pag.moveTo(850, 720)  # 鼠标移动X.Y 方位  清除浏览历史书签 按钮
        pag.rightClick()  # 右击
        time.sleep(1)


    def 模具一一重新激活浏览器窗口(self):
        print('重新激活浏览器窗口')
        pag.hotkey('winleft', 'd')  # press()一次完整的击键.hotkey('ctrl','c'):热键函数 .keyDown()按下某个键.keyUp()松开某个键.

        pag.PAUSE = 0.5  # 增加延迟
        pag.moveTo(258, 962)  # 鼠标移动X.Y 方位  重新激活浏览器窗口 在CMD 与  回归桌面之间
        pag.rightClick()  # 右击





    """============旧模具================"""

    def 模具一一手机模式访问并注册知乎(self):
        头部信息 = "user - agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_5 like Mac OS X) AppleWebKit/612.1.60(KHTML, like Gecko) CriOS/66.0.2524.75 Mobile/15E5239e Safari/612.1'"

        # url = "http://www.sunchateau.com/free/UA.htm"#  浏览器UA头部信息 在线查询
        url = "https://www.zhihu.com/signin?next=https://www.zhihu.com/"
        # 随机手机型号= random.choice(["iPhone 5","iPhone 6","iPhone 6 Plus","iPhone 7","iPhone 7 Plus","iPhone 8","iPhone 8 Plus","iPhone X"])

        随机手机型号 = random.choice(
            ["iPhone 5", "iPhone 6", "iPhone 6 Plus", "iPad Pro", "iPad"])

        随机手机型号 = "iPhone 6"
        print('随机手机型号', 随机手机型号)

        mobile_emulation = {"deviceName": 随机手机型号}  # 设置成手机模式
        options = Options()
        options = webdriver.ChromeOptions()  # 设置中文
        options.add_experimental_option("mobileEmulation", mobile_emulation)  # 更改 浏览头部信息为手机模式
        # options.add_argument(头部信息)

        # options.add_argument('disable-infobars')# 加启动配置 去除正在受到自动软件的控制
        # options.add_argument('headless')  # 静默模式

        # prefs = {"profile.managed_default_content_settings.images": 2}#配置不加载图片
        # options.add_experimental_option("prefs", prefs)#配置不加载图片

        操作 = webdriver.Chrome(chrome_options=options)  # 打开chrome浏览器
        # driver = webdriver.Chrome(chrome_options=options)

        # self.模具一一获取接收的手机号码()
        # self.手机号码='17131632268'

        操作.get(url)  # 访问网址

        time.sleep(1000)  # 等待

        time.sleep(5)  # 等待
        # 操作.find_element_by_xpath("//*[@id=\"address\"]").send_keys(Keys.CONTROL,'DELETE') # 键盘按击或输入  请空输入框:clear()
        # 操作.find_element_by_xpath("//*[@id=\"address\"]").click()# 光标 点击.click()
        # 操作.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/header/div/div/div/a[2]").click()  # 光标 点击.click()

        # 操作.find_element_by_name("username").send_keys(self.手机号码)  # 键盘按击或输入  请空输入框:clear()
        操作.find_element_by_xpath("//*[@id=\"root\"]/div/main/div/form/div[1]/div[1]/div[2]/div[1]/input").send_keys(
            self.手机号码)  # 键盘按击或输入  请空输入框:clear()
        time.sleep(1)  # 等待
        # 操作.find_element_by_class_name("CountingDownButton").click() # 光标 点击.click()

        定位 = 操作.find_element_by_xpath('//*[@id="root"]/div/main/div/form/div[1]/div[2]/button')  # 触摸事件 发送验证码 按扭
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
        print('保存cookie:\n', 保存cookie)

        time.sleep(1000)  # 等待

        # 操作.quit()  # 关闭浏览器U

    def 模具一一浏览器访问并注册知乎(self):
        self.模具一一换头部信息()

        头部信息 = str(self.头部信息).replace("'User-Agent':", "user-agent=")  # 替换   , 1) 次数 1
        头部信息 = 头部信息.replace("{", "")  # 替换   , 1) 次数 1
        头部信息 = 头部信息.replace("}", "")  # 替换   , 1) 次数 1
        后缀 = 'user-agent=Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'

        options = webdriver.ChromeOptions()  # 设置中文
        # options = Options()
        options.add_argument('disable-infobars')  # 加启动配置 去除正在受到自动软件的控制
        print('头部信息:', 头部信息)
        print('后缀:', 后缀)
        options.add_argument(后缀)

        浏览器操作 = webdriver.Chrome(chrome_options=options)  # 打开chrome浏览器

        url = "https://www.zhihu.com"  # 注册页面  https://www.zhihu.com/signup?next=%2Fexplore
        浏览器操作.get(url)
        time.sleep(500)  # 等待


class 类一一注册知乎(类一一公共库):        # 调用 类的模具 self.模具一一数据库()
    def __init__(self):
        self.模具一一换头部信息()
        time.sleep(10000)  # 等待
        self.清除全部 =0
        条件循环 = 1
        while 条件循环 == 1:  # 条件循环  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            开始时间计数 = int(time.time())
            self.模具一一重新激活浏览器窗口()

            self.模具一一输入手机号码并验证()

            self.模具一一输入短信内容并注册()

            if len(self.短信内容) != 0:
                self.模具一一设置用户名与密码()

                self.模具一一选择职业或专业()

                self.模具一一点击选择关注话题()

                self.cookie=self.模具一一提取登录界面的cookie()

                self.模具一一保存数据库一知乎用户密码等()

            self.模具一一清除浏览器历史缓存()
            self.模具一一重新打开注册知乎标签页()
            结束时间计数 = int(time.time())
            用时 = 结束时间计数 - 开始时间计数
            print('操作:', 用时, '秒')
            time.sleep(1)  # 等待

    def 模具一一重新打开注册知乎标签页(self):
        pag.moveTo(200, 78)  # 鼠标移动X.Y 方位  注册知乎标签页 按钮
        pag.rightClick()  # 右击
        time.sleep(2)

    def 模具一一输入手机号码并验证(self):

        self.模具一一获取接收的手机号码()
        if len(self.手机号码) <10:
            self.模具一一获取接收的手机号码()

        """测试页面属性"""
        页面关键词='注册知乎'
        self.模具一一测试页面属性(页面关键词)
        pag.moveTo(643, 396)  # 鼠标移动X.Y 方位
        pag.rightClick()  # 右击pag.rightClick() 左击pag.leftClick() 中击 pag.middleClick()
        pag.typewrite(self.手机号码)  # 输入手机号码

        pag.PAUSE = 1.5  # 增加延迟
        pag.moveTo(740, 456)  # 鼠标移动X.Y 方位  发送验证码 按钮
        pag.rightClick()  # 右击pag.rightClick()

        pag.PAUSE = 1.5  # 增加延迟
        pag.moveTo(740, 456)  # 鼠标移动X.Y 方位  发送验证码 按钮
        pag.rightClick()  # 右击pag.rightClick()

    def 模具一一输入短信内容并注册(self):
        self.开始计时数 = int(time.time())

        self.模具一一获取短信()
        self.模具一一重新激活浏览器窗口()
        if len(self.短信内容) == 0:
            return#返回

        规则 = '\d{6}'
        内容列表 = re.findall(规则, self.短信内容)  # 提取
        self.短信内容 = 内容列表[0]


        结束时数 = int(time.time())
        if 结束时数 > self.开始计时数 + 60:
            pag.moveTo(627, 557)  # 鼠标移动X.Y 方位 大于 60秒的 注册 按钮
        else:  #否则
            pag.moveTo(596, 450)  # 鼠标移动X.Y 方位  60秒以内的 注册 按钮
        pag.rightClick()  # 右击
        pag.PAUSE = 0.5  # 增加延迟
        pag.typewrite(self.短信内容)  # 输入 短信内容

        pag.PAUSE = 0.5  # 增加延迟
        pag.moveTo(626, 539)  # 鼠标移动X.Y 方位  注册 按钮
        pag.rightClick()  # 右击

    def 模具一一设置用户名与密码(self):
        """设置用户名与密码"""

        """测试页面属性"""
        页面关键词 = '设置用户名和密码'
        self.模具一一测试页面属性(页面关键词)


        self.模具一一随机取女名()
        pag.moveTo(538, 403)  # 鼠标移动X.Y 方位
        pag.rightClick()  # 右击
        pag.PAUSE = 0.5  # 增加延迟
        pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c'):



        密码数字 = random.randrange(100000, 1000000)
        self.密码 = "qq{}Q%".format(密码数字)
        print('密码:', self.密码)
        pag.PAUSE = 0.5  # 增加延迟
        pag.moveTo(518, 466)  # 鼠标移动X.Y 方位
        pag.rightClick()  # 右击
        pag.PAUSE = 0.5  # 增加延迟
        pag.typewrite(self.密码)  # 输入 密码



        pag.PAUSE = 0.5  # 增加延迟
        pag.moveTo(621, 532)  # 鼠标移动X.Y 方位  进入知乎 按钮
        pag.rightClick()  # 右击

    def 模具一一选择职业或专业(self):
        """你的职业或专业是什么?"""
        pag.PAUSE = 2 # 增加延迟

        """测试页面属性"""
        页面关键词 = '职业或专业'
        self.模具一一测试页面属性(页面关键词)

        print('选择职业或专业')
        self.模具一一随机职业名()


        pag.moveTo(612, 273)  # 鼠标移动X.Y 方位
        pag.rightClick()  # 右击
        pag.PAUSE = 0.5  # 增加延迟
        pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c'):



        pag.PAUSE = 0.5  # 增加延迟
        pag.moveTo(812, 273)  # 鼠标移动X.Y 方位  完成 按钮
        pag.rightClick()  # 右击

    def 模具一一点击选择关注话题(self):
        """测试页面属性"""
        页面关键词 = '关注哪些话题'
        self.模具一一测试页面属性(页面关键词)
        """你想关注哪些话题?"""
        话题方位组列表 = [(256, 305), (432, 326), (620,326), (800, 326), (991,326),
                   (256, 522), (432, 522), (620, 522), (800, 522), (991,522),
                   (256, 696), (432, 696), (620, 696), (800, 696), (991,696,)]

        话题方位组 = random.choice(话题方位组列表)
        pag.moveTo(话题方位组[0], 话题方位组[1])  # 鼠标移动X.Y 方位  完成 按钮
        pag.rightClick()  # 右击

        pag.PAUSE = 0.5  # 增加延迟
        pag.moveTo(632, 877)  # 鼠标移动X.Y 方位  进入知乎 按钮
        pag.rightClick()  # 右击


    def 模具一一保存数据库一知乎用户密码等(self):
        print('打开数据库连接')
        # 打开数据库连接,
        今天时间 = str(time.strftime("%y-%m-%d", time.localtime()))

        db = pymysql.connect("localhost", "root", "", "影视发帖推广", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句
        sql = """INSERT INTO `知乎帐号`(`帐号`, `密码`, `注册手机号`, `注册日期`, `cookie`) 
        VALUES ("{}","{}","{}","{}",'{}')""" .format(self.取女名,self.密码,self.手机号码,今天时间,self.cookie)#不换行 end=""

        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            print('=保存数据库一知乎用户密码')
        except:
            # 如果发生错误则回滚
            print('=====================数据库执行发生错误:===============')
            db.rollback()
        # 关闭数据库连接
        db.close()


if __name__ == '__main__':
    类 = 类一一注册知乎()



