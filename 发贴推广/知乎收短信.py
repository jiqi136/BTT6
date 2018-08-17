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
import 发贴推广.推广公共库  # 导入模块


class 类一一收短信(发贴推广.推广公共库.类一一公共库):  # 调用 类的模具 self.模具一一数据库()
    def __init__(self):
        self.模具一一换头部信息()
        开始时间计数 = int(time.time())

        # self.模具一一易码短信平台()
        # self.模具一一浏览器访问并注册知乎()
        self.模具一一鼠标操作浏览器()

        结束时间计数 = int(time.time())
        用时 = 结束时间计数 - 开始时间计数
        print('操作:', 用时, '秒')
        print('等待5000秒:')
        time.sleep(5000) # 等待



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
        pag.PAUSE = 2  # 增加延迟
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

    def 模具一一提取登录界面的cookie(self):
        pag.PAUSE = 1  # 增加延迟
        pag.moveTo(1197, 45)  # 鼠标移动X.Y 方位  cookie插件激活 按钮
        pag.rightClick()  # 右击

        pag.PAUSE = 0.5  # 增加延迟
        pag.moveTo(999, 91)  # 鼠标移动X.Y 方位  导出到剪切板 按钮
        pag.rightClick()  # 右击

        self.cookie =self.模具一一获取剪切板内容()
        print(self.cookie)

        pag.PAUSE = 0.5  # 增加延迟
        pag.moveTo(682, 91)  # 鼠标移动X.Y 方位  清除全部cookie    按钮
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






    def 模具一一鼠标操作浏览器(self):  # VK_CODE为键盘encoding='UTF-8'
        # @Keyboard

        条件循环 = 1
        while 条件循环 == 1:  # 条件循环  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            self.模具一一重新激活浏览器窗口()

            self.模具一一输入手机号码并验证()

            self.模具一一输入短信内容并注册()

            if len(self.短信内容) !=0:
                self.模具一一设置用户名与密码()

                self.模具一一选择职业或专业()

                self.模具一一点击选择关注话题()


                self.模具一一提取登录界面的cookie()

                self.模具一一保存数据库一知乎用户密码等()

            self.模具一一清除浏览器历史缓存()
            time.sleep(1) # 等待


类 = 类一一收短信()



