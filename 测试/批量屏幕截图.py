import pyautogui as pag
import time


def 批量屏幕截图():
    time.sleep(2)

    横坐标 = 0
    宽度 = 1273 - 横坐标

    竖坐标 = 21
    高度 = 881 - 竖坐标


    条件循环 = 1


    while 条件循环 == 1:


        img = pag.screenshot(region=(横坐标,竖坐标,宽度 ,高度))

        图片名=r'C:\下载中转站\批量屏幕截图2\{}.jpg'.format(time.time())
        pag.press('Spacebar')# 暂停

        img.save(图片名)
        print('完成屏幕截图：',图片名)
        time.sleep(0.1)
        pag.press('Spacebar')  # 继续


批量屏幕截图()