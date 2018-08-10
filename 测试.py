import pyautogui as pag
import win32api
import time
import os


import pyautogui as pag
import pyautogui
img=pag.screenshot()

合名='旷尽管BTT影视'


f = open(r'E:\PY学习文件\BTT影视剧\发贴推广\复制内容.txt', "w")  # 保存cookie 文件
f.write(合名)
f.close()

win32api.ShellExecute(0, 'open',  r'E:\PY学习文件\BTT影视剧\发贴推广\复制内容.txt','', '', 1)
time.sleep(2)  # 等待
pag.hotkey('ctrlleft', 'a')  # press()一次完整的击键。hotkey(‘ctrl’,’c’)：
pag.PAUSE = 0.5  # 增加延迟
pag.hotkey('ctrlleft', 'c')  # press()一次完整的击键。hotkey(‘ctrl’,’c’)：
pag.PAUSE = 0.5  # 增加延迟
pag.hotkey('altleft', 'F4')  # press()一次完整的击键。hotkey(‘ctrl’,’c’)：






