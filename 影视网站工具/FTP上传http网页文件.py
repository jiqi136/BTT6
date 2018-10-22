# -*- coding:utf-8

import re  #正则表达式
import time #时间
import os #处理电脑系统文件和目录
import fileinput
from ftplib import FTP
import socket


class 类一一上传目录链接网页: #调用 类的模具 self.模具_数据库()
    def __init__(self):
        self.新旧影视 = "最新"

        #self.新旧影视 = "合集"
        self.模具一一开始调度()


    def 模具一一开始调度(self):
        self.上传文件数 = 0
        self.模具一一ftp尝试登录()
        self.模具一一提取文件()
        print('self.上传文件数:', self.上传文件数)

        print('等待20秒')
        time.sleep(20)


    def 模具一一提取文件(self):
        目标目录='F:/下载种子目录/ftp上传目录链接网页'

        子目录列表与文件列表 = os.listdir(目标目录)  # 分离出目录列表与文件列表
        for 子目录或文件 in 子目录列表与文件列表:
            根目录的子目录或文件路径 = os.path.join(目标目录, 子目录或文件)
            if os.path.isdir(根目录的子目录或文件路径):  # 判断是不是文件夹
                # os.path.isfile() 函数判断某一路径是否为文件
                子目录 = 根目录的子目录或文件路径
                二级子目录列表与文件列表 = os.listdir(子目录)  # 分离出目录列表与文件列表
            else:  # 否则 为文件

                self.二级子目录文件 = 根目录的子目录或文件路径

                print('self.二级子目录文件:', self.二级子目录文件)
                self.模具一一提取保存目录()

                self.模具一一读取文本每一行()

                print('=================')


    def 模具一一提取保存目录(self):
        if '最新' in str(self.二级子目录文件):  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环

            保存文件目录 = 'F:/下载种子目录/ftp上传目录链接网页/html网页文件/2html/{}'
        else:  # 否则
            保存文件目录 = 'F:/下载种子目录/ftp上传目录链接网页/html网页文件/html/{}'


        类型拼音字典 = {'电影': 'dying', '动漫': 'dongman', '电视剧': 'dianshiju'}
        for 字典键 in 类型拼音字典:  # 范围 range
            if 字典键 in str(self.二级子目录文件):
                保存目录的影视类型 = 类型拼音字典[字典键]
                self.保存文件目录 = 保存文件目录.format(保存目录的影视类型)  # 不换行 end=""


    def 模具一一读取文本每一行(self):
        self.上传等待数 = 0

        #文本 = open(self.二级子目录文件, 'r',encoding='UTF-8')
        #文本内容列表 = 文本.readlines()  # 读取所有行，储存在列表中，每个元素是一行。

        try:  # 调用异常处理，应对易发生错误的位置
            文本 = open(self.二级子目录文件, 'r', encoding='UTF-8')
            文本内容列表 = 文本.readlines()  # 读取所有行，储存在列表中，每个元素是一行。
        except UnicodeDecodeError as 异常原因:  # 异常处理
            print(异常原因)
            文本 = open(self.二级子目录文件, 'r',encoding='gbk')
            文本内容列表 = 文本.readlines()  # 读取所有行，储存在列表中，每个元素是一行。
        else:  # 必须放在所有的except子句之后。这个子句将在try子句没有发生任何异常的时候执行。
            文本.close()

        #文本 = open(self.二级子目录文件, 'r',encoding='UTF-8')
        #文本内容 = 文本.read()  # read() #读取
        #文本.close()

        #文本内容列表 =文本内容.split("\n")

        if len(文本内容列表) == 0:
            print('空文本文件')
            return  #  结束循环  返回

        self.模具一一ftp的目录文件文本()

        for self.网盘文件名与链接 in 文本内容列表:


            self.模具一一读取文件名与http网页()
            if self.文件名 in self.目录与文件列表文本 and "最新" in self.新旧影视: #  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环

                continue  # 跳过当前循环

            elif "合集" in self.新旧影视:
                print('转换为http网页，========等待========')
                self.模具一一转换为http网页()
            else:# 否则  模具一一ftp上传网页文件
                self.模具一一转换为http网页()

                self.模具一一ftp上传网页文件()
         # 清空文本文件


        文本 = open(self.二级子目录文件, 'w', encoding='UTF-8')  # 读取encoding='UTF-8'utf8的文件, encoding='UTF-8'
        文本.write('')  # read() #读取
        文本.close()
        print('清空文本文件', self.二级子目录文件)


    def 模具一一读取文件名与http网页(self):
        规则 = ': https.{1,}'  #
        文件名 = re.sub(规则,'',self.网盘文件名与链接)  #
        if len(文件名) == 0:
            return

        文件名 = 文件名.replace(".zip", "") #替换   , 1) 次数 1
        文件名 = 文件名.rstrip()  # 指定删除的字符串末尾的字符（默认为空格）

        列表 = ["\\xa0", "[", "]", "\'", "\"", ":", "*", "/", "\\", "#", "\"", "?", ".", "\'", "'", "\'", "'", '',
              ',', ':', ':',' ','`',' ',
              '！', '\\n', '\n', '>', '<', '%', '?', ':', '｜', '|', '！']  # 英中字符
        for 符号 in 列表:
            文件名 = 文件名.replace(符号, '')


        # 替换不同字符间的符号
        if '[' in 文件名 or ']' in 文件名:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            文件名 = 文件名.replace("[", "[")  # 替换   , 1) 次数 1
            文件名 = 文件名.replace("]", "]")  # 替换   , 1) 次数 1
        elif '(' in 文件名 or ')' in 文件名:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            文件名 = 文件名.replace("(", "（")  # 替换   , 1) 次数 1
            文件名 = 文件名.replace(")", "）")  # 替换   , 1) 次数 1
        self.文件名 = 文件名


        规则 = '.{1,}: https'  #
        目录链接 = re.sub(规则, 'https', self.网盘文件名与链接)  #
        目录链接 = 目录链接.rstrip()  # 指定删除的字符串末尾的字符（默认为空格）


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

    def 模具一一转换为http网页(self):

        self.文件路径 =self.保存文件目录+'/'+self.文件名+'.html'
        文本 = open(self.文件路径, 'w', encoding='UTF-8')  # 读取encoding='UTF-8'utf8的文件, encoding='UTF-8'
        文本.write(self.网页内容)  # read() #读取
        文本.close()

    def 模具一一ftp尝试登录(self):
        self.ftp = FTP()  # 设置变量
        #self.ftp.set_debuglevel(2)  # 打开调试级别2,显示详细信息
        self.ftp.connect("123.108.110.122", 21)  # 连接的ftp sever和端口
        self.ftp.login("ecom", "b35eR33yPi")  # 连接的用户名,密码
        print('===登录成功========')

    def 模具一一ftp的目录文件文本(self):

        ftp的目录 = str(self.保存文件目录).replace("F:/下载种子目录/ftp上传目录链接网页/html网页文件/", "/domains/3e38.com/public_html/uploads/") #替换   , 1) 次数 1
        self.ftp.cwd(ftp的目录) #进入操作目录

        self.目录与文件列表文本=str(self.ftp.nlst()) #列出目录 下的目录与文件
        self.ftp的目录= ftp的目录
    def 模具一一ftp上传网页文件(self):
        设置的缓冲区大小 = 10024
        本地文件路径 = self.文件路径
        获取上传文件名 =self.文件名+'.html'
        上传内容字节 = open(本地文件路径, 'rb')  # 打开文件
        print('准备上传')

                    
        try:  # 调用异常处理,应对易发生错误的位置


            self.ftp.storbinary('STOR ' + 获取上传文件名, 上传内容字节, 设置的缓冲区大小)  # 上传文件
            #self.ftp.set_debuglevel(0)
            上传内容字节.close()

            #time.sleep(1)
            # ftp.rename(encoding='UTF-8'上传获取文件名, 'fwfewfwg')  # 将fromname修改名称为toname.
        except (UnicodeDecodeError)as 异常原因:  # 异常处理
            print(异常原因)
            return  # 返回
        else:  # 必须放在所有的except子句之后.这个子句将在try子句没有发生任何异常的时候执行.

            print('==上传完成====', 获取上传文件名)
            self.上传等待数=self.上传等待数+1
            self.上传文件数=self.上传文件数+1


类=类一一上传目录链接网页()

            