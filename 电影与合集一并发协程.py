# -*- coding:utf-8

import grequests  # 并发协程
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
from selenium import webdriver  # 浏览的驱动
import win32api  # 操作本地文件
from 每日最新剧集一批量一并发 import 类一一公共库# 导入模块





class 类一一后台发布(类一一公共库):
    def __init__(self):
        self.模具一一测试cookies存活()
        # self.新旧剧集 = '电影与合集'
        # self.模具一一调度控制()
        self.新旧剧集 = '最新影视剧'
        self.模具一一调度控制()
        # print('等待:500秒')
        # time.sleep(500)  # 等待

    def 模具一一调度控制(self):
        影视类型列表 = ['电影', '电视剧', '动漫']
        for self.影视类型 in 影视类型列表:
            print('上传类型:', self.影视类型)
            self.模具一一读取内容数据库()
            self.模具一一数据表反向过滤短标题()
            self.模具一一发布文章()
        self.模具一一模具一一明天日期更新剧集的全部更新()
        self.模具一一更新数据库里剧集发布状态()

    def 模具一一打开的网址请求返回网页内容(self, 网址, 文章内容):
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
                返回网页内容 = self.s.post(网址, data=文章内容, headers=头部信息, timeout=1)
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
                        print('成功发布', self.长标题)
                        break  # 结束循环
                else:
                    print('网站网络异常,状态码:', 返回网页内容)
                    print('等待10秒')
                    time.sleep(10)

    def 模具一一模具一一明天日期更新剧集的全部更新(self):
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

    def 模具一一数据表反向过滤短标题(self):
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
                print('过滤的长标题........', 长标题)
                continue  # 跳过当前循环,继续进行下一轮循环
            self.反向过滤数据表.append(每行数据)
            短标题列表.append(短标题)
            短标题列表.append(长标题)
        self.反向过滤数据表.reverse()  # 反向排序 列表
        短标题列表 = []

    def 模具一一更新数据库里剧集发布状态(self):
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

    def 模具一一读取内容数据库(self):
        # 连接数据库
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "", self.新旧剧集, charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句   已下载内容网址
        sql = "SELECT  `影视类型`, `长标题`, `短标题`, `主栏目ID`, `副栏目ID`, `摘要`, `正文`, `标题图`, `主演之标题前栏目字符串`, `文章来源之更新集数`, `帖子链接` FROM `网站文章内容` WHERE `发布`='否'  and `影视类型`=('%s') " % (
            self.影视类型)  # 不换行 end=""
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        self.数据表 = cursor.fetchall()
        # 关闭数据库连接
        db.close()

    def 模具一一发布文章(self):
        for 单条文章内容 in self.反向过滤数据表:
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
            self.帖子链接 = 单条文章内容[10]
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
            后台提交网址 = 'http://3e38.com/image/article_add.php?channelid=17'
            self.长标题 = 长标题
            self.模具一一打开的网址请求返回网页内容(后台提交网址, 文章内容)


