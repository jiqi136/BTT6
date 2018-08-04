import win32api
import time
import os




def 换ip连接():
    # coding:gbk
    print('宽带连接进行时.....')
    os.system(r"rasphone -h 宽带连接")  # xxx0是你的拨号名称，xp下默认是“宽带连接”。
    os.system(r"rasdial 宽带连接 02007044432@163.gd  77341859")  # xxx0同上，xxx1 拨号用户名 ，xxx2拨号密码。

    print('宽带连接完成')
    print('等待10秒，启动浏览器..........')
    time.sleep(10)


def 启动文本每日提醒():
    win32api.ShellExecute(0, 'open', 'notepad.exe', 'D:\桌面\每日提醒.txt', '', 1)
    # 运行位于E:\book\code目录中的MessageBox.py脚本
    #  win32api.ShellExecute(0, 'open', 'E:\\book\\code\\MessageBox.py', '', '', 1)\\

    # 启动火狐()
    # win32api.ShellExecute(0, 'open', 'D:\\2D安装盘\\FF45\\firefox.exe', '', '', 1)
    win32api.ShellExecute(0, 'open', 'https://www.baidu.com/s?tn=baidutop10&rsv_idx=2&wd=%E5%B9%BF%E5%B7%9E%E5%A4%A9%E6%B0%94%E9%A2%84%E6%8A%A5', '', '', 1)
    print('已启动浏览器，耐心等待........')
    time.sleep(20)


#win32api.ShellExecute(0, 'open','http://www.weather.com.cn/weather/101280101.shtml','','', 1)




换ip连接()
启动文本每日提醒()

