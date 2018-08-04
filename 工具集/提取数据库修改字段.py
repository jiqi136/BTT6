

import requests #人性化的 浏览器
import re  #正则表达式
import time #时间
import os #处理电脑系统文件和目录
import pymysql #mysql数据库
import random #随机数
from lxml import etree#解析与定位网页
import datetime  # 时间
import shutil


class 类一一提取数据库修改字段: #调用 类的模具 self.模具_数据库()
    def __init__(self):
        self.数据库名= "电影与合集"
        self.数据库名 = "最新影视剧"
        self.模具一一提取数据库里的摘要与链接()
        self.模具一一遍历组列表()
        pass




            
    

    def 模具一一提取数据库里的摘要与链接(self):
        # 提取数据库里的过滤网址
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "",self.数据库名, charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # SQL 查询语句
        sql = "SELECT `摘要`,`帖子链接` FROM `网站文章内容` "
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        self.摘要帖子链接组列表 = cursor.fetchall()
        # 关闭数据库连接
        db.close()

    def 模具一一遍历组列表(self):
        计数器=0
        倒数=len(self.摘要帖子链接组列表)
        for 摘要帖子链接组 in self.摘要帖子链接组列表:
            self.标题相同 = 1

            self.摘要=摘要帖子链接组[0]
            self.帖子链接=摘要帖子链接组[1]

            print('========================:')
            print('更新倒数:', 倒数)
            倒数 = 倒数 - 1
            self. 模具一一清洗字段()
            if self.标题相同 == 0:
                print('标题相同:跳过当前循环')
                continue  # 跳过当前循环,继续进行下一轮循环
            self.模具一一更新数据库里的清洗后字段()




    def 模具一一清洗字段(self):
        规则 = '(?<=uploads).{1,}(?=.html)'
        文本列表 = re.findall(规则, str(self.摘要))  # 提取 前面
        if len(文本列表)==0:
            self.标题相同 = 0
            return  # 返回

        短标题 = 文本列表[0]
        原标题 =短标题

        短标题 = 短标题.replace("[", "【")  # 替换   , 1) 次数 1
        短标题 = 短标题.replace("]", "】")  # 替换   , 1) 次数 1
        短标题 = 短标题.replace("(", "（")  # 替换   , 1) 次数 1
        短标题 = 短标题.replace(")", "）")  # 替换   , 1) 次数 1
        短标题 = 短标题.replace(" ", "")  # 替换   , 1) 次数 1
        短标题 = 短标题.replace(' ', "")  # 替换   , 1) 次数 1
        短标题 = 短标题.replace("`", "")  # 替换   , 1) 次数 1

        清洗后短标题 =短标题
        print('清洗后短标题',清洗后短标题)
        if 原标题==清洗后短标题:
            self.标题相同=0
            return  # 返回
        self.合成摘要 = str(self.摘要).replace(原标题, 清洗后短标题) #替换   , 1) 次数 1
        print('合成摘要', self.合成摘要)

    def 模具一一更新数据库里的清洗后字段(self):
        # 提取数据库里的过滤网址
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "",self.数据库名, charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # SQL 查询语句 self.各帖子链接
        sql = "UPDATE `网站文章内容` SET `摘要`=('%s') WHERE `帖子链接`=('%s')" % (self.合成摘要, self.帖子链接)
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()

        # 关闭数据库连接
        db.close()
        print('更新数据库里的清洗后字段完成')


类=类一一提取数据库修改字段()