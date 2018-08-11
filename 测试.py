import pyautogui as pag
import win32api
import time
import os
import re

链接文件名='【AngelEcho】アイドル事変IdolIncidents偶像事变第07话.torrent: https://u13288317.ctfile.com/fs/13288317-302962076'
规则 = ': https.{1,}'  #
文件名 = re.sub(规则,'',链接文件名)  #


文件名 = 文件名.replace(".zip", "") #替换   , 1) 次数 1
文件名 = 文件名.rstrip()  # 指定删除的字符串末尾的字符（默认为空格）
print('文件名',文件名)


规则 = '.{1,}: https'  #
目录链接 = re.sub(规则, 'https',链接文件名)  #
目录链接 = 目录链接.rstrip()  # 指定删除的字符串末尾的字符（默认为空格）
print('目录链接',目录链接)






