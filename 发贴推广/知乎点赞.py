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
from 发贴推广.推广公共库 import 类一一公共库# 导入模块


"""
页面1  操作页面
页面2  导出COOKIE
页面3  设置浏览头部信息
页面4  清除 缓存
页面5  查询ip地址
"""

class 类一一知乎点赞(类一一公共库):  # 调用 类的模具 self.模具一一数据库()
    def __init__(self):
        self.模具一一换头部信息()
        self.模具一一提取推广库里的知乎点赞帐号()

        self.清除全部 = 998



        赞内容 = '拓展滴滴的新业务'
        self.ip段集=''
        for 帐号cookie组 in self.帐号cookie组列表:
            for 行内容 in str(帐号cookie组[5]).split("IP行"):
                if 赞内容 in 行内容:
                    规则='.{0,}'+赞内容
                    文本 =re.sub(规则, '', 行内容)#替换   ,count=0,re.S|re.I
                    self.ip段集 =self.ip段集+文本

            self.模具一一检测ip段重复()


        for 帐号cookie组 in self.帐号cookie组列表:

            self.帐号 = 帐号cookie组[0]
            self.密码 = 帐号cookie组[1]
            self.注册手机号 = 帐号cookie组[2]
            self.cookie = 帐号cookie组[3]
            存活 = 帐号cookie组[4]
            self.点赞内容 = str(帐号cookie组[5])


            if len(self.注册手机号)==0 or len(self.密码)==0 or '封' in str(存活) or 赞内容 in self.点赞内容:
                continue  # 跳过循环

            if 'zhihu.com' in str(帐号cookie组):
                continue  # 跳过循环            zhihu.com   Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 6.0; The World)
                self.模具一一布置浏览头()

                self.点赞内容 = 赞内容+self.前ip+'IP行'+self.点赞内容

                self.模具一一导入界面的登录cookie()
                self.模具一一测试登录页面属性(self.帐号)
            else:  # 否则
                self.点赞内容 = 赞内容 + self.前ip + 'IP行' + self.点赞内容
                self.模具一一布置浏览头()
                self.模具一一输入用户手机号与密码登录()
                self.模具一一测试登录页面属性(self.帐号)

            self.模具一一打开点赞页面并点击点赞()

            self.模具一一保存数据库一更新知乎登录cookie与点赞内容()

            self.模具一一等待7分钟()
            self.模具一一等待7分钟()
            self.模具一一重新激活浏览器窗口()

            self.模具一一清除浏览器历史缓存() # 1 次
            self.模具一一刷新知乎点赞页()
            self.模具一一清除浏览器历史缓存() # 2 次


            self.模具一一查看外网ip()

    def 模具一一检测ip段重复(self):
        条件循环 = 0
        while 条件循环 == 0:
            self.模具一一重新激活浏览器窗口()

            pag.hotkey('ctrlleft', '5')  # 鼠标移动X.Y 方位  cookie插件布置 页面
            time.sleep(1)  # 等待
            self.前ip = self.模具一一提取数字ip()
            self.前ip = str(self.前ip)
            print('self.前ip:', self.前ip)
            if self.前ip in self.ip段集:  # break # 结束循环 continue # 跳过当前循环，继续进行下一轮循环
                print('ip段重复,等待14分后继续:')
                self.模具一一等待7分钟()
                self.模具一一等待7分钟()

                self.模具一一换ip连接二()

            else:  # 否则

                条件循环 = 998

    def 模具一一查看外网ip(self):

        条件循环 = 0
        while 条件循环 == 0:


            pag.hotkey('ctrlleft', '5')  # 鼠标移动X.Y 方位  cookie插件布置 页面
            self.模具一一换ip连接二()

            pag.hotkey('ctrlleft', 'r')  # 刷新页面
            time.sleep(3)  # 等待         zhihu.com   Mozilla/5.0(Macintosh;IntelMacOSX10_8_0)AppleWebKit/883.3(KHTML,likeGecko)Chrome/78.0.1063.0Safari/536.3

            后ip=self.模具一一提取数字ip()
            后ip =str(后ip)

            print('后ip:', 后ip)
            


            if 后ip in self.前ip or 后ip in self.ip段集:
                print('ip段相同,等待7分后继续:')
                self.模具一一等待7分钟()
                # time.sleep(60)  # 等待
                self.模具一一重新激活浏览器窗口()

            else:  # 否则
                self.前ip= 后ip
                self.ip段集=后ip+self.ip段集
                条件循环 = 998


    def 模具一一等待7分钟(self):
        for 倒数 in range(7, 0, -1):  # 范围 range
            print('================')
            print('等待:', 倒数, '分后继续:')
            time.sleep(60)  # 等待


    def 模具一一页面内容(self):

        time.sleep(0.5)  # 等待  # 增加延迟
        pag.moveTo(950, 139)  # 鼠标移动X.Y 方位 页面定位
        pag.rightClick()  # 右击

        time.sleep(0.5)  # 等待  # 增加延迟
        pag.hotkey('ctrlleft', 'a')  # press()一次完整的击键.hotkey('ctrl','c'):复制内容

        time.sleep(0.5)  # 等待  # 增加延迟

        pag.hotkey('ctrlleft', 'c')  # press()一次完整的击键.hotkey('ctrl','c'):复制内容

        self.页面内容 = self.模具一一获取剪切板内容()

        #print('页面内容\n',self.页面内容)

    def 模具一一提取数字ip(self):
        self.模具一一页面内容()

        for 行内容 in self.页面内容.split("\n"):
            if '您现在的' in 行内容:
                IP行=行内容

                规则 = ".{1,}IP:"
                IP = re.sub(规则, '',IP行)

                规则 = ".{1,}IP："
                IP = re.sub(规则, '', IP行)

                IP = IP.strip()  # 默认则是去除空格

                # 提取 前面(去除最后一个符号后面字符)

                规则 = r'.{1,}(?=\..*)'  # .*(文本)  *号是贪婪的,放置在最前方会消耗尽可能多的字符.
                文本列表 = re.findall(规则, IP)  # 提取 前面
                IP文本 = 文本列表[0]

                return  IP文本# 返回






    def 模具一一刷新知乎点赞页(self):
        pag.hotkey('ctrlleft', '1')  # 鼠标移动X.Y 方位  cookie插件布置 页面
        pag.PAUSE = 1  # 增加延迟

        pag.hotkey('ctrlleft', 'r')  # 刷新页面
        pag.PAUSE = 3  # 增加延迟

    def 模具一一保存数据库一更新知乎登录cookie与点赞内容(self):
        print('打开数据库连接')
        # 打开数据库连接,
        db = pymysql.connect("localhost", "root", "", "影视发帖推广", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句
        if self.清除全部 == 0:
            self.模具一一提取登录界面的cookie()
            sql = """UPDATE `知乎帐号` SET `cookie`='{}',`点赞内容`='{}' WHERE `注册手机号`='{}'""".format(self.cookie,self.点赞内容,self.注册手机号)  # 不换行 '{}'
        else:  # 否则
            sql = """UPDATE `知乎帐号` SET `点赞内容`='{}' WHERE `注册手机号`='{}'""".format(self.点赞内容,self.注册手机号)  # 不换行 '{}'
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            print('=保存数据库一更新知乎与点赞内容')
        except:
            # 如果发生错误则回滚
            print('=====================数据库执行发生错误:===============')
            db.rollback()
        # 关闭数据库连接
        db.close()

    def 模具一一打开点赞页面并点击点赞(self):
        pag.PAUSE = 0.5  # 增加延迟
        pag.moveTo(530, 630)  # 鼠标移动X.Y 方位  回答内容 方框
        pag.rightClick()  # 右击
        pag.PAUSE = 0.3  # 增加延迟

        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')
        pag.PAUSE = 0.3  # 增加延迟
        #pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')
        #       zhihu.com   Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/830.24(KHTML,likeGecko)Chrome/21.0.1055.1Safari/535.24
        # pag.PAUSE = 0.3  # 增加延迟
        pag.press('enter')  # press()一次完整的击键.hotkey('ctrl','c') 赞同 按钮

        pag.PAUSE = 3  # 增加延迟

        # 等待用户输入 = input("\n按下 enter 确认键后继续")

        # self.模具一一重新激活浏览器窗口()
        pag.PAUSE = 0.5  # 增加延迟

    def 模具一一测试登录页面属性(self,登录用户名):

        pag.hotkey('ctrlleft', '1')  # 鼠标移动X.Y 方位  点赞 页面
        pag.PAUSE = 0.5  # 增加延迟
        pag.hotkey('ctrlleft', 'r')  # 刷新页面
        time.sleep(6)  # 等待
        for i in '1230':
            pag.PAUSE = 0.5  # 增加延迟
            pag.hotkey('ctrlleft', 'a')  # press()一次完整的击键.hotkey('ctrl','c'):复制内容
            # pag.mouseDown(x=498, y=336, button='right')  # 按下 选择的右键
            pag.PAUSE = 0.5  # 增加延迟
            # pag.moveTo(643, 396)  # 鼠标移动X.Y 方位
            pag.hotkey('ctrlleft', 'c')  # press()一次完整的击键.hotkey('ctrl','c'):复制内容
            # pag.mouseUp(x=589, y=336, button='right')#  松开 选择的右键
            页面属性 = self.模具一一获取剪切板内容()
            登录信息='提问'
            if 登录信息 in 页面属性 and '登录' not in 页面属性:
                print(登录用户名, '成功登录')
                return  # 返回
            else:  # 否则
                pag.hotkey('ctrlleft', 'r')  # 刷新页面

                # pag.moveTo(77, 46)  # 鼠标移动X.Y 方位  刷新页面
                # pag.rightClick()  # 右击pag.rightClick()
                time.sleep(6)  # 等待
        self.模具一一输入用户手机号与密码登录()
        pag.PAUSE = 0.5  # 增加延迟
        pag.moveTo(950, 91)  # 鼠标移动X.Y 方位  导入 按钮
        pag.rightClick()  # 右击

        pag.PAUSE = 0.5  # 增加延迟
        pag.moveTo(937, 153)  # 鼠标移动X.Y 方位  导入 按钮
        pag.rightClick()  # 右击

    def 模具一一输入用户手机号与密码登录(self):
        self.清除全部 = 0

        pag.hotkey('ctrlleft', '1')  # 鼠标移动X.Y 方位  点赞 页面
        time.sleep(0.5)  # 等待
        pag.moveTo(900, 120)  # 鼠标移动X.Y 方位 知乎登录顶页栏
        pag.rightClick()  # 右击
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.3)  # 等待
        pag.press('enter')  # press()一次完整的击键.hotkey('ctrl','c')   确认登录 按钮
        time.sleep(2)  # 等待

        """测试页面属性"""
        页面关键词 = '登录知乎'
        #self.模具一一测试页面属性(页面关键词)
        # ==========登录 方框

        # ====手机号
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')  输入手机方框
        time.sleep(0.3)  # 等待  # 增加延迟
        pag.typewrite(self.注册手机号)  # 输入手机号码

        # ====密码
        time.sleep(0.3)  #   等待  # 增加延迟
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')  输入密码方框
        time.sleep(0.3)  # 等待  # 增加延迟
        pag.typewrite(self.密码)  # 输入密码


        # ====确认登录


        pag.moveTo(651, 590)  # 鼠标移动X.Y 方位 知乎登录顶页栏
        pag.rightClick()  # 右击

        time.sleep(2)  # 等待



    def 模具一一提取推广库里的知乎点赞帐号(self):
        # 提取数据库里的过滤网址
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "", "影视发帖推广", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句
        sql = "SELECT  `帐号`, `密码`, `注册手机号`,`cookie` ,`存活`,`点赞内容` FROM `知乎帐号`"
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        self.帐号cookie组列表 = cursor.fetchall()

        # 关闭数据库连接
        db.close()

    def 模具一一导入界面的登录cookie(self):

        pag.hotkey('ctrlleft', '2')  # 鼠标移动X.Y 方位  cookie插件布置 页面

        time.sleep(0.5)  # 等待  # 增加延迟
        pag.moveTo(652, 120)  # 鼠标移动X.Y 方位  导入 按钮
        pag.rightClick()  # 右击

        time.sleep(0.3)  # 等待  # 增加延迟
        pag.moveTo(590, 210)  # 鼠标移动X.Y 方位  输入框 位置
        pag.rightClick()  # 右击

        self.模具一一写入剪切板内容(self.cookie)

        time.sleep(0.3)  # 等待  # 增加延迟
        pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c')

        time.sleep(0.3)  # 等待  # 增加延迟
        pag.moveTo(650, 630)  # 鼠标移动X.Y 方位  绿色勾选 按钮
        pag.rightClick()  # 右击


        #pag.hotkey('ctrlleft', 'F4')  # 确认  关闭当前标签页   按钮

    def 模具一一布置浏览头(self):

        pag.hotkey('ctrlleft', '3')  # 鼠标移动X.Y 方位  cookie插件布置 页面

        time.sleep(0.5)  # 等待  # 增加延迟
        pag.moveTo(600, 200)  # 鼠标移动X.Y 方位  确定布置浏览头 页面
        pag.rightClick()  # 右击
        time.sleep(0.3)  # 等待  # 增加延迟

        # pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')
        # pag.PAUSE = 0.3  # 增加延迟
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.3)  # 等待  # 增加延迟
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c') 添加浏览头网址 方框

        浏览头网址='zhihu.com'
        self.模具一一写入剪切板内容(浏览头网址)
        time.sleep(0.3)  # 等待  # 增加延迟
        pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c')

        #====================================
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')
        self.模具一一换头部信息()

        self.模具一一写入剪切板内容(self.头部信息['User-Agent'])
        time.sleep(0.3)  # 等待  # 增加延迟
        pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c')

        # ====================================
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')

        time.sleep(0.3)  # 等待  # 增加延迟
        pag.press('enter')  # press()一次完整的击键.hotkey('ctrl','c')

        # pag.hotkey('ctrlleft', 'F4')  # 确认  关闭当前标签页   按钮


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
        print('后缀:', 后缀)
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


if __name__ == '__main__':
    类 = 类一一知乎点赞()




