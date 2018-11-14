# -*- coding:utf-8

from 网页采集公共库 import 类一一采集公共库# 导入模块
import re  # 正则式
import time  # 时间

import os  # 本地操作
import random  # 随机
import win32gui  # 窗口控件
import pymysql  # 数据库


import pyautogui as pag  # 模拟鼠标键盘操作
import pyautogui#模拟鼠标键盘操作
from selenium import webdriver  # 浏览的驱动
import selenium # 浏览的驱动
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC  # =判断网页文本



"""


"""


class 类一一百度采集留言帖子链接(类一一采集公共库):  # 调用 类的模具 self.模具一一数据库()
    def __init__(self):
        self.模具一一高位换头部信息()
        self.测试打印 = '测试'

        self.数据库名 = "影视发帖推广"
        self.留言帖子链接列表 = []


        self.模具一一提取数据库百度已翻下一页过滤网址()

        影视类型列表=['剧集','动漫','电影']
        for self.影视类型 in 影视类型列表:
            self.模具一一查看变量输出文本值("self.影视类型", self.影视类型)

            if '剧集' in self.影视类型: #  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                self.影视类型='美剧'
                self.模具一一换ip连接()
                self.模具一一剧集贴吧目录网址列表()

            elif '动漫' in self.影视类型:# 其它条件.
                self.模具一一换ip连接()
                self.模具一一动漫贴吧目录网址列表()

            elif '电影' in self.影视类型:  # 其它条件.
                self.模具一一换ip连接()
                self.模具一一电影贴吧目录网址列表()

            self.模具一一采集并解析贴吧目录网址列表()
            self.模具一一采集并解析每个贴吧网址()

            self.模具一一采集并解析每个贴吧网址()

            self.模具一一采集并解析最新非零回复帖子链接()

            self.留言帖子链接列表=list(set(self.留言帖子链接列表))

            self.模具一一查看变量输出文本值("留言帖子链接数", len(self.留言帖子链接列表))
            for 留言帖子链接 in self.留言帖子链接列表:
                self.模具一一查看变量输出文本值("留言帖子链接", 留言帖子链接, 8)

    """        1       """



    def 模具一一提取数据库百度已翻下一页过滤网址(self):
        self.sql语句 = """SELECT `帖子网址` FROM `百度帖子网址记录`"""
        self.模具一一内容数据库()
        self.过滤网址=str(self.数据库内容组列表)

        self.sql语句 = """DELETE FROM `百度帖子网址记录` WHERE `记录`='{}'""".format("等待留言")
        self.模具一一内容数据库("删除 等待留言 所有网址")



    def 模具一一剧集贴吧目录网址列表(self):
        剧集贴吧目录网址列表=[]
        for 序号 in '123':
            欧美剧目录 = 'http://tieba.baidu.com/sign/index?kw=%C9%F1%B6%DC%BE%D6&type=3&pn={}'.format(序号)#'代入 '{}'
            剧集贴吧目录网址列表.append(欧美剧目录)#列表追加

        for 序号 in '1':
            内地电视剧目录 = 'http://tieba.baidu.com/sign/index?kw=%CE%E4%C1%D6%CD%E2%B4%AB&type=3&pn={}'.format(序号)#'代入 '{}'
            韩国电视剧目录 = 'http://tieba.baidu.com/sign/index?kw=%D4%AD%C0%B4%CA%C7%C3%C0%C4%D0%B0%A1&type=3&pn={}'.format(序号)#'代入 '{}'
            日本电视剧目录 = 'http://tieba.baidu.com/sign/index?kw=%BB%A8%D1%F9%C4%D0%D7%D3&type=3&pn={}'.format(序号)#'代入 '{}'
            香港电视剧目录 = 'http://tieba.baidu.com/sign/index?kw=%B7%A8%D6%A4%CF%C8%B7%E6&type=3&pn={}'.format(序号)#'代入 '{}'

            剧集贴吧目录网址列表.append(内地电视剧目录)#列表追加
            剧集贴吧目录网址列表.append(韩国电视剧目录)  # 列表追加
            剧集贴吧目录网址列表.append(日本电视剧目录)  # 列表追加
            剧集贴吧目录网址列表.append(香港电视剧目录)  # 列表追加


        self.贴吧目录网址列表 = 剧集贴吧目录网址列表


    def 模具一一动漫贴吧目录网址列表(self):
        动漫贴吧目录网址列表 = []
        for 序号 in '12345':
            动漫目录 = 'http://tieba.baidu.com/sign/index?kw=%BB%F0%D3%B0%C8%CC%D5%DF&type=3&pn={}'.format(序号)  # '代入 '{}'
            动漫贴吧目录网址列表.append(动漫目录)  # 列表追加
        for 序号 in '123':

            国产动漫目录 = 'http://tieba.baidu.com/sign/index?kw=%BB%AD%BD%AD%BA%FE&type=3&pn={}'.format(序号)  # '代入 '{}'
            动漫相关目录 = 'http://tieba.baidu.com/sign/index?kw=%C7%A7%D2%F4%B6%AF%C2%FE&type=3&pn={}'.format(序号)  # '代入 '{}'
            动漫贴吧目录网址列表.append(国产动漫目录)  # 列表追加
            动漫贴吧目录网址列表.append(动漫相关目录)  # 列表追加



        self.贴吧目录网址列表=动漫贴吧目录网址列表

    def 模具一一电影贴吧目录网址列表(self):
        电影贴吧目录网址列表 = []

        for 序号 in '1':
            欧美电影目录 = 'http://tieba.baidu.com/sign/index?kw=%B8%B4%B3%F0%D5%DF%C1%AA%C3%CB&type=3&pn={}'.format(序号)#'代入 '{}'
            日本电影目录 = 'http://tieba.baidu.com/sign/index?kw=%B4%F3%CC%D3%C9%B1&type=3&pn={}'.format(序号)#'代入 '{}'
            韩国电影目录 = 'http://tieba.baidu.com/sign/index?kw=%CB%AA%BB%A8%B5%EA&type=3&pn={}'.format(序号)#'代入 '{}'
            电影话题目录 = 'http://tieba.baidu.com/sign/index?kw=%B5%E7%D3%B0&type=3&pn={}'.format(序号)#'代入 '{}'

            电影贴吧目录网址列表.append(欧美电影目录)  # 列表追加
            电影贴吧目录网址列表.append(日本电影目录)  # 列表追加
            电影贴吧目录网址列表.append(韩国电影目录)  # 列表追加
            电影贴吧目录网址列表.append(电影话题目录)  # 列表追加



        self.贴吧目录网址列表 = 电影贴吧目录网址列表



    """        2       """

    def 模具一一采集并解析贴吧目录网址列表(self):

        def 模具一一网页解析(返回网页内容):
            帖子内容html = etree.HTML(返回网页内容.text)  #

            # ========签到人数列表

            规则 = '/html/body/div[4]/div[2]/table/tbody/tr[*]/td[3]/text()'  # /@href  text()
            签到人数列表 = 帖子内容html.xpath(规则)

            self.模具一一查看变量输出文本值("签到人数列表一", 签到人数列表, 8)

            规则 = 'html/body/div[4]/div[2]/table/tr[*]/td[3]//text()'  # /@href  text()
            签到人数列表 = 帖子内容html.xpath(规则)

            self.模具一一查看变量输出文本值("签到人数列表3", 签到人数列表, 8)

            规则 = str(规则).replace("/tbody", "")
            签到人数列表 = 帖子内容html.xpath(规则)
            self.模具一一查看变量输出文本值("签到人数列表二", 签到人数列表, 8)

        def 模具一一网页解析提取签到大于1000的贴吧链接(返回网页内容):
            网页 = 返回网页内容.replace("td>\n", "td>")  # 替换   , 1) 次数 1
            网页 = 网页.replace("td>\r\n", "td>")  # 替换   , 1) 次数 1 encoding='UTF-8'= "gbk"  win下用\r\n表示换行.

            # self.模具一一查看变量输出文本值("网页", 网页, 8)

            for 每栏 in 网页.split("\r\n"):

                if "href=" in 每栏 and "forum_name" in 每栏 and "forum_sign_num" in 每栏 and "forum_member" in 每栏:

                    规则 = '.{1,}forum_sign_num">'
                    签到人数 = re.sub(规则, '', 每栏)  # 替换   ,count=0,re.S|re.I

                    规则 = '<.{0,}'
                    签到人数 = re.sub(规则, '', 签到人数)  # 替换   ,count=0,re.S|re.I
                    self.模具一一查看变量输出文本值("签到人数", 签到人数, 8)

                    if int(签到人数) > 1000:
                        规则 = '.{0,}href="'
                        贴吧链接 = re.sub(规则, '', 每栏)  # 替换   ,count=0,re.S|re.I
                        规则 = '">.{0,}'
                        贴吧链接 = re.sub(规则, '', 贴吧链接)  # 替换   ,count=0,re.S|re.I
                        self.模具一一查看变量输出文本值("贴吧链接", 贴吧链接, 8)
                        self.贴吧链接列表.append(贴吧链接)  # 列表追加

        self.贴吧目录网址列表 = list(set(self.贴吧目录网址列表))
        for 贴吧目录网址 in self.贴吧目录网址列表:
            self.模具一一查看变量输出文本值("贴吧目录网址", 贴吧目录网址, 8)

        self.贴吧链接列表 = []


        返回网页一链接组列表 = self.模具一一gr无序网址列表请求返回网页内容(self.贴吧目录网址列表[0:2], 编码="gbk")
        self.模具一一查看变量输出文本值("返回网页一链接组列表", 返回网页一链接组列表, 8)

        for 返回网页一链接组 in 返回网页一链接组列表:
            返回网页内容 = 返回网页一链接组[0]
            self.模具一一查看变量输出文本值("返回网页内容", 返回网页内容, 8)
            返回网页内容文本 = 返回网页内容.text
            # 模具一一网页解析(返回网页内容)

            模具一一网页解析提取签到大于1000的贴吧链接(返回网页内容文本)


    def 模具一一采集并解析每个贴吧网址(self):
        def 模具一一解析网页内容(返回网页内容文本):
            网页 = 返回网页内容文本.replace('"最后回复时间">\r\n', '"最后回复时间">')  # 替换   , 1) 次数 1
            网页 = 网页.replace('center_text"\r\n', 'center_text"')  # 替换   , 1) 次数 1


            栏目内容列表 = []


            for 每栏 in 网页.split("j_threadlist_li_left"):

                if '"最后回复时间">' in 每栏 and '"回复"' in 每栏:
                    内容字典 = {}
                    # self.模具一一查看变量输出文本值("每栏", 每栏,8)
                    for 每行 in 每栏.split("\r\n"):
                        if '"最后回复时间">' in 每行 and "title=" in 每行 and "threadlist_reply_date" in 每行:
                            规则 = '.{1,}最后回复时间">'
                            最后回复时间 = re.sub(规则, '', 每行)  # 替换   ,count=0,re.S|re.I
                            规则 = '<.{0,}'
                            最后回复时间 = re.sub(规则, '', 最后回复时间)  # 替换   ,count=0,re.S|re.I
                            最后回复时间 = 最后回复时间.strip()  # 默认则是去除空格

                            内容字典["最后回复时间"] = 最后回复时间
                            self.模具一一查看变量输出文本值("最后回复时间", 最后回复时间, 8)



                        if '"回复"' in 每行 and "title=" in 每行 and "threadlist_rep_num" in 每行:
                            规则 = '.{1,}回复">'
                            回复数 = re.sub(规则, '', 每行)  # 替换   ,count=0,re.S|re.I
                            规则 = '<.{0,}'
                            回复数 = re.sub(规则, '', 回复数)  # 替换   ,count=0,re.S|re.I
                            回复数 = 回复数.strip()  # 默认则是去除空格
                            内容字典["回复数"] = int(回复数)
                            self.模具一一查看变量输出文本值("回复数", 回复数, 8)



                        if 'href=' in 每行 and "title=" in 每行 and "noreferrer" in 每行 and "_blank" in 每行 and "j_th_tit" in 每行:
                            规则 = '.{1,}href="'
                            帖子链接 = re.sub(规则, '', 每行)  # 替换   ,count=0,re.S|re.I
                            规则 = '".{0,}'
                            帖子链接 = re.sub(规则, '', 帖子链接)  # 替换   ,count=0,re.S|re.I
                            帖子链接 = 帖子链接.strip()  # 默认则是去除空格

                            帖子链接 = 'http://tieba.baidu.com{}'.format(帖子链接)  # '代入 '{}'



                            内容字典["帖子链接"] = 帖子链接
                            self.模具一一查看变量输出文本值("帖子链接", 帖子链接, 8)

                    if 帖子链接 in self.过滤网址:
                        self.模具一一查看变量输出文本值("过滤的网址", 帖子链接, 8)
                        continue  # 跳过循环

                    栏目内容列表.append(内容字典)  # 列表追加

            for 内容字典 in 栏目内容列表:

                if ':' in 内容字典["最后回复时间"] and 内容字典["回复数"] > 1:
                    self.最新非零回复帖子链接列表.append(内容字典["帖子链接"])  # 列表追加

        self.最新非零回复帖子链接列表 = []
        self.贴吧链接列表 = list(set(self.贴吧链接列表))
        返回网页一链接组列表 = self.模具一一gr无序网址列表请求返回网页内容(self.贴吧链接列表)
        for 返回网页一链接组 in 返回网页一链接组列表:
            返回网页内容 = 返回网页一链接组[0]

            返回网页内容文本 = 返回网页内容.text

            模具一一解析网页内容(返回网页内容文本)



    def 模具一一采集并解析最新非零回复帖子链接(self):

        self.最新非零回复帖子链接列表 = list(set(self.最新非零回复帖子链接列表))
        返回网页一链接组列表 = self.模具一一gr无序网址列表请求返回网页内容(self.最新非零回复帖子链接列表)
        for 返回网页一链接组 in 返回网页一链接组列表:
            返回网页内容 = 返回网页一链接组[0]
            网址 = 返回网页一链接组[1]


            返回网页内容文本 = 返回网页内容.text

            #self.模具一一查看变量输出文本值("返回网页内容文本", 返回网页内容文本,8)
            if '">下一页</a>' in 返回网页内容文本 or '">尾页</a>' in 返回网页内容文本 or'回复贴' not in 返回网页内容文本:
                self.模具一一查看变量输出文本值("存在 <下一页>", "过滤", 8)

                self.sql语句 = """INSERT INTO `百度帖子网址记录`(`记录`,`影视类型`,`帖子网址`) VALUES ("{}","{}","{}")""".format("过滤网址",self.影视类型,网址)#'代入 '{}'
                self.模具一一内容数据库("添加 过滤网址")

            else:  #否则
                self.留言帖子链接列表.append(网址)#列表追加

                self.sql语句 = """INSERT INTO `百度帖子网址记录`(`记录`,`影视类型`,`帖子网址`) VALUES ("{}","{}","{}")""".format("等待留言",self.影视类型,网址)  # '代入 '{}'
                self.模具一一内容数据库("添加 等待留言网址")


    """       3       """

    """        4       """

    def 模具一一示例(self):
        pass


