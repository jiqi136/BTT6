# -*- coding:utf-8


import re  # 正则式
import time  # 时间
import requests  # 网页浏览
import os  # 本地操作
import random# 随机
import win32gui #窗口控件
import pymysql  # 数据库

import pyautogui as pag #模拟鼠标键盘操作
from selenium import webdriver  # 浏览的驱动
from selenium.webdriver.support import expected_conditions as EC #=判断网页文本
from hashlib import md5 # md5值
from PIL import Image#图片处理



from 推广公共库 import 类一一公共库# 导入模块
from 百度号注册 import 类一一百度号注册# 导入模块

"""


"""


            
class 类一一百度号控制浏览器注册(类一一公共库):  # 调用 类的模具 self.模具一一数据库()
    def __init__(self,帐号类型):
        self.帐号类型 = 帐号类型


        self.首次 = 0

        self.手机号码验证数 = 0
        self.临时图片目录 = r"F:\影视发帖推广\临时图片"
        self.旧目录路径 = r"F:\影视发帖推广\贴吧顶贴\头像\百度主号上传小头像"


        # ===

        self.模具一一提取影视剧数据库里的易码短信平台账户信息()
        self.模具一一提取推广库里的百度发贴帐号()

        self.账户密码 = str(self.账户密码).replace("qq", "q")
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

        # ====控制
        self.Chrome控制 = webdriver.ChromeOptions()  # 设置控制
        # options = Options()
        self.Chrome控制.add_argument('disable-infobars')  # 加启动配置 去除正在受到自动软件的控制

        计数器 = 0
        for 字符 in self.内容:
            for 影视类型 in self.电影美剧表:
                随机 = random.randrange(0, len(self.内容))
                字符 = self.内容[随机]
                self.跳过循环=''

                self.百度发贴名 = 字符 + 影视类型
                self.跳过循环 = ''
                self.手机号码验证数 = 0
                self.手机号码验证换ip次数 = 0

                if self.百度发贴名 in self.已注册帐号手机号:
                    continue  # 跳过当前循环,继续进行下一轮循环



                计数器 = 计数器 + 1
                if 计数器 > 30:
                    条件循环 = 998
                开始时间计数 = int(time.time())

                self.模具一一高位换头部信息()
                self.模具一一换ip连接()

                self.模具一一打开百度首页()





                self.模具一一判断手机号码已注册()

                if '跳过循环' in str(self.跳过循环):

                    self.模具一一正常60秒后换IP时间数()
                    self.浏览器操作.quit()  # .退出浏览器

                    continue  # 跳过循环

                self.模具一一输入图片字符()
                #self.模具一一百度注册浏览器激活窗口()

                if '跳过循环' in str(self.跳过循环):

                    self.模具一一正常60秒后换IP时间数()
                    self.浏览器操作.quit()  # .退出浏览器
                    continue  # 跳过循环

                self.模具一一输入短信内容()

                if '跳过循环' in str(self.跳过循环):

                    self.模具一一正常60秒后换IP时间数()
                    self.浏览器操作.quit()  # .退出浏览器
                    continue  # 跳过循环

                self.模具一一输入自动化百度用户名()

                if '跳过循环' not in str(self.跳过循环):
                    self.模具一一输入密码()
                    self.模具一一确认注册()

                    self.模具一一确认成功注册()

                    self.模具一一控制浏览器提取cookie()


                    self.模具一一保存数据库一百度发贴帐号等()

                    self.模具一一正常60秒后换IP时间数()
                    self.浏览器操作.quit()  # .退出浏览器


                    continue  # 跳过循环



                if '跳过循环' not in str(self.跳过循环):
                    self.模具一一确认注册()

                    self.模具一一提取登录界面的cookie()

                    self.模具一一保存数据库一百度发贴帐号等()

                    self.模具一一百度上传图片头像()

                self.模具一一清除浏览器历史缓存()

                # ===

                self.模具一一换ip连接二()
                self.模具一一百度注册浏览器激活窗口()

                结束时间计数 = int(time.time())
                用时 = 结束时间计数 - 开始时间计数
                print('操作:', 用时, '秒')
                time.sleep(1)  # 等待

                # pyautogui.alert('确认后继续')
                time.sleep(5)  # 等待  # 增加延迟
                self.模具一一正常60秒后换IP时间数()


    def 模具一一输入图片字符(self):
        def 判断字符正确提醒窗口消失():
            # ===判断手机号码已注册提醒窗口

            定位 = ("id", 'TANGRAM__PSP_17__titleText')

            判断文本 = r"安全验证"

            try:  # 调用异常处理,应对易发生错误的位置
                手机号码已注册True = EC.text_to_be_present_in_element(定位, 判断文本)(self.浏览器操作)

            except:  # 异常处理 (,)as 异常原因
                print('图片验证完成')

                结束循环 = '结束循环'
                return 结束循环  # 返回

                # print(异常原因 )
            else:  # 必须放在所有的except子句之后.这个子句将在try子句没有发生任何异常的时候执行.


                if 手机号码已注册True == True:
                    print('图片验证错误')

                    结束循环 = ''
                    return 结束循环  # 返回


                else:  #
                    print('图片验证完成')

                    结束循环 = '结束循环'
                    return 结束循环  # 返回

        def 模具一一保存至文本(内容):
            文本 = open("F:\影视发帖推广\临时字符图片\图片验证错误.txt", 'a', encoding='UTF-8') #追加 a

            文本.write(内容)  # write 写入  read() #读取
            文本.close()
            print('保存至文本;', 内容)
        计数器=0
        for i in '123':

            if 计数器 !=0:
                图片字符=self.图片字符+'\n'
                模具一一保存至文本(图片字符)

                """请空输入框"""
                self.浏览器操作.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__confirmVerifyCode"]').clear()  # 输入.send_keys("python3")  请空输入框:clear()
                time.sleep(1)  # 等待  # 增加延迟

                """换一张字符图片"""
                self.浏览器操作.find_element_by_xpath(
                    '//*[@id="TANGRAM__PSP_3__confirmVerifyCodeChange"]').click()  # 点击 .click() 短信验证码
                time.sleep(1)  # 等待  # 增加延迟
            计数器 = 计数器 + 1
            self.模具一一浏览器截图()
            self.模具一一上传图片检测()

            self.浏览器操作.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__confirmVerifyCode"]').send_keys(self.图片字符)  # 输入.send_keys("python3")  请空输入框:clear()
            time.sleep(1)  # 等待  # 增加延迟



            """点击  确定"""
            self.浏览器操作.find_element_by_xpath(
                '//*[@id="TANGRAM__PSP_22__confirm_continue"]').click()  # 点击 .click() 短信验证码
            time.sleep(2)  # 等待  # 增加延迟

            """提醒窗口消失"""
            结束循环=判断字符正确提醒窗口消失()
            if '结束循环' in 结束循环:
                return # 返回

        self.跳过循环='跳过循环'

    def 模具一一上传图片检测(self,题目类型 = 4020):
        # 4020	2位汉字  3040 4位混合英数
        图片缓存 = open(self.图片地址, 'rb').read()  # 读取图片内容
        检测超时 = 60
        self.帐号与软件名 = {
            'username': 'jiqi1136',
            'password': md5(self.账户密码.encode("utf-8")).hexdigest(),
            'softid': '114814',
            'softkey': '48e1d1764a64484086446a320a860783',
        }

        #self.headers = {'Connection': 'Keep-Alive','Expect': '100-continue','User-Agent': 'ben',}

        params = {
            'typeid': 题目类型,
            'timeout': 检测超时,
        }

        params.update(self.帐号与软件名)
        files = {'image': ('a.jpg', 图片缓存)}
        for i in '256517':
            try:  # 调用异常处理，应对易发生错误的位置
                返回网页内容 = requests.post('http://api.ruokuai.com/create.json', data=params, files=files, headers=self.头部信息)
                图片字符字典 = 返回网页内容.json()
                self.图片字符 = 图片字符字典['Result']
            except:
                pass
            else:
                if '200' in str(返回网页内容):
                    break  # 结束循环

        print('图片字符',self.图片字符)  # ['typeid']
    def 模具一一浏览器截图(self):
        time.sleep(1)
        self.图片地址 = r'F:\影视发帖推广\临时字符图片\百度图片字符.png'

        self.浏览器操作.get_screenshot_as_file(self.图片地址)#全屏 截图
        time.sleep(1)
        """"区域剪切截图"""

        图片缓存 = Image.open(self.图片地址)
        四角坐标 = (220, 192, 310, 235)  # （左，上，右，下）
        剪切的图 = 图片缓存.crop(四角坐标)

        del 图片缓存
        剪切的图.save(self.图片地址)  # 另存为
        #剪切的图.show()  # 显示
        print('截图完成')
        time.sleep(1)




    def 模具一一确认成功注册(self):
        # 等待10秒


        for i in '123':

            try:  # 调用异常处理,应对易发生错误的位置
                self.浏览器操作.implicitly_wait(10)  # 隐式等待
                self.浏览器操作.find_element_by_xpath(
                    '//*[@id="kw"]').click()  # 点击  百度 搜索 输入框

            except:  # 异常处理
                self.浏览器操作.refresh()  # 刷新当前页面
                time.sleep(3)  # 等待  # 增加延迟

            else:  # 必须放在所有的except子句之后.这个子句将在try子句没有发生任何异常的时候执行.
                time.sleep(1)  # 等待  # 增加延迟
                break  # 结束循环



        time.sleep(2)  # 等待  # 增加延迟

    def 模具一一控制浏览器提取cookie(self):
        cookie= self.浏览器操作.get_cookies()

        self.cookie = str(cookie).replace("'", '"')
        print(self.cookie)



    def 模具一一确认注册(self):
        self.浏览器操作.find_element_by_xpath(
            '//*[@id="TANGRAM__PSP_3__isAgree"]').click()  # 点击  同意协议 按钮
        time.sleep(1)  # 等待  # 增加延迟
        

        self.浏览器操作.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__submit"]').click() # 点击  注册 按钮
        time.sleep(1)  # 等待  # 增加延迟

    def 模具一一输入密码(self):
        # ======密码=======


        密码数字 = random.randrange(100000, 1000000)
        self.密码 = "qq{}Q%".format(密码数字)
        print('密码:', self.密码)

        self.浏览器操作.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__password"]').send_keys(
            self.密码)  # 输入.send_keys("python3")  请空输入框:clear()
        time.sleep(1)  # 等待  # 增加延迟

    def 模具一一输入自动化百度用户名(self):
        # ===定位 用户名 输入框

        if '顶贴号' in self.帐号类型:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            self.随机取名 = self.模具一一随机取女名()
        else:  # 否则
            self.随机取名 =self.百度发贴名 + '3e38_com'

        self.浏览器操作.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__userName"]').send_keys(
            self.随机取名)  # 输入.send_keys("python3")  请空输入框:clear()

        print('百度发贴名:',self.随机取名)
        time.sleep(1)  # 等待  # 增加延迟

    def 模具一一获取百度短信(self):

        self.项目编号 = "13043"

        获取短信网址 = "http://api.fxhyd.cn/UserInterface.aspx?action=getsms&token={}&itemid={}&mobile={}".format(
            self.通信令牌token,
            self.项目编号, self.手机号码)
        """&release=1  自动释放号码标识符 若该参数值为1时,获取到短信的同时系统将自己释放该手机号码.若要继续使用该号码,请勿带入该参数."""

        条件循环 = 0
        while 条件循环 < 2:  # 条件循环  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            self.短信内容 = ''

            for i in '12345':
                print('等待 15秒:')
                time.sleep(14)  # 等待
                网址内容 = self.模具一一打开的网址请求返回网页内容(获取短信网址)
                if 'success' in 网址内容.text:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                    self.短信内容 = 网址内容.text.replace("success|", "")  # 替换   , 1) 次数 1
                    print('短信内容:', self.短信内容)
                    条件循环 = 998

                    return  # 返回
                elif '3001' in 网址内容.text:  # 其它条件.
                    print('短信尚未到达:3001,继续调用取短信接口,直到超时为止.')

                elif '2008' in 网址内容.text:  # 其它条件.
                    print('2008，号码已离线')
                    条件循环 = 998
                    self.跳过循环 = '跳过循环'

                elif '2007' in 网址内容.text:  # 其它条件.
                    print('2007，号码已被释放')
                    条件循环 = 998
                    self.跳过循环 = '跳过循环'

                elif '1008' in 网址内容.text:  # 其它条件.
                    print('1008，账户余额不足')
                    条件循环 = 998
                    self.跳过循环 = '跳过循环'

                elif '2004' in 网址内容.text:  # 其它条件.
                    print('2004，暂时没有可用的号码')
                    条件循环 = 998
                    self.跳过循环 = '跳过循环'

                else:  # 否则
                    print('请求失败:', 网址内容.text)
            条件循环 = 条件循环 + 1
            if 条件循环 ==2:
                释放手机号码接口 = "http://api.fxhyd.cn/UserInterface.aspx?action=release&token={}&itemid={}&mobile={}".format(
                    self.通信令牌token, self.项目编号, self.手机号码)
                释放手机号码网址内容 = self.模具一一打开的网址请求返回网页内容(释放手机号码接口)
                self.模具一一百度项目拉黑手机号码()
                self.跳过循环 = '跳过循环'
                continue  # 跳过当前循环,继续进行下一轮循环
            #self.模具一一百度注册浏览器激活窗口()

            self.浏览器操作.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__verifyCodeSend"]').click()  # 点击 .click() 短信验证码

            self.模具一一输入图片字符()
            #self.模具一一开关提醒声()

            #time.sleep(20)  # 等待  # 增加延迟




    def 模具一一百度注册浏览器激活窗口(self):

        pag.hotkey('winleft', 'd')  # press()一次完整的击键.hotkey('ctrl','c') 全选 图片
        time.sleep(0.5)  # 等待  # 增加延迟

        类名 = ''
        窗口标题 = "注册百度帐号 - Google Chrome"

        if len(类名) == 0:
            窗口句柄 = win32gui.FindWindow(None, 窗口标题)
        else:  #
            窗口句柄 = win32gui.FindWindow(类名, None)
        
        窗口标题 = win32gui.GetWindowText(窗口句柄)
       
        print('窗口标题', 窗口标题)
        
      

        win32gui.ShowWindow(窗口句柄, 11)  # 即使拥有窗口的线程被挂起也会最小化.在从其他线程最小化窗口时才使用这个参数
        time.sleep(0.5)  # 等待  # 增加延迟
        win32gui.ShowWindow(窗口句柄, 1)  # 激活并显示一个窗口.如果窗口被最小化或最大化,系统将其恢复到原来的尺寸和大小.
        time.sleep(2)  # 等待  # 增加延迟




    def 模具一一输入短信内容(self):
        #self.模具一一点击获取手机验证码()
        #self.模具一一开关提醒声()
        #time.sleep(20)  # 等待  # 增加延迟


        self.模具一一获取百度短信()
        #self.模具一一百度注册浏览器激活窗口()

        if len(self.短信内容) == 0 or '跳过循环' in str(self.跳过循环):
            return  # 返回

        规则 = '\d{6}'
        内容列表 = re.findall(规则, self.短信内容)  # 提取
        self.短信内容 = 内容列表[0]

        self.浏览器操作.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__verifyCode"]').send_keys(self.短信内容)  # 输入.send_keys("python3")  请空输入框:clear()  .click() 短信内容 输入框
        time.sleep(1)  # 等待  # 增加延迟


    def 模具一一重复验证手机号(self):

        self.项目编号 = "13043"
        if '再验证' in self.再验证手机号:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            self.模具一一读取文本的手机号码()

        
        条件循环 = 1
        while 条件循环 == 1:  # 条件循环  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环

            self.模具一一高位换头部信息()
            self.模具一一换ip连接()
            self.模具一一提取影视剧数据库里的易码短信平台账户信息()
            self.模具一一打开百度首页()
            
            if '再验证' in self.再验证手机号: #  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                self.模具一一再验证手机号()

            else:# 否则
                self.模具一一判断手机号码已注册()


            正常60秒后换IP时间数 =self.换IP时间计数+65
            当下时间数 = int(time.time())
            if 当下时间数<正常60秒后换IP时间数:
                print('等待:', 正常60秒后换IP时间数-当下时间数,'秒')
                time.sleep(正常60秒后换IP时间数-当下时间数)  # 等待  # 增加延迟

            self.浏览器操作.quit()  # .退出浏览器


            if '再验证' in self.再验证手机号:
                if len(self.等待验证手机号列表)==0:
                    print('等待验证手机号 已空')
                    条件循环 = 998





        #等待用户输入 = input("\n按下 enter 确认键后继续")

    def 模具一一打开百度首页(self):
        def 换头部信息():

            头部信息 = "user-agent=" + self.头部信息['User-Agent']
            print('头部信息:', 头部信息)
            self.Chrome控制.add_argument(头部信息)
        for i in '123':
            try:  # 调用异常处理,应对易发生错误的位置
                换头部信息()

                # ====self.浏览器操作

                # 点击.click() 或  输入.send_keys("python3")  请空输入框:clear()
                self.浏览器操作 = webdriver.Chrome(chrome_options=self.Chrome控制)  # 打开chrome浏览器
                self.浏览器操作.set_window_size(500, 500)# driver.maximize_window() 浏览器全屏显示,不带参数
                time.sleep(1)  # 等待  # 增加延迟


                pag.hotkey('altleft', 'tab')  # press()一次完整的击键.hotkey('ctrl','c') 全选 图片
                time.sleep(2)  # 等待  # 增加延迟
                #self.模具一一自身最小化()


                url = "https://passport.baidu.com/v2/?reg&tt=1537956495492&overseas=undefined&gid=8515458-8F51-407D-AEBC-A53A793AC038&tpl=mn&u=https%3A%2F%2Fwww.baidu.com%2F"  # 注册页面  https://www.zhihu.com/signup?next=%2Fexplore
                self.浏览器操作.get(url)
            except:  # 异常处理
                pass

            else:  # 必须放在所有的except子句之后.这个子句将在try子句没有发生任何异常的时候执行.
                time.sleep(1)  # 等待  # 增加延迟
                break  # 结束循环

    def 模具一一自身最小化(self):
        标题 = "注册百度帐号 - Google Chrome"

        窗口句柄 = win32gui.FindWindow(None,标题)
        if 窗口句柄 > 0:
            win32gui.ShowWindow(窗口句柄, 11)  # 即使拥有窗口的线程被挂起也会最小化.在从其他线程最小化窗口时才使用这个参数

    def 模具一一获取百度接收的手机号码(self):
        # 通信令牌token = self.cookie
        self.项目编号 = "13043"

        #排除号段 = '170.171'
        排除号段 = '170.171.130.131.132.134.135.136.137.138.139'
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

    def 模具一一追加保存手机号码到文本(self):
        if '再验证' in self.再验证手机号:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环

            手机号码 = self.手机号码.replace("\n", "") #替换   , 1) 次数 1
            手机号码 = 手机号码 + '再验证\n'
        else:  # 否则
            手机号码=self.手机号码+'\n'
        文本 = open(r"F:\影视发帖推广\可以注册手机号码.txt", 'a', encoding='UTF-8')

        文本.write(手机号码)  # write 写入  read() #读取
        文本.close()
        print('追加保存至文本;', 手机号码)

    def 模具一一读取文本的手机号码(self):
        try:  # 调用异常处理,应对易发生错误的位置
            文本 = open(r"F:\影视发帖推广\可以注册手机号码.txt", 'r', encoding='UTF-8')
            文本内容列表 = 文本.readlines()  # read() #全部读取   readlines每一行
        except UnicodeDecodeError as 异常原因:  # 异常处理
            print(异常原因)
            文本 = open(r"F:\影视发帖推广\可以注册手机号码.txt", 'r', encoding='gbk')
            文本内容列表 = 文本.readlines()  # read() #全部读取   readlines每一行
        else:  # 必须放在所有的except子句之后.这个子句将在try子句没有发生任何异常的时候执行.
            文本.close()


        self.等待验证手机号列表=[]
        for 每行文本内容 in 文本内容列表:
            if  '再验证' not in 每行文本内容 and len(每行文本内容)>5:
                self.等待验证手机号列表.append(每行文本内容)
    def 模具一一再验证手机号(self):

        for i in '12345':

            def 判断手机号码已注册提醒窗口():
                # ===判断手机号码已注册提醒窗口

                定位 = ("id", 'TANGRAM__PSP_17__titleText')
                判断文本 = r"安全验证"

                try:  # 调用异常处理,应对易发生错误的位置
                    手机号码已注册True = EC.text_to_be_present_in_element(定位, 判断文本)(self.浏览器操作)

                except:  # 异常处理 (,)as 异常原因
                    return  # 返回
                    # print(异常原因 )
                else:  # 必须放在所有的except子句之后.这个子句将在try子句没有发生任何异常的时候执行.
                    if 手机号码已注册True == True:
                        print('手机号码未曾注册')
                    else:  # 否则
                        self.模具一一百度项目拉黑手机号码()
                        time.sleep(1)  # 等待  # 增加延迟
                        跳过当前循环 = '跳过循环'

                        return 跳过当前循环  # 返回

            def 判断手机号码本月上限():
                # =========判断手机号码本月上限
                定位 = ("id", 'TANGRAM__PSP_3__phoneError')
                判断文本 = r"上限"
                try:  # 调用异常处理,应对易发生错误的位置
                    号码本月上限True = EC.text_to_be_present_in_element(定位, 判断文本)(self.浏览器操作)
                    print('号码本月上限', 号码本月上限True)
                except:  # 异常处理 (,)as 异常原因
                    return  # 返回
                    # print(异常原因 )
                else:  # 必须放在所有的except子句之后.这个子句将在try子句没有发生任何异常的时候执行.
                    if 号码本月上限True == True:
                        self.模具一一百度项目拉黑手机号码()

                        self.浏览器操作.refresh()  # 刷新当前页面

                        time.sleep(2)  # 等待  # 增加延迟

                        跳过当前循环 = '跳过循环'
                        return 跳过当前循环  # 返回

            def 发送短信过多():
                # =========判断发送短信过多

                定位 = ("id", 'TANGRAM__PSP_3__phoneError')
                判断文本 = r"发送短信过多"
                try:  # 调用异常处理,应对易发生错误的位置
                    发送短信过多True = EC.text_to_be_present_in_element(定位, 判断文本)(self.浏览器操作)
                    print('发送短信过多', 发送短信过多True)
                except:  # 异常处理 (,)as 异常原因
                    return  # 返回
                    # print(异常原因 )
                else:  # 必须放在所有的except子句之后.这个子句将在try子句没有发生任何异常的时候执行.

                    if 发送短信过多True == True:
                        跳过当前循环 = '结束循环'
                        return 跳过当前循环  # 返回

            self.浏览器操作.refresh()  # 刷新当前页面
            time.sleep(3)  # 等待  # 增加延迟


            if len(self.等待验证手机号列表)==0:
                print('等待验证手机号 已空')
                return  # 返回


            self.手机号码=self.等待验证手机号列表[0]
            del self.等待验证手机号列表[0]



            # ====网页操作
            time.sleep(1)  # 等待  # 增加延迟

            self.浏览器操作.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__phone"]').send_keys(
                self.手机号码)  # 输入.send_keys("python3")  请空输入框:clear()
            time.sleep(1)  # 等待  # 增加延迟
            self.浏览器操作.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__password"]').send_keys('123')  # 点击 .click() 密码框

            time.sleep(3)  # 等待  # 增加延迟

            # ===========================判断网页文本
            跳过当前循环 = 判断手机号码已注册提醒窗口()
            if '跳过循环' in str(跳过当前循环):
                continue  # 跳过循环

            self.模具一一追加保存手机号码到文本()
            time.sleep(2)  # 等待  # 增加延迟




    def 模具一一判断手机号码已注册(self):

        for i in '1':


            def 判断手机号码已注册提醒窗口():
                # ===判断手机号码已注册提醒窗口

                定位 = ("id", 'TANGRAM__PSP_17__titleText')

                判断文本 = r"安全验证"
                
                try:  #调用异常处理,应对易发生错误的位置
                    手机号码已注册True = EC.text_to_be_present_in_element(定位,判断文本)(self.浏览器操作)

                except  :#异常处理 (,)as 异常原因
                    self.模具一一百度项目拉黑手机号码()
                    跳过当前循环 = '跳过循环'
                    return 跳过当前循环  # 返回


                    #print(异常原因 )
                else:#必须放在所有的except子句之后.这个子句将在try子句没有发生任何异常的时候执行.
                    if 手机号码已注册True == True:
                        print('手机号码未曾注册')

                        time.sleep(1)  # 等待  # 增加延迟
                        return  # 返回


                    else:  #
                        self.模具一一百度项目拉黑手机号码()
                        print('手机号码已经注册')
                        跳过当前循环 = '跳过循环'
                        return 跳过当前循环  # 返回





            def 判断手机号码本月上限():
                # =========判断手机号码本月上限
                定位 = ("id", 'TANGRAM__PSP_3__phoneError')
                判断文本 = r"上限"
                try:  #调用异常处理,应对易发生错误的位置
                    号码本月上限True = EC.text_to_be_present_in_element(定位, 判断文本)(self.浏览器操作)
                    print('号码本月上限', 号码本月上限True)
                except  :#异常处理 (,)as 异常原因
                    return   # 返回
                    #print(异常原因 )
                else:#必须放在所有的except子句之后.这个子句将在try子句没有发生任何异常的时候执行.
                    if 号码本月上限True == True:
                        self.模具一一百度项目拉黑手机号码()

                        self.浏览器操作.refresh()  # 刷新当前页面
                        time.sleep(2)  # 等待  # 增加延迟

                        跳过当前循环 = '跳过循环'
                        return 跳过当前循环  # 返回

            def 发送短信过多():
                # =========判断发送短信过多

                定位 = ("id", 'TANGRAM__PSP_3__phoneError')
                判断文本 = r"发送短信过多"
                try:  # 调用异常处理,应对易发生错误的位置
                    发送短信过多True = EC.text_to_be_present_in_element(定位, 判断文本)(self.浏览器操作)
                    print('发送短信过多', 发送短信过多True)
                except:  # 异常处理 (,)as 异常原因
                    return  # 返回
                    # print(异常原因 )
                else:  # 必须放在所有的except子句之后.这个子句将在try子句没有发生任何异常的时候执行.


                    if 发送短信过多True == True:

                        跳过当前循环 = '结束循环'
                        return 跳过当前循环  # 返回

            self.模具一一获取百度接收的手机号码()
            #self.手机号码='18272129148'

            for i in '123':
            
                try:  #调用异常处理,应对易发生错误的位置
                    self.浏览器操作.implicitly_wait(5)  # 隐式等待
                    self.浏览器操作.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__phone"]').send_keys(
                        self.手机号码)  # 输入.send_keys("python3")  请空输入框:clear()
                    time.sleep(1)  # 等待  # 增加延迟

                    self.浏览器操作.find_element_by_xpath(
                        '//*[@id="TANGRAM__PSP_3__verifyCodeSend"]').click()  # 点击 .click() 短信验证码
                    time.sleep(3)  # 等待  # 增加延迟


                except :#异常处理
                    self.浏览器操作.refresh()  # 刷新当前页面
                    time.sleep(3)  # 等待  # 增加延迟

                else:#必须放在所有的except子句之后.这个子句将在try子句没有发生任何异常的时候执行.
                    time.sleep(1)  # 等待  # 增加延迟
                    break # 结束循环

            # ===========================判断网页文本
            self.跳过循环 =判断手机号码已注册提醒窗口()
            if '跳过循环' in str(self.跳过循环):
                self.浏览器操作.refresh()  # 刷新当前页面

                #time.sleep(2)  # 等待  # 增加延迟
                continue#跳过循环

            return  # 返回

                #self.模具一一追加保存手机号码到文本()
                #time.sleep(2)  # 等待  # 增加延迟

    """=========数据库======================="""

    def 模具一一提取推广库里的百度发贴帐号(self):

        # 提取数据库里的过滤网址
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "", "影视发帖推广", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句
        sql = "SELECT `帐号`, `注册手机号` FROM `推广帐号` WHERE `类型`='{}' ".format(self.帐号类型)  # 不换行 '{}'
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        帐号手机号组列表 = cursor.fetchall()
        self.已注册帐号手机号 = str(帐号手机号组列表)

        # 关闭数据库连接
        db.close()

    def 模具一一保存数据库一百度发贴帐号等(self):
        print('打开数据库连接')
        记录='已经注册'
        # 打开数据库连接,
        今天时间 = str(time.strftime("%y-%m-%d", time.localtime()))

        db = pymysql.connect("localhost", "root", "", "影视发帖推广", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句

        sql = """INSERT INTO `推广帐号`( `类型`, `帐号`, `密码`, `注册手机号`, `注册日期`, `cookie`,`记录`) VALUES
             ("{}","{}","{}","{}",'{}','{}','{}')""".format(self.帐号类型, self.随机取名, self.密码, self.手机号码, 今天时间,
                                                       self.cookie,记录)  # 不换行 end=""

        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            print('=保存数据库一百度发贴帐号')
        except:
            # 如果发生错误则回滚
            print('=====================数据库执行发生错误:===============')
            db.rollback()
        # 关闭数据库连接
        db.close()





if __name__ == '__main__':

    帐号类型 = '百度顶贴'
    帐号类型 = '百度发贴'

    类 = 类一一百度号控制浏览器注册(帐号类型)
