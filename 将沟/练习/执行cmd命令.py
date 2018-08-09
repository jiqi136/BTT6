import win32api #处理电脑系统文件和目录
import time #时间
import pyautogui as pag





pag.PAUSE = 0.5  # 增加延迟
pag.moveTo(368, 178)  # 鼠标移动X.Y 方位
pag.rightClick()  # 右击pag.rightClick() 左击pag.leftClick() 中击 pag.middleClick()
pag.PAUSE = 0.5  # 增加延迟
pag.hotkey('enter')  # press()一次完整的击键。hotkey(‘ctrl’,’c’)：热键函数 。keyDown()按下某个键。keyUp()松开某个键。

with open('E:\PY学习文件\BTT影视剧\将沟\练习\CMD命令文本.txt', 'r') as 文本内容:
    CMD命令=(文本内容.split(r"\n"))[0]


time.sleep(2)
pag.hotkey('CMD命令')  # press()一次完整的击键。hotkey(‘ctrl’,’c’)：热键函数 。keyDown()按下某个键。keyUp()松开某个键。

pag.PAUSE = 0.5  # 增加延迟
pag.moveTo(500, 430)  # 鼠标移动X.Y 方位
pag.pag.leftClick()   # 右击pag.rightClick() 左击pag.leftClick() 中击 pag.middleClick()


pag.PAUSE = 0.5  # 增加延迟
pag.hotkey('e')  # press()一次完整的击键
pag.PAUSE = 0.5  # 增加延迟


pag.hotkey('p')  # press()一次完整的击键
pag.PAUSE = 0.5  # 增加延迟

pag.hotkey('enter')  # press()一次完整的击键。hotkey(‘ctrl’,’c’)：热键函数 。keyDown()按下某个键。keyUp()松开某个键。
#pag.hotkey("Python manage.py runserver")  # press()一次完整的击键。hotkey(‘ctrl’,’c’)：热键函数 。keyDown()按下某个键。keyUp()松开某个键。

