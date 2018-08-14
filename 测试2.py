import pyautogui as pag
import ctypes

#引入winapi
gdi32 = ctypes.windll.gdi32
user32 = ctypes.windll.user32

#获取句柄
hdc = user32.GetDC(None)



img=pag.screenshot()

pag.PAUSE = 0.5  # 增加延迟
pag.moveTo(367, 957)  # 鼠标移动X.Y 方位 激活浏览器
pag.rightClick()  # 右击pag.rightClick() 左击pag.leftClick() 中击 pag.middleClick()

pag.PAUSE = 2.5
横坐标=213
竖坐标=701


for i in '5646416464':
    横坐标 =横坐标+3
    竖坐标 = 竖坐标 + 3
    pag.moveTo(横坐标, 竖坐标)
    pag.PAUSE = 0.5  # 增加延迟

    print(img.getpixel((横坐标, 竖坐标)))

