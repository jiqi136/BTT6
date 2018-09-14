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
SELECT * FROM `知乎话题` WHERE `短标题` != '空' ORDER BY `知乎话题`.`赞同数` DESC 
超过  500k  大小的图片删除
IP：121.32.193.219
"""

class 类一一知乎发贴(类一一公共库):  # 调用 类的模具 self.模具一一数据库()
    def __init__(self):
        self.粘贴标题 = r"豆瓣2018上半年评分8.6以上的好电影推荐"
        self.模具一一换头部信息()
        self.模具一一重新激活浏览器窗口()
        #self.模具一一打开全屏写回答()

        self.模具一一填充发贴内容()
        #self.模具一一提交回答()

    """=========打开全屏写回答与提交回答=========================="""

    def 模具一一打开全屏写回答(self):

        pag.moveTo(123, 283)  # 鼠标移动X.Y 方位  确定  写回答 栏
        pag.rightClick()  # 右击
        time.sleep(0.3)  # 等待  # 增加延迟

        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.3)  # 等待  # 增加延迟
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.3)  # 等待  # 增加延迟
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c') 打开  写回答 方框

        time.sleep(0.3)  # 等待  # 增加延迟
        pag.press('enter')  # press()一次完整的击键.hotkey('ctrl','c')

        #=======================
        time.sleep(1)  # 等待  # 增加延迟
        pag.moveTo(778, 438)  # 鼠标移动X.Y 方位    全屏模式
        pag.rightClick()  # 右击
        time.sleep(1)  # 等待  # 增加延迟

        pag.moveTo(450, 250)  # 鼠标移动X.Y 方位    输入 框
        pag.rightClick()  # 右击

    def 模具一一提交回答(self):
        pag.moveTo(707, 870)  # 鼠标移动X.Y 方位  确定  写回答 栏
        pag.rightClick()  # 右击
        time.sleep(0.3)  # 等待  # 增加延迟

        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.3)  # 等待  # 增加延迟
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')  提交回答

        time.sleep(0.3)  # 等待  # 增加延迟
        pag.press('enter')  # press()一次完整的击键.hotkey('ctrl','c') 确认


    """=========填充发贴内容======================="""

    def 模具一一粘贴标题(self):

        self.模具一一写入剪切板内容(self.粘贴标题)
        pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.3)  # 等待  # 增加延迟

        pag.hotkey('ctrlleft', 'shiftleft', 'S')  # 分隔线
    def 模具一一填充发贴内容(self):
        self.模具一一提取文本短标题()
    def 模具一一提取文本短标题(self):


        文本内容 = open(r'F:\影视发帖推广\知乎\影视短标题.txt', 'r')  # 打开所保存的cookies内容文件 粘贴
        文本内容 =文本内容.read()
        self.粘贴标题=self.粘贴标题+'\n'+文本内容+'\n'
        self.模具一一粘贴标题()

        行内容列表=文本内容.split('\n')
        if len(行内容列表)>6:
            self.图片目录 = 998
            self.模具一一插入链接地址()
        else:  #否则
            self.图片目录 = 0

        计数器=0
        for 行内容 in 行内容列表:  # 按照字符:进行划分读取 [26:50]

            # 其设置为1就会把字符串拆分成2份
            self.短标题=行内容
            print(self.短标题)
            self.模具一一提取正文()

            if len(self.正文) == 0:
                print('跳过循环')
                continue #跳过循环  # 返回
            self.模具一一粘贴正文发贴内容()  #
            self.模具一一上传图片()

            计数器 = 计数器 + 1
            if 计数器 ==7:
                self.模具一一插入链接地址()
                计数器 = 0
                # time.sleep(10000)  # 等待
        self.模具一一插入链接地址()

    """=========提取正文========================"""

    def 模具一一粘贴正文发贴内容(self):
        self.模具一一写入剪切板内容(self.发贴内容)
        time.sleep(0.3)  # 等待  # 增加延迟
        pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c')


    def 模具一一提取正文(self):
        self.新旧影视库 = '最新影视剧'
        #self.模具一一短标题提取数据库正文内容()


        self.模具一一短标题提取豆瓣电影数据库正文内容()
        self.旧影视库 =998

        if self.旧影视库 == 0:
            self.新旧影视库 = '电影与合集'
            self.模具一一短标题提取数据库正文内容()
        if len(self.正文)==0:
            print('正文内容为空')
            return#返回
        #self.模具一一清洗正文()  #
        self.发贴内容 = self.短标题 + '\n'+self.正文 + '\n'
        print(self.发贴内容)

    def 模具一一清洗正文(self):


        # print(self.正文)
        文本 =self.正文
        
        if '◎简' in 文本: #  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            规则 = '.{1,}◎简'
            文本 = re.sub(规则, '', 文本)  # 替换   ,count=0,re.S|re.I

        elif '简介' in 文本:# 其它条件.
            规则 = '.{1,}简介'
            文本 = re.sub(规则, '', 文本)  # 替换   ,count=0,re.S|re.I


        elif '简' in 文本:  # 其它条件.
            规则 = '.{1,}简'
            文本 = re.sub(规则, '', 文本)  # 替换   ,count=0,re.S|re.I
        规则 = '◎.{1,}'# 删除 提奖内容
        文本 = re.sub(规则, '', 文本)  # 替换   ,count=0,re.S|re.I
        规则 = '<.{1,}?>'  # 删除 提奖内容
        文本 = re.sub(规则, '\n', 文本)  # 替换   ,count=0,re.S|re.I

        替换列表=["&nbsp;"]
        for 替换文 in 替换列表:
            文本 = 文本.replace(替换文, "\n")  # 替换   , 1) 次数 1


        发贴内容=''
        for 行内容 in 文本.split('\n'):  # 按照字符:进行划分读取
            if len(行内容)>5:
                发贴内容 =发贴内容+"\n"+行内容

                #self.发贴内容=self.模具一一文本随机插入字符测试(发贴内容)
        self.发贴内容 =self.短标题+发贴内容+'\n'
        print(self.发贴内容)

    def 模具一一文本随机插入字符测试(self,文本列表):
        计数器 =0
        文本 =''
        for 每个字 in 文本列表:
            计数器 = 计数器 + 1
            if 计数器 == 12:
                符号表 = random.choice('↕↟↡↥↧↨↾↿⇂⇃⇞⇟⇡⇣´`ˆ')
                文本 = 文本 + 符号表
                计数器 = 0
            文本 = 文本 + 每个字
        return 文本# 返回
    def 模具一一短标题提取豆瓣电影数据库正文内容(self):
        # 提取数据库里的过滤网址
        # 打开数据库连接
        self.正文 =''
        db = pymysql.connect("localhost", "root", "", '影视发帖推广', charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句

        sql = "SELECT  `正文` FROM `2018上半年豆瓣电影` WHERE `标题`= '{}'".format(self.短标题)#不换行 '{}'
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        正文组列表 = cursor.fetchall()

        if len(正文组列表) == 0:
            self.旧影视库 = 0
            return  # 返回
        else:  # 否则
            self.旧影视库 = 998
            正文组 = 正文组列表[0]
            self.正文 = 正文组[0]

        # 关闭数据库连接
        db.close()
    def 模具一一短标题提取数据库正文内容(self):
        # 提取数据库里的过滤网址
        # 打开数据库连接
        self.正文 =''
        db = pymysql.connect("localhost", "root", "", self.新旧影视库, charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句

        sql = "SELECT `正文` FROM `网站文章内容` WHERE `短标题`= '{}'".format(self.短标题)#不换行 '{}'
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        正文组列表 = cursor.fetchall()

        if len(正文组列表) == 0:
            self.旧影视库 = 0
            return  # 返回
        else:  # 否则
            self.旧影视库 = 998
            正文组 = 正文组列表[0]
            self.正文 = 正文组[0]

        # 关闭数据库连接
        db.close()

    """=========上传图片与分隔线========================"""
    def 模具一一图片目录移动图片(self):
        self.移动文件目录名 = r"F:\影视发帖推广\临时图片"
        self.模具一一清空移动文件目录()
        self.递归展开知乎目录与文件()

    def 递归展开知乎目录与文件(self):
        目标目录 = r"F:\影视发帖推广\知乎\上传图"

        for 根路径, 一层目录列表, 一层文件列表 in os.walk(目标目录, topdown=False):  # "."目录,topdown=False先子文件夹再到全层元组文件夹
            for 纯目录名 in 一层目录列表:  # dirs遍历目录  files遍历文件
                if self.短标题 in 纯目录名:
                    self.旧目录路径 = os.path.join(根路径, 纯目录名)  # 合并成为 完全的地址
                    print(self.旧目录路径)
                    self.展开知乎上传图下一层目录与文件()

                    # print(新目录)
                    return#返回

    def 展开知乎上传图下一层目录与文件(self):
        子目录列表与文件列表 = os.listdir(self.旧目录路径)  # 分离出目录列表与文件列表
        for 子目录或文件 in 子目录列表与文件列表[0:2]:
            根目录的子目录或文件路径 = os.path.join(self.旧目录路径, 子目录或文件)
            if os.path.isfile(根目录的子目录或文件路径):  # 判断是不是文件  判断文件 os.path.isfile
                # os.path.isfile() 函数判断某一路径是否为文件
                self.图片文件 = 根目录的子目录或文件路径
                print(self.图片文件, '复制文件:', self.移动文件目录名)
                shutil.copy(self.图片文件, self.移动文件目录名)

    def 模具一一清空移动文件目录(self):
        子目录列表与文件列表 = os.listdir(self.移动文件目录名)  # 分离出目录列表与文件列表
        for 子目录或文件 in 子目录列表与文件列表:
            根目录的子目录或文件路径 = os.path.join(self.移动文件目录名, 子目录或文件)
            os.unlink(根目录的子目录或文件路径)  # 删除原来 文件 与文件
        print('清空移动文件目录:', self.移动文件目录名)

    def 模具一一图片目录地址框(self):
        pag.moveTo(366, 45)  # 鼠标移动X.Y 方位  确定  打开图片 按钮
        pag.rightClick()  # 右击
        time.sleep(0.3)  # 等待  # 增加延迟

        pag.hotkey('ctrlleft', 'a')  # press()一次完整的击键.hotkey('ctrl','c') 全选 图片
        time.sleep(0.3)  # 等待  # 增加延迟

        图片目录地址= r"F:\影视发帖推广\临时图片"

        self.模具一一写入剪切板内容(图片目录地址)

        pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.3)  # 等待  # 增加延迟
        pag.press('enter')  # press()一次完整的击键.hotkey('ctrl','c') 确认
        time.sleep(0.3)  # 等待  # 增加延迟



    def 模具一一上传图片(self):
        self.模具一一图片目录移动图片()



        if self.图片目录 == 0: #  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            图片按钮 = 180
            pag.moveTo(595, 图片按钮)  # 鼠标移动X.Y 方位  确定  打开图片 按钮
            pag.rightClick()  # 右击
            time.sleep(3)  # 等待  # 增加延迟

            self.模具一一图片目录地址框()

        else:  #否则
            图片按钮 =118
            pag.moveTo(580, 图片按钮)  # 鼠标移动X.Y 方位  确定  打开图片 按钮
            pag.rightClick()  # 右击
            time.sleep(3)  # 等待  # 增加延迟


        pag.moveTo(173, 148)  # 鼠标移动X.Y 方位  确定  图片目录空白处
        pag.rightClick()  # 右击

        time.sleep(0.3)  # 等待  # 增加延迟
        pag.hotkey('ctrlleft', 'a')  # press()一次完整的击键.hotkey('ctrl','c') 全选 图片
        time.sleep(1)  # 等待  # 增加延迟
        pag.hotkey('altleft', 'o')  # press()一次完整的击键.hotkey('ctrl','c') 提交图片
        time.sleep(5)  # 等待  # 增加延迟 已经有等待 3秒了

        pag.moveTo(218, 872)  # 鼠标移动X.Y 方位  定位 草稿已保存 栏 空白处
        pag.rightClick()  # 右击
        time.sleep(0.3)  # 等待  # 增加延迟
        页面关键词= '草稿已保存'
        self.模具一一测试页面属性一等待(页面关键词)

        # pag.hotkey('ctrlleft', 'shiftleft', 'S')  # 分隔线
        if self.图片目录 == 0:
            pag.moveTo(668, 180)  # 鼠标移动X.Y 方位  定位 分隔线豆瓣2018上半年评分8.6以上的好电影推荐
            self.图片目录 = 998
        else:  # 否则
            pag.moveTo(668, 120)  # 鼠标移动X.Y 方位  定位 分隔线
        pag.rightClick()  # 右击
        time.sleep(0.5)  # 等待  # 增加延迟

    """=========插入链接地址(========================"""
    def 模具一一插入链接地址(self):


        pag.hotkey('ctrlleft', 'k')  # press()一次完整的击键.hotkey('ctrl','c') 插入链接地址
        time.sleep(2)  # 等待  # 增加延迟

        pag.moveTo(505, 400)  # 鼠标移动X.Y 方位  定位  插入链接地址  方框
        pag.rightClick()  # 右击
        time.sleep(0.3)  # 等待  # 增加延迟


        # ==================
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.3)  # 等待  # 增加延迟
        链接文本 = r"电影美剧→→: http://3e38.com"
        self.模具一一写入剪切板内容(链接文本)
        pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.3)  # 等待  # 增加延迟
        # ==================
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.3)  # 等待  # 增加延迟
        链接地址 = r"http://3e38.com"
        self.模具一一写入剪切板内容(链接地址)
        pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.3)  # 等待  # 增加延迟
        # ==================
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.3)  # 等待  # 增加延迟
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.3)  # 等待  # 增加延迟
        pag.press('enter')  # press()一次完整的击键.hotkey('ctrl','c') 确认
        time.sleep(1)  # 等待  # 增加延迟

        pag.hotkey('ctrlleft', 'shiftleft', 'S')  # 分隔线



类=类一一知乎发贴()