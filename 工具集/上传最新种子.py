# -*- coding:utf-8
import pyautogui as pag
import win32api  # 操作本地文件
import win32clipboard as w# 提取剪切板内容
import win32con#提取剪切板内容
import re  # 正则式
import time  # 时间
import pyautogui

import os  # 本地操作



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
        print('等待 10分钟')
        time.sleep(600)  # 等待  # 增加延迟


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

