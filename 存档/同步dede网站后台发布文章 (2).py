import time#导入时间
# -*- coding: UTF-8 -*-

import random# 导入随机

import datetime#导入时间
import pymysql #mysql数据库
import requests  # 导入浏览器
import re
from selenium import webdriver# 浏览的驱动


#================提取网页内容===============================

class 类_后台发布:
    def __init__(self, 影视类型):
        self.影视类型 = 影视类型
        print(self.影视类型)

    def 模具_明天日期的全部更新(self):
        print('正在更新....')
        url = 'http://3e38.com/image/makehtml_all.php?action=make&uptype=time&starttime=2018-01-29&startid=0&Submit=%E5%BC%80%E5%A7%8B%E6%9B%B4%E6%96%B0'
        今天时间加八小时 = (datetime.datetime.now() + datetime.timedelta(hours=8)).strftime("%Y-%m-%d")
        url = str(url).replace('2018-01-29', 今天时间加八小时)
        req3 = self.s.post(url)

        url列表 = ['http://3e38.com/image/makehtml_all.php?action=make&step=2&uptype=time&mkvalue=1517068800',
                 'http://3e38.com/image/makehtml_archives_action.php?endid=0&startid=-1&typeid=0&totalnum=31&startdd=20&pagesize=20&seltime=0&sstime=1517101367&stime=&etime=&uptype=time&mkvalue=1517068800&isremote=0&serviterm=',
                 'http://3e38.com/image/makehtml_all.php?action=make&step=3&uptype=time&mkvalue=1517068800',
                 'http://3e38.com/image/makehtml_all.php?action=make&step=4&uptype=time&mkvalue=1517068800',
                 'http://3e38.com/image/makehtml_list_action.php?gotype=mkall',
                 'http://3e38.com/image/makehtml_all.php?action=make&step=10']
        for url in url列表:
            req3 = self.s.post(url)
        print('生成今日的全部更新')

    def 模具_浏览器输入验证码提取cookies(self):
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        driver = webdriver.Chrome(chrome_options=option)

        driver.get("http://3e38.com/image/login.php?gotopage=%2Fimage%2Findex.php")

        # 参数是像素点宽，高
        driver.set_window_size(800, 800)
        # driver.maximize_window() 浏览器全屏显示，不带参数

        driver.implicitly_wait(10)  # 设置 隐式等待.单位是秒（s）,

        driver.find_element_by_xpath('//*[@id="login-box"]/div[2]/form/dl/dd[1]/input').send_keys(
            "ad38min")  # 定位用户名
        driver.find_element_by_xpath('//*[@id="login-box"]/div[2]/form/dl/dd[2]/input').send_keys(
            "qq962962")  # 定位密码

        input("\n\n按下 确认键enter 键后继续.")
        driver.find_element_by_xpath('//*[@id="login-box"]/div[2]/form/dl/dd[4]/button').click()  # 定位确认登录
        print('正在登录......')
        driver.implicitly_wait(10)  # 设置  隐式等待（s）,
        driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[4]/div/form/input[1]').click()  # 定位确认登录
        print('登录成功，提取保存cookie')
        保存cookie = [item["name"] + ":" + item["value"] for item in driver.get_cookies()]
        # cookiestr = ';'.join(item for item in 保存cookie)
        规则 = r"[\'\[\]]{1}"
        保存cookie = re.sub(规则, '', str(保存cookie))
        保存cookie = str(保存cookie).replace(",", ";")
        保存cookie = str(保存cookie).replace(":", "=")

        保存cookie = str(保存cookie)
        f = open("E:\PY学习文件\PyCharm文件\BT影视剧\de3ede38.txt", "w")  # 保存cookie 文件

        f.write(保存cookie)
        f.close()

    def 模具_导入cookie(self):
        with open('E:\PY学习文件\PyCharm文件\BT影视剧\de3ede38.txt', 'r') as f:

            self.cookies = {}
            for line in f.read().split(';'):
                name, value = line.strip().split('=', 1)  # 1代表只分割一次
                self.cookies[name] = value
    def 模具_测试cookies存活(self):

        self.模具_导入cookie()

        self.url = 'http://3e38.com/image/article_add.php?channelid=17'
        self.s = requests.Session()  # 创建全局会话
        self.s.cookies.update(self.cookies)  # 格式化cookie，全网页才能共享登录cookie，

        返回网页内容 = self.s.get(self.url)

        返回网页内容=返回网页内容.text

        if '看不清' in 返回网页内容:
            print('登录失效，浏览器输入验证码提取cookies')
            self.模具_浏览器输入验证码提取cookies()

    def 模具_数据表反向过滤短标题(self):
        # 关闭数据库连接
        数据表 = list(self.数据表)  # 转换为列表
        数据表.reverse()  # 反向排序 列表

        短标题列表 = []
        self.反向过滤数据表 = []
        for 每行数据 in 数据表:
            每行数据= 每行数据
            短标题 = 每行数据[2]
            长标题 = 每行数据[1]
            if 短标题 in 短标题列表:
                if len(短标题) == 0:
                    self.反向过滤数据表.append(每行数据)
                    # self.时间ID列表.append(每行数据[0])  # 每个时间ID都加入列表
                    continue  # 跳过当前循环，继续进行下一轮循环

                print('过滤的短标题', 短标题)
                #self.时间ID列表.append(每行数据[0])  # 每个时间ID都加入列表
                continue  # 跳过当前循环，继续进行下一轮循环
            elif 长标题 in 短标题列表:
                if len(长标题) == 0:
                    self.反向过滤数据表.append(每行数据)
                    # self.时间ID列表.append(每行数据[0])  # 每个时间ID都加入列表
                    continue  # 跳过当前循环，继续进行下一轮循环
                print('过滤的长标题........',长标题)
                #self.时间ID列表.append(每行数据[0])  # 每个时间ID都加入列表
                continue  # 跳过当前循环，继续进行下一轮循环

            self.反向过滤数据表.append(每行数据)
            短标题列表.append(短标题)
            短标题列表.append(长标题)
        self.反向过滤数据表.reverse()  # 反向排序 列表
        短标题列表 = []

    def 模具_更新数据库里剧集发布状态(self):
        # 连接数据库
        # 连接数据库
        print('连接数据库....')
        db = pymysql.connect("localhost", "root", "", self.影视类型, charset="utf8")
        cursor = db.cursor()
        # SQL 查询语句   已下载内容网址
        for 时间ID in self.时间ID列表:
            # 获取游标
            sql = """UPDATE 剧集 
                    SET 发布='已发布'
                   WHERE 时间ID=('%d');""" % (时间ID)
            # 执行SQL语句
            cursor.execute(sql)

        # 提交到数据库执行
        db.commit()
        # 关闭数据库连接
        db.close()

    def 模具_读取数据库(self):

        # 连接数据库
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "",self.影视类型, charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句   已下载内容网址
        sql = "SELECT * FROM 剧集"
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        self.数据表 = cursor.fetchall()
        # 关闭数据库连接
        db.close()
        self.模具_数据表反向过滤短标题()

    def 模具_发布文章(self):
        for 单条文章内容 in self.反向过滤数据表:
            # 时间ID, 长标题, 短标题, 主栏目ID, 网站副栏目ID, 摘要, 正文, 标题图, 标题前栏目字符串

            时间ID = 单条文章内容[0]
            长标题 = 单条文章内容[1]
            if len(长标题) == 0:
                长标题 = '空标题' + str(random.randrange(1, 100000))
            短标题 = 单条文章内容[2]
            主栏目ID = 单条文章内容[3]
            网站副栏目ID = 单条文章内容[4]
            网站副栏目ID = str(网站副栏目ID).replace("连载", "")
            网站副栏目ID = str(网站副栏目ID).replace("犯罪", "40")
            网站副栏目ID = str(网站副栏目ID).replace("灾难", "36")
            网站副栏目ID = str(网站副栏目ID).replace("印度", "31")
            网站副栏目ID = str(网站副栏目ID).replace("多国", "31")
            网站副栏目ID = str(网站副栏目ID).replace(" ", "")
            网站副栏目ID = str(网站副栏目ID).replace(",,", ",")
            网站副栏目ID = str(网站副栏目ID).strip(',')
            摘要 = 单条文章内容[5]
            正文 = 单条文章内容[6]
            正文 = 正文.strip('[')
            正文 = 正文.strip(']')
            标题图 = 单条文章内容[7]
            文章来源标题前栏目字符串 = 单条文章内容[8]
            更新集数 = 单条文章内容[9]
            更新时间 = time.strftime("%Y-%m-%d ", time.localtime())
            随机浏览数 = random.randrange(1001, 10000)

            文章内容 = {"channelid": 17,
                    "dopost": "save",
                    "title": 长标题,
                    "shorttitle": 短标题,
                    "redirecturl": "",
                    "tags": "",
                    "weight": 26185,
                    "picname": 标题图,
                    '"litpic"; filename=""': "Content-Type: application/octet-stream",
                    "source": 更新集数,
                    "writer": "",
                    "typeid": 主栏目ID,
                    "typeid2": 网站副栏目ID,
                    "keywords": "",
                    "autokey": 1,
                    "description": 摘要,
                    "authors": 文章来源标题前栏目字符串,
                    "areas": "",
                    "murls": "",
                    "dede_addonfields": "authors,multitext;areas,text;murls,multitext",
                    "needwatermark": 1,
                    "sptype": 'hand',
                    "spsize": 5000,
                    "body": 正文,
                    "voteid": "",
                    "notpost": 0,
                    "click": 随机浏览数,
                    "sortup": 0,
                    "color": "",
                    "arcrank": 0,
                    "money": 0,
                    "pubdate": 更新时间,
                    "ishtml": 1, "filename": "",
                    "templet": "",
                    "imageField.x": 33,
                    "imageField.y": 9}

            url = 'http://3e38.com/image/article_add.php?channelid=17'
            # url = str(url) + str(主栏目ID)
            循环 = 0
            while 循环 == 0:  # 条件循环
                try:
                    返回网页内容 = self.s.post(url, data=文章内容)
                    break  # 结束循环
                except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout,
                        requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout):
                    time.sleep(10)# 等待



            返回网页内容=返回网页内容.text

            if '成功' not in (返回网页内容):
                time.sleep(10)  # 等待
                循环 = 0
                while 循环 == 0:  # 条件循环
                    try:
                        返回网页内容 = self.s.post(url, data=文章内容)
                        break  # 结束循环
                    except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout,
                            requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout):
                        time.sleep(10)# 等待

                返回网页内容 = 返回网页内容.text
                if '成功' not in (返回网页内容):
                    print('发布失败')
                    print(时间ID, 单条文章内容[0])
                    print(返回网页内容)
                else:
                    print('成功发布', 长标题)
                    #self.时间ID列表.append(self.时间ID)  # 每个时间ID都加入列表
            else:
                print('成功发布', 长标题)
                #self.时间ID列表.append(时间ID)  # 每个时间ID都加入列表
    def 模具_运行(self):
        self.模具_测试cookies存活()
        self.时间ID列表 = []
        self.模具_读取数据库()
        self.模具_发布文章()


    def 模具_更新剧集(self):
        self.模具_明天日期的全部更新()
        #self.模具_更新数据库里剧集发布状态()

#============================================
电影发布 = 类_后台发布('电影')
电影发布.模具_运行()
电视剧集发布 = 类_后台发布('电视剧集')
电视剧集发布.模具_运行()
动漫发布 = 类_后台发布('动漫')
动漫发布.模具_运行()
动漫发布.模具_更新剧集()

