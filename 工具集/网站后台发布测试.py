import time#导入时间
# -*- coding: UTF-8 -*-

import random# 导入随机

import datetime#导入时间
import pymysql #mysql数据库
import requests  # 导入浏览器
import re
from selenium import webdriver# 浏览的驱动
from 每日最新剧集一批量一并发 import 类一一公共库# 导入模块


#================提取网页内容===============================

class 类_后台发布(类一一公共库):
    def __init__(self):
        self.模具一一测试cookies存活()
        self.新旧剧集 = '电影与合集'
        self.模具_调度控制()
        self.新旧剧集 = '最新影视剧'
        self.模具_调度控制()

        #print('等待:500秒')
        #time.sleep(500)  # 等待

    def 模具_调度控制(self):
        影视类型列表=['电影','电视剧','动漫']
        for self.影视类型 in 影视类型列表:
            print('上传类型:',self.影视类型)
            self.模具_读取内容数据库()
            self.模具_数据表反向过滤短标题()

            self.模具_发布文章()
        self.模具_模具_明天日期更新剧集的全部更新()
        self.模具_更新数据库里剧集发布状态()




    def 模具_打开的网址请求返回网页内容(self,网址,文章内容):
        # global 换IP时间计数  # 时间计数全局变量声明
        循环 = 0
        缓冲时间 = 0
        次数循环 = 0
        while 循环 == 0:  # 条件循环  post
            头部信息 = {'User-Agent': 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'}

            try:
                此时数2 = int(time.time())
                if 缓冲时间 > 此时数2:
                    time.sleep(1)
                返回网页内容 = self.s.post(网址, data=文章内容, headers=头部信息, timeout=3)
                缓冲时间 = int(time.time()) + 1
            except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout,
                    requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout,
                    requests.exceptions.ChunkedEncodingError, requests.exceptions.InvalidSchema) as 异常:

                次数循环 += 1
                print('网络异常等待', 异常)
                print('倒数6秒再连接', 次数循环, '次')
                time.sleep(3)
                if 'None, 10053,' in str(异常):
                    pass

            else:
                if '200' in str(返回网页内容):
                    返回网页内容.encoding = "UTF-8"  # 转换encoding='UTF-8' "gbk"
                    返回网页内容 = 返回网页内容.text

                    if '成功' in (返回网页内容):
                        print('成功发布',self.长标题)
                        break  # 结束循环
                else:
                    print('网站网络异常,状态码:', 返回网页内容)
                    print('等待10秒')
                    time.sleep(10)


    def 模具_模具_明天日期更新剧集的全部更新(self):
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


    def 模具一一浏览器输入验证码提取cookies(self):
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        driver = webdriver.Chrome(chrome_options=option)
        driver.get("http://3e38.com/image/login.php?gotopage=%2Fimage%2Findex.php")
        # 参数是像素点宽,高
        driver.set_window_size(800, 800)
        # driver.maximize_window() 浏览器全屏显示,不带参数
        driver.implicitly_wait(10)  # 设置 隐式等待.单位是秒(s),
        driver.find_element_by_xpath('//*[@id="login-box"]/div[2]/form/dl/dd[1]/input').send_keys(
            "ad38min")  # 定位用户名
        driver.find_element_by_xpath('//*[@id="login-box"]/div[2]/form/dl/dd[2]/input').send_keys(
            "qq962962")  # 定位密码
        print('输入验证码')
        input("\n\n登录成功后,按下 确认键enter 键后继续.")
        print('提取保存cookie')
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
        driver.quit()
        print('关闭浏览器')

    def 模具一一导入cookie(self):
        with open('E:\PY学习文件\PyCharm文件\BT影视剧\de3ede38.txt', 'r') as f:

            self.cookies = {}
            for line in f.read().split(';'):
                name, value = line.strip().split('=', 1)  # 1代表只分割一次
                self.cookies[name] = value
    def 模具一一测试cookies存活(self):

        self.模具一一导入cookie()

        self.url = 'http://3e38.com/image/article_add.php?channelid=17'
        self.s = requests.Session()  # 创建全局会话
        self.s.cookies.update(self.cookies)  # 格式化cookie,全网页才能共享登录cookie,

        返回网页内容 = self.s.get(self.url)

        返回网页内容=返回网页内容.text

        if '看不清' in 返回网页内容:
            print('登录失效,浏览器输入验证码提取cookies')
            self.模具一一浏览器输入验证码提取cookies()
        else:# 否则
             print('======登录成功=========')
                    

    def 模具_数据表反向过滤短标题(self):
        # 关闭数据库连接
        数据表 = list(self.数据表)  # 转换为列表
        数据表.reverse()  # 反向排序 列表

        短标题列表 = []
        self.反向过滤数据表 = []
        for 每行数据 in 数据表:

            短标题 = 每行数据[2]
            长标题 = 每行数据[1]
            if 短标题 in 短标题列表:
                if len(短标题) == 0:
                    self.反向过滤数据表.append(每行数据)
                    # self.时间ID列表.append(每行数据[0])  # 每个时间ID都加入列表
                    continue  # 跳过当前循环,继续进行下一轮循环

                print('过滤的短标题', 短标题)
                continue  # 跳过当前循环,继续进行下一轮循环
            elif 长标题 in 短标题列表:
                if len(长标题) == 0:
                    self.反向过滤数据表.append(每行数据)
                    # self.时间ID列表.append(每行数据[0])  # 每个时间ID都加入列表
                    continue  # 跳过当前循环,继续进行下一轮循环
                print('过滤的长标题........',长标题)

                continue  # 跳过当前循环,继续进行下一轮循环

            self.反向过滤数据表.append(每行数据)
            短标题列表.append(短标题)
            短标题列表.append(长标题)
        self.反向过滤数据表.reverse()  # 反向排序 列表
        短标题列表 = []

    def 模具_更新数据库里剧集发布状态(self):
        # 连接数据库
        # 连接数据库
        print('连接数据库....')
        db = pymysql.connect("localhost", "root", "", self.新旧剧集, charset="utf8")
        cursor = db.cursor()
        # SQL 查询语句   已下载内容网址

        # 获取游标
        sql = "UPDATE `网站文章内容` SET `发布`='是' WHERE `发布`='否'"
        # 执行SQL语句
        cursor.execute(sql)

        # 提交到数据库执行
        db.commit()
        # 关闭数据库连接
        db.close()
        print('更新数据库...成功.')

    def 模具_读取内容数据库(self):

        # 连接数据库
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "",self.新旧剧集, charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句   已下载内容网址
        sql = "SELECT  `影视类型`, `长标题`, `短标题`, `主栏目ID`, `副栏目ID`, `摘要`, `正文`, `标题图`, `主演之标题前栏目字符串`, `文章来源之更新集数`, `帖子链接` FROM `网站文章内容` WHERE `发布`='否'  and `影视类型`=('%s') "% (self.影视类型)#不换行 end=""
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        self.数据表 = cursor.fetchall()
        # 关闭数据库连接
        db.close()

    def 模具_发布文章(self):
        倒数=len(self.反向过滤数据表)
        for 单条文章内容 in self.反向过滤数据表:
            print("发布倒数",倒数)
            倒数=倒数-1
            #  `影视类型`, `长标题`, `短标题`, `主栏目ID`, `副栏目ID`,
            # `摘要`, `正文`, `标题图`,
            # `主演之标题前栏目字符串`, `文章来源之更新集数`, `帖子链接

            影视类型 = 单条文章内容[0]
            长标题 = 单条文章内容[1]
            if len(长标题) == 0:
                长标题 = '空标题' + str(random.randrange(1, 100000))
            短标题 = 单条文章内容[2]
            主栏目ID = 单条文章内容[3]
            网站副栏目ID = 单条文章内容[4]
            摘要 = 单条文章内容[5]
            正文 = 单条文章内容[6]
            标题图 = 单条文章内容[7]
            文章来源标题前栏目字符串 = 单条文章内容[8]
            更新集数 = 单条文章内容[9]
            self.帖子链接= 单条文章内容[10]

            更新时间 = time.strftime("%Y-%m-%d ", time.localtime())
            随机浏览数 = random.randrange(10001, 1000000)

            网站副栏目ID = str(网站副栏目ID).replace(" ", "")
            网站副栏目ID = str(网站副栏目ID).replace(",,", ",")
            网站副栏目ID = str(网站副栏目ID).strip(',')
            正文 = 正文.strip('[')
            正文 = 正文.strip(']')
            正文 = 正文.strip('";')  # 文本前后截去特定字符串
            正文 = 正文.strip('"')  # 文本前后截去特定字符串

            文章内容 = {"channelid": 17,
                    "dopost": "save",
                    "title":长标题,
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

            后台提交网址 = 'http://3e38.com/image/article_add.php?channelid=17'
            self.长标题=长标题
            self.模具_打开的网址请求返回网页内容(后台提交网址,文章内容)

#============================================
类=类_后台发布()


#正文 = str(正文).strip('";')  # 文本前后截去特定字符串
#正文 = str(正文).strip('"')  # 文本前后截去特定字符串

