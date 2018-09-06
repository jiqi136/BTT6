import pyautogui as pag

import time

class 类一一点击分享():        # 调用 类的模具 self.模具一一数据库()
    def __init__(self):
        self.模具一一重新激活浏览器窗口()
        self.模具一一翻页25次()

    def 模具一一重新激活浏览器窗口(self):
        print('重新激活浏览器窗口')
        pag.hotkey('winleft', 'd')  # press()一次完整的击键.hotkey('ctrl','c'):热键函数 .keyDown()按下某个键.keyUp()松开某个键.

        pag.PAUSE = 0.5  # 增加延迟
        pag.moveTo(370, 962)  # 鼠标移动X.Y 方位  重新激活浏览器窗口 在CMD 与  回归桌面之间
        pag.rightClick()  # 右击

        pag.PAUSE = 2  # 增加延迟


    def 模具一一点击分享与按键向下(self):
        pag.moveTo(323, 216)  # 鼠标移动X.Y 方位  指定第一栏为指针 定位
        pag.rightClick()  # 右击


        for 数字遍历 in range(1, 1001, 1):  # 遍历100
            pag.PAUSE = 0.3  # 增加延迟
            pag.moveTo(218, 120)  # 鼠标移动X.Y 方位  点击分享 按钮
            pag.rightClick()  # 右击

            time.sleep(0.5)  # 等待
            pag.moveTo(436, 423)  # 鼠标移动X.Y 方位  ’创建分开链接‘按钮
            pag.rightClick()  # 右击

            time.sleep(0.5)  # 等待
            pag.hotkey('altleft', 'F4')  # 关闭   分享页面

            time.sleep(0.3)  # 等待

            if 数字遍历 < 30:
                pag.moveTo(323, 216)  # 鼠标移动X.Y 方位  指定第一栏为指针 定位
                pag.rightClick()  # 右击

                for 遍历 in range(1,数字遍历, 1):  # 遍历100
                    time.sleep(0.1)  # 等待
                    pag.press('down')  # press()一次完整的击键.hotkey('ctrl','c'):热键函数 .  按键向下

            else:  # 否则
                self.模具一一指针定位按键向下()







    def 模具一一指针定位按键向下(self):
        pag.moveTo(342, 888)  # 鼠标移动X.Y 方位  指定最后一栏为指标 定位
        pag.rightClick()  # 右击
        time.sleep(0.3)  # 等待
        pag.press('down')  # press()一次完整的击键.hotkey('ctrl','c'):热键函数 .  按键向下



    def 模具一一翻页25次(self):
        for 数字遍历 in range(1, 26, 1):  # 遍历100
            self.模具一一点击分享与按键向下()
            pag.PAUSE = 0.5  # 增加延迟
            pag.moveTo(763, 925)  # 鼠标移动X.Y 方位  ’翻页‘按钮
            pag.rightClick()  # 右击

            time.sleep(8)  # 等待

类=类一一点击分享()


