# -*- coding:utf-8


import re  # 正则式
import time  # 时间
import pyautogui as pag #模拟鼠标键盘操作
import pyautogui#模拟鼠标键盘操作
import win32api  # 时间
import ctypes
import tkinter

import tkinter.messagebox
import sys

from tkinter import *
import tkinter
import threading



from 发贴推广.推广公共库 import 类一一公共库# 导入模块

class 类一一百度号注册(类一一公共库):  # 调用 类的模具 self.模具一一数据库()
    def __init__(self):

        self.模具一一倒计时自动关闭的窗口()

    def 模具一一倒计时自动关闭的窗口(self):

        # 创建应用程序窗口,设置标题与大小
        root = tkinter.Tk()
        root.title('倒计时自动关闭的窗口')
        root['width'] = 400
        root['height'] = 300
        # 不允许改变窗口大小
        root.resizable(False, False)
        # 创建text组件,放置一些文字
        richtText = tkinter.Text(root, width=380)
        richtText.place(x=10, y=10, width=380, height=230)
        richtText.insert('0.0', '假设阅读这些文字需要10秒钟时间')

        # 显示倒计时的labe1
        lbTime = tkinter.Label(root, fg='red', anchor='w')
        lbTime.place(x=10, y=250, width=150)

        def autoClose():
            for i in range(10):
                lbTime['text'] = '距离窗口关闭还有{}'.format(10 - i)
                time.sleep(1)  # 等待  # 增加延迟

            root.destroy()

        # 创建并启动线程
        t = threading.Thread(target=autoClose)
        t.start()
        root.mainloop()





    def 模具一一浏览器访问百度(self):
        from selenium import webdriver  # 浏览的驱动

        def 换头部信息():
            self.模具一一知乎换头部信息()
            头部信息 ="user-agent="+self.头部信息['User-Agent']
            print('头部信息:', 头部信息)
            options.add_argument(头部信息)

        options = webdriver.ChromeOptions()  # 设置中文
        options.add_argument('disable-infobars')  # 加启动配置 去除正在受到自动软件的控制
        用户数据目录 = r'C:\Users\Administrator\AppData\Local\Google\Chrome\User Data'
        options.add_argument('--user-data-dir={}'.format(用户数据目录))#  '{}'  # 设置成用户自己的数据目录
        换头部信息()
        浏览器操作 = webdriver.Chrome(chrome_options=options)  # 打开chrome浏览器
        # driver = webdriver.Chrome(chrome_options=option)

        # url = "https://baidu.com"  # 注册页面  https://www.zhihu.com/signup?next=%2Fexplore
        url = "http://www.atool.org/useragent.php"
        浏览器操作.get(url)
        time.sleep(10)  # 等待  # 增加延迟

        浏览器操作.refresh()  # 刷新当前页面

        pyautogui.alert('完成')  # 弹窗 提示

    def 模具一一弹窗输入字符串(self):

        # win32api.ShellExecute(0, 'open', r'E:\PY学习文件\BTT影视剧\发贴推广\关闭弹窗.py', '', '', 1)

        pag.moveTo(505, 297)  # 鼠标 方位
        pag.PAUSE = 5
        pag.rightClick()  # 右击

        pyautogui.alert('这个消息弹窗是文字+OK按钮')

        # pag.hotkey('ctrlleft', 'F4')  # 确认  关闭当前标签页   按钮

        #选项字符串 = pyautogui.confirm('这个消息弹窗是文字+OK+Cancel按钮')
        #print(选项字符串)
        #输入字符串 = pyautogui.prompt('这个消息弹窗是让用户输入字符串，单击OK')
        #print(输入字符串) # 空值为  None



    def 模具一一协程(self):
        # 协程代码案例1 https://blog.csdn.net/july_whj/article/details/80919552
        def 分支协程():
            print(" 分支1，等待返回")
            x = yield # yield  分支协程暂停  等待返回 激活信号，调度主线程继续
            print(" 分支继续", x)

        # 主线程
        调度控制 = 分支协程()
        print(111)
        # 可以使用sc,send(None),效果一样
        next(调度控制)  # 预计 启动协程
        print(222)



        try:  # 调用异常处理，应对易发生错误的位置
            调度控制.send("主进程给协程发一个信号")  #  send调用 重新激活分支协程

        except StopIteration:  # 异常处理
            print("异常不理会")

        else:  # 必须放在所有的except子句之后。这个子句将在try子句没有发生任何异常的时候执行。
            pass




    def 模具一一图像对比(self):
        self.模具一一重新激活浏览器窗口()
        time.sleep(1)  # 等待  # 增加延迟
        开始时间计数 = int(time.time())

        图像位置= r'C:\下载中转站\图像测试.PNG'


        条件循环 = 0
        while 条件循环 == 0:
            图形坐标 = pag.locateOnScreen(图像位置)

            if 图形坐标 == None:
                #pyautogui.alert('图形坐标为空') # 弹窗 提示
                pag.press('pagedown')  # press()一次完整的击键.hotkey('ctrl','c') 向下翻页
                time.sleep(0.5)  # 等待

            else:  # 否则

                获得坐标中心点= pag.center((图形坐标[0], 图形坐标[1], 图形坐标[2], 图形坐标[3]))

                结束时间计数 = int(time.time())
                用时 = 结束时间计数 - 开始时间计数
                print('操作用时:', 用时, '秒')

                pag.moveTo(获得坐标中心点[0], 获得坐标中心点[1])  # 移动 鼠标 方位
                pag.rightClick()  # 右击
                time.sleep(1)  # 等待  # 增加延迟

                pyautogui.alert('完成') # 弹窗 提示
                条件循环 = 998
    def 模具一一提取像素(self):

        self.模具一一重新激活浏览器窗口()
        time.sleep(1)  # 等待  # 增加延迟
        img = pag.screenshot()
        横坐标, 竖坐标 = 1142, 132
        print(img.getpixel((横坐标, 竖坐标)))  # 提取像素
        像素匹配 = pag.pixelMatchesColor(横坐标, 竖坐标, (25, 132, 255))
        if 像素匹配 == True:

            print(像素匹配, '像素值正确')

        else:  # 否则

            print(像素匹配, '像素值不对')


        pag.moveTo(横坐标, 竖坐标)  # 鼠标 方位
        # pag.rightClick()  # 右击
        pyautogui.alert('完成')# 弹窗 提示


if __name__ == '__main__':

    类 = 类一一百度号注册()
