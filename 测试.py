
# -*- coding:utf-8
import re  # 正则式
import win32gui #窗口控件
类名 = 'TkTopLevel'
窗口标题 = ""

if len(类名) == 0:
	窗口句柄 = win32gui.FindWindow(None, 窗口标题)
else:  #
	窗口句柄 = win32gui.FindWindow(类名, None)
类名 = win32gui.GetClassName(窗口句柄)
窗口标题 = win32gui.GetWindowText(窗口句柄)

win32gui.ShowWindow(窗口句柄, 11)  # 即使拥有窗口的线程被挂起也会最小化.在从其他线程最小化窗口时才使用这个参数

文本列表 = 文本.split("n")

文本 = str(原文本).replace("25", "120") #替换   , 1) 次数 1

time.sleep(1) # 等待
                    

