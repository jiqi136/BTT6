
import win32gui

import time

#time.sleep(1.5)  # 等待  # 增加延迟
类名 = 'TkTopLevel'
窗口标题 = ""

if len(类名) == 0:
	窗口句柄 = win32gui.FindWindow(None, 窗口标题)
else:  #
	窗口句柄 = win32gui.FindWindow(类名, None)
类名 = win32gui.GetClassName(窗口句柄)
窗口标题 = win32gui.GetWindowText(窗口句柄)

#time.sleep(1)  # 等待  # 增加延迟
win32gui.ShowWindow(窗口句柄, 11)  # 即使拥有窗口的线程被挂起也会最小化。在从其他线程最小化窗口时才使用这个参数
