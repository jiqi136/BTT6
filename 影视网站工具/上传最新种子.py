# -*- coding:utf-8
import pyautogui as pag
import win32api  # 操作本地文件
import win32gui#窗口控件
import win32clipboard as w# 提取剪切板内容
import win32con#提取剪切板内容
import re  # 正则式
import time  # 时间
import pyautogui

import os  # 本地操作



class 类一一ALDrive上传文件:  # 调用 类的模具 self.模具一一数据库()
    def __init__(self):
        win32api.ShellExecute(0, 'open', r'E:\Ean\ESTsoft\ALDrive\ALDrive.exe', '', '', 1)
        time.sleep(0.5)  # 等待  # 增加延迟

        print('回归桌面')
        pag.hotkey('winleft', 'd')  # press()一次完整的击键.hotkey('ctrl','c'):热键函数 .keyDown()按下某个键.keyUp()松开某个键.
        time.sleep(10)  # 等待  # 增加延迟

        self.模具一一重新激活上传软件()

        self.模具一一选择城通最新网盘登录()


        #self.模具一一确认最新的网盘登录()
        self.模具一一下探目录与打开上传窗口()
        self.模具一一上传窗口选择文件目录()
        self.模具一一确认上传完成()

        self.模具一一退出上传软件()

    def 模具一一重新激活上传软件(self):


        类名 = 'ALDriveMutex'
        窗口标题 = ""

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
        if 'ALDrive' in 类名 or 'Mozilla' in 类名 or 'Chrome' in 类名:
            win32gui.ShowWindow(窗口句柄, 3)  # 激活并显示一个窗口。窗口最大化
        else:  #
            win32gui.ShowWindow(窗口句柄, 1)  # 激活并显示一个窗口。如果窗口被最小化或最大化，系统将其恢复到原来的尺寸和大小。
        time.sleep(2)  # 等待  # 增加延迟

    def 模具一一选择城通最新网盘登录(self):

        # ====确认程序已经 激活
        窗口标题 = "站点地图"
        窗口句柄 = win32gui.FindWindow(None, 窗口标题)
        类名 = win32gui.GetClassName(窗口句柄)
        窗口标题 = win32gui.GetWindowText(窗口句柄)
        win32gui.ShowWindow(窗口句柄, 11)  # 即使拥有窗口的线程被挂起也会最小化。在从其他线程最小化窗口时才使用这个参数
        time.sleep(1)  # 等待  # 增加延迟
        win32gui.ShowWindow(窗口句柄, 3)  # 激活并显示一个窗口。窗口最大化
        time.sleep(2)  # 等待  # 增加延迟


        pag.moveTo(53, 86)  # 鼠标移动X.Y 方位  第一的目录
        pag.rightClick()  # 右击
        time.sleep(1)  # 等待  # 增加延迟

        像素匹配 = pag.pixelMatchesColor(70,118, (230,189,41))  # FTP目录颜色
        if 像素匹配 == True:

            print('第一的目录 ，已经展开')

        else:  # 否则  False
            pag.press('enter')  # press()一次完整的击键.hotkey('ctrl','c'): 关闭 帐号窗口
            print('展开第一的目录')
            time.sleep()  # 等待  # 增加延迟

        pag.press('down')  # press()一次完整的击键.hotkey('ctrl','c'): 关闭 帐号窗口
        time.sleep(1)  # 等待  # 增加延迟

        pag.press('enter')  # press()一次完整的击键.hotkey('ctrl','c'): 关闭 帐号窗口
        time.sleep(3)  # 等待  # 增加延迟



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
        time.sleep(2)  # 等待  # 增加延迟

        pag.moveTo(596, 520)  # 鼠标 定位 ‘f 盘’按钮
        pag.rightClick()  # 右击
        time.sleep(2)  # 等待  # 增加延迟
        pag.press('enter')  # press()一次完整的击键.hotkey('c  trl','c')  确认
        time.sleep(2)  # 等待  # 增加延迟

        pag.moveTo(650, 538)  # 鼠标 定位 ‘下载种子目录’目录  按钮
        pag.rightClick()  # 右击
        time.sleep(2)  # 等待  # 增加延迟
        pag.press('enter')  # press()一次完整的击键.hotkey('c  trl','c')  确认
        time.sleep(2)  # 等待  # 增加延迟

        pag.moveTo(570, 333)  # 鼠标 定位 ‘上传网盘’ 目录  按钮
        pag.rightClick()  # 右击
        time.sleep(2)  # 等待  # 增加延迟
        pag.press('enter')  # press()一次完整的击键.hotkey('c  trl','c')  确认
        time.sleep(2)  # 等待  # 增加延迟

        pag.moveTo(720, 333)  # 鼠标 定位 ‘最新’ 目录  按钮
        pag.rightClick()  # 右击
        time.sleep(2)  # 等待  # 增加延迟
        pag.hotkey('altleft', 'o')  # press()一次完整的击键.hotkey('ctrl','c'):复制内容

        time.sleep(1)  # 等待  # 增加延迟

    def 模具一一确认上传完成(self):
        def 模具一一确认完成():
            pag.hotkey('winleft', 'up')  # press()一次完整的击键.hotkey('ctrl','c'):复制内容 窗口最大化
            time.sleep(1)  # 等待  # 增加延迟
            pag.moveTo(5520, 180)  # 鼠标移动X.Y 方位  我的站点 目录
            pag.rightClick()  # 右击
            time.sleep(1)  # 等待  # 增加延迟
            # ====颜色对比 确认上传完成
            像素匹配 = pag.pixelMatchesColor(119, 61, (246,131,6))  # 取消 按钮  颜色
            if 像素匹配 == True:
                print('第1层目录已展开')
                pag.moveTo(326, 286)  # 鼠标移动X.Y 方位  我的站点 目录
                pag.rightClick()  # 右击
                上传完成 = 0

            else:  # 否则  False
                print('上传完成')
                上传完成=998
            return 上传完成 # 返回



        pag.hotkey('winleft', 'up')  # press()一次完整的击键.hotkey('ctrl','c'):复制内容 窗口最大化
        time.sleep(1)  # 等待  # 增加延迟
        pag.moveTo(5520, 180)  # 鼠标移动X.Y 方位  我的站点 目录
        pag.rightClick()  # 右击

        print('等待 12分钟')
        time.sleep(720)  # 等待  # 增加延迟
        self.模具一一重新激活上传软件()
        上传完成 =模具一一确认完成()
        if 上传完成 !=0:
            return # 返回

        for i in '0123456':
            print('等待 5分钟')
            time.sleep(300)  # 等待  # 增加延迟
            self.模具一一重新激活上传软件()
            上传完成 =模具一一确认完成()
            if 上传完成 != 0:
                return  # 返回


    def 模具一一退出上传软件(self):

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
win32api.ShellExecute(0, 'open', r'E:\PY学习文件\BTT影视剧\py快捷方式\城通网盘提取链接.py.lnk', '', '', 1)

