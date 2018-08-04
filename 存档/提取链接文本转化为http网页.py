

import requests #人性化的 浏览器
import re  #正则表达式
import time #时间
import os #处理电脑系统文件和目录
import pymysql #mysql数据库
import random #随机数
from lxml import etree#解析与定位网页
import datetime  # 时间
import fileinput


class 类_读取文本: #调用 类的模具 self.模具_数据库()
    def __init__(self,类型):
        self.类型 =类型


    
    def 模具_插入数据库(self):
        db = pymysql.connect("localhost", "root", "", "综合影视剧", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句
        sql ="""INSERT INTO 本地目录链接文件(目录名,影视类型)
                       VALUES ('%s','%s')""" % (self.提取目录,self.类型)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            db.rollback()
        # 关闭数据库连接
        db.close()
    
    def 模具_提取目录(self):
        规则 = '(?<=blank">).{1,}(?=</a>)'#前后截取

        文本列表 = re.findall(规则, str(self.目录链接))  # 提取
        if len(文本列表)==0:
            return
        self.提取目录 = 文本列表[0]
        self.模具_插入数据库()
        print(self.提取目录)
    
    def 模具_保存文件(self):
        提取目录 = str(self.提取目录).replace("?", "")  # 替换   , 1) 次数 1
        提取目录 = str(提取目录).replace("|", "")  # 替换   , 1) 次数 1

        类型拼音字典={'电影':'dying','动漫':'dongman','电视剧':'dianshiju'}
         
        for 字典键 in 类型拼音字典:  # 范围 range
            if 字典键 in self.类型:
                类型 = str(self.类型).replace("self.类型", 类型拼音字典[字典键]) #替换   , 1) 次数 1

        文件目录 ='E:/PY学习文件/PyCharm文件/BT影视剧/ftp上传目录链接网页/html/{}'.format(类型)#不换行 end=""
        if not os.path.exists(文件目录):  # 必有条件选择,否则出错
            try:
                os.makedirs(文件目录)  # makedirs 创建多级目录文件夹,mkdir创建一个文件夹
            except (FileNotFoundError,OSError) as 异常原因:
                print('异常原因',异常原因)
                return # 跳过当前循环,继续进行下一轮循环


        文件路径='E:/PY学习文件/PyCharm文件/BT影视剧/ftp上传目录链接网页/{}/{}.html'.format(self.类型,提取目录)#不换行 end=""
        
        文本 = open(文件路径, 'w', encoding='UTF-8')# 读取encoding='UTF-8'utf8的文件, encoding='UTF-8'
        文本.write(self.网页内容) # read() #读取
        文本.close()
        print('成功保存文件',提取目录)
    
    def 模具_转化为http网页(self):
        规则 = '(?<=href=").{1,}(?=" target)'  # 前后截取

        目录链接列表 = re.findall(规则, str(self.目录链接))  # 提取
        if len(目录链接列表)==0:
            return
        目录链接= 目录链接列表[0]

        self.网页内容="""
        <html >
            <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf8" />
            <title>3e影视剧_最新美剧英语中字_海量电影:</title>
            <meta http-equiv="refresh" content="0.2;URL={}">
            </head>
            <body>
            </body>
            </html>""".format(目录链接)#不换行 end=""
    def 模具_每行读取文本(self):
        self.目录链接列表 = []
        文本文件="E:/PY学习文件/PyCharm文件/BT影视剧/txt文本/{}-城通网盘下地网址.txt".format(self.类型)#不换行 end=""
        for 目录链接 in fileinput.input(文本文件):
            self.目录链接 = str(目录链接).replace(r"\n", "")
            print(self.目录链接)

            self.模具_提取目录()
            self.模具_转化为http网页()
            self.模具_保存文件()

            self.目录链接列表.append(self.目录链接)
        print('共计链接为',len(self.目录链接列表))

#读取文本=类_读取文本('动漫')
#读取文本.模具_每行读取文本()
读取文本=类_读取文本('电影')
读取文本.模具_每行读取文本()
读取文本=类_读取文本('电视剧')
读取文本.模具_每行读取文本()