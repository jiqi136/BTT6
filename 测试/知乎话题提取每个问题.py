# -*- coding:utf-8

#

import re  # 正则式
import time  # 时间
import datetime  # 时间

import pymysql  # 数据库


class 类一一话题: #调用 类的模具 self.模具一一数据库()
    def __init__(self):
        self.过滤sql句后条件 = ''

        文本 = open(r"C:\下载中转站\英 - 知乎.htm", 'r', encoding='UTF-8')
        一楼内容 = 文本.read()  # read() #读取
        文本.close()

        类型 = '英剧'
        发布 = '否'

        问题列表 = 一楼内容.split('//收起')
        self.sql句后列表=[]

        for 问题层 in 问题列表:

            行列表= 问题层.split('\n')
            for 行 in 行列表:
                if '人赞同 <#>' in 行:
                    赞同数=行
                    规则 = '人赞同.{1,}'
                    赞同数 = re.sub(规则, '', 赞同数)

                    规则 = '.{0,}•'
                    赞同数 = re.sub(规则, '', 赞同数)
                    赞同数.strip()  # 默认则是去除空格 '{}'  •1


            规则='>.{1,}'
            问题行 = re.sub(规则, '',问题层,0,re.S)  # 替换   ,count=0,re.S|re.I
            if 'http'in 问题行:


                问题 = 问题行.replace('<', '')
                问题 = 问题.replace(' ', '')
                规则 = '\n'
                问题 = re.sub(规则, '', 问题)  # 替换   ,count=0,re.S|re.I
                问题行 =问题.strip()#默认则是去除空格 '{}'

                规则 = 'http.{1,}'
                问题 = re.sub(规则, '', 问题行)  # 替换   ,count=0,re.S|re.I

                规则 = '.{1,}http'
                链接 = re.sub(规则, 'http', 问题行)  # 替换   ,count=0,re.S|re.I
                if 'question' in 链接:
                    sql句后= "('{}','{}','{}','{}','{}'),".format(类型,问题,链接, 赞同数,发布)

                    self.sql句后列表.append(sql句后)
                    print(问题,链接,赞同数)

        self.模具一一保存数据库()
    
    def 模具一一保存数据库(self):
        # 打开数据库连接,保存已下载网址
        # ======数据库内操作====== list()
        return#返回


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



类=类一一话题()