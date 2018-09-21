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
工具栏左1 导出COOKIE
工具栏2 设置浏览头部信息
"""

class 类一一百度号注册(类一一公共库):  # 调用 类的模具 self.模具一一数据库()
    def __init__(self,帐号类型):
        self.帐号类型 =帐号类型
        self.模具一一换头部信息()
        self.模具一一换ip连接二()
        self.模具一一提取影视剧数据库里的易码短信平台账户信息()
        self.模具一一提取推广库里的百度发贴帐号()
        self.内容 = """0123456789qwertyuiopasdfghjklzxcvbnm_"""

        百度号注册网址 = 'https://passport.baidu.com/v2/?reg&tt=1537504173103&overseas=undefined&gid=CC444B7-EB8C-4A92-A981-5EB224EE546E&tpl=mn&u=https%3A%2F%2Fwww.baidu.com%2Fbaidu%3Fwd%3D2%26tn%3D54002054_dg%26ie%3Dutf-8'
        浏览头网址 = 'baidu.com'
        计数器 = 0
        条件循环 = 1
        while 条件循环 == 1:  # 条件循环  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环

            计数器 = 计数器 + 1
            if 计数器 > 30:
                条件循环 = 998
            开始时间计数 = int(time.time())
            self.模具一一重新激活浏览器窗口()
            self.模具一一布置浏览头(浏览头网址)

            self.模具一一地址栏输入网址(百度号注册网址)
            self.模具一一输入百度用户名()

            self.模具一一输入手机号()
            self.模具一一输入密码()
            self.模具一一输入短信内容()

            等待用户输入 = input("\n按下 enter 确认键后继续")
            self.模具一一重新激活浏览器窗口()

            self.模具一一确认注册()

            等待用户输入 = input("\n按下 enter 确认键后继续")
            self.模具一一重新激活浏览器窗口()

            self.模具一一提取登录界面的cookie()
            self.模具一一保存数据库一百度发贴帐号等()

            等待用户输入 = input("\n按下 enter 确认键后继续")
            self.模具一一重新激活浏览器窗口()

            self.模具一一清除浏览器历史缓存()
            self.模具一一换ip连接二()

            结束时间计数 = int(time.time())
            用时 = 结束时间计数 - 开始时间计数
            print('操作:', 用时, '秒')
            time.sleep(1)  # 等待

            # pyautogui.alert('确认后继续')
            time.sleep(10)  # 等待  # 增加延迟

    def 模具一一获取百度接收的手机号码(self):
        # 通信令牌token = self.cookie
        self.项目编号 = "30"
        排除号段 = '170.171'
        获取手机号码接口网址 = "http://api.fxhyd.cn/UserInterface.aspx?action=getmobile&token={}&itemid={}&excludeno={}".format(
            self.通信令牌token, self.项目编号, 排除号段)
        网址内容 = self.模具一一打开的网址请求返回网页内容(获取手机号码接口网址)

        self.手机号码 = 网址内容.text.replace("success|", "")  # 替换   , 1) 次数 1
        print('手机号码:', self.手机号码)

    def 模具一一输入手机号(self):

        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c') 光标定位于 用户名
        time.sleep(0.5)  # 等待  # 增加延迟
        self.模具一一获取百度接收的手机号码()
        if len(self.手机号码) <10 or self.手机号码 in self.已注册帐号手机号:
            self.模具一一获取百度接收的手机号码()
        time.sleep(0.3)  # 等待

        self.模具一一写入剪切板内容(self.手机号码)# 输入手机号码
        pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c'):

        time.sleep(0.5)  # 等待  # 增加延迟
        self.已注册帐号手机号 = self.手机号码 + self.已注册帐号手机号

    def 模具一一输入密码(self):
        # ======密码=======
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.5)  # 等待  # 增加延迟

        密码数字 = random.randrange(100000, 1000000)
        self.密码 = "qq{}Q%".format(密码数字)
        print('密码:', self.密码)


        self.模具一一写入剪切板内容(self.密码)
        pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c'):
        time.sleep(0.5)  # 等待  # 增加延迟

    def 模具一一点击获取手机验证码(self):
        # ======密码=======
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.5)  # 等待  # 增加延迟
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.5)  # 等待  # 增加延迟
        pag.press('enter')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.3)  # 等待  # 增加延迟

    def 模具一一输入短信内容(self):
        self.模具一一点击获取手机验证码()


        self.模具一一获取百度短信()
        self.模具一一重新激活浏览器窗口()
        if len(self.短信内容) == 0:
            return  # 返回

        规则 = '\d{6}'
        内容列表 = re.findall(规则, self.短信内容)  # 提取
        self.短信内容 = 内容列表[0]



        pag.moveTo(335, 440)  # 鼠标移动X.Y 方位 定位 注册页面 空白栏
        pag.rightClick()  # 右击
        time.sleep(0.5)  # 等待  # 增加延迟
        self.模具一一写入剪切板内容(self.短信内容)
        pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c'):
        time.sleep(0.5)  # 等待  # 增加延迟

    def 模具一一确认注册(self):


        time.sleep(0.5)  # 等待  # 增加延迟

        pag.moveTo(400, 540)  # 鼠标移动X.Y 方位  定位 注册 按钮

        pag.rightClick()  # 右击

    def 模具一一获取百度短信(self):


        获取短信网址 = "http://api.fxhyd.cn/UserInterface.aspx?action=getsms&token={}&itemid={}&mobile={}".format(
            self.通信令牌token,
            self.项目编号, self.手机号码)
        """&release=1  自动释放号码标识符 若该参数值为1时,获取到短信的同时系统将自己释放该手机号码.若要继续使用该号码,请勿带入该参数."""

        条件循环 = 0
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

                    return  # 返回
                elif '3001' in 网址内容.text:  # 其它条件.
                    print('短信尚未到达:3001,应继续调用取短信接口,直到超时为止.')

                else:  # 否则
                    print('请求失败:', 网址内容.text)
            条件循环 = 条件循环 + 1
            self.模具一一重新激活浏览器窗口()
            time.sleep(5)  # 等待
            pag.moveTo(490, 442)  # 鼠标移动X.Y 方位  发送验证码 按钮
            pag.rightClick()  # 右击pag.rightClick()


        释放手机号码接口 = "http://api.fxhyd.cn/UserInterface.aspx?action=release&token={}&itemid={}&mobile={}".format(
            self.通信令牌token, self.项目编号, self.手机号码)
        释放手机号码网址内容 = self.模具一一打开的网址请求返回网页内容(释放手机号码接口)



    def 模具一一输入百度用户名(self):
        pag.moveTo(255, 205)  # 鼠标移动X.Y 方位 定位 注册页面 空白栏
        pag.rightClick()  # 右击
        time.sleep(0.5)  # 等待  # 增加延迟
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c') 光标定位于 用户名
        time.sleep(0.5)  # 等待  # 增加延迟

        if '顶贴号' in self.帐号类型: #  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            self.随机取名=self.模具一一随机取女名()
        else:# 否则
            self.随机取名 =self.模具一一百度随机取名合并网址名()

        self.模具一一写入剪切板内容(self.随机取名)
        pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c'):
        time.sleep(0.5)  # 等待  # 增加延迟

    def 模具一一百度随机取名合并网址名(self):


        #内容 = 内容.replace("\n", "")
        #内容 = 内容.replace(" ", "")

        #名 = random.choice(内容)

        名 = str(self.内容[0])
        self.内容 = self.内容.strip(名)  # 默认则是去除空格

        电影美剧表 = ['电影', '美剧', '动漫']
        电影美剧名 = random.choice(电影美剧表)
        # 合名次序= random.choice('影视')
        # if '影' in 合名次序:
        合名 = 名 + 电影美剧名 + '3e38、com'
        # else:  # 否则
        # 合名 =  '3e38、com'+电影美剧名 +名
        if 合名 in self.已注册帐号手机号:
            self.模具一一百度随机取名合并网址名()


        print('随机取名合并网址名', 合名)
        self.已注册帐号手机号 =合名+self.已注册帐号手机号
        return 合名  # 返回

    """=========数据库======================="""

    def 模具一一提取推广库里的百度发贴帐号(self):
        # 提取数据库里的过滤网址
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "", "影视发帖推广", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句
        sql = "SELECT `帐号`, `注册手机号` FROM `推广帐号` WHERE `类型`='{}' ".format(self.帐号类型)#不换行 '{}'
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        帐号手机号组列表 = cursor.fetchall()
        self.已注册帐号手机号=str(帐号手机号组列表)

        # 关闭数据库连接
        db.close()

    def 模具一一保存数据库一百度发贴帐号等(self):
        print('打开数据库连接')
        # 打开数据库连接,
        今天时间 = str(time.strftime("%y-%m-%d", time.localtime()))

        db = pymysql.connect("localhost", "root", "", "影视发帖推广", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句

        sql = """INSERT INTO `推广帐号`( `类型`, `帐号`, `密码`, `注册手机号`, `注册日期`, `cookie`) VALUES
         ("{}","{}","{}","{}",'{}','{}')""".format(self.帐号类型,self.随机取名, self.密码, self.手机号码, 今天时间,
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
    帐号类型 ='百度顶贴'
    帐号类型 ='百度发贴'
    类 = 类一一百度号注册(帐号类型)