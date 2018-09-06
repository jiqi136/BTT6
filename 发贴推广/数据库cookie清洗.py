import pyautogui as pag
import win32con#提取剪切板内容

import win32clipboard as w# 提取剪切板内容

def 模具一一写入剪切板内容( 内容):  # 写入剪切板内容
    内容 = str(内容).encode('gbk')  # encoding='UTF-8'为 WIN7 系统 的中文
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_TEXT, 内容)
    w.CloseClipboard()

def 模具一一清洗cookie(sql命令):
    sql命令值=sql命令
    pag.PAUSE = 0.5  # 增加延迟
    pag.moveTo(495, 150)  # 鼠标移动X.Y 方位  打开数据库的sql 命令界面 按钮
    pag.rightClick()  # 右击
    模具一一写入剪切板内容(sql命令值)

    pag.PAUSE = 4 # 增加延迟
    pag.moveTo(830, 590)  # 鼠标移动X.Y 方位  sql 命令清除 按钮
    pag.rightClick()  # 右击
    # pag.PAUSE = 0.5  # 增加延迟
    # pag.moveTo(530, 300)  # 鼠标移动X.Y 方位  sql 命令输入框
    # pag.rightClick()  # 右击



    pag.PAUSE = 0.5  # 增加延迟
    pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c')

    pag.PAUSE = 0.5  # 增加延迟
    pag.moveTo(1212, 678)  # 鼠标移动X.Y 方位  执行 按钮
    pag.rightClick()  # 右击

    pag.PAUSE = 3  # 增加延迟

def 模具一一FF浏览器窗口():
    pag.PAUSE = 0.5  # 增加延迟
    pag.moveTo(465, 957)  # 鼠标移动X.Y 方位  打开数据库的sql 命令界面 按钮
    pag.rightClick()  # 右击
    pag.PAUSE =2  # 增加延迟


模具一一FF浏览器窗口()


sql命令="UPDATE `知乎帐号` SET `cookie`= replace(`cookie`,'\"[','[')"
模具一一清洗cookie(sql命令)
sql命令="UPDATE `知乎帐号` SET `cookie`= replace(`cookie`,']\"',']')"
模具一一清洗cookie(sql命令)





