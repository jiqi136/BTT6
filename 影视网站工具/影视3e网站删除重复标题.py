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

class 类一一38影视网站(类一一公共库):  # 调用 类的模具 self.模具一一数据库()
    def __init__(self):
        self.颜色变化=''
        self.激活窗口坐标 = [196, 918]
        self.模具一一图像对比激活窗口()
        输入网址 = 'http://3e38.com/image/article_test_same.php?dopost=analyse&channelid=17&deltype=delold&pagesize=10000&Submit=%E5%88%86%E6%9E%90%E6%A0%87%E9%A2%98%E9%87%8D%E5%A4%8D%E7%9A%84%E6%96%87%E6%A1%A3'
        self.模具一一地址栏输入网址(输入网址)

        self.模具一一提取影视剧数据库里的3e影视网站后台登录cookie()
        self.帐号 = self.用户名密码完全版cookie组[0]
        self.密码 = self.用户名密码完全版cookie组[1]
        self.完全版cookie = self.用户名密码完全版cookie组[2]
        self.cookie = self.完全版cookie

        time.sleep(2)  # 等待  # 增加延迟

        #===网页加载 ，颜色对比
        self.坐标 =[538,445]
        self.颜色像素 =[ 96,167,1]
        self.等待秒数 =3
        self.模具一一网页加载颜色对比()
        print(' 登录界面 页面 ，颜色检测通过')
        # ===


        self.模具一一导入界面的登录cookie(self.帐号)

        删除重复标题网址 = 'http://3e38.com/image/article_test_same.php?dopost=analyse&channelid=17&deltype=delold&pagesize=10000&Submit=%E5%88%86%E6%9E%90%E6%A0%87%E9%A2%98%E9%87%8D%E5%A4%8D%E7%9A%84%E6%96%87%E6%A1%A3'
        self.模具一一地址栏输入网址(删除重复标题网址)

        #等待用户输入 = input("\n按下 enter 确认键后继续")
        # ===网页加载 ，颜色对比
        self.坐标 = [692, 116]
        self.颜色像素 = [237,249,213]
        self.等待秒数 = 3
        self.模具一一网页加载颜色对比()
        print(' 删除重复标题 页面 ，颜色检测通过')
        # ==

        self.模具一一删除重复标题()


        更新主页网址 = 'http://3e38.com/image/makehtml_homepage.php'
        self.模具一一地址栏输入网址(更新主页网址)


        # ===网页加载 ，颜色对比
        self.坐标 = [510, 360]
        self.颜色像素 = [249,252,239]
        self.等待秒数 = 3
        self.模具一一网页加载颜色对比()
        print('更新主页 页面 ，颜色检测通过')

        self.模具一一更新主页()
    def 模具一一更新主页(self):
        pag.moveTo(700, 320)  # 鼠标移动X.Y 位  定位  页面空白处
        pag.rightClick()  # 右击
        time.sleep(2)  # 等待  # 增加延迟



    def 模具一一提取影视剧数据库里的3e影视网站后台登录cookie(self):
        # 提取数据库里的过滤网址
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "", "帐号", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句
        sql = "SELECT `用户名`, `密码`, `完全版cookie` FROM `3e影视网站` WHERE `网站`='3e影视网站管理后台' "
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        self.用户名密码完全版cookie组列表= cursor.fetchall()
        self.用户名密码完全版cookie组=self.用户名密码完全版cookie组列表[0]

        # 关闭数据库连接
        db.close()

    def 模具一一删除重复标题(self):
        pag.moveTo(709, 115)  # 鼠标移动X.Y 位  定位  页面空白处
        pag.rightClick()  # 右击
        time.sleep(0.5)  # 等待  # 增加延迟

        pag.press('end')  # press()一次完整的击键.hotkey('ctrl','c') 确认  拉至底部
        time.sleep(1)  # 等待  # 增加延迟

        pag.moveTo(70, 878)  # 鼠标移动X.Y 位  定位  全选
        pag.rightClick()  # 右击
        time.sleep(0.5)  # 等待  # 增加延迟

        pag.moveTo(176, 878)  # 鼠标移动X.Y 位  定位  删除
        pag.rightClick()  # 右击
        time.sleep(2)  # 等待  # 增加延迟


类=类一一38影视网站()