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
        self.粘贴标题 = r"2018上半年豆瓣高评分电影"
        self.清除全部 = 998
        self.模具一一换头部信息()
        self.模具一一换ip连接二()


        self.模具一一重新激活浏览器窗口()


        self.模具一一提取推广库里的知乎发贴帐号()
        今天时间 = str(time.strftime("%y-%m-%d", time.localtime()))
        贴内容=今天时间+'日期'

        for 帐号cookie组 in self.帐号cookie组列表:

            self.帐号 = 帐号cookie组[0]
            self.密码 = 帐号cookie组[1]
            self.注册手机号 = 帐号cookie组[2]
            self.cookie = 帐号cookie组[3]
            存活 = 帐号cookie组[4]
            self.发贴内容 = str(帐号cookie组[5])


            if len(self.注册手机号)==0 or len(self.密码)==0 or '封' in str(存活) or 贴内容 in self.发贴内容 or '美剧' in str(self.帐号):
                continue  # 跳过循环

            if 'zhihu.com' in str(帐号cookie组):
                continue  # 跳过循环

                self.模具一一布置浏览头()
                输入网址='https://www.zhihu.com'
                self.模具一一地址栏输入网址(输入网址)
                self.模具一一导入界面的登录cookie(self.帐号)

                #self.模具一一测试登录页面属性(self.帐号)
            else:  # 否则


                self.模具一一布置浏览头()
                输入登录网址 = 'https://www.zhihu.com/signin?next=%2Fexplore'
                self.模具一一地址栏输入网址(输入登录网址)
                print(self.帐号)


                self.模具一一输入用户手机号与密码登录()
                #self.模具一一测试登录页面属性(self.帐号)



            等待用户输入 = input("\n按下 enter 确认键后继续 填充发贴内容 ")
            self.模具一一重新激活浏览器窗口()

            提取网址 = self.模具一一提取浏览器地址栏网址()
            self.发贴内容 = 贴内容 + 提取网址 + '网址' + self.发贴内容

            self.模具一一打开全屏写回答()

            self.模具一一填充发贴内容()

            等待用户输入 = input("\n按下 enter 确认键后继续 提交回答")
            self.模具一一重新激活浏览器窗口()

            self.模具一一提交回答()
            等待用户输入 = input("\n按下 enter 确认键后继续  保存数据库")
            self.模具一一重新激活浏览器窗口()

            self.模具一一保存数据库一更新知乎登录cookie与发贴内容()
            self.模具一一清除浏览器历史缓存()  # 1 次
            self.模具一一换ip连接二()

            等待用户输入 = input("\n按下 enter 确认键后继续 下一轮")
            self.模具一一重新激活浏览器窗口()

    """=========数据库======================="""

    def 模具一一提取推广库里的知乎发贴帐号(self):
        # 提取数据库里的过滤网址
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "", "影视发帖推广", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句
        sql = "SELECT  `帐号`, `密码`, `注册手机号`,`cookie` ,`存活`,`发贴内容` FROM `知乎发贴帐号`"
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        self.帐号cookie组列表 = cursor.fetchall()

        # 关闭数据库连接
        db.close()

    def 模具一一保存数据库一更新知乎登录cookie与发贴内容(self):
        print('打开数据库连接')
        # 打开数据库连接,
        db = pymysql.connect("localhost", "root", "", "影视发帖推广", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句
        if self.清除全部 == 0:
            self.模具一一提取登录界面的cookie()
            sql = """UPDATE `知乎发贴帐号` SET `cookie`='{}',`发贴内容`='{}' WHERE `注册手机号`='{}'""".format(self.cookie,self.发贴内容,self.注册手机号)  # 不换行 '{}'
        else:  # 否则
            sql = """UPDATE `知乎发贴帐号` SET `发贴内容`='{}' WHERE `注册手机号`='{}'""".format(self.发贴内容,self.注册手机号)  # 不换行 '{}'
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

    """=========打开全屏写回答与提交回答=========================="""

    def 模具一一打开全屏写回答(self):
        def 模具一一旧保存():
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

            time.sleep(1)  # 等待  # 增加延迟
            pag.moveTo(793, 466)  # 鼠标移动X.Y 方位    全屏模式
            pag.rightClick()  # 右击
            time.sleep(1)  # 等待  # 增加延迟
            # =====================

        pag.hotkey('ctrlleft', '1')  # 方位  浏览器 主 页面
        time.sleep(0.5)  # 等待  # 增加延迟
        #=======================


        pag.moveTo(450, 250)  # 鼠标移动X.Y 方位    输入 框
        pag.rightClick()  # 右击

    def 模具一一提交回答(self):
        time.sleep(0.3)  # 等待  # 增加延迟
        pag.moveTo(670, 870)  # 鼠标移动X.Y 方位  确定  写回答 栏
        pag.rightClick()  # 右击
        time.sleep(0.3)  # 等待  # 增加延迟

        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')
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


        文本内容字节 = open(r'F:\影视发帖推广\知乎\影视短标题.txt', 'r')  # 打开所保存的cookies内容文件 粘贴
        文本内容 =文本内容字节.read()
        self.粘贴标题=self.粘贴标题+'\n'+文本内容+'\n'
        self.模具一一粘贴标题()

        行内容列表=文本内容.split('\n')
        if len(行内容列表)>6:
            self.图片目录 = 10
        else:  #否则
            self.图片目录 = 0

        计数器=0
        for 行内容 in 行内容列表[:11]:  # 按照字符:进行划分读取 [26:50]

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
                #self.模具一一插入链接地址()
                计数器 = 0
                # time.sleep(10000)  # 等待
        self.模具一一插入链接地址()

    """=========提取正文========================"""

    def 模具一一粘贴正文发贴内容(self):
        # self.模具一一写入剪切板内容(self.发贴正文)
        self.模具一一文本随机插入字符测试(self.发贴正文,5)
        self.模具一一提取文本内容()
        time.sleep(0.5)  # 等待  # 增加延迟
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
        self.发贴正文 = self.短标题 + '\n'+self.正文 + '\n'
        print(self.发贴正文)

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

                #self.发贴正文=self.模具一一文本随机插入字符测试(发贴内容)
        self.发贴正文 =self.短标题+发贴内容+'\n'
        print(self.发贴正文)


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
        pag.moveTo(366, 45)  # 鼠标移动X.Y 方位  确定  图片目录地址框
        pag.rightClick()  # 右击
        time.sleep(0.3)  # 等待  # 增加延迟

        pag.hotkey('ctrlleft', 'a')  # press()一次完整的击键.hotkey('ctrl','c') 全选 图片
        time.sleep(0.3)  # 等待  # 增加延迟
        pag.press('delete')  # press()一次完整的击键.hotkey('ctrl','c') 确认
        time.sleep(0.3)  # 等待  # 增加延迟

        图片目录地址= r"F:\影视发帖推广\临时图片"

        self.模具一一写入剪切板内容(图片目录地址)

        pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.3)  # 等待  # 增加延迟
        pag.press('enter')  # press()一次完整的击键.hotkey('ctrl','c') 确认
        time.sleep(1)  # 等待  # 增加延迟



    def 模具一一上传图片(self):
        self.模具一一图片目录移动图片()





        if self.图片目录 == 0: #  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            图片按钮 = 180
            pag.moveTo(595, 图片按钮)  # 鼠标移动X.Y 方位  确定  打开图片 按钮
            pag.rightClick()  # 右击


            # ========清除 图片水印提醒 的窗口===
            time.sleep(2)  # 等待  # 增加延迟
            pag.moveTo(650, 655)  # 鼠标移动X.Y 方位  清除 图片水印提醒 的窗口
            pag.rightClick()  # 右击
            time.sleep(0.5)  # 等待  # 增加延迟

            time.sleep(2)  # 等待  # 增加延迟
            self.图片目录 = 998
            self.模具一一图片目录地址框()

        elif self.图片目录 == 10:
            图片按钮 = 118
            pag.moveTo(580, 图片按钮)  # 鼠标移动X.Y 方位  确定  打开图片 按钮
            pag.rightClick()  # 右击

            # ========清除 图片水印提醒 的窗口===
            time.sleep(2)  # 等待  # 增加延迟
            pag.moveTo(650, 655)  # 鼠标移动X.Y 方位  清除 图片水印提醒 的窗口
            pag.rightClick()  # 右击
            time.sleep(0.5)  # 等待  # 增加延迟

            time.sleep(2)  # 等待  # 增加延迟

            self.图片目录 = 998

            self.模具一一图片目录地址框()


        else:  #否则
            图片按钮 =118
            pag.moveTo(580, 图片按钮)  # 鼠标移动X.Y 方位  确定  打开图片 按钮
            pag.rightClick()  # 右击

            time.sleep(2)  # 等待  # 增加延迟



        # =======选择图片 ==
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
        页面关键词 = '草稿已保存'
        self.模具一一测试页面属性一等待(页面关键词)
        time.sleep(0.3)  # 等待  # 增加延迟
        #======最底部分隔线=========
        pag.moveTo(1110, 276)  # 鼠标移动X.Y 方位  编辑器外栏
        pag.rightClick()  # 右击
        time.sleep(0.5)  # 等待  # 增加延迟
        # pag.hotkey('ctrlleft', 'shiftleft', 'S')  # 分隔线

        pag.press('end')  # press()一次完整的击键.hotkey('ctrl','c') 确认 编辑器外栏 最底部
        time.sleep(0.5)  # 等待  # 增加延迟

        pag.moveTo(356, 827)  # 鼠标移动X.Y 方位  定位 编辑器内 最底部
        pag.rightClick()  # 右击
        time.sleep(0.5)  # 等待  # 增加延迟

        pag.hotkey('ctrlleft', 'shiftleft', 'S')  # 分隔线

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

    """=========输入用户手机号与密码登录========================"""
    def 模具一一输入用户手机号与密码登录(self):
        self.清除全部 = 0


        time.sleep(2)  # 等待
        """测试页面属性"""
        页面关键词 = '登录知乎'
        # self.模具一一测试页面属性(页面关键词)
        # ==========登录 方框
        # ====手机号
        pag.moveTo(486, 316)  # 鼠标移动X.Y 方位 知乎登录顶  空白处
        pag.rightClick()  # 右击
        time.sleep(0.3)  # 等待
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')

        time.sleep(0.3)  # 等待  # 增加延迟
        pag.typewrite(self.注册手机号)  # 输入手机号码


        # ====密码
        time.sleep(0.3)  # 等待  # 增加延迟
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')  输入密码方框
        time.sleep(0.3)  # 等待  # 增加延迟
        pag.typewrite(self.密码)  # 输入密码

        # ====确认登录
        time.sleep(0.3)  # 等待  # 增加延迟

        pag.moveTo(651, 540)  # 鼠标移动X.Y 方位 登录 按钮
        pag.rightClick()  # 右击
        time.sleep(2)  # 等待





if __name__ == '__main__':
    类=类一一知乎发贴()