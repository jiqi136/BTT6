import requests  # 网页浏览
import re  # 正则式
import time
import os  # 正则式
import pyautogui as pag
import win32clipboard as w# 提取剪切板内容
import win32con#提取剪切板内容


class 类一一公共库:  # 调用 类的模具 self.模具一一数据库()
    def __init__(self):

        self.模具一一重新激活浏览器窗口()
        self.模具一一页面内容()
        self.模具一一提取数字ip()

    def 模具一一页面内容(self):
        time.sleep(0.5)  # 等待  # 增加延迟
        pag.hotkey('ctrlleft', 'a')  # press()一次完整的击键.hotkey('ctrl','c'):复制内容

        time.sleep(0.5)  # 等待  # 增加延迟

        pag.hotkey('ctrlleft', 'c')  # press()一次完整的击键.hotkey('ctrl','c'):复制内容

        self.页面内容 = self.模具一一获取剪切板内容()

        #print('页面内容\n',self.页面内容)

    def 模具一一提取数字ip(self):

        for 行内容 in self.页面内容.split("\n"):
            if '您现在的' in 行内容:
                IP行=行内容

                规则 = ".{1,}IP："
                IP = re.sub(规则, '',IP行)

                IP = IP.strip()  # 默认则是去除空格

                # 提取 前面（去除最后一个符号后面字符）

                规则 = r'.{1,}(?=\..*)'  # .*(文本)  *号是贪婪的，放置在最前方会消耗尽可能多的字符。
                文本列表 = re.findall(规则, IP)  # 提取 前面
                IP文本 = 文本列表[0]

                return  IP文本# 返回



    def 模具一一获取剪切板内容(self):# 获取剪切板内容
        w.OpenClipboard()
        t = w.GetClipboardData(win32con.CF_TEXT)
        w.CloseClipboard()

        t = t.decode('gbk')  # 解码为 编程的中文

        return t
    def 模具一一重新激活浏览器窗口(self):
        print('重新激活浏览器窗口')
        pag.hotkey('winleft', 'd')  # press()一次完整的击键.hotkey('ctrl','c'):热键函数 .keyDown()按下某个键.keyUp()松开某个键.

        time.sleep(0.5)  # 等待  # 增加延迟
        pag.moveTo(258, 962)  # 鼠标移动X.Y 方位  重新激活浏览器窗口 在CMD 与  回归桌面之间
        pag.rightClick()  # 右击
        time.sleep(1)  # 等待  # 增加延迟





类=类一一公共库()