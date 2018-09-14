# -*- coding:utf-8
import pyautogui as pag
import win32api  # 操作本地文件
import win32clipboard as w# 提取剪切板内容
import win32con#提取剪切板内容
import re  # 正则式
import time  # 时间
import pyautogui

import os  # 本地操作

class 类一一提取链接:  # 调用 类的模具 self.模具一一数据库()
    def __init__(self):
        win32api.ShellExecute(0, 'open',  r'D:\2D安装盘\城通网盘客户端\xt.exe','', '', 1)
        time.sleep(1)  # 等待  # 增加延迟
        pyautogui.alert('城通网盘已经启动，窗口最大化后继续')
        time.sleep(1)  # 等待  # 增加延迟
        # time.sleep(1)  # 等待  # 增加延迟
        # pyautogui.alert('第二次确认，城通网盘完全启动后，窗口最大化后继续')
        self.模具一一下探至链接目录()

        self.模具一一确认退出()
        #win32api.ShellExecute(0, 'open', r'E:\PY学习文件\BTT影视剧\工具集\FTP上传http网页文件.py', '', '', 1)

        #self.模具一一换头部信息()

    def 模具一一下探至链接目录(self):
        pag.moveTo(311, 37)  # 鼠标 定位 公有位 按钮
        pag.rightClick()  # 右击
        time.sleep(1)  # 等待  # 增加延迟

        pag.moveTo(60, 250)  # 鼠标 定位 上传网盘 按钮
        pag.rightClick()  # 右击
        time.sleep(1)  # 等待  # 增加延迟

        pag.moveTo(300, 240)  # 鼠标 定位 最新 按钮
        pag.rightClick()  # 右击
        time.sleep(1)  # 等待  # 增加延迟

        self.影视类型='电视剧'
        self.模具一一影视类型提取链接()
        self.影视类型 = '动漫'
        self.模具一一影视类型提取链接()
        self.影视类型 = '电影'
        self.模具一一影视类型提取链接()



    def 模具一一影视类型提取链接(self):
        竖坐标 = 239
        if '电视剧' in self.影视类型:
            横坐标=65
            self.文本文件名=r'F:\下载种子目录\ftp上传目录链接网页\最新电视剧.txt'
        elif '动漫' in self.影视类型:  # 其它条件。
            横坐标 = 182
            self.文本文件名 = r'F:\下载种子目录\ftp上传目录链接网页\最新动漫.txt'

        else:  # 否则
            横坐标 = 300
            self.文本文件名 = r'F:\下载种子目录\ftp上传目录链接网页\最新电影.txt'

        pag.moveTo(横坐标, 竖坐标)  # 鼠标 定位 各影视类型 按钮
        pag.rightClick()  # 右击
        time.sleep(5)  # 等待  # 增加延迟

        self.模具一一全选后提取链接()
        self.模具一一写入文本文件()
        self.模具一一返回影视类型()


        time.sleep(1)  # 等待  # 增加延迟

    def 模具一一全选后提取链接(self):
        def 模具一一全选定位():
            pag.moveTo(30, 150)  # 鼠标 定位 全选 按钮
            pag.rightClick()  # 右击

            time.sleep(5)  # 等待  # 增加延迟
            pag.moveTo(1080, 150)  # 鼠标 定位 分享 按钮
            pag.rightClick()  # 右击

        # ==========定位===========
        模具一一全选定位()
        time.sleep(5)  # 等待  # 增加延迟
        模具一一全选定位()
        # ==========提取链接==========
        time.sleep(5)  # 等待  # 增加延迟
        pag.moveTo(618, 280)  # 鼠标 定位 文件名与链接 方框
        pag.rightClick()  # 右击
        time.sleep(1)  # 等待  # 增加延迟

        pag.hotkey('ctrlleft', 'a')  # press()一次完整的击键.hotkey('ctrl','c'):复制内容
        time.sleep(1)  # 等待  # 增加延迟
        pag.hotkey('ctrlleft', 'c')  # press()一次完整的击键.hotkey('ctrl','c'):复制内容
        time.sleep(1)  # 等待  # 增加延迟

        self.文件名与链接 = self.模具一一获取剪切板内容()


    def 模具一一获取剪切板内容(self):  # 获取剪切板内容
        w.OpenClipboard()
        t = w.GetClipboardData(win32con.CF_TEXT)
        w.CloseClipboard()

        t = t.decode('gbk')  # 解码为 编程的中文
        return t

    def 模具一一写入文本文件(self):

        #self.文件名与链接=self.文件名与链接(encoding='UTF-8')

        文本 = open(self.文本文件名, 'w', encoding='UTF-8')
        文本.write(self.文件名与链接)  # write() #写入
        文本.close()

    def 模具一一返回影视类型(self):
        pag.moveTo(620, 98)  # 鼠标 定位 分享 方框栏
        pag.rightClick()  # 右击
        time.sleep(1)  # 等待  # 增加延迟

        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.3)  # 等待  # 增加延迟
        pag.press('enter')  # press()一次完整的击键.hotkey('c  trl','c')  确认 叉叉  按钮
        time.sleep(2)  # 等待  # 增加延迟

        pag.moveTo(375, 150)  # 鼠标 定位 返回 按钮
        pag.rightClick()  # 右击
        time.sleep(2)  # 等待  # 增加延迟
    def 模具一一确认退出(self):
        pyautogui.alert('确认退出')
        time.sleep(1)  # 等待  # 增加延迟
        pag.hotkey('altleft', 'f4')  # press()一次完整的击键.hotkey('ctrl','c'):复制内容
        # pag.moveTo(1255, 25)  # 鼠标 定位 分享 方框栏
        # pag.rightClick()  # 右击
        time.sleep(1)  # 等待  # 增加延迟

