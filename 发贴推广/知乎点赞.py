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

import pyautogui as pag #模拟鼠标键盘操作
import pyautogui#模拟鼠标键盘操作
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
        浏览头网址 = 'zhihu.com'



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
                self.模具一一布置浏览头(浏览头网址)

                self.点赞内容 = 赞内容+self.前ip+'IP行'+self.点赞内容

                self.模具一一导入界面的登录cookie()
                self.模具一一测试登录页面属性(self.帐号)
            else:  # 否则
                self.点赞内容 = 赞内容 + self.前ip + 'IP行' + self.点赞内容
                self.模具一一布置浏览头(浏览头网址)
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









if __name__ == '__main__':
    类 = 类一一知乎点赞()




