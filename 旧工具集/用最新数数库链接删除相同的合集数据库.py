
import requests #人性化的 浏览器
import re  #正则表达式
import time #时间
import os #处理电脑系统文件和目录
import pymysql #mysql数据库
import random #随机数
from lxml import etree#解析与定位网页
import datetime  # 时间


class 类一删除相同合集: #调用 类的模具 self.模具_数据库()
    def __init__(self):
        self.模具一最新数据库链接()
        print('删除帖子总数:',len(self.帖子链接列表))
        for 最新链接组 in self.帖子链接列表:
            self.最新链接=最新链接组[0]
            print('最新链接:',self.最新链接)
            self.模具一用链接删除合集数据库的相同剧集()


    def 模具一最新数据库链接(self):
         # 打开数据库连接
         db = pymysql.connect("localhost", "root", "", "最新影视剧", charset="utf8")
         # 使用cursor()方法获取操作游标
         cursor = db.cursor()

         # SQL 查询语句
         sql = "SELECT DISTINCT `帖子链接` FROM `网站文章内容`;"
         # 执行SQL语句
         cursor.execute(sql)
         # 获取所有记录列表
         self.帖子链接列表 = cursor.fetchall()


         # 关闭数据库连接
         db.close()

    def 模具一用链接删除合集数据库的相同剧集(self):
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "", "电影与合集", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # SQL 查询语句
        sql = """DELETE FROM `网站文章内容` WHERE `帖子链接`=('%s')""" % (self.最新链接)



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
        print('成功删除:')



类=类一删除相同合集()