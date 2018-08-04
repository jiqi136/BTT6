
import requests #人性化的 浏览器
import re  #正则表达式
import time #时间
import os #处理电脑系统文件和目录
import pymysql #mysql数据库
import random #随机数
from lxml import etree#解析与定位网页
import datetime  # 时间
import shutil
import pyautogui as pag
import pyautogui
import string




def 模具一邀請註冊碼遍历():
    小写字母的字符串='abcdefghijklmnopqrstuvwxyz'
    数字字符串='0123456789'

    for 字母 in 小写字母的字符串:  # 范围 range
        for 数字 in 数字字符串:  # 范围 range
            邀請註冊碼='{0}a9fb85fd0e2f9e{1}'.format(字母,数字)#不换行 end=""
            print('邀請註冊碼:', 邀請註冊碼)


            for 数字 in range(20):  # 范围 range
                pag.press('backspace')  # 清空输入框


time.sleep(2) # 等待
pag.PAUSE = 0.3  # 等待
#清空输入框
pag.moveTo(583,609)
pag.PAUSE = 0.3  #
pag.click(button='right')
pag.PAUSE = 0.3  # 等待

pag.PAUSE = 0.3  # 等待

pag.typewrite('Hello world')
pag.PAUSE = 0.3  # 等待

# 检查邀請註冊碼
pag.moveTo(700,600)
pag.PAUSE = 0.3  # 等待
pag.click(button='right') # 点击
pag.PAUSE = 2  # 等待


img=pag.screenshot()
(r, g, b) = img.getpixel((735, 649))
print('颜色像素:',r,g,b)
if r==255:
    print('颜色像素配对完成:')

else:# 否则
    print('颜色像素为数字:')


                    