class 类一一百度回帖留言(类一一采集公共库):  # 调用 类的模具 self.模具一一数据库()
    def __init__(self):
        def 检测记录时间的危险范围():
            跳过循环 = ''
            if '成功' in self.记录:
                时间 = self.记录.replace("成功", "")  # 替换   , 1) 次数 1
                危险范围时间 = int(时间) + 79200  # 22小时
            else:  # 否则
                时间 = self.记录.replace("失败", "")  # 替换   , 1) 次数 1
                危险范围时间 = int(时间) + 259200  # 3 天 时间
            当前时间秒数 = int(time.time())
            if 当前时间秒数 < 危险范围时间:
                跳过循环 = '跳过循环'
            return 跳过循环  # 返回

        self.测试打印 = '测试'
        self.模具一一换手机头部信息()

        self.数据库名 = "影视发帖推广"



        self.模具一一提取数据库百度完好cookie()



        """设置选项"""
        self.浏览器设置选项 = webdriver.ChromeOptions()  # 进入浏览器设置
        影视类型列表 = ['美剧', '动漫', '电影']

        for self.影视类型 in 影视类型列表:
            self.模具一一提取数据库留言帐号()
            self.模具一一提取数据库百度留言帖子链接()
            self.留言帖子链接列表 = []



            for 留言帐号组 in self.留言帐号组列表:
                self.记录 = 留言帐号组[5]
                if len(str(self.记录)) >5:
                    跳过循环 =检测记录时间的危险范围()
                    if '跳过循环' in 跳过循环:
                        continue #跳过循环


                self.ID=留言帐号组[0]
                self.帐号 = 留言帐号组[1]
                self.密码 = 留言帐号组[2]
                self.cookie字典 = 留言帐号组[3]
                self.互相关注 = 留言帐号组[4]

                self.留言帖子链接 ='http://tieba.baidu.com/p/5937470895'
                self.模具一一浏览器回帖留言()

                if len(self.留言帖子链接列表)==0:
                    self.模具一一重新检测留言帖子链接()

                self.留言帖子链接 = self.留言帖子链接列表[0]
                del self.留言帖子链接列表[0]

    """        1       """

    def 模具一一提取数据库百度完好cookie(self):

        self.sql语句 = """SELECT `cookie`FROM `推广帐号` WHERE `ID`=129 """
        self.模具一一内容数据库()
        self.cookie组列表 = self.数据库内容组列表

        cookie组=self.cookie组列表[0]
        cookie字典列表 = cookie组[0]


    def 模具一一重新检测留言帖子链接(self):
        重新检测留言帖子链接列表 = []

        for i in range(1, 11):  # 范围 1至10
            等待留言网址组 = random.choice(self.等待留言网址组列表)  # 列表随机项
            self.等待留言网址组列表.remove(等待留言网址组)  # 列表 按值删除
            重新检测留言帖子链接列表.append(等待留言网址组[0])  # 列表追加

        返回网页一链接组列表 = self.模具一一gr无序网址列表请求返回网页内容(重新检测留言帖子链接列表)
        for 返回网页一链接组 in 返回网页一链接组列表:
            返回网页内容 = 返回网页一链接组[0]
            网址 = 返回网页一链接组[1]

            返回网页内容文本 = 返回网页内容.text

            # self.模具一一查看变量输出文本值("返回网页内容文本", 返回网页内容文本,8)
            if '">下一页</a>' in 返回网页内容文本 or '">尾页</a>' in 返回网页内容文本 or '回复贴' not in 返回网页内容文本:
                self.模具一一查看变量输出文本值("存在 <下一页>", "过滤", 8)

                self.sql语句 = """INSERT INTO `百度帖子网址记录`(`记录`,`影视类型`,`帖子网址`) VALUES ("{}","{}","{}")""".format("过滤网址",
                                                                                                             self.影视类型,
                                                                                                             网址)  # '代入 '{}'

                self.模具一一内容数据库("添加 过滤网址")

            else:  # 否则
                self.留言帖子链接列表.append(网址)  # 列表追加

    def 模具一一提取数据库留言帐号(self):
        self.sql语句 = """SELECT `ID`, `帐号`, `密码`, `cookie`, `互相关注`,`记录` FROM `推广帐号` WHERE `类型` = '百度顶贴' AND `互相关注` LIKE '%{}%' """.format(
            self.影视类型)  # '代入 '{}'
        self.模具一一内容数据库()

        self.留言帐号组列表 = self.数据库内容组列表

    def 模具一一提取数据库百度留言帖子链接(self):

        self.sql语句 = """SELECT `帖子网址` FROM `百度帖子网址记录` WHERE `记录` = '等待留言' AND `影视类型` LIKE '%{}%' """.format(
            self.影视类型)  # '代入 '{}'

        self.模具一一内容数据库()
        self.等待留言组列表集 = set(self.数据库内容组列表)

        self.sql语句 = "SELECT `帖子网址` FROM `百度帖子网址记录` WHERE `记录` = '已留言' "
        self.模具一一内容数据库()
        self.已留言组列表集 = set(self.数据库内容组列表)

        self.等待留言网址组列表 = list(self.等待留言组列表集 - self.已留言组列表集)



    """        2       """


    def 模具一一浏览器回帖留言(self):
        def 模具一一导入发贴cookie列表(cookie字典):
            def 字典清洁(文本行):

                字典名值列表 = 文本行.split('":')
                字典值 = 字典名值列表[1]
                字典值 = 字典值.strip()  # 默认则是去除空格
                字典值 = 字典值.strip('"')  # 默认则是去除空格
                字典值 = 字典值.strip("'")  # 默认则是去除空格

                return 字典值  # 返回


            替换字典 = self.替换字典

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

         #self.模具一一换ip连接()
        self.模具一一查看变量输出文本值("登录帐号:", self.帐号)

        self.模具一一浏览器设置选项并启动()


        self.模具一一查看变量输出文本值("浏览器设置选项并启动(", "", 8)
        # self.浏览器操作.get("https://www.baidu.com")  # 打开 网址

        self.浏览器操作.get(self.留言帖子链接)  # 打开 网址

        等待用户输入 = input("\n按下 enter 确认键后继续")


        获取所有cookies列表 = self.浏览器操作.get_cookies()  # 获取所有cookies
        self.替换字典 = 获取所有cookies列表[0]
        模具一一导入发贴cookie列表(self.cookie字典)

        # 设定页面加载timeout时长,需要的元素能加载出来就行

        #self.浏览器操作.set_page_load_timeout(5)  # 设置限定页面加载限制时间
        # os.system("taskkill /F /IM chromedriver.exe")  # 关闭程序名 chromedriver.exe




        """========================操作===================="""
        self.模具一一查看变量输出文本值("留言帖子链接0", self.留言帖子链接, 8)
        try:  #调用异常处理,应对易发生错误的位置
            # self.浏览器操作.get(self.留言帖子链接)  # 打开 网址
            self.浏览器操作.implicitly_wait(10)
        except (selenium.common.exceptions.TimeoutException)as 异常原因 :#异常处理
            try:
                self.浏览器操作.execute_script("window.stop();")  # 调用js脚本使浏览器停止加载
            except (selenium.common.exceptions.TimeoutException)as 异常原因:  # 异常处理
                try:
                    self.浏览器操作.execute_script('document.execCommand("Stop");')  # 调用js脚本使浏览器停止加载

                except (selenium.common.exceptions.TimeoutException)as 异常原因:  # 异常处理
                    pass


            pass
            self.模具一一查看变量输出文本值("打开网址异常原因", "", 8)
        else:#必须放在所有的except子句之后.这个子句将在try子句没有发生任何异常的时候执行.
            pass

        self.模具一一查看变量输出文本值("留言帖子链接", self.留言帖子链接, 8)
        self.浏览器操作.set_page_load_timeout(3)  # 设置限定页面加载限制时间


        """隐式等待 试错"""
        for 序号 in '123':
            try:  # 调用异常处理,应对易发生错误的位置
                #self.浏览器操作.implicitly_wait(20)  # 隐式等待
                """点击  发表 按钮"""
                self.浏览器操作.find_element_by_xpath('//*[@id="wd1"]').click()  # 点击
                self.模具一一查看变量输出文本值("隐式等待", "点击  发表 按钮",8)
                pass


            except (selenium.common.exceptions.TimeoutException)as 异常原因:  # 异常处理

                self.模具一一查看变量输出文本值("隐式等待,异常原因", "", 8)
                break  # 结束循环
                if '1' in 序号:
                    pass
                #self.浏览器操作.refresh()  # 刷新下页面
                elif '2' in 序号:

                    self.跳过循环 = '跳过循环'
                    return  # 返回
            else:  # 必须放在所有的except子句之后.这个子句将在try子句没有发生任何异常的时候执行.
                break  # 结束循环




        
        try:  #调用异常处理,应对易发生错误的位置
            self.浏览器操作.refresh()  # 刷新下页面就见证奇迹了
        except (selenium.common.exceptions.TimeoutException)as 异常原因:  # 异常处理
            self.模具一一查看变量输出文本值("刷新下页面就见证奇迹了", "", 8)
        else:#必须放在所有的except子句之后.这个子句将在try子句没有发生任何异常的时候执行.
            pass
        time.sleep(2)  # 等待  # 增加延迟
        self.模具一一查看变量输出文本值("一导入发贴cookie列表", "", 8)

        self.模具一一检测cookie是否生效()
        if '跳过循环' in self.跳过循环:
            return  # 返回

        try:  # 调用异常处理,应对易发生错误的位置
            """回复 框输入"""
            self.浏览器操作.find_element_by_xpath('//*[@id="ueditor_replace"]').send_keys('@' + self.互相关注)  # 输入
        except (selenium.common.exceptions.TimeoutException)as 异常原因:  # 异常处理
            pass

        time.sleep(1)  # 等待  # 增加延迟


        等待用户输入 = input("\n按下 enter 确认键后继续")


        """点击  发表 按钮"""
        self.浏览器操作.find_element_by_xpath('//*[@id="tb_rich_poster"]/div[3]/div[3]/div/a/span/em').click()  # 点击


        time.sleep(5)  # 等待  # 增加延迟
        self.浏览器操作.refresh()  # 刷新下页面
        time.sleep(2)  # 等待  # 增加延迟

        """检测 回复成败 """

        获取网页源码= self.浏览器操作.page_source

        当前时间秒数 = int(time.time())  # 返回当前时间的时间戳(1970纪元后经过的浮点秒数)
        if self.互相关注 in 获取网页源码 :
            self.模具一一查看变量输出文本值("回复成功,留言内容", self.互相关注)
            记录='成功'+str(当前时间秒数)
            回复内容='成功留言 '+self.互相关注
            等待用户输入 = input("\n按下 enter 确认键后继续")


        else:  #否则
            self.模具一一查看变量输出文本值("回复失败,留言内容", self.互相关注)
            记录 = '失败' + str(当前时间秒数)
            回复内容 = '失败留言 ' + self.互相关注
            等待用户输入 = input("\n按下 enter 确认键后继续")


        self.sql语句 = "UPDATE `推广帐号` SET `记录`='{}' WHERE`ID`={}".format(记录,self.ID)  # '代入 '{}' #'
        self.模具一一内容数据库("更新 留言记录与时间秒数")

        self.sql语句 = """INSERT INTO `百度帖子网址记录`(`记录`, `影视类型`, `帖子网址`, `回复内容`) VALUES ("{}","{}","{}","{}")""".format('已留言', self.影视类型,self.留言帖子链接,回复内容)  # '代入 '{}' #'
        self.模具一一内容数据库("添加 已留言 记录 ")

        # time.sleep(6)  # 等待  # 增加延迟

        self.浏览器操作.quit()  # .退出浏览器

    def 模具一一浏览器设置选项并启动(self):

        def 换头部信息():

            self.模具一一换手机头部信息()
            #self.手机头部信息['Referer']= "http://tieba.baidu.com"
            头部信息 = "user-agent=" + self.手机头部信息['User-Agent']
            #头部信息 = "user-agent=" + self.手机头部信息
            print('头部信息:', 头部信息)
            self.浏览器设置选项.add_argument(头部信息)

        """设置选项"""

        #option.add_argument('headless')  # 静默模式
        self.浏览器设置选项.add_argument('disable-infobars')  # 加启动配置 去除正在受到自动软件的控制
        # 用户数据目录 = r'C:\Users\Administrator\AppData\Local\Google\Chrome\User Data'
        # self.浏览器设置选项.add_argument('--user-data-dir={}'.format(用户数据目录))  # '代入{}'  # 设置成用户自己的数据目录
        """配置不加载图片"""
        # 配置不加载图片 = {"profile.managed_default_content_settings.images": 2}  # 配置不加载图片
        #self.浏览器设置选项.add_experimental_option("prefs", 配置不加载图片)
        #self.浏览器设置选项.add_extension(r'E:\PY学习文件\程序库\chrome插件\ublock+origin+1.7.6.crx')


        换头部信息()

        self.浏览器操作 = webdriver.Chrome(chrome_options=self.浏览器设置选项)  # 打开chrome浏览器

        """设置浏览器窗口大小"""


        self.浏览器操作.set_window_size(800, 800)# 参数是像素点宽,高
        # self.浏览器操作.maximize_window() # 浏览器全屏显示,不带参数
        time.sleep(1)  # 设置暂停等待.单位是秒(s),时间值可以是小数也可以是整数

    def 模具一一检测cookie是否生效(self):
        self.跳过循环 = ''
        for 序号 in '一二三':
            time.sleep(2)  # 等待  # 增加延迟
            要求登录 = self.模具一一判断要求登录存在()
            if '要求登录' not in 要求登录:

                if  '一' not in 序号:
                    获取所有cookies列表 = self.浏览器操作.get_cookies()  # 获取所有cookies
                    self.sql语句 = 'UPDATE `推广帐号` SET `cookie`="{}" WHERE `ID`={}'.format(获取所有cookies列表,
                                                                                        self.ID)  # '代入 '{}'   # ' '{}' # SQL 查询语句
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



    """        3       """

    def 模具一一示例(self):
        pass
        返回网页一链接组列表 = self.模具一一gr无序网址列表请求返回网页内容(self.贴吧目录网址列表, 编码="gbk")
        for 返回网页一链接组 in 返回网页一链接组列表:
            返回网页内容 = 返回网页一链接组[0]
            网址 = 返回网页一链接组[1]

        self.数据库名 = "影视发帖推广"
        self.sql语句 = "UPDATE `微博抽奖转发内容` SET `转发`='是' WHERE `ID`={}".format(self.数据库id)  # '代入 '{}' #'
        self.模具一一内容数据库("更新 转发栏为 是")
        self.数据库内容组列表 = self.数据库内容组列表

        帖子链接 = ''
        self.模具一一查看变量输出文本值("过滤的网址", 帖子链接, 8)
        pass
        js内容广告过滤规则= """http://tb1.bdstatic.com/tb/static-pfrs/widget/forum_card/forum_card.js
http://tb1.bdstatic.com/tb/static-pfrs/widget/forum_card/forum_track.js
http://tb1.bdstatic.com/??/tb/_/app_f6b8e80.js,/tb/_/card_93a9436.js,/tb/_/js_pager_995a38c.js,/tb/_/login_dialog_a32bb1c.js,/tb/_/user_head_b4ef389.js,/tb/_/user_api_7ac4d9c.js,/tb/_/icons_f7109e4.js,/tb/_/wallet_dialog_30b6e3f.js,/tb/_/tb_lcs_7acf17b.js,/tb/_/flash_lcs_d56216f.js,/tb/_/event_center_a6d6257.js,/tb/_/new_message_system_4605012.js,/tb/_/messenger_5fe02ec.js,/tb/_/base_user_data_caf0d64.js,/tb/_/cashier_dialog_025ae09.js,/tb/_/qianbao_cashier_dialog_a94a250.js,/tb/_/base_dialog_user_bar_b277bdb.js,/tb/_/qianbao_purchase_member_5ef3001.js,/tb/_/pay_member_7cdb50f.js,/tb/_/http_transform_ceea7be.js,/tb/_/userbar_5f34b18.js,/tb/_/footer_5586124.js,/tb/_/poptip_169f7e9.js,/tb/_/ad_stats_d895455.js,/tb/_/adblock_stats_0af9273.js,/tb/_/util_54a512c.js,/tb/_/preview_01cc209.js,/tb/_/pb_track_48655d9.js,/tb/_/conf_skin_87bc5d9.js,/tb/_/platform_skin_d41d8cd.js
http://bdimg.share.baidu.com*
https://hm.baidu.com/*
https://passport.baidu.com/*
https://passport.baidu.com/*
http://api.geetest.com/*
http://passport.bdimg.com/*
http://static.geetest.com/*
http://dn-staticdown.qbox.me/*
http://fex.bdstatic.com/*
        """
        百度回复框js ='http://tb1.bdstatic.com/tb/static-pcommon/widget/jiyan_service/captcha_gt.js'

# 百度采集网址=类一一百度采集留言帖子链接()

百度回帖留言=类一一百度回帖留言()


