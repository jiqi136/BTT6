
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
import asyncio, aiohttp # 异步浏览
import pyautogui  # 键盘控制
from 网页采集公共库 import 类一一采集公共库# 导入模块

class 类一一微博抽奖(类一一采集公共库): #调用 类的模具 self.模具一一数据库()
    def __init__(self):
        self.模具一一高位换头部信息()
        self.模具一一抽奖网站列表内容()
        self.模具一一分解网页内容()



    def 模具一一示例(self):
        pass

    def 模具一一抽奖网站列表内容(self):
        抽奖网站列表=[]

        for 页数 in range(1,2):
            抽奖页数网址='https://s.weibo.com/weibo?q=%E8%BD%AC%E5%8F%91&scope=ori&suball=1&Refer=g&page={}'.format(页数)#'代入 '{}' 原创
            抽奖网站列表.append(抽奖页数网址)
        print('抽奖网站列表:',抽奖网站列表)
        self.返回网页一链接组列表=self.模具一一gr无序网址列表请求返回网页内容(抽奖网站列表)

    def 模具一一分解网页内容(self):
        for 返回网页一链接组列表 in self.返回网页一链接组列表:
            返回网页内容=返回网页一链接组列表[0]
            网页网址 = 返回网页一链接组列表[0]

            print('返回网页内容:', 返回网页内容.text)
            time.sleep(100000)  # 等待

            帖子内容html = etree.HTML(返回网页内容.text)  #




            # ========端口列表
            规则 = '//*[@id="pl_feedlist_index"]/div[1]/div[*]/div/div[1]/div[2]/text()'  # /@href  text()
            端口列表 = 帖子内容html.xpath(规则)
            规则二 = str(规则).replace("/tbody", "")
            端口列表 = 端口列表 + (帖子内容html.xpath(规则二))



if __name__ == '__main__':
    类=类一一微博抽奖()