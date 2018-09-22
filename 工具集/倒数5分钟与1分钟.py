#import pyautogui
import time
import win32api



def 模具一一弹窗关闭(说明):
    内容="""import time
print('{}，10秒后关闭弹窗' )
time.sleep(10)  # 等待  # 增加延迟""".format(说明)# '{}'

    文本 = open(r"E:\PY学习文件\BTT影视剧\工具集\关闭弹窗.py", 'w', encoding='UTF-8')

    文本.write(内容)  # read() #读取
    文本.close()
    time.sleep(1)  # 等待  # 增加延迟
    win32api.ShellExecute(0, 'open', r'E:\PY学习文件\BTT影视剧\工具集\关闭弹窗.py', '', '', 1)




for i in  '54321':
    print('倒数',i,'分钟')
    time.sleep(60)  # 等待

#pyautogui.alert('5分钟时间已到')
模具一一弹窗关闭('5分钟时间到')


等待用户输入=input("\n按下 enter 确认键后继续倒数1分钟。")
print("继续，倒数1分钟")


time.sleep(60)# 等待

#pyautogui.alert('1分时间已到')

模具一一弹窗关闭('1分钟 开水时间 到')

time.sleep(5)# 等待