class 类一一综合影视类型(类一一公共库):  # 调用 类的模具 self.模具一一数据库()
    def __init__(self):
        self.模具一一测试cookies存活()
        self.模具一一换头部信息()

        self.页面提取帖子链接列表文本 = ''
        self.模具一一置顶帖子剧集动漫类型()  # 电视剧集动漫


        今天天数 = datetime.datetime.now()
        三月前时间 = 今天天数 + datetime.timedelta(days=-90)
        规则 = '\s.{0,}'
        三月前时间 = re.sub(规则, '', str(三月前时间))  # 除掉后面的时间分数 替换   ,count=0,re.S|re.I
        self.三月前时间 = int(str(三月前时间).replace("-", ""))  # 替换   , 1) 次数 1


        影视类型列表=['电影','电视剧','动漫']
        for 影视类型 in 影视类型列表:
            self.影视类型 =影视类型

            self.模具一一提取电影与合集数据库里的过滤网址一已下载内容网址一过滤种子网址()
            self.模具一一提取最新影视剧数据库里的过滤网址()

            self.过滤帖子网址 = self.过滤帖子网址 + self.过滤帖子网址二 +self.页面提取帖子链接列表文本
            if '电视剧' in self.影视类型:
                self.倒页总数 = 100
                self.页数网址 = 'http://91btbtt.com/forum-index-fid-950-page-123.htm'

            elif '动漫' in self.影视类型:  # 其它条件.
                self.倒页总数 = 50
                self.页数网址 = 'http://91btbtt.com/forum-index-fid-981-page-123.htm'

            else:  # 否则
                self.倒页总数 = 0 # 电影
                self.页数网址 = 'http://91btbtt.com/forum-index-fid-951-page-123.htm'



            self.模具一一总提取帖子链接列表()
            self.模具一一综合影视各链接网址处理()

    def 模具一一综合影视各链接网址处理(self):
        self.目录与种子名一下载地址组列表 = []  # 初始设定
        self.种子下载地址列表 = []  # 初始设定


        self.模具一一换头部信息()
        print('========================等待==============================')

        内容页列表 = self.模具一一grequests打开网址随机无序集(self.页面提取帖子链接列表)
        倒计数 = len(内容页列表)
        for 内容页 in 内容页列表:
            倒计数 = 倒计数 - 1
            self.跳过循环 = 1  # 设定初始值
            self.符号清洗不过滤空格 = 0  # 设定初始值
            print('========倒计数=========', 倒计数)
            # ======================
            self.帖子内容 = 内容页.text
            self.各帖子链接 = 内容页.url
            self.帖子内容html = etree.HTML(内容页.text)
            print('==================:')
            print('网址:', self.各帖子链接)
            # =====================
           
            # ===========发贴时间半年前比较=========================
            if self.影视类型 == '电影':
                self.模具一一判断发贴时间三月前或内()
            if self.跳过循环 == 0:
                continue  # 跳过循环
            # ====================================
            self.帖子标题列表 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/h2/text()')
            self.标题前的栏目列表 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/h2/a/text()')


            # ===========帖子标题列表清洗===========================================
            self.模具一一提取帖子标题()


            # =========#过滤标题栏目=====================================================
            if self.影视类型 == '电视剧' or self.影视类型 == '动漫':
                self.模具一一剧集过滤标题栏目()
            else:  # 否则
                self.模具一一电影过滤标题栏目()
            if self.跳过循环 == 0:
                self.模具一一保存电影与合集过滤帖子网址()
                continue  # 跳过循环
            # ========过滤图片已破与标记其它网站,跳过循环=================================================================
            self.模具一一过滤图片已破与标记其它网站()
            if self.跳过循环 == 0:
                self.模具一一保存电影与合集过滤帖子网址()
                continue  # 跳过循环
            # ========提取一楼种子名进行过滤=============================================================
            if self.影视类型 == '电视剧' or self.影视类型 == '动漫':
                self.模具一一提取一楼种子名进行过滤()
            else:  # 否则
                self.模具一一电影过滤一楼种子名()
            if self.跳过循环 == 0:
                self.模具一一保存电影与合集过滤帖子网址()
                continue  # 跳过循环

            # ===================提取长标题===============================
            self.模具一一提取长标题()
            if self.跳过循环 == 0:
                self.模具一一保存电影与合集过滤帖子网址()
                continue  # 跳过循环
            print('长标题:', self.长标题)
            # 符号清洗
            # ==============短标题的清洗============================
            self.模具一一提取短标题()
            if len(self.短标题) == 0:
                self.短标题 = self.原版标题
            print('短标题', self.短标题)
            # ==============摘要===========================
            if '电视剧' in self.影视类型:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                self.摘要 = '<h2>资源下载:<a href="/uploads/3html/dianshiju/{}.html"target="_blank">{}.torrent</a></h2>'.format(
                    self.短标题, self.长标题)  # 代入 .不换行 end=""
            elif '动漫' in self.影视类型:  # 其它条件.
                self.摘要 = '<h2>资源下载:<a href="/uploads/3html/dongman/{}.html"target="_blank">{}.torrent</a></h2>'.format(
                    self.短标题, self.长标题)  # 代入 .不换行 end=""
            else:  # 否则
                self.摘要 = '<h2>资源下载:<a href="/uploads/3html/dying/{}.html"target="_blank">{}.torrent</a></h2>'.format(
                    self.短标题, self.长标题)  # 代入 .不换行 end=""
            print('摘要', self.摘要)
            # ===========self.主栏目ID、self.标题前栏目字符串==============================================================================================
            self.标题前栏目字符串 = ''.join(self.标题前的栏目列表)
            self.时间ID = int(time.strftime("%y%m%d%H%M%S", time.localtime()))
            self.更新集数='合集'
            print('标题前栏目字符', self.标题前栏目字符串)
            # ===========self.网站副栏目ID============================================================================
            if '电视剧' in self.影视类型:
                self.模具一一电视剧网站副栏目ID()
            elif '动漫' in self.影视类型:  # 其它条件.
                self.模具一一动漫网站副栏目ID()
            else:  # 否则
                self.模具一一电影网站副栏目ID()

            # =========(模具)self.正文清洗=====================================================
            self.标题图列表 = []
            self.模具一一帖子正文清洗()
            # =========(模具)标题图===============================================
            self.模具一一提取标题图()
            if self.跳过循环 == 0:
                self.模具一一保存电影与合集过滤帖子网址()
                continue  # 跳过循环
            self.标题图 = self.模具一一网站图片网址清洗转换(self.标题图)
            # =========== 提取一楼种子列表==================================================================
            self.模具一一提取一楼种子()
            # =========== 提取各分层页种子列表=================================================================
            self.模具一一提取各分层页种子列表()
            # self.模具一一保存最新影视剧已下载内容页网址()
            if self.各帖子链接 in self.过滤帖子网址:
                print('网站内容页已经存在,跳过保存')
            else:  # 否则
                self.模具一一保存电影与合集帖子内容至数据库()

                self.过滤帖子网址 = self.过滤帖子网址 + str(self.各帖子链接)
        self.模具一一下载并保存种子()
    """======================="""

    def 模具一一置顶帖子剧集动漫类型(self):

        网址列表 = []
        打开的网址 = 'http://91btbtt.com'
        网址列表.append(打开的网址)
        首页网页内容列表 = self.模具一一grequests打开网址随机无序集(网址列表)
        # self.模具一一打开的网址请求返回网页内容(打开的网址)
        帖子内容html = etree.HTML(首页网页内容列表[0].text)
        # ==================置顶类型帖子网址列表================================
        # for 帖子位置数 in range(2,6):  # 范围
        置顶类型帖子网址列表 = []
        for self.帖子位置数 in range(2, 6):
            规则 = "//*[@id=\"threadlist\"]/table[{}]/tbody/tr/td[1]/a[5]/@href".format(
                self.帖子位置数)  # text()format 代入{}内,不换行 end=""
            规则 = str(规则).replace("/tbody", "")
            置顶类型帖子 = 帖子内容html.xpath(规则)
            置顶类型帖子网址 = 'http://91btbtt.com/' + str(置顶类型帖子[0])
            置顶类型帖子网址列表.append(置顶类型帖子网址)
        # =================置顶类型帖子网页内容===============================
        置顶类型帖子网页内容列表 = self.模具一一grequests打开网址随机无序集(置顶类型帖子网址列表)
        for 置顶类型帖子网页内容 in 置顶类型帖子网页内容列表:
            self.类型帖子内容html = etree.HTML(置顶类型帖子网页内容.text)

            self.模具一一提炼类型帖子最新各剧集链接()


    def 模具一一总提取帖子链接列表(self):
        self.模具一一提取电影与合集数据库里的总提取帖子链接列表()


        总提取帖子链接列表 = []

        if self.倒页总数 == 0:
            pass
        else:  # 否则
            总倒页链接 = []
            for 倒页数 in range(self.倒页总数, 0, -1):
                print('倒页数', 倒页数)
                各帖子链接 = str(self.页数网址).replace("123", str(倒页数))
                print(self.影视类型,'各页数链接', 各帖子链接)
                # =========请求各帖子链接网页内容======================
                各帖子链接 = self.模具一一网站图片网址清洗转换(各帖子链接)
                总倒页链接.append(各帖子链接)
            页数链接列表网页内容列表 = self.模具一一grequests打开网址随机无序集(总倒页链接)
            计数器=0
            for 页数链接列表网页内容 in 页数链接列表网页内容列表:
                # ====================================================
                帖子列表html = etree.HTML(页数链接列表网页内容.text)
                提取帖子链接列表 = 帖子列表html.xpath('//*[@id="threadlist"]/table[*]/tr/td[1]/a[1]/@href')
                for 各帖子链接 in 提取帖子链接列表:
                    if '-page' in 各帖子链接:
                        规则 = '-page.{1,}'
                        各帖子链接 = re.sub(规则, '.htm', str(各帖子链接))  # 替换   ,count=0,re.S|re.I
                    规则 = '.{1,}thread'
                    各帖子链接 = re.sub(规则, 'http://91btbtt.com/thread', str(各帖子链接))  # 替换
                    if 各帖子链接 in self.过滤帖子网址:
                        continue  # 跳过循环
                    self.模具一一保存电影与合集总提取帖子链接列表(各帖子链接)
                    总提取帖子链接列表.append(各帖子链接)
                    print('提取帖子链接数', 计数器)
                    计数器=计数器+1

        for 各帖子链接组 in self.总提取帖子数据库链接组列表:
            各帖子链接 = 各帖子链接组[0]
            if 各帖子链接 in self.过滤帖子网址:
                print('过滤帖子网址二,跳过采集')
                continue  # 跳过循环
            总提取帖子链接列表.append(各帖子链接)
        print('===帖子链接总数:=====', len(总提取帖子链接列表))
        总提取帖子链接列表 = set(总提取帖子链接列表)
        self.页面提取帖子链接列表 = list(总提取帖子链接列表)
        self.电视剧类型 = "最新电影"
        print('====================帖子链接总数去重复后:=================', len(self.页面提取帖子链接列表))

    """==========各类型模具============="""

    def 模具一一剧集过滤标题栏目(self):
        列表 = ['[单集]', '[讨论]', '[Resilio-Sync]', '猪猪', '音乐', '动漫']
        for 符号 in 列表:
            if self.影视类型 == '电视剧' and 符号 == '猪猪':
                continue  # 跳过当前循环,继续进行下一轮循环
            if 符号 in str(self.标题前的栏目列表):
                print(符号, '过滤的栏目跳过循环')
                print('=====================')
                self.模具一一保存电影与合集过滤帖子网址()
                self.跳过循环 = 0
                return  # 返回 0 值,跳过循环
        if 'torrent.gif' not in self.帖子内容 and '个附件' not in self.帖子内容:
            print('无种子附件,跳过循环')
            print('=====================')
            self.模具一一保存电影与合集过滤帖子网址()
            self.跳过循环 = 0
            return  # 返回 0 值,跳过循环

    def 模具一一电影过滤标题栏目(self):
        列表 = ['删节版', '删减版', 'TS', '抢先', '抢鲜', 'TC', '清晰', '大陆', '中国', 'BT之家整合', '版块公告', '版块专用', '[猪猪]',
              '[Resilio-Sync]', '有水印', '有广告']
        帖子标题 = str(self.帖子标题) + str(self.标题前的栏目列表)
        版本表 = ['抢', '删', '鲜']
        for 版符号 in 版本表:
            if 版符号 in 帖子标题 and '版' in 帖子标题:
                print(版符号, '版,跳过循环')
                print('=====================')
                self.模具一一保存电影与合集过滤帖子网址()
                self.跳过循环 = 0
                return  # 返回 0 值,跳过循环
        for 符号 in 列表:
            if 符号 in 帖子标题:
                print(符号, '列表符号,跳过循环')
                print('=====================')
                self.模具一一保存电影与合集过滤帖子网址()
                self.跳过循环 = 0
                return  # 返回 0 值,跳过循环

    def 模具一一判断发贴时间三月前或内(self):
        发帖时间列表 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[2]/td[3]/div/b[1]/text()')
        发帖时间 = 发帖时间列表[0]
        规则 = '\s.{0,}'
        发帖时间天数 = re.sub(规则, '', str(发帖时间))  # 除掉后面的时间分数 替换   ,count=0,re.S|re.I
        发帖时间天数 = int(str(发帖时间天数).replace("-", ""))  # 替换   , 1) 次数 1
        if self.三月前时间 > 发帖时间天数:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            
            print('发贴时间为三月前:')
        else:  # 否则
            self.跳过循环 == 0

            print('发贴时间为三月内最新电影,跳过循环:')

    def 模具一一发贴时间半年前过滤(self):
        发帖时间列表 = self.帖子内容html.xpath('//*[@id="body"]/div/table[2]/tr[2]/td[3]/div/b[1]/text()')
        self.发帖时间 = 发帖时间列表[0]
        规则 = '\s.{0,}'
        发帖时间天数 = re.sub(规则, '', str(self.发帖时间))  # 除掉后面的时间分数 替换   ,count=0,re.S|re.I
        发帖时间天数 = int(str(发帖时间天数).replace("-", ""))  # 替换   , 1) 次数 1
        if 发帖时间天数 < self.半年前时间 and '4378529' not in str(self.各帖子链接):  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            self.跳过循环 = 0
            print('发贴时间为半年前,跳过循环:')
            return  # 返回

    def 模具一一动漫网站副栏目ID(self):
        # 全部合集时 载入'[连载]更改为,'[合集]': '124',
        网站副栏目字典 = {'[合集]': '124', '[连载]': '124', '[美国]': '120', '[英国]': '120', '[多国]': '120', '[大陆]': '119',
                   '[香港]': '119', '[台湾]': '119',
                   '[日本]': '118',
                   '[法国]': '120', '[加剧]': '120',
                   '[合 集]': '124',
                   '[全集]': '124', '[打包]': '124', '[断载]': '124', '[2006]': '137',
                   '[2007]': '136', '[2008]': '135', '[2009]': '134', '[2010]': '133', '[2011]': '132', '[2012]': '131',
                   '[2013]': '130', '[2014]': '129', '[2015]': '128', '[2016]': '127', '[2017]': '126', '[2018]': '125',
                   '[更 早]': '138', '[新番]': '124', '[火影]': '124', '[海贼]': '124', '[柯南]': '124', '[敢达]': '124',
                   '[死神]': '124',
                   '[银魂]': '124', '[妖尾]': '124', '[龙珠]': '124', '[布袋戏]': '124', '[完结]': '124', '[其他]': '124',
                   '[音乐]': '139', '[]': '', '单集': '', '[纯净版]': ''}
        网站副栏目ID = [网站副栏目字典[x] if x in 网站副栏目字典 else x for x in self.标题前的栏目列表]
        网站副栏目ID = str(网站副栏目ID)
        # 符号清洗
        self.符号清洗不过滤空格 = 1  # 符号清洗不过滤 空格
        网站副栏目ID = self.模具一一符号清洗(网站副栏目ID)
        网站副栏目ID = 网站副栏目ID.strip()
        if len(网站副栏目ID) == 0:
            网站副栏目ID = '124'
        网站副栏目ID = str(网站副栏目ID).replace(" ", ",")
        网站副栏目ID = 网站副栏目ID.replace("124,124,124", "124")
        self.网站副栏目ID = 网站副栏目ID.replace("124,124", "124")

        if '118' in 网站副栏目ID:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            self.主栏目ID = '118'
        else:  # 否则
            self.主栏目ID = '23'

        print('网站副栏目ID', self.网站副栏目ID)

    def 模具一一电影网站副栏目ID(self):
        网站副栏目字典 = {'[]': '', '[纯净版]': '', '[欧美]': '25', '[美国]': '25', '[英国]': '25', '[大陆]': '26', '[香港]': '27',
                   '[台湾]': '28', '[日本]': '29',
                   '[韩国]': '30',
                   '[法国]': '31', '[西剧]': '31', '[泰国]': '31', '[加剧]': '31', '[意剧]': '31', '[澳剧]': '31', '[德国]': '31',
                   '[新马]': '31', '[多国]': '31', '[剧情]': '34', '[喜剧]': '33', '[爱情]': '34', '[偶像]': '34', '[动作]': '32',
                   '[奇幻]': '37',
                   '[科幻]': '35', '[印度]': '31',
                   '[悬疑]': '40', '[罪案]': '40', '[犯罪]': '40', '[刑侦]': '40', '[战争]': '38', '[灾难]': '38', '[谍战]': '40',
                   '[军旅]': '38', '[历史]': '39',
                   '[古装]': '39', '[惊悚]': '43', '[恐怖]': '43', '[真人]': '34', '[时装]': '34',
                   '[医务]': '34', '[歌舞]': '34', '[其他]': '44', '[都市]': '34', '[情感]': '34',
                   '[家庭]': '34',
                   '[武侠]': '39', '[纪录]': '42', '[经典]': '42', '[动画]': '41',
                   '[微电影]': '44', '[同性]': '44', '[其他]': '44', '[合集]': '140', '[系列]': '140', '[2006]': '58',
                   '[2007]': '57', '[2008]': '56', '[2009]': '55', '[2010]': '54', '[2011]': '53', '[2012]': '52',
                   '[2013]': '51', '[2014]': '50', '[2015]': '49', '[2016]': '48', '[2017]': '47', '[2018]': '46',
                   '[更 早]': '45', '[更早]': '45'}
        网站副栏目ID = [网站副栏目字典[x] if x in 网站副栏目字典 else x for x in self.标题前的栏目列表]
        网站副栏目ID = str(网站副栏目ID)
        if '41' in str(网站副栏目ID):
            if '25' in str(网站副栏目ID):
                网站副栏目ID = str((网站副栏目ID)).replace("25", "25 120")
            elif '29' in str(网站副栏目ID):
                网站副栏目ID = str((网站副栏目ID)).replace("29", "29 118")
        # 符号清洗
        self.符号清洗不过滤空格 = 1  # 符号清洗不过滤 空格
        网站副栏目ID = self.模具一一符号清洗(网站副栏目ID)
        网站副栏目ID = 网站副栏目ID.strip()
        if len(网站副栏目ID) == 0:
            网站副栏目ID = '34'
        self.网站副栏目ID = str(网站副栏目ID).replace(" ", ",")
        if '25' in self.网站副栏目ID:
            self.主栏目ID = '25'
        else:  # 否则
            self.主栏目ID = '21'
        print('.主栏目ID', self.主栏目ID)
        print('网站副栏目ID', self.网站副栏目ID)

    def 模具一一电视剧网站副栏目ID(self):
        # 全部合集时 载入'[连载] '60'':改为全集 '61',
        网站副栏目字典 = {'[连载]': '61', '[]': '', '[美国]': '84', '[英国]': '84', '[大陆]': '85', '[香港]': '86', '[台湾]': '87',
                   '[日本]': '88',
                   '[韩国]': '89',
                   '[法国]': '90', '[多国]': '90', '[印度]': '90', '[西剧]': '90', '[泰国]': '90', '[加剧]': '84', '[意剧]': '90',
                   '[澳剧]': '90', '[德国]': '90',
                   '[新马]': '90', '[剧情]': '91', '[喜剧]': '92', '[爱情]': '93', '[偶像]': '91', '[动作]': '94', '[奇幻]': '95',
                   '[科幻]': '96',
                   '[悬疑]': '97', '[罪案]': '97', '[灾难]': '97', '[刑侦]': '97', '[战争]': '98', '[谍战]': '97', '[军旅]': '98',
                   '[历史]': '99',
                   '[古装]': '99', '[惊悚]': '100', '[恐怖]': '100', '[真人]': '101', '[时装]': '91',
                   '[医务]': '91', '[歌舞]': '91', '[其他]': '91', '[都市]': '91', '[情感]': '91',
                   '[家庭]': '91',
                   '[武侠]': '94', '[纪录]': '102', '[经典]': '103', '[合 集]': '61',
                   '[全集]': '61', '[打包]': '61', '[单集]': '61', '[合集]': '61', '[断载]': '61', '[2006]': '117',
                   '[2007]': '116', '[2008]': '115', '[2009]': '114', '[2010]': '113', '[2011]': '112', '[2012]': '111',
                   '[2013]': '110', '[2014]': '109', '[2015]': '108', '[2016]': '107', '[2017]': '106', '[2018]': '105',
                   '[更 早]': '104', '[星期一]': '141', '[情感]': '91', '[情感]': '91', '[情感]': '91', '[情感]': '91', '[情感]': '91',
                   '[情感]': '91'}
        网站副栏目ID = [网站副栏目字典[x] if x in 网站副栏目字典 else x for x in self.标题前的栏目列表]
        网站副栏目ID = str(网站副栏目ID)
        if '[动画]' in str(网站副栏目ID):
            if '88' in str(网站副栏目ID):
                网站副栏目ID = str((网站副栏目ID)).replace("[动画]", "118")
            elif '85' in str(网站副栏目ID):
                网站副栏目ID = str((网站副栏目ID)).replace("[动画]", "119")
            elif '84' in str(网站副栏目ID):
                网站副栏目ID = str((网站副栏目ID)).replace("[动画]", "120")
            elif '87' in str(网站副栏目ID):
                网站副栏目ID = str((网站副栏目ID)).replace("[动画]", "")
            else:
                网站副栏目ID = str((网站副栏目ID)).replace("[动画]", "90")
        # 符号清洗
        self.符号清洗不过滤空格 = 1  # 符号清洗不过滤 空格
        网站副栏目ID = self.模具一一符号清洗(网站副栏目ID)
        if len(网站副栏目ID) == 0:
            网站副栏目ID = '91'
        self.网站副栏目ID = str(网站副栏目ID).replace(" ", ",")

        if '84' in self.网站副栏目ID:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            self.主栏目ID ='84'
        else:  # 否则
            self.主栏目ID = '22'

        print('网站副栏目ID', self.网站副栏目ID)

    def 模具一一电视剧副栏目一星期数ID(self):
        规则 = '\s.{0,}'
        星期数 = re.sub(规则, '', str(self.发帖时间))  # 替换   ,count=0,re.S|re.I
        星期数 = 星期数.strip('[')
        星期数 = 星期数.strip('\'')
        发贴时间列表 = 星期数.split("-")
        年 = int(发贴时间列表[0])
        月 = int(发贴时间列表[1])
        日 = int(发贴时间列表[2])
        # a=(datetime.strptime(发贴时间, "%w"
        today = int(time.strftime("%w"))
        星期数 = datetime.datetime(年, 月, 日).strftime("%w")
        星期数字典 = {'0': '141', '1': '141', '2': '142', '3': '143', '4': '144', '5': '145', '6': '146', '7': '147'}
        for 字符 in 星期数字典:  # 范围 range
            if 字符 in 星期数:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                self.网站副栏目一星期数ID = 星期数字典[字符]
                print('网站副栏目一星期数ID', self.网站副栏目一星期数ID)
                break  # 结束循环

    def 模具一一动漫副栏目一星期数ID(self):
        规则 = '\s.{0,}'
        星期数 = re.sub(规则, '', str(self.发帖时间))  # 替换   ,count=0,re.S|re.I
        星期数 = 星期数.strip('[')
        星期数 = 星期数.strip('\'')
        发贴时间列表 = 星期数.split("-")
        年 = int(发贴时间列表[0])
        月 = int(发贴时间列表[1])
        日 = int(发贴时间列表[2])
        # a=(datetime.strptime(发贴时间, "%w"
        today = int(time.strftime("%w"))
        星期数 = datetime.datetime(年, 月, 日).strftime("%w")
        星期数字典 = {'1': '148', '2': '149', '3': '150', '4': '151', '5': '152', '6': '153', '7': '154'}
        for 字符 in 星期数字典:  # 范围 range
            if 字符 in 星期数:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                self.网站副栏目一星期数ID = 星期数字典[字符]
                break  # 结束循环

    def 模具一一电影过滤一楼种子名(self):
        种子名列表 = self.帖子内容html.xpath(
            '//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[*]/td[1]/a/text()|//*[@id="body"]/div/table[2]/tr[1]/td[3]/font/b/div[1]/table/tr[3]/td[1]/a/text()')
        种子名列表 = str(种子名列表)
        版本表 = ['抢', '删', '鲜']
        for 版符号 in 版本表:
            if 版符号 in 种子名列表 and '版' in 种子名列表:
                print(版符号, '版,跳过循环,一楼种子名')
                print('=====================')
                self.模具一一保存电影与合集过滤帖子网址()
                self.跳过循环 = 0
                return  # 返回 0 值,跳过循环
        列表 = ('删节版', '删减版', 'TS', '抢先', 'TC', '清晰', '大陆', '中国', 'www.', '.com', '.net')
        for 符号 in 列表:
            if 符号 in 种子名列表:
                print(符号, '列表符号,跳过循环,一楼种子名')
                print('=====================')
                self.模具一一保存电影与合集过滤帖子网址()
                self.跳过循环 = 0
                return  # 返回 0 值,跳过循环

    """=========数据库=============="""




开始时间计数 = int(time.time())
类 = 类一一综合影视类型()  # 电视剧、动漫
类c = 类一一后台发布()
结束时间计数 = int(time.time())
用时 = 结束时间计数 - 开始时间计数
取整除分数 = int(用时) // 60
除的余数的秒数 = int(用时) % 60
print('用时计数:', 取整除分数, '分:', 除的余数的秒数, '秒')