class 类一一ALDrive上传文件:  # 调用 类的模具 self.模具一一数据库()
    def __init__(self):
        win32api.ShellExecute(0, 'open',  r'E:\Ean\ESTsoft\ALDrive\ALDrive.exe','', '', 1)
        time.sleep(1)  # 等待  # 增加延迟
        pyautogui.alert('上传软件已经启动')
        time.sleep(1)  # 等待  # 增加延迟

        self.模具一一确认最新的网盘登录()
        self.模具一一下探目录与打开上传窗口()
        self.模具一一上传窗口选择文件目录()
        self.模具一一退出上传软件()

    def 模具一一确认最新的网盘登录(self):
        pag.moveTo(252, 280)  # 鼠标 定位 城通 栏
        pag.rightClick()  # 右击
        time.sleep(1)  # 等待  # 增加延迟
        pag.press('enter')  # press()一次完整的击键.hotkey('c  trl','c')  确认 叉叉  按钮
        time.sleep(1)  # 等待  # 增加延迟

        pag.press('down')  # press()一次完整的击键.hotkey('c  trl','c')  确认 叉叉  按钮
        time.sleep(1)  # 等待  # 增加延迟

        pag.moveTo(750, 580)  # 鼠标 定位 连接 按钮
        pag.rightClick()  # 右击
        time.sleep(1)  # 等待  # 增加延迟

    def 模具一一下探目录与打开上传窗口(self):
        pyautogui.alert('窗口最大化后继续')
        time.sleep(1)  # 等待  # 增加延迟

        # ======下探至上传目录======
        pag.moveTo(260, 230)  # 鼠标 定位 上传网盘  目录 栏
        pag.rightClick()  # 右击
        time.sleep(1)  # 等待  # 增加延迟
        pag.press('enter')  # press()一次完整的击键.hotkey('c  trl','c')  确认
        time.sleep(3)  # 等待  # 增加延迟
        #======打开上传窗口======
        pag.moveTo(241, 70)  # 鼠标 定位 上传 按钮
        pag.rightClick()  # 右击
        time.sleep(3)  # 等待  # 增加延迟

    def 模具一一上传窗口选择文件目录(self):
        pag.moveTo(410, 510)  # 鼠标 定位 ‘ 计算机’按钮
        pag.rightClick()  # 右击
        time.sleep(1)  # 等待  # 增加延迟

        pag.moveTo(596, 520)  # 鼠标 定位 ‘f 盘’按钮
        pag.rightClick()  # 右击
        time.sleep(1)  # 等待  # 增加延迟
        pag.press('enter')  # press()一次完整的击键.hotkey('c  trl','c')  确认
        time.sleep(1)  # 等待  # 增加延迟

        pag.moveTo(650, 538)  # 鼠标 定位 ‘下载种子目录’目录  按钮
        pag.rightClick()  # 右击
        time.sleep(1)  # 等待  # 增加延迟
        pag.press('enter')  # press()一次完整的击键.hotkey('c  trl','c')  确认
        time.sleep(1)  # 等待  # 增加延迟

        pag.moveTo(570, 333)  # 鼠标 定位 ‘上传网盘’ 目录  按钮
        pag.rightClick()  # 右击
        time.sleep(1)  # 等待  # 增加延迟
        pag.press('enter')  # press()一次完整的击键.hotkey('c  trl','c')  确认
        time.sleep(1)  # 等待  # 增加延迟

        pag.moveTo(720, 333)  # 鼠标 定位 ‘最新’ 目录  按钮
        pag.rightClick()  # 右击
        time.sleep(1)  # 等待  # 增加延迟
        pag.hotkey('altleft', 'o')  # press()一次完整的击键.hotkey('ctrl','c'):复制内容

        time.sleep(1)  # 等待  # 增加延迟

    def 模具一一退出上传软件(self):
        print('等待 半小时')
        time.sleep(3600)  # 等待  # 增加延迟


        pag.moveTo(132, 908)  # 鼠标 定位 激活 上传软件
        pag.rightClick()  # 右击
        time.sleep(2)  # 等待  # 增加延迟

        pyautogui.alert('上传完成后继续')
        time.sleep(1)  # 等待  # 增加延迟
        pag.moveTo(600, 300)  # 鼠标 定位 激活 上传软件 窗口栏
        pag.rightClick()  # 右击
        time.sleep(1)  # 等待  # 增加延迟

        pag.hotkey('altleft', 'f4')  # press()一次完整的击键.hotkey('ctrl','c'):复制内容
        time.sleep(1)  # 等待  # 增加延迟

        pag.hotkey('altleft', 'f4')  # press()一次完整的击键.hotkey('ctrl','c'):复制内容
        time.sleep(1)  # 等待  # 增加延迟

        pag.press('enter')  # press()一次完整的击键.hotkey('c  trl','c')  确认
        time.sleep(1)  # 等待  # 增加延迟



类=类一一ALDrive上传文件()
类=类一一提取链接()


#win32api.ShellExecute(0, 'open', r'E:\PY学习文件\BTT影视剧\工具集\FTP上传http网页文件.py', '', '', 1)
win32api.ShellExecute(0, 'open', r'D:\桌面\FTP上传http网页文件.py.lnk', '', '', 1)