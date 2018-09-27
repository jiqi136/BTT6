
import win32gui
import win32con
import time


标题 = 'C:\Windows\py.exe'# 最小化，自身的窗口
窗口句柄 = win32gui.FindWindow( None,标题)
win32gui.ShowWindow(窗口句柄, 11)  # 即使拥有窗口的线程被挂起也会最小化。在从其他线程最小化窗口时才使用这个参数

print("等待5秒")
#easygui.msgbox("这是一个弹窗", title="提醒", ok_button="知道啦")#

类名 = 'TkTopLevel'
窗口句柄 = win32gui.FindWindow(类名, None)
win32gui.ShowWindow(窗口句柄, 11)  # 即使拥有窗口的线程被挂起也会最小化。在从其他线程最小化窗口时才使用这个参数
time.sleep(0.5)  # 等待  # 增加延迟
win32gui.ShowWindow(窗口句柄, 1)  # 激活并显示一个窗口。如果窗口被最小化或最大化，系统将其恢复到原来的尺寸和大小。
time.sleep(5)  # 等待  # 增加延迟


win32gui.ShowWindow(窗口句柄, 11)  # 即使拥有窗口的线程被挂起也会最小化。在从其他线程最小化窗口时才使用这个参数
time.sleep(0.5)  # 等待  # 增加延迟


win32gui.ShowWindow(窗口句柄, 1)  # 激活并显示一个窗口。如果窗口被最小化或最大化，系统将其恢复到原来的尺寸和大小
time.sleep(0.5)  # 等待  # 增加延迟
win32gui.SendMessage(窗口句柄, win32con.WM_CLOSE)  # 关闭窗口