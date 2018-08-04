

import requests #人性化的 浏览器
import re  #正则表达式
import time #时间
import os #处理电脑系统文件和目录
import pymysql #mysql数据库
import random #随机数
from lxml import etree#解析与定位网页
import datetime  # 时间
import shutil
#import MYSQLdb  %j
import tarfile

# bufsize = 1024  # 设置的缓冲区大小
# filename = "filename.txt"  # 需要下载的文件
# file_handle = open(filename, "wb").write  # 以写模式在本地打开文件
# ftp.retrbinaly("RETR filename.txt", file_handle, bufsize)  # 接收服务器上文件并写入本地文件
# ftp.set_debuglevel(0)  # 关闭调试模式
# ftp.quit()  # 退出ftp

# ftp相关命令操作
# ftp.cwd(pathname)  # 设置FTP当前操作的路径
# ftp.dir()  # 显示目录下所有目录信息
# ftp.nlst()  # 获取目录下的文件
# ftp.mkd(pathname)  # 新建远程目录
# ftp.pwd()  # 返回当前所在位置
# ftp.rmd(dirname)  # 删除远程目录
# ftp.delete(filename)  # 删除远程文件
# ftp.rename(fromname, toname)  # 将fromname修改名称为toname.
# ftp.storbinaly("STOR filename.txt", file_handel, bufsize)  # 上传目标文件
# ftp.retrbinary("RETR filename.txt", file_handel, bufsize)  # 下载FTP文件   ftp.encoding = 字符集

import ftplib
from ftplib import FTP            #加载ftp模块   for 字符集 in 字符集列表:  字符集列表 = ['UTF-8', 'gbk', 'utf8_croatian_ci', 'UTF8', 'GB2312', 'GB18030', 'Unicode', 'HZ', 'HZ', 'HZ''Big5', 'ASCII']


ftp=FTP()                         #设置变量


ftp.set_debuglevel(2)             #打开调试级别2,显示详细信息
ftp.connect("123.108.110.122",21)          #连接的ftp sever和端口
ftp.login("ecom","b35eR33yPi")      #连接的用户名,密码
#print(ftp.getwelcome())           #打印出欢迎信息
print('=====显示根目录==========')
#print(ftp.dir()) #显示目录下所有目录信息
#ftp.cwd("/domains/3e38.com/public_html/uploads/html")                 #设置FTP当前操作的路径
#ftp.mkd("regfr")                 #新建远程目录
#ftp.cmd("domains")                #进入远程目录 ,这是一个错误的操作语
#ftp.nlst()                        #获取目录下的文件
#print('=====显示当前操作目录==============')
#print(ftp.dir()) #显示目录下所有目录信息

#从本地上传文件到ftp
def 从本地上传文件到ftp():
    ftp.cwd("/domains/3e38.com/public_html/uploads/2html")
    设置的缓冲区大小 = 1024
    本地文件路径='F:/下载种子目录/ftp上传目录链接网页/html网页文件/html/dianshiju/马场大亨.html'
    上传获取文件名='马场有物一大亨.html'
    print('上传获取文件名',上传获取文件名)

    上传内容字节=open(本地文件路径, 'rb')  #打开文件

    try:  #调用异常处理,应对易发生错误的位置
        ftp.storbinary('STOR ' + 上传获取文件名, 上传内容字节, 设置的缓冲区大小)  # 上传文件
        ftp.set_debuglevel(0)
        上传内容字节.close()

        # ftp.rename(encoding='UTF-8'上传获取文件名, 'fwfewfwg')  # 将fromname修改名称为toname.


    except (UnicodeDecodeError)as 异常原因 :#异常处理
        print(异常原因 )
        return#返回


    else:#必须放在所有的except子句之后.这个子句将在try子句没有发生任何异常的时候执行.
        print('====上传完成=========')
        目录与文件列表=ftp.nlst()
        print('目录与文件列表：' ,目录与文件列表)

        for 目录与文件 in 目录与文件列表:
            print('目录与文件3：',目录与文件)



从本地上传文件到ftp()




