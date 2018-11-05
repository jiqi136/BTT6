# -*- coding:utf-8

from 网页采集公共库 import 类一一采集公共库# 导入模块
import re  # 正则式
import time  # 时间
import requests  # 网页浏览
import os  # 本地操作
import random# 随机
import win32gui #窗口控件
import pymysql  # 数据库

import pyautogui as pag #模拟鼠标键盘操作
import pyautogui#模拟鼠标键盘操作
from selenium import webdriver  # 浏览的驱动
from selenium.webdriver.support import expected_conditions as EC #=判断网页文本



class 类一一帐号互相关注(类一一采集公共库):#调用 类的模具 self.模具一一查看变量输出文本值('变量名', self.测试打印, 8)
    def __init__(self):
        self.模具一一高位换头部信息()
        self.数据库名 = "影视发帖推广"
        self.测试打印 = '放'
        self.跳过循环= ''

        #self.模具一一提取文本并提炼()

        self.模具一一帐号互相关注()

    """      1     """

    def 模具一一提取文本并提炼(self):
        def 模具一一保存数据库百度顶贴账号():

            self.sql语句 = """INSERT INTO `推广帐号`(`类型`, `帐号`, `密码`, `名值cookie`)
             VALUES ("{}","{}","{}","{}")""".format('百度顶贴', self.账号, self.密码, self.名值cookie文本)  # '代入 '{}'

            self.模具一一内容数据库("保存 百度顶贴账号")

        def 模具一一提取数据库百度顶贴账号():

            self.sql语句 = "SELECT `帐号` FROM `推广帐号` WHERE `类型`='百度顶贴' "  # ' '{}' # SQL 查询语句
            self.模具一一内容数据库()

        """提取数据库"""
        模具一一提取数据库百度顶贴账号()
        self.数据库百度顶贴账号文本 = str(self.数据库内容组列表)
        """提取文本"""
        文本位置=r'F:\影视发帖推广\贴吧顶贴\购买的手机注册账号.txt'

        try:  # 调用异常处理,应对易发生错误的位置
            文本 = open(文本位置, 'r', encoding='UTF-8')
            文本内容列表 = 文本.readlines()  # read() #全部读取   readlines每一行
        except UnicodeDecodeError as 异常原因:  # 异常处理
            self.模具一一查看变量输出文本值('提取文本,异常原因:更换', 异常原因,8)
            文本 = open(文本位置, 'r', encoding='gbk')
            文本内容列表 = 文本.readlines()  # read() #全部读取   readlines每一行
        else:  # 必须放在所有的except子句之后.这个子句将在try子句没有发生任何异常的时候执行.
            文本.close()

        if len(文本内容列表)==0:
            self.模具一一查看变量输出文本值('提取文本为空', '')
            return#返回

        """提炼文本"""
        for 文本内容 in 文本内容列表:
            self.模具一一查看变量输出文本值('文本内容',文本内容, 8)
            文本内容=文本内容+"----"
            文本列表 = 文本内容.split("----")
            self.账号=文本列表[0]
            self.模具一一查看变量输出文本值('self.账号', self.账号)

            if self.账号 in self.数据库百度顶贴账号文本:
                self.模具一一查看变量输出文本值('百度顶贴账号', '已经存在,跳过循环')

                continue#跳过循环

            self.密码 = 文本列表[1]
            self.模具一一查看变量输出文本值('self.密码', self.密码, 8)
            self.名值cookie文本= 文本列表[2]
            self.模具一一查看变量输出文本值('self.名值cookie文本', self.名值cookie文本, 8)

            模具一一保存数据库百度顶贴账号()
            self.数据库百度顶贴账号文本 =self.数据库百度顶贴账号文本+self.账号



    """      2     """
    def 模具一一启动操作浏览器(self):
        def 换头部信息():
            self.模具一一高位换头部信息()
            头部信息 = "user-agent=" + self.头部信息['User-Agent']
            print('头部信息:', 头部信息)
            self.浏览器设置选项.add_argument(头部信息)



        换头部信息()
        """配置不加载图片"""
        配置不加载图片 = {"profile.managed_default_content_settings.images": 2}  # 配置不加载图片
        # self.浏览器设置选项.add_experimental_option("prefs", 配置不加载图片)

        self.浏览器操作 = webdriver.Chrome(chrome_options=self.浏览器设置选项)  # 打开chrome浏览器


        self.浏览器操作.set_window_size(800, 800)  # 参数是像素点宽,高

    def 模具一一帐号互相关注(self):
        """设置选项"""
        self.浏览器设置选项 = webdriver.ChromeOptions()  # 设置控制
        # options = Options()
        self.浏览器设置选项.add_argument('disable-infobars')  # 加启动配置 去除正在受到自动软件的控制

        self.模具一一提取数据库百度顶贴与发贴账号()

        for 百度顶贴账号cookie组 in self.百度顶贴账号cookie组列表:
            if "密码错误" in str(百度顶贴账号cookie组[-1]):
                self.模具一一查看变量输出文本值("密码错误,跳过循环", 百度顶贴账号cookie组[1])
                continue  # 跳过循环

            elif len(str(百度顶贴账号cookie组[4])) > 5:  # 组[4]  互相关注名
                self.模具一一查看变量输出文本值("互相关注名 > 5,跳过循环", 百度顶贴账号cookie组[4])
                continue  # 跳过循环

            self.跳过循环 = ''

            for 百度发贴账号cookie组 in self.百度发贴账号cookie组列表:

                if 百度发贴账号cookie组[1] in self.互相关注名:
                    # self.百度发贴账号cookie组列表.remove(百度发贴账号cookie组)  # 列表 按值删除
                    self.模具一一查看变量输出文本值("互相关注名已经存在,跳过循环", 百度发贴账号cookie组[1])
                    break  # 结束循环

                elif "密码错误" in str(百度发贴账号cookie组):
                    self.模具一一查看变量输出文本值("密码错误,跳过循环", 百度发贴账号cookie组)
                    break  # 结束循环

                elif '38_' not in str(百度发贴账号cookie组[1]):
                    self.模具一一查看变量输出文本值("非38_帐号, 跳过循环", 百度发贴账号cookie组[1])
                    continue  # 跳过循环


                self.顶贴cookie = 百度顶贴账号cookie组[5]
                传递字典={}
                self.ID=百度顶贴账号cookie组[0]
                self.帐号= 百度顶贴账号cookie组[1]
                self.密码 = 百度顶贴账号cookie组[2]

                self.关注帐号 = 百度发贴账号cookie组[1]



                """登录  顶贴帐号"""
                if len(str(self.顶贴cookie)) > 5:
                    self.名值 = ''
                    self.cookie字典 = 百度顶贴账号cookie组[5]
                    self.模具一一网页操作相互关注账号()

                else:  # 否则
                    self.名值 = '名值'
                    self.cookie字典 = 百度顶贴账号cookie组[3]
                    self.模具一一网页操作相互关注账号()

                if '跳过循环' in self.跳过循环:
                    break  # 结束循环

                """登录  发贴帐号"""

                self.名值 = ''
                self.ID = 百度顶贴账号cookie组[0]
                self.帐号 = 百度发贴账号cookie组[1]
                self.密码 = 百度发贴账号cookie组[2]
                self.cookie字典 = 百度发贴账号cookie组[3]

                self.关注帐号 = 百度顶贴账号cookie组[1]
                self.顶贴ID = self.ID


                self.模具一一网页操作相互关注账号()

                if '跳过循环' in self.跳过循环:
                    break  # 结束循环

                self.模具一一数据库更新一互相关注()

    def 模具一一提取数据库百度顶贴与发贴账号(self):

        self.sql语句 = "SELECT `ID`, `帐号`, `密码`,`名值cookie`, `互相关注`,`cookie` FROM `推广帐号` WHERE `类型`='百度顶贴' "  # ' '{}' # SQL 查询语句
        self.模具一一内容数据库()
        self.百度顶贴账号cookie组列表 = list(self.数据库内容组列表)

        self.sql语句 = "SELECT `ID`,`帐号`, `密码`,`cookie` FROM `推广帐号` WHERE `类型`='百度发贴' "  # ' '{}' # SQL 查询语句
        self.模具一一内容数据库()
        self.百度发贴账号cookie组列表 = list(self.数据库内容组列表)

        """过滤顶贴账号已有 互相关注"""
        self.模具一一查看变量输出文本值("self.百度顶贴账号cookie组列表", len(self.百度顶贴账号cookie组列表), 8)

        """提取数据库 互相关注名"""
        self.sql语句 = "SELECT `互相关注` FROM `推广帐号`"  # ' '{}' # SQL 查询语句
        self.模具一一内容数据库()
        self.互相关注名 =set(self.数据库内容组列表)
        self.互相关注名 = str(self.互相关注名)
        self.模具一一查看变量输出文本值("self.互相关注名", self.互相关注名, 8)




    """      3     """

    def 模具一一网页操作相互关注账号(self):
        """========================操作===================="""

        def 模具一一导入顶贴名值cookie(cookie字典):
            self.模具一一查看变量输出文本值('self.顶贴名值cookie',cookie字典, 8)

            获取所有cookies列表 = self.浏览器操作.get_cookies()  # 获取所有cookies
            替换字典 = 获取所有cookies列表[0]

            for 名值cookie in cookie字典.split(";"):
                if len(名值cookie) > 0:
                    名值cookie列表 = 名值cookie.split("=")
                    cookie名 = 名值cookie列表[0]
                    cookie值 = 名值cookie.replace(cookie名 + "=", "")  # 替换   , 1) 次数 1
                    替换字典["name"] = cookie名
                    替换字典["value"] = cookie值

                    try:  # 调用异常处理,应对易发生错误的位置
                        self.浏览器操作.add_cookie(替换字典)  # 添加列表二

                    except:  # 异常处理
                        pass

                    else:  # 必须放在所有的except子句之后.这个子句将在try子句没有发生任何异常的时候执行.
                        pass

            # 刷新下页面就见证奇迹了
            self.浏览器操作.refresh()

        def 模具一一导入发贴cookie列表(cookie字典):
            def 字典清洁(文本行):

                字典名值列表 = 文本行.split('":')
                字典值 = 字典名值列表[1]
                字典值 = 字典值.strip()  # 默认则是去除空格
                字典值 = 字典值.strip('"')  # 默认则是去除空格
                字典值 = 字典值.strip("'")  # 默认则是去除空格

                return 字典值  # 返回

            获取所有cookies列表 = self.浏览器操作.get_cookies()  # 获取所有cookies
            替换字典 = 获取所有cookies列表[0]

            for 字典行 in str(cookie字典).split("}"):
                字典行 = 字典行.replace("':", '":')  # 替换   , 1) 次数 1
                字典 = 替换字典
                for 文本行 in 字典行.split(","):


                    if 'name' in 文本行:
                        字典值 = 字典清洁(文本行)
                        字典['name'] = 字典值

                    if 'value' in 文本行:
                        字典值 = 字典清洁(文本行)
                        字典['value'] = 字典值
                        self.模具一一查看变量输出文本值('字典', 字典, 8)

                    try:  # 调用异常处理,应对易发生错误的位置
                        self.浏览器操作.add_cookie(字典)  # 添加列表二

                    except:  # 异常处理
                        pass

                    else:  # 必须放在所有的except子句之后.这个子句将在try子句没有发生任何异常的时候执行.
                        pass


            self.浏览器操作.refresh()# 刷新下页面就见证奇迹了

        self.模具一一换ip连接()

        self.模具一一启动操作浏览器()
        self.模具一一查看变量输出文本值("登录帐号:", self.帐号)

        账号个人主页 = "http://tieba.baidu.com/home/main?un={}&fr=pb&ie=utf-8".format(self.关注帐号)  # '代入 '{}'
        self.浏览器操作.get(账号个人主页)

        if  '名值' in self.名值:
            模具一一导入顶贴名值cookie(self.cookie字典)

        else:  # 否则
            模具一一导入发贴cookie列表(self.cookie字典)
            
        self.模具一一检测cookie是否生效()
        if '跳过循环' in self.跳过循环:
            return  # 返回



        """隐式等待 试错"""
        for 序号 in '123':
            try:  #调用异常处理,应对易发生错误的位置

                self.浏览器操作.implicitly_wait(10)  # 隐式等待
                """点击  点击关注按钮"""
                self.浏览器操作.find_element_by_xpath('//*[@id="userinfo_wrap"]/div[2]/div[1]/div/div/a[1]').click()  # 点击
                pass

            except:  # 异常处理
                if '1' in 序号:
                    self.浏览器操作.refresh()  # 刷新下页面
                elif '2' in 序号:
                    self.跳过循环='跳过循环'
                    return  # 返回
            else:  # 必须放在所有的except子句之后.这个子句将在try子句没有发生任何异常的时候执行.
               break # 结束循环



        time.sleep(1)  # 等待  # 增加延迟

        """点击  随机选择头像"""
        # self.模具一一随机选择头像()
        self.模具一一上传设置头像()


        # time.sleep(6)  # 等待  # 增加延迟

        self.浏览器操作.quit()  # .退出浏览器

    def 模具一一检测cookie是否生效(self):
        for 序号 in '一二三':
            time.sleep(2)  # 等待  # 增加延迟
            要求登录 = self.模具一一判断要求登录存在()
            if '要求登录' not in 要求登录:
                if '名值' in self.名值:
                    获取所有cookies列表 = self.浏览器操作.get_cookies()  # 获取所有cookies
                    self.sql语句 = 'UPDATE `推广帐号` SET `cookie`="{}" WHERE `ID`={}'.format(获取所有cookies列表,
                                                                                        ID)  # '代入 '{}'   # ' '{}' # SQL 查询语句
                    self.模具一一内容数据库('更新 帐号cookies')

                break # 结束循环

            else:  #否则
                if  '一' in 序号:
                    """点击 登录 按钮"""
                    self.浏览器操作.find_element_by_xpath('//*[@id="com_userbar"]/ul/li[4]/div/a').click()  # 点击
                    self.浏览器操作.implicitly_wait(5)  # 隐式等待

                    """点击 用户名登录 按钮"""
                    self.浏览器操作.find_element_by_xpath('//*[@id="passport-login-pop-dialog"]/div/div/div/div[3]/p[2]').click()  # 点击
                    self.浏览器操作.implicitly_wait(5)  # 隐式等待

                    """输入 帐号"""
                    self.浏览器操作.find_element_by_xpath('//*[@id="passport-login-pop-api"]/form/p[5]/input[2]').send_keys(self.帐号)  # 输入
                    time.sleep(0.5)  # 等待  # 增加延迟

                    """输入 密码"""
                    self.浏览器操作.find_element_by_xpath('//*[@id="passport-login-pop-api"]/form/p[6]/input[2]').send_keys(
                        self.密码)  # 输入
                    time.sleep(0.5)  # 等待  # 增加延迟

                    """点击 登录 按钮"""
                    self.浏览器操作.find_element_by_xpath(
                        '//*[@id="passport-login-pop-api"]/form/p[9]/input').click()  # 点击
                    time.sleep(1)  # 等待  # 增加延迟



                elif  '二' in 序号:
                    self.模具一一查看变量输出文本值("登录错误,帐号", self.帐号)
                    self.模具一一开关提醒声()

                    pyautogui.alert('输入验证码,点"登录”后,继续')  # 弹窗 提示



                elif '三' in 序号:
                    self.模具一一查看变量输出文本值("密码错误,帐号:", self.帐号)
                    self.sql语句 = 'UPDATE `推广帐号` SET `cookie`="{}" WHERE `ID`={}'.format("密码错误",
                                                                                        self.ID)  # '代入 '{}'   # ' '{}' # SQL 查询语句
                    self.模具一一内容数据库("更新条目为 密码错误")

                    self.跳过循环= '跳过循环'

    def 模具一一判断要求登录存在(self):
        # ===判断手机号码已注册提醒窗口

        定位 = ("xpath", '//*[@id="com_userbar"]/ul/li[4]/div/a')
        判断文本 = r"登录"
        要求登录 = ''
        try:  # 调用异常处理,应对易发生错误的位置
            要求登录True = EC.text_to_be_present_in_element(定位, 判断文本)(self.浏览器操作)

        except:  # 异常处理 (,)as 异常原因

            return 要求登录  # 返回
            # print(异常原因 )
        else:  # 必须放在所有的except子句之后.这个子句将在try子句没有发生任何异常的时候执行.
            if 要求登录True == True:

                self.模具一一查看变量输出文本值("cookie登录失败", '要求登录')
                要求登录 = '要求登录'


            else:  #

                self.模具一一查看变量输出文本值("成功登录", '', 8)

            return 要求登录  # 返回

    def 模具一一上传设置头像(self):
        def 模具一一随机图像文件():
            目标目录 = r'F:\影视发帖推广\贴吧顶贴\头像\百度主号上传小头像'
            子目录列表与文件列表 = os.listdir(目标目录)  # 分离出目录列表与文件列表

            for i in '12345':
                随机图像 = random.choice(子目录列表与文件列表)# 随机列表
                随机图像文件路径 = os.path.join(目标目录, 随机图像)
                if os.path.isdir(随机图像文件路径):  # 判断是不是文件夹  判断文件 os.path.isfile
                    pass
                else:  # 否则 为文件

                    break  # 结束循环
            return 随机图像文件路径  # 返回


        头像设置 = 'http://www.baidu.com/p/setting/profile/portrait'
        self.浏览器操作.get(头像设置)
        随机图像 = 模具一一随机图像文件()

        """============隐式等待 试错============"""
        for 序号 in '123':
            try:  # 调用异常处理,应对易发生错误的位置
                self.浏览器操作.implicitly_wait(10)  # 隐式等待
                """点击  热门推荐头像"""

                self.浏览器操作.find_element_by_xpath('//*[@id="fileImg"]').send_keys(随机图像)# 文件路径

            except:  # 异常处理
                if '1' in 序号:
                    self.浏览器操作.refresh()  # 刷新下页面
                elif '2' in 序号:
                    self.跳过循环 = '跳过循环'
                    return  # 返回
            else:  # 必须放在所有的except子句之后.这个子句将在try子句没有发生任何异常的时候执行.
                break  # 结束循环
        time.sleep(2)  # 等待
        self.浏览器操作.implicitly_wait(10)  # 隐式等待
        """点击  热门推荐头像"""
        self.浏览器操作.find_element_by_xpath('//*[@id="savePortrait"]').click()  # 点击

        time.sleep(2) # 等待

        self.模具一一查看变量输出文本值("设置头像完成,随机图像", 随机图像)


    def 模具一一随机选择头像(self):
        头像设置='http://www.baidu.com/p/setting/profile/portrait'
        self.浏览器操作.get(头像设置)

        """============隐式等待 试错============"""
        for 序号 in '123':
            try:  # 调用异常处理,应对易发生错误的位置
                self.浏览器操作.implicitly_wait(10)  # 隐式等待
                """点击  热门推荐头像"""
                self.浏览器操作.find_element_by_xpath('//*[@id="portraitHotrecomLi"]').click()  # 点击

            except:  # 异常处理
                if '1' in 序号:
                    self.浏览器操作.refresh()  # 刷新下页面
                elif '2' in 序号:
                    self.跳过循环 = '跳过循环'
                    return  # 返回
            else:  # 必须放在所有的except子句之后.这个子句将在try子句没有发生任何异常的时候执行.
                break  # 结束循环



        time.sleep(1)  # 等待

        """点击  随机点击头像"""
        从1到24中随机挑选一个整数 = random.randrange(1, 25)

        定位='//*[@id="hot-wildkid-{}"]/img'.format(str(从1到24中随机挑选一个整数))#'代入 '{}'
        self.浏览器操作.find_element_by_xpath(定位).click()  # 点击
        time.sleep(1)  # 等待

        """点击  保存头像"""
        self.浏览器操作.find_element_by_xpath('//*[@id="savePortrait"]').click()  # 点击
        time.sleep(2)  # 等待

        self.模具一一查看变量输出文本值("设置头像完成", "")



    """      4     """
    def 模具一一数据库更新一互相关注(self):
        """更新数据库"""
        self.sql语句 = 'UPDATE `推广帐号` SET `互相关注`="{}" WHERE `ID`={}'.format(self.帐号,
                                                                          self.顶贴ID)  # '代入 '{}'   # ' '{}' # SQL 查询语句
        self.模具一一查看变量输出文本值("self.sql语句", self.sql语句, 8)
        self.模具一一内容数据库("更新 已 互相关注 的帐号")


        os.system("taskkill /F /IM chromedriver.exe")  # 关闭程序名 chromedriver.exe


    def 模具一一示例(self):
        pass

类=类一一帐号互相关注()






