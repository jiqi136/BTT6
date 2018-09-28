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
import socket # 获取本机ip
from 发贴推广.推广公共库 import 类一一公共库# 导入模块




class 类一一注册知乎(类一一公共库):        # 调用 类的模具 self.模具一一数据库()
    def __init__(self,知乎发贴号):
        self.知乎发贴号 = 知乎发贴号
        self.模具一一高位换头部信息()
        self.模具一一换ip连接二()


        self.模具一一提取影视剧数据库里的易码短信平台账户信息()

        self.清除全部 =0
        知乎注册网址 = 'https://www.zhihu.com/signup?next=%2Fexplore'
        浏览头网址 = 'zhihu.com'


        计数器=0
        条件循环 = 1
        while 条件循环 == 1:  # 条件循环  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环

            计数器 =计数器+1
            if 计数器 >25:
                条件循环 = 998
            开始时间计数 = int(time.time())
            self.模具一一重新激活浏览器窗口()


            self.模具一一布置浏览头(浏览头网址)

            self.模具一一地址栏输入网址(知乎注册网址)

            self.模具一一输入手机号码并验证()

            self.模具一一输入短信内容并注册()

            if len(self.短信内容) != 0:
                self.临时图片目录 = r"F:\影视发帖推广\临时图片"
                self.旧目录路径 = r"F:\影视发帖推广\贴吧顶贴\头像\上传头像"
                self.模具一一清空临时图片目录()
                self.模具一一移动图片文件至临时图片目录()

                self.模具一一设置用户名与密码()

                self.模具一一选择职业或专业()

                self.模具一一点击选择关注话题()

                self.模具一一添加头像()


                self.模具一一提取登录界面的cookie()


                self.模具一一保存数据库一知乎用户密码等()


            self.模具一一清除浏览器历史缓存()

            # self.模具一一刷新知乎点赞页()

            # self.模具一一清除浏览器历史缓存()
            结束时间计数 = int(time.time())
            用时 = 结束时间计数 - 开始时间计数
            print('操作:', 用时, '秒')
            time.sleep(1)  # 等待
            self.模具一一换ip连接二()

            #pyautogui.alert('确认后继续')
            time.sleep(10)  # 等待  # 增加延迟



    def 模具一一输入手机号码并验证(self):

        self.模具一一获取接收的手机号码()
        if len(self.手机号码) <10:
            self.模具一一获取接收的手机号码()

        """测试页面属性"""
        页面关键词='注册知乎'
        self.模具一一测试页面属性(页面关键词)
        pag.moveTo(643, 380)  # 鼠标移动X.Y 方位
        pag.rightClick()  # 右击pag.rightClick() 左击pag.leftClick() 中击 pag.middleClick()
        time.sleep(0.3)  # 等待
        pag.typewrite(self.手机号码)  # 输入手机号码
        time.sleep(1)  # 等待


        pag.moveTo(775, 437)  # 鼠标移动X.Y 方位  发送验证码 按钮
        pag.rightClick()  # 右击pag.rightClick()
        time.sleep(0.3)  # 等待


        pag.moveTo(740, 456)  # 鼠标移动X.Y 方位  发送验证码 按钮
        #pag.rightClick()  # 右击pag.rightClick()

    def 模具一一输入短信内容并注册(self):
        self.开始计时数 = int(time.time())

        self.模具一一获取短信()
        self.模具一一重新激活浏览器窗口()
        if len(self.短信内容) == 0:
            return#返回

        规则 = '\d{6}'
        内容列表 = re.findall(规则, self.短信内容)  # 提取
        self.短信内容 = 内容列表[0]




        pag.moveTo(595, 450)  # 鼠标移动X.Y 方位  输入 短信内容 方框
        pag.rightClick()  # 右击
        time.sleep(0.5)  # 等待  # 增加延迟
        pag.typewrite(self.短信内容)  # 输入 短信内容

        time.sleep(0.5)  # 等待  # 增加延迟

        结束时数 = int(time.time())
        if 结束时数 > self.开始计时数 + 60:
            pag.moveTo(650, 536)  # 鼠标移动X.Y 方位 大于 60秒的 注册 按钮
        else:  # 否则
            pag.moveTo(650, 523)  # 鼠标移动X.Y 方位  60秒以内的 注册 按钮

        pag.rightClick()  # 右击

    def 模具一一设置用户名与密码(self):
        """设置用户名与密码"""

        """测试页面属性"""
        页面关键词 = '设置用户名和密码'
        self.模具一一测试页面属性(页面关键词)

        
        if self.知乎发贴号==0: #  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            self.随机取名=self.模具一一随机取女名()
        else:# 否则
            self.随机取名 =self.模具一一随机取名合并网址名()
            
            
        self.模具一一写入剪切板内容(self.随机取名)

        pag.moveTo(475, 280)  # 鼠标移动X.Y 方位 定位 设置用户名和密码 空白栏
        pag.rightClick()  # 右击
        time.sleep(0.5)  # 等待  # 增加延迟
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.3)  # 等待  # 增加延迟
        #======随机取名=======
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.3)  # 等待  # 增加延迟
        pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c'):

        # ======密码=======
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.3)  # 等待  # 增加延迟

        密码数字 = random.randrange(100000, 1000000)
        self.密码 = "qq{}Q%".format(密码数字)
        print('密码:', self.密码)
        # time.sleep(0.5)  # 等待  # 增加延迟
        #  pag.moveTo(518, 466)  # 鼠标移动X.Y 方位
        # pag.rightClick()  # 右击
        # time.sleep(0.5)  # 等待  # 增加延迟
        pag.typewrite(self.密码)  # 输入 密码

        # ======确认 注册======
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.3)  # 等待  # 增加延迟
        pag.press('enter')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.3)  # 等待  # 增加延迟

        # time.sleep(0.5)  # 等待  # 增加延迟
        # pag.moveTo(621, 532)  # 鼠标移动X.Y 方位  进入知乎 按钮
        # pag.rightClick()  # 右击

    def 模具一一选择职业或专业(self):
        """你的职业或专业是什么?"""
        time.sleep(2)  # 等待  # 增加延迟

        """测试页面属性"""
        页面关键词 = '职业或专业'
        self.模具一一测试页面属性(页面关键词)

        print('选择职业或专业')
        
        职业名 = self.模具一一随机职业名()
        self.模具一一写入剪切板内容(职业名)

        
        
        pag.moveTo(612, 273)  # 鼠标移动X.Y 方位
        pag.rightClick()  # 右击
        time.sleep(0.5)  # 等待  # 增加延迟
        pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c'):



        time.sleep(0.5)  # 等待  # 增加延迟
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

        time.sleep(0.5)  # 等待  # 增加延迟
        pag.moveTo(655, 836)  # 鼠标移动X.Y 方位  进入知乎 按钮
        pag.rightClick()  # 右击

    def 模具一一添加头像(self):
        """测试页面属性"""
        # ========发现界面===========
        页面关键词 = '消息'
        self.模具一一测试页面属性(页面关键词)

        time.sleep(0.5)  # 等待  # 增加延迟
        pag.moveTo(1076, 120)  # 鼠标移动X.Y 方位  用户主页界面 按钮
        pag.rightClick()  # 右击
        time.sleep(1)  # 等待  # 增加延迟

        #========用户主页===========
        页面关键词 = '编辑个人资料'
        self.模具一一测试页面属性(页面关键词)



        time.sleep(0.5)  # 等待  # 增加延迟
        pag.moveTo(250, 300)  # 鼠标移动X.Y 方位  上传图记头像 按钮
        pag.rightClick()  # 右击
        time.sleep(3)  # 等待  # 增加延迟

        self.模具一一图片目录地址框()


        self.模具一一上传图片窗口选择图片()

        pag.moveTo(655, 705)  # 鼠标移动X.Y 方位  定位 保存  按钮
        pag.rightClick()  # 右击
        time.sleep(1)  # 等待  # 增加延迟


    def 模具一一保存数据库一知乎用户密码等(self):
        print('打开数据库连接')
        # 打开数据库连接,
        今天时间 = str(time.strftime("%y-%m-%d", time.localtime()))

        db = pymysql.connect("localhost", "root", "", "影视发帖推广", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句
        if self.知乎发贴号 == 0:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            sql = """INSERT INTO `知乎帐号`(`帐号`, `密码`, `注册手机号`, `注册日期`, `cookie`) 
                  VALUES ("{}","{}","{}","{}",'{}')""".format(self.随机取名, self.密码, self.手机号码, 今天时间,
                                                              self.cookie)  # 不换行 end=""
        else:  # 否则
            sql = """INSERT INTO `知乎发贴帐号`(`帐号`, `密码`, `注册手机号`, `注册日期`, `cookie`) 
                  VALUES ("{}","{}","{}","{}",'{}')""".format(self.随机取名, self.密码, self.手机号码, 今天时间,
                                                              self.cookie)  # 不换行 end=""



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
    知乎发贴号 = 998
    知乎发贴号 = 0

    类 = 类一一注册知乎(知乎发贴号)



