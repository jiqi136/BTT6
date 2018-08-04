#!/usr/bin/python3


import requests #人性化的 浏览器
import re  #正则表达式
import time #时间
import os #处理电脑系统文件和目录
import pymysql #mysql数据库
import random #随机数
from lxml import etree#解析与定位网页
import datetime  # 时间
import shutil

def 模具_符号清洗(原文):
    列表=["\'","\"",":","*","/","#","\"","?",".","\'","'","\'","'",'',',','！','\\n','\n','>','<','\\xa0']
    for 符号 in 列表:
        原文 = str(原文).replace(符号, '')
    原文 = str(原文).replace('F\\电影', 'F:\\电影')
    return 原文
def 模具_目录名清洗():
    for root, dirs, files in os.walk("F:\电影模板\下载种子目录2\电视剧", topdown=False):#"."目录,topdown=False先子文件夹再到元组文件夹

        for name in dirs:#遍历文件夹
            name2=模具_符号清洗(name)

            旧目录=os.path.join(root, name)
            新目录=os.path.join(root, name2)
            #print(旧目录)
            #print(新目录)
            try:
                os.renames(旧目录, 新目录)
                print("成功修改:",新目录)
            except (FileNotFoundError,FileExistsError,PermissionError):
                continue  # 跳过当前循环,继续进行下一轮循环
def 模具_符号清洗2(原文):
    列表=["\'","\"","*","#","\"","?",".","\'","'","\'","'",'',',','！','\\n','\n','>','<','\\xa0']
    for 符号 in 列表:
        原文 = str(原文).replace(符号, '')
    原文 = str(原文).replace('\\\\', '/')
    原文 = str(原文).strip('[')  # 文本前后截去特定字符串
    原文 = str(原文).strip(']')  # 文本前后截去特定字符串
    原文 = str(原文).strip(', ')  # 文本前后截去特定字符串
    return 原文
def 模具_移动目录():
    循环计数 = 1.
    分目录计数 = 8

    for root, dirs, files in os.walk("F:/电影模板/下载种子目录2", topdown=False):  # "."目录,topdown=False先子文件夹再到元组文件夹True

        for name in dirs:  # 遍历文件夹
            计数分目录='F:/电影模板/下载种子目录3/{}'.format(分目录计数)
            旧目录 = os.path.join(root, name)
            新目录 =str(旧目录).replace('F:/电影模板/下载种子目录2', 计数分目录)
            规则 = r'.{1,}(?=\\)'
            新目录 = re.findall(规则, str(新目录))
            新目录 = 模具_符号清洗2(新目录)
            try:
                os.rmdir(旧目录)  # 只能删除空目录
                print("删除空目录:", 旧目录)

                if 循环计数 >4300:

                    print('4800条目录分隔:', 新目录)
                    分目录计数 += 1
                    循环计数 = 0

                    continue  # 跳过当前循环,继续进行下一轮循环
                循环计数 += 1
                continue  # 跳过当前循环,继续进行下一轮循环
            except (OSError):# 目录不为空
                # 移动目录z
                循环计数 += 1
                try:
                    if not os.path.exists(新目录):  # 必有条件选择,否则出错
                        os.makedirs(新目录)  # makedirs 创建多级目录文件夹,mkdir创建一个文件夹
                except (FileNotFoundError, OSError):
                    pass

                try:
                    shutil.move(旧目录, 新目录)
                    print("旧目录:", 旧目录)
                    print("完成移动新目录:", 新目录)

                except (shutil.Error):

                    continue  # 跳过当前循环,继续进行下一轮循环
def 模具_种子名清洗():
    for root, dirs, files in os.walk("F:/电影模板/下载种子目录3/2", topdown=False):#"."目录,topdown=False先子文件夹再到元组文件夹

        for name in files:#遍历文件夹

            name2 = str(name).strip('.')  # 文本前后截去特定字符串
            name2 = str(name2).strip(')')  # 文本前后截去特定字符串



            旧种子名=os.path.join(root, name)
            新种子名=os.path.join(root, name2)
            #print(旧目录)
            #print(新目录)
            try:
                os.renames(旧种子名, 新种子名)
                print(旧种子名, "成功修改新种子名:",新种子名)
            except (FileNotFoundError,FileExistsError,PermissionError):
                continue  # 跳过当前循环,继续进行下一轮循环


class 类_操作目录: #调用 类的模具 self.模具_数据库()
    def __init__(self):
        self.模具_遍历第三层目录()
        #self.data =data
    

         
    def 模具_查找数据库(self):
        db = pymysql.connect("localhost", "root", "", "综合影视剧", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句
        sql ="""SELECT 目录名 FROM 本地目录链接文件 ;""" #数值条件查找后选取
        # 执行sql语句
        cursor.execute(sql)
        # 获取所有记录列表
        self.数据库记录列表 = cursor.fetchall()
         # 关闭数据库连接
        db.close()
    
    def 模具_更改数据库(self):
        db = pymysql.connect("localhost", "root", "", "综合影视剧", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        self.单个纯净目录
        单个目录 = str(self.单个目录).replace("\\", "/") #替换   , 1) 次数 1
        # SQL 插入语句
        sql ="""UPDATE 本地目录链接文件 
            SET 本地种子目录=('%s') #想要修改的内容
            WHERE 目录名=('%s');""" % (单个目录,self.单个纯净目录)#省略了 WHERE 子句没有具体条件的更新,将会修改表中所有 列的 数据

        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()

        # 关闭数据库连接
        db.close()
        print('成功更改本地种子目录 数据库')
            
    def 模具_遍历第三层目录(self):
        self.模具_查找数据库()
        print(self.数据库记录列表)
        目标目录='F:\电影模板\下载种子目录3'
        fileList = os.listdir(目标目录)  # 获取path目录下所有文件
        for 目录 in fileList:
            第一层序号目录 = os.path.join(目标目录, 目录)  # 获取path与filename组合后的路径

            if not os.path.isdir(第一层序号目录):  # 如果 不是目录
                continue  # 跳过当前循环,继续进行下一轮循环

            第一层序号目录列表 = os.listdir(第一层序号目录)  # 获取path目录下所有文件
            for 第二层类型目录 in 第一层序号目录列表:
                第二层类型目录 = os.path.join(第一层序号目录, 第二层类型目录)  # 获取path与filename组合后的路径
                if not os.path.isdir(第二层类型目录):  # 如果是目录
                    continue  # 跳过当前循环,继续进行下一轮循环

                第二层类型目录列表 = os.listdir(第二层类型目录)  # 获取path目录下所有文件
                for 单个目录 in 第二层类型目录列表:
                    self.单个纯净目录 =单个目录
                    print(self.单个纯净目录)
                    self.单个目录 = os.path.join(第二层类型目录, 单个目录)  # 获取path与filename组合后的路径
                    if not os.path.isdir(self.单个目录):  # 如果是目录
                        continue  # 跳过当前循环,继续进行下一轮循环
                    print(self.单个目录)
                    
                    if self.单个纯净目录 in str(self.数据库记录列表): #  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                        self.模具_更改数据库()

                    else:# 否则
                        print('跳过当前循环')
                        continue  # 跳过当前循环,继续进行下一轮循环







    def 模具_浏览器(self):
        新目录列表=[]
        新目录=[]

        try:
            shutil.move(新目录, self.单个目录)#移动文件
            print("完成回填目录:", self.单个目录)
            新目录列表.append(新目录)
        except (shutil.Error) as 异常原因:
            print("失败:", 异常原因)
            print("回填目录失败:", self.单个目录)
            return

操作目录=类_操作目录()
#操作目录.模具_遍历第三层目录()

