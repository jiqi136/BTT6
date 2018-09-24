# -*- coding:utf-8



import time  # 时间
import pyautogui as pag #模拟鼠标键盘操作
import pyautogui#模拟鼠标键盘操作


from 推广公共库 import 类一一公共库# 导入模块 E:\PY学习文件\BTT影视剧\电影与合集一并发协程.py

class 类一一百度号注册(类一一公共库):  # 调用 类的模具 self.模具一一数据库()
    def __init__(self):
        self.模具一一高位换头部信息()


        self.模具一一重新激活浏览器窗口()
        self.模具一一二星号循环()

    def 模具一一1星号循环(self):
        内容 = """0123456789qwertyuiopasdfghjklzxcvbnm"""
        for 第一字符 in 内容:
            self.注册码 = 'd{}4{}2d26e5759833'.format(第一字符)# {}
            self.模具一一验证注册码()

        pyautogui.alert('注册码已轮空')  # 弹窗 提示

    def 模具一一二星号循环(self):
        内容 = """56789qwertyuiopasdfghjklzxcvbnm"""
        内容二 = """0123456789qwertyuiopasdfghjklzxcvbnm"""
        for 第一字符 in 内容:
            for 第二字符 in 内容二:
                self.注册码 = 'd{}4{}2d26e5759833'.format(第一字符, 第二字符) # {}
                self.模具一一验证注册码()
            self.模具一一换IP再刷新()
        pyautogui.alert('注册码已轮空')  # 弹窗 提示

    def 模具一一换IP再刷新(self):
        self.模具一一换ip连接二()
        pag.hotkey('ctrlleft', 'r')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(5)  # 等待  # 增加延迟 模具一一等待过程

    def 模具一一验证注册码(self):
        img = pag.screenshot()

        #====清空输入框
        pag.moveTo(617, 533)  # 鼠标 方位
        pag.rightClick()  # 右击
        time.sleep(0.3)  # 等待  # 增加延迟
        pag.hotkey('ctrlleft', 'a')  # press()一次完整的击键.hotkey('ctrl','c'):
        time.sleep(0.5)  # 等待  # 增加延迟
        pag.press('delete')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.5)  # 等待  # 增加延迟# : d*4*2d26e5759833

        # ====输入注册码


        self.模具一一写入剪切板内容(self.注册码)  # 输入手机号码
        pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.3)  # 等待  # 增加延迟 模具一一等待过程

        # ====验证注册码
        pag.moveTo(672, 533)  # 鼠标 方位
        pag.rightClick()  # 右击
        time.sleep(0.3)  # 等待  # 增加延迟

        # ===模具一一等待过程

        self.模具一一等待过程()



        # ==== 像素匹配----注册码
        像素匹配 = pag.pixelMatchesColor(513, 563, (255,0,0))
        if 像素匹配 == True:
            #pyautogui.alert('测试')  # 弹窗 提示
            return  # 结束模具，返回空值‘nome’


            print(像素匹配, '像素值正确')

        else:  # 否则
            print(像素匹配, '注册码正确')
            print(self.注册码, '注册码正确')
            pyautogui.alert('注册码正确')# 弹窗 提示



    def 模具一一等待过程(self):
        条件循环 = 0
        计数=0
        while 条件循环 == 0:
            计数 =计数+1
            # ==== 像素匹配---等待过程
            像素匹配 = pag.pixelMatchesColor(539, 563, (0, 0, 0))
            if 像素匹配 == True:
                time.sleep(0.5)  # 等待  # 增加延迟
            else:  # 否则
                条件循环 =998
                return  # 返回
            if 计数 == 20:
                # ====验证注册码
                pag.moveTo(672, 533)  # 鼠标 方位
                pag.rightClick()  # 右击
                time.sleep(0.3)  # 等待  # 增加延迟
            if 计数 ==50:
                self.模具一一换ip连接二()
                pag.hotkey('ctrlleft', 'r')  # press()一次完整的击键.hotkey('ctrl','c')
                time.sleep(5)  # 等待  # 增加延迟 模具一一等待过程

                # ====清空输入框
                pag.moveTo(617, 533)  # 鼠标 方位
                pag.rightClick()  # 右击
                time.sleep(0.3)  # 等待  # 增加延迟

                # ====输入注册码
                self.模具一一写入剪切板内容(self.注册码)  # 输入手机号码
                pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c')
                time.sleep(0.3)  # 等待  # 增加延迟 模具一一等待过程
                # ====验证注册码
                pag.moveTo(672, 533)  # 鼠标 方位
                pag.rightClick()  # 右击
                time.sleep(0.3)  # 等待  # 增加延迟
                计数 = 0




if __name__ == '__main__':

    类 = 类一一百度号注册()