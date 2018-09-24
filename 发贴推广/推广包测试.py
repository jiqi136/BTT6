# -*- coding:utf-8


import re  # 正则式
import time  # 时间
import pyautogui as pag #模拟鼠标键盘操作
import pyautogui#模拟鼠标键盘操作
import win32api  # 时间
import ctypes
import tkinter

import tkinter.messagebox
import win32gui

from tkinter import *
import tkinter
import threading
import easygui

from tkinter import *           # 导入 tkinter 库


import os

import win32gui
import win32api
import win32con
from PIL import ImageGrab
import win32com
from win32com.client import Dispatch,constants




##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

from 推广公共库 import 类一一公共库# 导入模块 E:\PY学习文件\BTT影视剧\电影与合集一并发协程.py

class 类一一百度号注册(类一一公共库):  # 调用 类的模具 self.模具一一数据库()
    def __init__(self):
        #win32api.ShellExecute(0, 'open', r'E:\PY学习文件\BTT影视剧\py快捷方式\关闭弹窗.py.lnk', '', '', 1)


        self.模具一一提取像素()

    def 模具一一激活窗口二(self):
        类名 = ''

        窗口标题 = "自.动.点.击.器"

        if len(类名) == 0:
            窗口句柄 = win32gui.FindWindow(None, 窗口标题)
            窗口句柄 = win32gui.FindWindowEx(0, 0, None, 窗口标题)

        else:  #
            窗口句柄 = win32gui.FindWindow(类名, None)
        类名 = win32gui.GetClassName(窗口句柄)
        窗口标题 = win32gui.GetWindowText(窗口句柄)
        print('类名', 类名)
        print('窗口标题', 窗口标题)
        print('窗口句柄', 窗口句柄)

        win32gui.ShowWindow(窗口句柄, 11)  # 即使拥有窗口的线程被挂起也会最小化。在从其他线程最小化窗口时才使用这个参数
        time.sleep(1)  # 等待  # 增加延迟
        if '记事本' in 窗口标题 or 'QQ' in 窗口标题 or 'Tk' in 类名:
            win32gui.ShowWindow(窗口句柄, 1)  # 激活并显示一个窗口。如果窗口被最小化或最大化，系统将其恢复到原来的尺寸和大小。
        else:  #
            win32gui.ShowWindow(窗口句柄, 3)  # 激活并显示一个窗口。窗口最大化
        time.sleep(1)  # 等待  # 增加延迟
        # win32gui.SendMessage(窗口句柄, win32con.WM_CLOSE)  # 关闭窗口
        if 窗口句柄 > 0:
            第一个控件句柄 = win32gui.FindWindowEx(窗口句柄, None, None, None)  # 获取hld下第一个为edit控件的句柄

            窗口的菜单句柄 = win32gui.GetSubMenu(第一个控件句柄,2)
            print('窗口的菜单句柄', 窗口的菜单句柄)
    def 模具一一激活窗口(self):
        类名 = ''

        窗口标题="技術討論區 | 草榴社區 - t66y.com - Mozilla Firefox"

        if len(类名)==0:
            窗口句柄 = win32gui.FindWindow( None,窗口标题)

        else:  #
            窗口句柄 = win32gui.FindWindow(类名, None)
        类名 = win32gui.GetClassName(窗口句柄)
        窗口标题 = win32gui.GetWindowText(窗口句柄)
        print('类名', 类名)
        print('窗口标题', 窗口标题)
        print('窗口句柄', 窗口句柄)

        win32gui.ShowWindow(窗口句柄, 11)#即使拥有窗口的线程被挂起也会最小化。在从其他线程最小化窗口时才使用这个参数
        time.sleep(1)  # 等待  # 增加延迟
        if 'ALDrive'in 类名 or 'Chrome'in 类名:
            win32gui.ShowWindow(窗口句柄, 3)  # 激活并显示一个窗口。窗口最大化

        elif 'Mozilla'in 类名:  #
            win32gui.ShowWindow(窗口句柄, 3)  # 激活并显示一个窗口。窗口最大化
            time.sleep(2)  # 等待  # 增加延迟
            pag.hotkey('altleft', 'tab')  # press()一次完整的击键.hotkey('ctrl','c'):复制内容
            time.sleep(2)  # 等待  # 增加延迟
            pag.hotkey('altleft', 'tab')  # press()一次完整的击键.hotkey('ctrl','c'):复制内容


        else:  #
            win32gui.ShowWindow(窗口句柄, 1)  # 激活并显示一个窗口。如果窗口被最小化或最大化，系统将其恢复到原来的尺寸和大小。
        time.sleep(1)  # 等待  # 增加延迟
        # win32gui.SendMessage(窗口句柄, win32con.WM_CLOSE)  # 关闭窗口





        """ ////////////////////////////////////////////
        nCmdShow：指定窗口如何显示。如果发送应用程序的程序提供了STARTUPINFO结构，则应用程序第一次调用ShowWindow时该参数被忽略。
        否则，在第一次调用ShowWindow函数时，该值应为在函数WinMain中nCmdShow参数。在随后的调用中，该参数可以为下列值之一：
        #     win32gui.ShowWindow(窗口句柄, win32con.SW_SHOWNORMAL)
        等同于 win32gui.ShowWindow(窗口句柄, 8)
       
        11  SW_FORCEMINIMIZE：在WindowNT5.0中最小化窗口，即使拥有窗口的线程被挂起也会最小化。
          在从其他线程最小化窗口时才使用这个参数。nCmdShow=11。
        0   SW_HIDE：隐藏窗口并激活其他窗口。nCmdShow=0。
        1   SW_SHOWNORMAL：激活并显示一个窗口。如果窗口被最小化或最大化，系统将其恢复到原来的尺寸和大小。
            应用程序在第一次显示窗口的时候应该指定此标志。nCmdShow=1。
        2   SW_SHOWMINIMIZED：激活窗口并将其最小化。nCmdShow=2。
        3   SW_MAXIMIZE：最大化指定的窗口。nCmdShow=3。
        4   SW_SHOWNOACTIVATE：以窗口最近一次的大小和状态显示窗口。激活窗口仍然维持激活状态。nCmdShow=4。
        5   SW_SHOW：在窗口原来的位置以原来的尺寸激活和显示窗口。nCmdShow=5。
        6   SW_MINIMIZE：最小化指定的窗口并且激活在Z序中的下一个顶层窗口。nCmdShow=6。
        7   SW_SHOWMINNOACTIVE：窗口最小化，激活窗口仍然维持激活状态。nCmdShow=7。
        8   SW_SHOWNA：以窗口原来的状态显示窗口。激活窗口仍然维持激活状态。nCmdShow=8。
        9   SW_RESTORE：激活并显示窗口。如果窗口最小化或最大化，则系统将窗口恢复到原来的尺寸和位置。
            在恢复最小化窗口时，应用程序应该指定这个标志。nCmdShow=9。
        10  SW_SHOWDEFAULT：依据在STARTUPINFO结构中指定的SW_FLAG标志设定显示状态，STARTUPINFO 结构是由启动应用程序的程序传递
            给CreateProcess函数的。nCmdShow=10。
            
        ////////////////////////////////////////////
        各程序             标题          类名 
        种子上传工具       ALDrive       ALDriveMutex
        文本              新建文本文档.txt - 记事本  类名 Notepad
        Opera浏览器        IP.cn - IP 地址查询 | 地理位置 | 手机归属地 - Opera   类名 Chrome_WidgetWin_1
        Firefox浏览器      技術討論區 | 草榴社區 - t66y.com - Mozilla Firefox     类名 MozillaWindowClass
        Chrome浏览器       微博-随时随地发现新鲜事 - Google Chrome                类名 被Opera浏览器代替了
        城通网盘客户端     城通网盘客户端                                         类名 被Opera浏览器代替了
        QQ                  QQ                                                  类名 TXGuiFoundation
        弹窗              提醒                                                  类名 TkTopLevel

        """





    def 模具一一窗口标题二(self):
        # 获取当前所有句柄
        # 搜索子窗口

        窗口句柄 = win32gui.FindWindow("MozillaWindowClass", None)

        print('窗口句柄', 窗口句柄)
        #  枚举子窗口
        win32gui.ShowWindow(窗口句柄, win32con.SW_SHOWMAXIMIZED)



        if 窗口句柄 > 0:




            第一个控件句柄 = win32gui.FindWindowEx(窗口句柄, None, None, None)  # 获取hld下第一个为edit控件的句柄
            第二个控件句柄 = win32gui.FindWindowEx(第一个控件句柄, None, None, None)  # 获取hld下第一个为edit控件的句柄

            if 第二个控件句柄 == 0:
                print('第一个控件句柄', 第一个控件句柄)
                win32gui.SetForegroundWindow(第一个控件句柄)  # 指定句柄设置为前台，也就是激活

                窗口的菜单句柄 = win32gui.GetMenu(第一个控件句柄)
                print('窗口的菜单句柄', 窗口的菜单句柄)

                # 获取窗口文本不含截尾空字符的长度
                #  参数：窗口句柄； 消息类型； 参数WParam； 参数IParam
                窗口文本 = win32api.SendMessage(第一个控件句柄, win32con.WM_GETTEXTLENGTH, 0, 0) + 1
                print('窗口文本', 窗口文本)

            else:  # 否则
                print('第二个控件句柄', 第二个控件句柄)
                win32gui.SetForegroundWindow(第二个控件句柄)  # 指定句柄设置为前台，也就是激活

                窗口的菜单句柄 = win32gui.GetMenu(第二个控件句柄)
                print('窗口的菜单句柄', 窗口的菜单句柄)

                time.sleep(3)  # 等待  # 增加延迟

                # 获取窗口文本不含截尾空字符的长度
                #  参数：窗口句柄； 消息类型； 参数WParam； 参数IParam
                窗口文本 = win32api.SendMessage(第二个控件句柄, win32con.WM_GETTEXTLENGTH, 0, 0) +1
                print('窗口文本', 窗口文本)


            time.sleep(5)  # 等待  # 增加延迟

    def 模具一一窗口标题(self):

        # 窗口句柄 = win32gui.FindWindow(None, "win32gui.FindWindowEx 当前窗口_百度搜索")
        #窗口句柄 = win32gui.FindWindow("MozillaWindowClass", None)

        # 获取某个句柄的类名和标题
        # 标题 = win32gui.GetWindowText(窗口句柄)
        # 类名 = win32gui.GetClassName(窗口句柄)



        # 新建文本文档.txt - 记事本  类名 Notepad

        # IP.cn - IP 地址查询 | 地理位置 | 手机归属地 - Opera   类名 Chrome_WidgetWin_1
        #技術討論區 | 草榴社區 - t66y.com - Mozilla Firefox     类名 MozillaWindowClass
        #微博-随时随地发现新鲜事 - Google Chrome


        窗口标题 =r'IP.cn - IP 地址查询 | 地理位置 | 手机归属地 - Opera'  # 此处假设主窗口名为tt
        窗口句柄 = win32gui.FindWindow(None, 窗口标题)
        print('窗口句柄',窗口句柄)
        time.sleep(1)  # 等待  # 增加延迟
        if 窗口句柄 > 0:
            第一个控件句柄 = win32gui.FindWindowEx(窗口句柄, None, None, None)  # 获取hld下第一个为edit控件的句柄
            第二个控件句柄 = win32gui.FindWindowEx(第一个控件句柄, None, None, None)  # 获取hld下第一个为edit控件的句柄
            for i in '1234578902':

                pag.hotkey('altleft','shiftleft','tab')  # press()一次完整的击键.hotkey('ctrl','c'):热键函数 .keyDown()按下某个键.keyUp()松开某个键.




                time.sleep(2)  # 等待  # 增加延迟
            if 第二个控件句柄==0:
                print('第一个控件句柄',第一个控件句柄)
                win32gui.SetForegroundWindow(第一个控件句柄)  # 指定句柄设置为前台，也就是激活



            else:  # 否则
                print('第二个控件句柄',第二个控件句柄)
                win32gui.SetForegroundWindow(第二个控件句柄)  # 指定句柄设置为前台，也就是激活



    def 模具一一窗口图形(self):

      
        top = tkinter.Tk()

        # def helloCallBack():

        #tkMessageBox.showinfo("Hello Python", "Hello Runoob")

        B = tkinter.Button(top, text="点我", command=helloCallBack)

        B.pack()
        top.mainloop()

    def 模具一一弹窗关闭(self,说明):
        内容="""import time
print('{}，10秒后关闭弹窗' )
time.sleep(10)  # 等待  # 增加延迟""".format(说明)# '{}'

        文本 = open(r"E:\PY学习文件\BTT影视剧\工具集\关闭弹窗.py", 'w', encoding='UTF-8')

        文本.write(内容)  # read() #读取
        文本.close()
        time.sleep(1)  # 等待  # 增加延迟
        win32api.ShellExecute(0, 'open', r'E:\PY学习文件\BTT影视剧\工具集\关闭弹窗.py', '', '', 1)

    def 模具一一窗口二(self):

        i = 1


        easygui.msgbox("别忘了打卡！", title="提醒", ok_button="知道啦")#
        time.sleep(2)

        return  # 返回

    def 模具一一控制本地窗口(self):
        # 根据类名及标题名查询句柄
        # 窗口句柄 = win32gui.FindWindow("notepad", "新建文本文档.txt")

        窗口句柄 =win32ui.FindWindow('新建文本文档', None)

        print(窗口句柄)
        # 指定句柄设置为前台，也就是激活
        win32gui.SetForegroundWindow(窗口句柄)


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
        richtText.insert('0.0', '假设阅读这些文字需要3秒钟时间')

        # 显示倒计时的labe1
        lbTime = tkinter.Label(root, fg='red', anchor='w')
        lbTime.place(x=10, y=250, width=150)

        def autoClose():
            for i in range(3):
                lbTime['text'] = '距离窗口关闭还有{}'.format(3 - i)
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
        time.sleep(1)  # 等待  # 增加延迟 105,252,216
        img = pag.screenshot()
        横坐标, 竖坐标 = 649, 880
        print(img.getpixel((横坐标, 竖坐标)))  # 提取像素
        像素匹配 = pag.pixelMatchesColor(横坐标, 竖坐标, (0,136,204))
        if 像素匹配 == True:

            print(像素匹配, '像素值正确')

        else:  # 否则

            print(像素匹配, '像素值不对')


        pag.moveTo(横坐标, 竖坐标)  # 鼠标 方位
        # pag.rightClick()  # 右击
        pyautogui.alert('完成')# 弹窗 提示


if __name__ == '__main__':

    类 = 类一一百度号注册()
