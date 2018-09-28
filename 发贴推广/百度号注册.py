# -*- coding:utf-8

import requests  # 网页浏览
import re  # 正则式
import time  # 时间
import datetime  # 时间
import os  # 本地操作
import pymysql  # 数据库
import random  # 随机
from lxml import etree  # 网页分析
import shutil  # 移动复制文件目录
from lxml import html  # 网页分析
import win32api,win32gui  # 操作本地文件
import win32clipboard as w# 提取剪切板内容
import win32con#提取剪切板内容

import pyautogui as pag #模拟鼠标键盘操作
import pyautogui#模拟鼠标键盘操作
from 推广公共库 import 类一一公共库# 导入模块


"""
工具栏左1 导出COOKIE
工具栏2 设置浏览头部信息

passport.baidu.com
tieba.baidu.com
i.baidu.com
www.baidu.com

"""

class 类一一百度号注册(类一一公共库):  # 调用 类的模具 self.模具一一数据库()
    def __init__(self,帐号类型):
        self.帐号类型 =帐号类型
        self.模具一一高位换头部信息()
        self.首次 = 0
        self.激活窗口图像位置= r'E:\PY学习文件\BTT影视剧\py快捷方式\opera浏览器.PNG'#
        self.手机号码验证数 = 0
        self.临时图片目录 = r"F:\影视发帖推广\临时图片"
        self.旧目录路径 = r"F:\影视发帖推广\贴吧顶贴\头像\百度主号上传小头像"
        self.颜色变化 = ''
        self.激活窗口坐标=[196,918]


        self.模具一一换ip连接二()
        self.模具一一图像对比激活窗口()
        self.模具一一清除浏览器历史缓存()

        print(' 注册界面 页面 ,颜色检测通过')
        # ===

        self.模具一一提取影视剧数据库里的易码短信平台账户信息()
        self.模具一一提取推广库里的百度发贴帐号()
        内容 = """柔蓉安蓝春语彤晴语菱霜紫莲翠烟南寻慕蕊雪海沛宛晓菡巧
                听卉靖枫梓晨丽丹佩惠月玉婉晓玲倩瑞静颖棋芹萍幻露灵含雅薇瑶丹丽云亿仪伊伶佳依俞俪倩偲兰冰凝凡凤叆呤
                爱姿惠娇媛妩萱娈瑷悠源赫晗贻楚梦琪忆柳桃慕兰岚香沛菡珊曼菱寒薇忆旋芷蕾代
                芙盼蝶筠瑶珍谷荷画嘉囡女如妃妍妙妮妹姐姑姗姝姞姣梅梦楠檀欢欣歆毓水洁涵淑清滟滢漪漫澜灵煜燕
                玉玥玫环玲珂珊珍珠姬娅娆娇娉娜娟娣娥娴婉婕婧婵婷媚媛嫔嫣嫱安宛宜宝容巧希彤彩心忆念怀怜思怡情惠
                慧敏旭春晴曼月琦琪琬琰琳琴琼瑗瑛瑜瑶瑾璇璐璟白盈盼碧秀筠红绮美翠艳芃芊芝芬芮芯芳芷芸苑若苹茗茜茵茹荔荭
                荷莉莎莲莹菁菡菲萍萱蓉蓓蔓蕊蕾薇诗语贞采钰银雅雨雪雯霏霖霜霞露青靖静音韵颖颜香馨黛"""
        内容 = 内容.replace("\n", "")
        self.内容 = 内容.replace(" ", "")

        self.字符集 = """0123456789qwertyuiopasdfghjklzxcvbnm"""
        self.电影美剧表 = ['电影', '美剧', '动漫']

        百度号注册网址 = 'https://passport.baidu.com/v2/?reg&tt=1537956495492&overseas=undefined&gid=8515458-8F51-407D-AEBC-A53A793AC038&tpl=mn&u=https%3A%2F%2Fwww.baidu.com%2F'
        浏览头网址 = 'baidu.com'

        计数器 = 0
        for 字符 in self.内容:
            for 影视类型 in self.电影美剧表:
                self.百度顶贴名=字符+影视类型
                self.跳过循环 = ''
                self.手机号码验证数 = 0
                self.手机号码验证换ip次数 = 0


                if self.百度顶贴名 in self.已注册帐号手机号:
                    continue  # 跳过当前循环,继续进行下一轮循环

                计数器 = 计数器 + 1
                if 计数器 > 30:
                    条件循环 = 998
                开始时间计数 = int(time.time())

                self.模具一一百度注册布置浏览头()

                self.模具一一地址栏输入网址(百度号注册网址)

                self.模具一一输入百度用户名()

                self.模具一一输入手机号()
                if '跳过循环' not in self.跳过循环:

                    self.模具一一输入密码()

                    self.模具一一输入短信内容()

                if '跳过循环' not in self.跳过循环:


                    self.模具一一确认注册()

                    self.模具一一提取登录界面的cookie()
                    self.模具一一保存数据库一百度发贴帐号等()

                    self.模具一一百度上传图片头像()

                self.模具一一清除浏览器历史缓存()

                # ===

                self.模具一一换ip连接二()
                self.模具一一图像对比激活窗口()

                结束时间计数 = int(time.time())
                用时 = 结束时间计数 - 开始时间计数
                print('操作:', 用时, '秒')
                time.sleep(1)  # 等待

                # pyautogui.alert('确认后继续')
                time.sleep(5)  # 等待  # 增加延迟

    def 模具一一获取百度接收的手机号码(self):
        # 通信令牌token = self.cookie
        self.项目编号 = "13043"

        #排除号段 = '170.171'
        排除号段 = '170.171.131.132.134.135.136.137.138.139'
        获取手机号码接口网址 = "http://api.fxhyd.cn/UserInterface.aspx?action=getmobile&token={}&itemid={}&excludeno={}".format(
            self.通信令牌token, self.项目编号, 排除号段)
        网址内容 = self.模具一一打开的网址请求返回网页内容(获取手机号码接口网址)

        self.手机号码 = 网址内容.text.replace("success|", "")  # 替换   , 1) 次数 1
        print('手机号码:', self.手机号码)

    def 模具一一百度项目拉黑手机号码(self):
        # 通信令牌token = self.cookie

        百度项目拉黑手机号码接口网址 = "http://api.fxhyd.cn/UserInterface.aspx?action=addignore&token={}&itemid={}&mobile={} ".format(
            self.通信令牌token, self.项目编号,self.手机号码 )
        网址内容 = self.模具一一打开的网址请求返回网页内容(百度项目拉黑手机号码接口网址)
        print('百度项目拉黑手机号码:')

    def 模具一一输入手机号(self):


        for 次数 in range(1,10):  # 范围 range
            if 次数==5:
                self.跳过循环 = '跳过循环'
                return  # 结束模具，返回空值

            # ========定位能 输入手机号框
            time.sleep(0.5)  # 等待
            pag.moveTo(378, 321)  # 鼠标移动X.Y 方位 定位 输入手机号框
            pag.rightClick()  # 右击


            # ========
            self.模具一一获取百度接收的手机号码()
            if len(self.手机号码) <10 or self.手机号码 in self.已注册帐号手机号:
                self.模具一一获取百度接收的手机号码()
            time.sleep(0.5)  # 等待

            self.模具一一写入剪切板内容(self.手机号码)# 输入手机号码
            pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c'):

            time.sleep(0.5)  # 等待  # 增加延迟
            # ==定位 输入密码  框
            pag.moveTo(323, 381)  # 鼠标移动X.Y 方位 定位 输入密码  框
            pag.rightClick()  # 右击
            time.sleep(2)  # 等待  # 增加延迟



            # ===手机已注册 提醒弹窗 ,颜色对比
            已注册像素匹配 = pag.pixelMatchesColor(817, 559, (63, 137, 236))

            if 已注册像素匹配 == True :

                print(已注册像素匹配, '手机已注册')
                # ==取消 手机已注册 提醒弹窗
                pag.moveTo(706,561)  # 鼠标移动X.Y 方位 定位 取消 按钮
                pag.rightClick()  # 右击

                self.模具一一百度项目拉黑手机号码()
                self.手机号码验证数 =self.手机号码验证数+1
                if self.手机号码验证数 ==2:
                    print('手机号码验证5次，跳过循环')
                    self.模具一一清除浏览器历史缓存()


                    time.sleep(50)  # 等待  # 增加延迟


                    self.模具一一换ip连接二()
                    self.模具一一图像对比激活窗口()


                    self.手机号码验证数 =0
                    #self.跳过循环 ='跳过循环'

                    self.模具一一输入百度用户名()

                    #return #返回
                continue  # 跳过当前循环，继续进行下一轮循环




            # ===手机已注册 提醒弹窗 ,颜色对比
            上限像素匹配 = pag.pixelMatchesColor(600,317, (252, 67, 67))



            if 上限像素匹配 == True:
                print('手机号的申请次数已达上限，跳过循环')
                self.模具一一百度项目拉黑手机号码()
                self.手机号码验证数 = self.手机号码验证数 + 1
                if self.手机号码验证数 ==5:
                    print('手机号码验证5次，跳过循环')

                    self.模具一一换ip连接二()
                    self.手机号码验证数 =0
                    #self.跳过循环 ='跳过循环'


                # ========刷新
                self.模具一一清除浏览器历史缓存()
                self.模具一一输入百度用户名()

                self.模具一一输入手机号()
                continue  # 跳过当前循环，继续进行下一轮循环
        #self.模具一一测验手机无注册过()
            break  # 结束循环



        self.已注册帐号手机号 = self.手机号码 + self.已注册帐号手机号




    def 模具一一输入密码(self):
        # ======密码=======
        pag.moveTo(323, 381)  # 鼠标移动X.Y 方位 定位 输入密码  框
        pag.rightClick()  # 右击
        time.sleep(0.5)  # 等待  # 增加延迟

        密码数字 = random.randrange(100000, 1000000)
        self.密码 = "qq{}Q%".format(密码数字)
        print('密码:', self.密码)


        self.模具一一写入剪切板内容(self.密码)
        pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c'):
        time.sleep(0.5)  # 等待  # 增加延迟

    def 模具一一点击获取手机验证码(self):
        # ======密码=======
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.5)  # 等待  # 增加延迟
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.5)  # 等待  # 增加延迟
        pag.press('enter')  # press()一次完整的击键.hotkey('ctrl','c')
        time.sleep(0.3)  # 等待  # 增加延迟

    def 模具一一输入短信内容(self):
        self.模具一一点击获取手机验证码()
        self.模具一一开关提醒声()
        time.sleep(5)  # 等待  # 增加延迟


        self.模具一一获取百度短信()
        self.模具一一图像对比激活窗口()

        if len(self.短信内容) == 0 or '跳过循环' in self.跳过循环:
            return  # 返回

        规则 = '\d{6}'
        内容列表 = re.findall(规则, self.短信内容)  # 提取
        self.短信内容 = 内容列表[0]



        pag.moveTo(335, 440)  # 鼠标移动X.Y 方位 定位 注册页面 空白栏
        pag.rightClick()  # 右击
        time.sleep(0.5)  # 等待  # 增加延迟
        self.模具一一写入剪切板内容(self.短信内容)
        pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c'):
        time.sleep(0.5)  # 等待  # 增加延迟

    def 模具一一确认注册(self):

        time.sleep(0.5)  # 等待  # 增加延迟
        pag.moveTo(243, 493)  # 鼠标移动X.Y 方位  定位 用户协议 按钮
        pag.rightClick()  # 右击

        time.sleep(0.5)  # 等待  # 增加延迟
        pag.moveTo(400, 540)  # 鼠标移动X.Y 方位  定位 注册 按钮
        pag.rightClick()  # 右击

        time.sleep(5)  # 等待  # 增加延迟

        # ===网页加载 ,颜色对比
        self.坐标 = [649, 234]
        self.颜色像素 = [35, 25, 220]
        self.等待秒数 = 3
        self.模具一一网页加载颜色对比()
        print(' 注册成功 页面 ,颜色检测通过')
        # ===

    def 模具一一获取百度短信(self):


        获取短信网址 = "http://api.fxhyd.cn/UserInterface.aspx?action=getsms&token={}&itemid={}&mobile={}".format(
            self.通信令牌token,
            self.项目编号, self.手机号码)
        """&release=1  自动释放号码标识符 若该参数值为1时,获取到短信的同时系统将自己释放该手机号码.若要继续使用该号码,请勿带入该参数."""

        条件循环 = 0
        while 条件循环 < 5:  # 条件循环  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            self.短信内容 = ''

            for i in '123456':
                print('等待 15秒:')
                time.sleep(14)  # 等待
                网址内容 = self.模具一一打开的网址请求返回网页内容(获取短信网址)
                if 'success' in 网址内容.text:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                    self.短信内容 = 网址内容.text.replace("success|", "")  # 替换   , 1) 次数 1
                    print('短信内容:', self.短信内容)
                    条件循环 = 998

                    return  # 返回
                elif '3001' in 网址内容.text:  # 其它条件.
                    print('短信尚未到达:3001,应继续调用取短信接口,直到超时为止.')

                else:  # 否则
                    print('请求失败:', 网址内容.text)
            条件循环 = 条件循环 + 1
            self.模具一一图像对比激活窗口()

            pag.moveTo(490, 442)  # 鼠标移动X.Y 方位  发送验证码 按钮
            pag.rightClick()  # 右击pag.rightClick()


        释放手机号码接口 = "http://api.fxhyd.cn/UserInterface.aspx?action=release&token={}&itemid={}&mobile={}".format(
            self.通信令牌token, self.项目编号, self.手机号码)
        释放手机号码网址内容 = self.模具一一打开的网址请求返回网页内容(释放手机号码接口)

        self.跳过循环='跳过循环'



    def 模具一一输入百度用户名(self):
        # ===网页加载 ,颜色对比
        self.坐标 = [503,548]
        self.颜色像素 = [63,137,236]
        self.等待秒数 = 3
        self.模具一一网页加载颜色对比()
        print(' 刷新 页面 ,颜色检测通过')
        # ===


        pag.moveTo(255, 205)  # 鼠标移动X.Y 方位 定位 注册页面 空白栏
        pag.rightClick()  # 右击
        time.sleep(0.5)  # 等待  # 增加延迟
        pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c') 光标定位于 用户名
        time.sleep(0.5)  # 等待  # 增加延迟

        if '顶贴号' in self.帐号类型: #  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            self.随机取名=self.模具一一随机取女名()
        else:# 否则
            self.随机取名 =self.模具一一百度随机取名合并网址名()

        self.模具一一写入剪切板内容(self.随机取名)
        pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c'):
        time.sleep(0.5)  # 等待  # 增加延迟



    def 模具一一百度随机取名合并网址名(self):



        #内容 = 内容.replace("\n", "")
        #内容 = 内容.replace(" ", "")

        #名 = random.choice(内容)

        #名 = str(self.字符集[0])

        #if len(self.字符集) == 1:
        #self.字符集 = """0123456789qwertyuiopasdfghjklzxcvbnm_"""
        #else:  # 否则
        #self.字符集 = self.字符集[1:]  #


        #电影美剧名 = random.choice(电影美剧表)
        # 合名次序= random.choice('影视')
        # if '影' in 合名次序:

        # else:  # 否则
        # 合名 =  '3e38、com'+电影美剧名 +名






        合名 = self.百度顶贴名 + '3e38_com'


        print('随机取名合并网址名', 合名)
        self.已注册帐号手机号 =合名+self.已注册帐号手机号
        return 合名  # 返回

    def 模具一一百度上传图片头像(self):
        def 模具一一进入个人中心():
            # ======消除COOKIE 的界面======
            pag.moveTo(83,171)  # 鼠标移动X.Y 方位 定位 空白处
            pag.rightClick()  # 右击
            time.sleep(2)  # 等待  # 增加延迟


            # ======进入个人  中心======
            pag.moveTo(1056, 113)  # 鼠标移动X.Y 方位 定位 ID帐号 链接
            pag.rightClick()  # 右击
            time.sleep(3)  # 等待  # 增加延迟

            # ===网页加载 ,颜色对比
            self.坐标 = [1012,190]
            self.颜色像素 = [76, 95, 119]
            self.等待秒数 = 3
            self.模具一一网页加载颜色对比()
            print(' 个人中心 页面 ,颜色检测通过')
            # ===

        def 模具一一更换头像():
            # ======更换头像 ======
            pag.moveTo(247, 359)  # 鼠标移动X.Y 方位 定位 更换头像 链接
            time.sleep(1)  # 等待  # 增加延迟
            pag.rightClick()  # 右击
            time.sleep(4)  # 等待  # 增加延迟

            # ===网页加载 ,颜色对比
            self.坐标 = [164, 222]
            self.颜色像素 = [46, 130, 255]
            self.等待秒数 = 3
            self.模具一一网页加载颜色对比()
            print(' 头像设置 页面 ,颜色检测通过')
            # ===

        def 模具一一退出两个页面回到百度首页():
            for i in '12':
                pag.hotkey('ctrlleft', 'F4')  # press()一次完整的击键.hotkey('ctrl','c') 全选 图片
                time.sleep(1)  # 等待  # 增加延迟

        self.模具一一清空临时图片目录()
        self.模具一一移动图片文件至临时图片目录()




        模具一一进入个人中心()
        模具一一更换头像()


        self.模具一一百度选择图片头像()
        模具一一退出两个页面回到百度首页()

    def 模具一一百度选择图片头像(self):
        # ======上传图片头像 ======
        pag.moveTo(472,382)  # 鼠标移动X.Y 方位  选择图片 按钮
        pag.rightClick()  # 右击
        time.sleep(3)  # 等待  # 增加延迟



        if self.首次==0:
            self.模具一一选择图片头像窗口最大化()
            self.模具一一图片目录地址框()

            self.首次 =998
        self.模具一一上传图片窗口选择图片()

        #==保存头像
        time.sleep(3)  # 等待  # 增加延迟
        print('等待3秒,图片上传')

        # ====== 保存头像 ======
        pag.moveTo(473,691)  # 鼠标移动X.Y 方位  保存头像 按钮
        pag.rightClick()  # 右击
        time.sleep(1)  # 等待  # 增加延迟

    """=========数据库======================="""

    def 模具一一提取推广库里的百度发贴帐号(self):
        # 提取数据库里的过滤网址
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "", "影视发帖推广", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句
        sql = "SELECT `帐号`, `注册手机号` FROM `推广帐号` WHERE `类型`='{}' ".format(self.帐号类型)#不换行 '{}'
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        帐号手机号组列表 = cursor.fetchall()
        self.已注册帐号手机号=str(帐号手机号组列表)

        # 关闭数据库连接
        db.close()

    def 模具一一保存数据库一百度发贴帐号等(self):
        print('打开数据库连接')
        # 打开数据库连接,
        今天时间 = str(time.strftime("%y-%m-%d", time.localtime()))

        db = pymysql.connect("localhost", "root", "", "影视发帖推广", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句

        sql = """INSERT INTO `推广帐号`( `类型`, `帐号`, `密码`, `注册手机号`, `注册日期`, `cookie`) VALUES
         ("{}","{}","{}","{}",'{}','{}')""".format(self.帐号类型,self.随机取名, self.密码, self.手机号码, 今天时间,
                                                          self.cookie)  # 不换行 end=""




        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            print('=保存数据库一知乎用户密码')
        except:
            # 如果发生错误则回滚
            print('=====================数据库执行发生错误:===============')
            db.rollback()
        # 关闭数据库连接
        db.close()

    """========浏览器操作====================="""
        
    def 模具一一百度注册布置浏览头(self):
        浏览头网址列表=['passport.baidu.com','tieba.baidu.com','www.baidu.com','i.baidu.com']
        self.模具一一高位换头部信息()
        pag.hotkey('altleft', '3')  # 鼠标移动X.Y 方位  cookie插件布置 页面
        # pag.moveTo(1252 , 49)  # 鼠标移动 定位  确定布置浏览头 按钮
        # pag.rightClick()  # 右击
        time.sleep(2)  # 等待  # 增加延迟

        # ===网页加载 ,颜色对比
        self.坐标 = [933, 145]
        self.颜色像素 = [228, 218, 188]

        self.等待秒数 = 3
        self.模具一一网页加载颜色对比()
        print(' 布置浏览头 页面 ,颜色检测通过')
        # ===


        for 浏览头网址 in 浏览头网址列表:




            # pag.moveTo(1009, 93)  # 鼠标移动 定位  布置浏览头 空白处
            # pag.rightClick()  # 右击
            # time.sleep(1)  # 等待  # 增加延迟
            # ==============================
            pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c') 添加浏览头网址 方框


            self.模具一一写入剪切板内容(浏览头网址)
            time.sleep(1)  # 等待  # 增加延迟
            pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c')
            time.sleep(1)  # 等待  # 增加延迟


            # ====================================

            pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')


            self.模具一一写入剪切板内容(self.头部信息['User-Agent'])
            time.sleep(1)  # 等待  # 增加延迟
            pag.hotkey('ctrlleft', 'v')  # press()一次完整的击键.hotkey('ctrl','c')
            time.sleep(0.5)  # 等待  # 增加延迟

            # ====================================
            pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')  定位  add添加 按钮

            time.sleep(1)  # 等待  # 增加延迟
            pag.press('enter')  # press()一次完整的击键.hotkey('ctrl','c')
            time.sleep(1)  # 等待  # 增加延迟
            # ==========重回开始============
            pag.press('tab')  # press()一次完整的击键.hotkey('ctrl','c')  定位  add添加 按钮

            time.sleep(1)  # 等待  # 增加延迟

        pag.moveTo(981, 52)  # 鼠标移动 定位  页面 空白处
        time.sleep(2)  # 等待  # 增加延迟


class 类一一头像上传(类一一百度号注册):
    def __init__(self):
        self.模具一一高位换头部信息()
        self.首次 = 0
        self.激活窗口图像位置 = r'E:\PY学习文件\BTT影视剧\py快捷方式\opera浏览器.PNG'  #
        self.手机号码验证数 = 0
        self.临时图片目录 = r"F:\影视发帖推广\临时图片"
        self.旧目录路径 = r"F:\影视发帖推广\贴吧顶贴\头像\百度主号上传头像"
        self.颜色变化 = ''
        self.模具一一图像对比激活窗口()
        self.模具一一百度上传图片头像()


if __name__ == '__main__':
    帐号类型 ='百度顶贴'
    帐号类型 ='百度发贴'
    类 = 类一一百度号注册(帐号类型)

    #类 = 类一一头像上传()



