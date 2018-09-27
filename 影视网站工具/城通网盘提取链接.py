# -*- coding:utf-8
import pyautogui as pag
import win32api  # 操作本地文件
import win32clipboard as w# 提取剪切板内容
import win32con#提取剪切板内容
import re  # 正则式
import time  # 时间
import pyautogui

import os  # 本地操作
import win32gui#窗口控件

class 类一一提取链接:  # 调用 类的模具 self.模具一一数据库()
    def __init__(self):
        win32api.ShellExecute(0, 'open',  r'D:\2D安装盘\城通网盘客户端\xt.exe','', '', 1)
        time.sleep(1)  # 等待  # 增加延迟

        print('回归桌面')
        pag.hotkey('winleft', 'd')  # press()一次完整的击键.hotkey('ctrl','c'):热键函数 .keyDown()按下某个键.keyUp()松开某个键.
        time.sleep(30)  # 等待  # 增加延迟
        self.模具一一重新激活城通网盘客户端()


        self.模具一一下探至链接目录()

        self.模具一一确认退出()
        #win32api.ShellExecute(0, 'open', r'E:\PY学习文件\BTT影视剧\工具集\FTP上传http网页文件.py', '', '', 1)

        #self.模具一一换头部信息()

    def 模具一一重新激活城通网盘客户端(self):


        类名 = ''
        窗口标题 = "城通网盘客户端"

        if len(类名) == 0:
            窗口句柄 = win32gui.FindWindow(None, 窗口标题)
        else:  #
            窗口句柄 = win32gui.FindWindow(类名, None)
        类名 = win32gui.GetClassName(窗口句柄)
        窗口标题 = win32gui.GetWindowText(窗口句柄)
        print('类名', 类名)
        print('窗口标题', 窗口标题)
        print('窗口句柄', 窗口句柄)

        win32gui.ShowWindow(窗口句柄, 11)  # 即使拥有窗口的线程被挂起也会最小化。在从其他线程最小化窗口时才使用这个参数
        time.sleep(1)  # 等待  # 增加延迟
        if 'ALDrive' in 类名 or 'Mozilla' in 类名 or 'Chrome' in 类名 or '城通网盘' in 窗口标题:
            win32gui.ShowWindow(窗口句柄, 3)  # 激活并显示一个窗口。窗口最大化
        else:  #
            win32gui.ShowWindow(窗口句柄, 1)  # 激活并显示一个窗口。如果窗口被最小化或最大化，系统将其恢复到原来的尺寸和大小。
        time.sleep(2)  # 等待  # 增加延迟

        # ====确认程序已经 激活
        像素匹配 = pag.pixelMatchesColor(625, 100, (102,136,166))  # FTP目录颜色
        if 像素匹配 == True:
            print('确认程序已经 激活')

        else:  # 否则  False
            time.sleep(20)  # 等待  # 增加延迟
            print('程序未激活，等待10秒')

    def 模具一一下探至链接目录(self):
        pag.moveTo(311, 37)  # 鼠标 定位 公有位 按钮
        pag.rightClick()  # 右击
        time.sleep(2)  # 等待  # 增加延迟

        pag.moveTo(60, 250)  # 鼠标 定位 上传网盘 按钮
        pag.rightClick()  # 右击
        time.sleep(2)  # 等待  # 增加延迟

        pag.moveTo(300, 240)  # 鼠标 定位 最新 按钮
        pag.rightClick()  # 右击
        time.sleep(2)  # 等待  # 增加延迟

        self.首次 = 0
        self.影视类型='电视剧'
        self.模具一一影视类型提取链接()
        self.首次 = 998
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
        if self.首次 != 0:
            pag.moveTo(30, 150)  # 鼠标 定位 全选 按钮
            pag.rightClick()  # 右击
            time.sleep(1)  # 等待  # 增加延迟

        pag.moveTo(30, 150)  # 鼠标 定位 全选 按钮
        pag.rightClick()  # 右击

        time.sleep(5)  # 等待  # 增加延迟
        pag.moveTo(1080, 150)  # 鼠标 定位 分享 按钮
        pag.rightClick()  # 右击

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
        #pyautogui.alert('确认退出')

        pag.hotkey('altleft', 'f4')  # press()一次完整的击键.hotkey('ctrl','c'):复制内容
        # pag.moveTo(1255, 25)  # 鼠标 定位 分享 方框栏
        # pag.rightClick()  # 右击
        time.sleep(1)  # 等待  # 增加延迟



类=类一一提取链接()
win32api.ShellExecute(0, 'open', r'E:\PY学习文件\BTT影视剧\py快捷方式\FTP上传http网页文件.py.lnk', '', '', 1)


