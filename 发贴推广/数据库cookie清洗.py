import pyautogui as pag
import win32con#提取剪切板内容

import win32clipboard as w# 提取剪切板内容
import time

def 模具一一写入剪切板内容( 内容):  # 写入剪切板内容
    内容 = str(内容).encode('gbk')  # encoding='UTF-8'为 WIN7 系统 的中文
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_TEXT, 内容)
    w.CloseClipboard()

def 模具一一清洗cookie(sql命令):
    sql命令值=sql命令
    time.sleep( 0.5 )
    pag.moveTo(495, 150)  # 鼠标移动X.Y 方位  打开数据库的sql 命令界面 按钮
    pag.rightClick()  # 右击
    模具一一写入剪切板内容(sql命令值)

    time.sleep( 4)
    pag.moveTo(830, 590)  # 鼠标移动X.Y 方位  sql 命令清除 按钮
    pag.rightClick()  # 右击
    # time.sleep( 0.5 )
    # pag.moveTo(530, 300)  # 鼠标移动X.Y 方位  sql 命令输入框
    # pag.rightClick()  # 右击



    time.sleep( 0.5 )
    pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c')

    time.sleep( 0.5 )
    pag.moveTo(1212, 678)  # 鼠标移动X.Y 方位  执行 按钮
    pag.rightClick()  # 右击

    time.sleep( 3 )

def 模具一一FF浏览器窗口():
    time.sleep(1)  # 等待 )
    pag.moveTo(490, 920)  # 鼠标移动X.Y 方位  打开数据库的sql 命令界面 按钮
    pag.rightClick()  # 右击

    time.sleep(2)  # 等待 )


模具一一FF浏览器窗口()

表名='知乎帐号'
表名='知乎发贴帐号'
sql命令="UPDATE `{}` SET `cookie`= replace(`cookie`,'\"[','[')".format(表名)
模具一一清洗cookie(sql命令)
sql命令="UPDATE `{}` SET `cookie`= replace(`cookie`,']\"',']')".format(表名)
模具一一清洗cookie(sql命令)





