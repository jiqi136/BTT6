# -*- coding:utf-8

#

import re  # 正则式
import time  # 时间
import datetime  # 时间

import pymysql  # 数据库


class 类一一话题: #调用 类的模具 self.模具一一数据库()
    def __init__(self):
        文本 = open(r"C:\下载中转站\2018上半年豆瓣电影口碑榜Top50.htm", 'r', encoding='UTF-8')
        self.一楼内容 = 文本.read()  # read() #读取
        文本.close()

        类型 = '电影'
        发布 = '否'

        self.模具一一文本整理()

    def 模具一一文本整理(self):
        一楼内容 =self.一楼内容

        规则 = '欢迎留言讨论.{1,}'
        一楼内容 = re.sub(规则, '', 一楼内容, 0, re.S)  # 替换   ,count=0,re.S|re.I

        规则 = '.{1,}以下为完整榜单'
        一楼内容 = re.sub(规则, '', 一楼内容, 0, re.S)  # 替换   ,count=0,re.S|re.I

        标题列表 = 一楼内容.split('<https')


        self.sql句后列表=[]

        for 标题层 in 标题列表:


            if '大陆' in 标题层:
                continue#跳过循环
                #print(标题层)
            行列表= 标题层.split('\n')

            for 标题行 in 行列表:
                sql句后 =''

                if '(2'in 标题行 and '/' not in 标题行:
                    标题 =标题行
                    规则 = r'\(.{1,}'
                    标题 = re.sub(规则, '',标题)# 替换   ,count=0,re.S|re.I

                    print('标题',标题)
                    continue  # 跳过循环

                if '/' in 标题行 and 'movie' not in 标题行:
                    地区 =标题行

                    print( '地区',地区)
                    continue  # 跳过循环

            sql句后= "('{}','{}','{}','{}'),".format(类型,标题,地区,发布)

                #self.sql句后列表.append(sql句后)
                #print(标题,地区)

            self.模具一一保存数据库()
            #self.标题 = 标题
            #self.地区 = 地区
            #self.模具一一保存数据库二()

    def 模具一一保存数据库(self):
        # 打开数据库连接,保存已下载网址
        # ======数据库内操作====== list()



        db = pymysql.connect("localhost", "root", "", '影视发帖推广', charset="utf8")

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句

        
        条件循环 = 1
        while 条件循环 == 1:  # 条件循环  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            sql句后条件 = ''
            for sql句后 in self.sql句后列表[0:100]:
                sql句后条件 = sql句后条件 + sql句后

            if len(self.sql句后列表)>99: #  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                del self.sql句后列表[0:100]
            else:# 否则
                条件循环 = 998

            sql句后条件 = sql句后条件.strip(',')  # 去除最后一个 ,号  默认则是去除空格
            sql句首 = "INSERT INTO 知乎话题二 ( `类型`, `话题`, `链接`, `赞同数`, `发布`) VALUES " + sql句后条件
            sql = sql句首

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
        print('知乎话题保存完成')

    def 模具一一保存数据库二(self):
        # 打开数据库连接,保存已下载网址


        db = pymysql.connect("localhost", "root", "", '影视发帖推广', charset="utf8")

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句

        sql="INSERT INTO `2018上半年豆瓣电影`(`类型`, `标题`, `链接`, `发布`) VALUES ('{}','{}','{}','{}')".format(self.类型,self.标题,self.地区,self.发布)


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
        print('知乎话题保存完成')



类=类一一话题()