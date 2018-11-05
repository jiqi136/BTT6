# -*- coding:utf-8

from 网页采集公共库 import 类一一采集公共库# 导入模块
import re  # 正则式
import time  # 时间
import requests  # 网页浏览
import os  # 本地操作
import random  # 随机
import win32gui  # 窗口控件
import pymysql  # 数据库
from lxml import etree  # 解析与定位网页

import pyautogui as pag  # 模拟鼠标键盘操作
from selenium import webdriver  # 浏览的驱动
from selenium.webdriver.support import expected_conditions as EC  # =判断网页文本
from hashlib import md5  # md5值
from PIL import Image  # 图片处理


"""


"""


class 类一一百度回帖留网址ID(类一一采集公共库):  # 调用 类的模具 self.模具一一数据库()
    def __init__(self):
        self.模具一一高位换头部信息()
        self.测试打印 = '测试'

        self.数据库名 = "影视发帖推广"
        self.留言帖子链接列表 = []

        self.模具一一提取数据库百度已翻下一页过滤网址()

        self.模具一一采集并解析每个贴吧网址()

        self.模具一一采集并解析最新非零回复帖子链接()

        影视类型列表=['剧集','动漫','电影']
        for self.影视类型 in 影视类型列表:
            
            if '剧集' in self.影视类型: #  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                self.模具一一剧集贴吧目录网址列表()

                self.模具一一采集并解析贴吧目录网址列表()
                self.模具一一采集并解析每个贴吧网址()

            elif '动漫' in self.影视类型:# 其它条件.
                self.模具一一动漫贴吧目录网址列表()

            elif '电影' in self.影视类型:  # 其它条件.
                self.模具一一电影贴吧目录网址列表()

    """        1       """




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

        for 贴吧目录网址 in self.贴吧目录网址列表:
            self.模具一一查看变量输出文本值("贴吧目录网址", 贴吧目录网址, 8)

        self.贴吧链接列表 = []
        self.模具一一查看变量输出文本值("self.影视类型", self.影视类型, 8)

        返回网页一链接组列表 = self.模具一一gr无序网址列表请求返回网页内容(self.贴吧目录网址列表[0:2], 编码="gbk")
        self.模具一一查看变量输出文本值("返回网页一链接组列表", 返回网页一链接组列表, 8)

        for 返回网页一链接组 in 返回网页一链接组列表:
            返回网页内容 = 返回网页一链接组[0]
            self.模具一一查看变量输出文本值("返回网页内容", 返回网页内容, 8)
            返回网页内容文本 = 返回网页内容.text
            # 模具一一网页解析(返回网页内容)

            模具一一网页解析提取签到大于1000的贴吧链接(返回网页内容文本)

    """        2       """

    def 模具一一提取数据库百度已翻下一页过滤网址(self):
        self.sql语句 = """SELECT `过滤网址` FROM `百度已翻下一页过滤网址`"""
        self.模具一一内容数据库()
        self.过滤网址=str(self.数据库内容组列表)


    def 模具一一采集并解析最新非零回复帖子链接(self):
        最新非零回复帖子链接列表 = ['https://tieba.baidu.com/p/5562148419']

        返回网页一链接组列表 = self.模具一一gr无序网址列表请求返回网页内容(最新非零回复帖子链接列表)
        for 返回网页一链接组 in 返回网页一链接组列表:
            返回网页内容 = 返回网页一链接组[0]
            网址 = 返回网页一链接组[1]


            返回网页内容文本 = 返回网页内容.text

            #self.模具一一查看变量输出文本值("返回网页内容文本", 返回网页内容文本,8)
            if '">下一页</a>' in 返回网页内容文本 or '">尾页</a>' in 返回网页内容文本:
                self.模具一一查看变量输出文本值("存在 <下一页>", "过滤", 8)

                self.sql语句 = """INSERT INTO `百度已翻下一页过滤网址`(`过滤网址`) VALUES ("{}")""".format(网址)#'代入 '{}'
                self.模具一一内容数据库("添加 过滤网址")

            else:  #否则
                self.留言帖子链接列表.append(网址)#列表追加


            time.sleep(10000)  # 等待
            模具一一解析网页内容(返回网页内容文本)

            for 帖子链接 in self.最新非零回复帖子链接列表:
                print("帖子链接二:", 帖子链接)

            time.sleep(10000)  # 等待

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

                            print("最后回复时间", 最后回复时间)

                        if '"回复"' in 每行 and "title=" in 每行 and "threadlist_rep_num" in 每行:
                            规则 = '.{1,}回复">'
                            回复数 = re.sub(规则, '', 每行)  # 替换   ,count=0,re.S|re.I
                            规则 = '<.{0,}'
                            回复数 = re.sub(规则, '', 回复数)  # 替换   ,count=0,re.S|re.I
                            回复数 = 回复数.strip()  # 默认则是去除空格
                            内容字典["回复数"] = int(回复数)

                            print("回复数", 回复数)

                        if 'href=' in 每行 and "title=" in 每行 and "noreferrer" in 每行 and "_blank" in 每行 and "j_th_tit" in 每行:
                            规则 = '.{1,}href="'
                            帖子链接 = re.sub(规则, '', 每行)  # 替换   ,count=0,re.S|re.I
                            规则 = '".{0,}'
                            帖子链接 = re.sub(规则, '', 帖子链接)  # 替换   ,count=0,re.S|re.I
                            帖子链接 = 帖子链接.strip()  # 默认则是去除空格

                            帖子链接 = 'http://tieba.baidu.com{}'.format(帖子链接)  # '代入 '{}'



                            内容字典["帖子链接"] = 帖子链接
                            print("帖子链接", 帖子链接)
                    if 帖子链接 in self.过滤网址:
                        self.模具一一查看变量输出文本值("过滤的网址", 帖子链接, 8)
                        continue  # 跳过循环

                    栏目内容列表.append(内容字典)  # 列表追加

            for 内容字典 in 栏目内容列表:

                if ':' in 内容字典["最后回复时间"] and 内容字典["回复数"] > 1:
                    self.最新非零回复帖子链接列表.append(内容字典["帖子链接"])  # 列表追加


        贴吧链接列表=['https://tieba.baidu.com/f?kw=highschooldxd']
        self.最新非零回复帖子链接列表 = []
        返回网页一链接组列表 = self.模具一一gr无序网址列表请求返回网页内容(贴吧链接列表)
        for 返回网页一链接组 in 返回网页一链接组列表:
            返回网页内容 = 返回网页一链接组[0]

            返回网页内容文本 = 返回网页内容.text

            # self.模具一一查看变量输出文本值("返回网页内容文本", 返回网页内容文本,8)
            模具一一解析网页内容(返回网页内容文本)

            for 帖子链接 in self.最新非零回复帖子链接列表:
                print("帖子链接二:", 帖子链接)

            time.sleep(10000) # 等待





        for 贴吧网址 in self.贴吧链接列表:
            self.模具一一查看变量输出文本值("每个贴吧网址", 贴吧网址, 8)





    """       3       """

    """        4       """

    def 模具一一示例(self):
        pass

百度回帖留网址ID=类一一百度回帖留网址ID()