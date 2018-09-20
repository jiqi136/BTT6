# -*- coding:utf-8


import re  # 正则式
import time  # 时间

import os  # 本地操作
import pymysql  # 数据库
import random  # 随机

import shutil  # 移动复制文件目录

import win32api  # 操作本地文件
import win32clipboard as w# 提取剪切板内容
import win32con#提取剪切板内容


import pyautogui as pag #模拟鼠标键盘操作
import pyautogui#模拟鼠标键盘操作
from 发贴推广.推广公共库 import 类一一公共库# 导入模块

class 类一一发布微博(类一一公共库):  # 调用 类的模具 self.模具一一数据库()
    def __init__(self):
        self.新旧影视库= '最新影视剧'
        self.模具一一换头部信息()
        self.模具一一换ip连接二()
        self.模具一一重新激活浏览器窗口()
        self.模具一一提取影视剧数据库里的微博3e影视用户名与密码()
        self.用户名 =self.用户名密码组[0]
        self.密码 =self.用户名密码组[1]
        输入网址 = 'https://weibo.com'
        self.模具一一地址栏输入网址(输入网址)
        time.sleep(7)  # 等待  # 增加延迟



        self.模具一一输入帐号密码登录微博()

        time.sleep(15)  # 等待  # 增加延迟

        影视类列表=['动漫', '电视剧','电影']
        首次 = 0
        for 类型 in 影视类列表:

            self.影视类型 =类型
            self.模具一一读取内容数据库()
            if len(self.短标题集数组列表) == 0:
                continue  # 跳过当前循环，继续进行下一轮循环
            if 首次!=0:
                time.sleep(20)  # 等待  # 增加延迟

            类型合名=类型+'---更新：'
            for 剧名集数组 in self.短标题集数组列表:

                剧名 ='[{}]'.format(剧名集数组[0])
                集数 = 剧名集数组[1]
                if 剧名 in 类型合名:
                    continue  # 跳过当前循环，继续进行下一轮循环
                if '电影' in self.影视类型:
                    类型合名 = 类型合名 + 剧名 + '，'
                else:  # 否则
                    类型合名 = 类型合名 + 剧名 + ' ' + 集数 + '，'

            self.类型合名 = 类型合名.strip('，') # 去除最后一个 ，号  默认则是去除空格

            self.类型合名 = self.类型合名 +'。网址：3e38.com'

            self.模具一一发布微博()
            首次 = 998

        self.模具一一更新数据库里剧集发布状态()

    def 模具一一发布微博(self):
        pag.press('n')  # press()一次完整的击键.hotkey('ctrl','c') 弹出 发布微博 框
        time.sleep(2)  # 等待  # 增加延迟

        # =============输入类型微博
        pag.moveTo(555, 495)  # 鼠标移动X.Y   定位  发布微博  输入框
        pag.rightClick()  # 右击
        time.sleep(0.5)  # 等待  # 增加延迟

        self.模具一一写入剪切板内容(self.类型合名)

        pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.5)  # 等待  # 增加延迟


        # =============确认 发布

        pag.hotkey('ctrlleft', 'enter')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(2)  # 等待  # 增加延迟


    def 模具一一输入帐号密码登录微博(self):
        time.sleep(1)  # 等待  # 增加延迟
        #=============输入帐号
        pag.moveTo(1070, 260)  # 鼠标移动X.Y   定位  帐号 输入框
        pag.rightClick()  # 右击
        time.sleep(0.3)  # 等待  # 增加延迟

        self.模具一一写入剪切板内容(self.用户名)

        pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.3)  # 等待  # 增加延迟
        # =============输入密码
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.3)  # 等待  # 增加延迟
        self.模具一一写入剪切板内容(self.密码)
        pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.3)  # 等待  # 增加延迟
        # =============确认登录
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.3)  # 等待  # 增加延迟
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.3)  # 等待  # 增加延迟

        pag.press('enter')  # press()一次完整的击键.hotkey('ctrl','c') 确认
        time.sleep(2)  # 等待  # 增加延迟


    def 模具一一提取影视剧数据库里的微博3e影视用户名与密码(self):
        # 提取数据库里的过滤网址
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "", "帐号", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句
        sql = "SELECT `用户名`, `密码` FROM `3e影视网站` WHERE `网站`='微博3e影视' "
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        self.用户名密码组列表 = cursor.fetchall()
        self.用户名密码组 = self.用户名密码组列表[0]

        # 关闭数据库连接
        db.close()

    def 模具一一更新数据库里剧集发布状态(self):
        # 连接数据库
        # 连接数据库
        print('连接数据库....')
        db = pymysql.connect("localhost", "root", "", self.新旧影视库, charset="utf8")
        cursor = db.cursor()
        # SQL 查询语句   已下载内容网址
        # 获取游标
        sql = "UPDATE `网站文章内容` SET `发布`='是' WHERE `发布`='微博'"
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        # 关闭数据库连接
        db.close()
        print('更新数据库...成功.')
    def 模具一一读取内容数据库(self):
        # 连接数据库
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "",self.新旧影视库, charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句   已下载内容网址
        sql = "SELECT  `短标题`,`文章来源之更新集数` FROM `网站文章内容` WHERE `发布`='微博'  and `影视类型`=('%s') " % (
            self.影视类型)  # 不换行 end=""
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        self.短标题集数组列表 = cursor.fetchall()
        # 关闭数据库连接
        db.close()


类=类一一发布微博()
pyautogui.alert('完成发布微博')