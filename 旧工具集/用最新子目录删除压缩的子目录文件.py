
import requests #人性化的 浏览器
import re  #正则表达式
import time #时间
import os #处理电脑系统文件和目录
import pymysql #mysql数据库
import random #随机数
from lxml import etree#解析与定位网页
import datetime  # 时间


class 类_用最新子目录删除压缩的子目录文件: #调用 类的模具 self.模具_数据库()
    def __init__(self):
        self.最新子目录子目录 = r'F:\电影模板\下载种子目录2\动漫'
        self.删除压缩子目录文件前缀 = r'F:\电影模板\压缩-下载种子\动漫' + '\\'
        self.删除打包的目录= r'F:\电影模板\压缩-下载种子\动漫打包'+ '\\'

        self.模具_展开最新子目录子目录()

    def 模具_展开最新子目录子目录(self):

        子目录列表与文件列表 = os.listdir(self.最新子目录子目录)  # 分离出目录列表与文件列表
        for self.子目录或文件 in 子目录列表与文件列表:
            根目录的子目录或文件路径 = os.path.join(self.最新子目录子目录, self.子目录或文件)
            if os.path.isdir(根目录的子目录或文件路径):  # 判断为 目录 文件夹

                self.子目录 = 根目录的子目录或文件路径
                self.删除压缩文件目录名 = self.删除压缩子目录文件前缀 + str(self.子目录或文件)

                self.模具_判断子目录子目录为文件夹()

    def 模具_判断子目录子目录为文件夹(self):
        元组目录列表与文件列表 = os.listdir(self.子目录)  # 分离出目录列表与文件列表

        子文件夹个数 = 0
        for self.元组子目录或文件 in 元组目录列表与文件列表:
            元组目录的子目录或文件路径 = os.path.join(self.子目录, self.元组子目录或文件)  # 合并为完全 的 访问路径


            if os.path.isdir(元组目录的子目录或文件路径): # 判断为 目录 文件夹
                self.目录路径 = 元组目录的子目录或文件路径
                子文件夹个数 = 1

                self.模具_删除压缩的子目录文件()
        if 子文件夹个数==0: #  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
            删除打包的压缩文件名=self.删除打包的目录 +self.子目录或文件+ '.zip'


            if os.path.exists(删除打包的压缩文件名):  # 必有条件选择,否则出错

                print('删除打包的压缩文件名:', 删除打包的压缩文件名)



                os.unlink(删除打包的压缩文件名)
                print('成功删除:', 删除打包的压缩文件名)
            else:  # 否则
                print('文件名为空:', 删除打包的压缩文件名)

    def 模具_删除压缩的子目录文件(self):

        删除压缩的子目录文件名=self.删除压缩文件目录名+ '\\'+ self.元组子目录或文件+ '.zip'



        if os.path.exists(删除压缩的子目录文件名):  # 必有条件选择,否则出错

            print('删除压缩的子目录文件名:', 删除压缩的子目录文件名)


            os.unlink(删除压缩的子目录文件名)
            print('成功删除:',删除压缩的子目录文件名)
        else:  # 否则
            print('文件名为空:', 删除压缩的子目录文件名)






    def 模具_判断子目录元组目录列表个数(self):
        print('==================')
        for 根路径, 元组目录列表, 文件列表 in os.walk(self.子目录):  # "."目录,topdown=False先子文件夹再到元组文件夹
            print('一层元组目录列表:', 元组目录列表)
            if len(元组目录列表) != 0:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环

                元组目录列表与文件列表 = os.listdir(self.子目录)  # 分离出目录列表与文件列表
                for 子目录或文件 in 元组目录列表与文件列表:
                    元组目录的子目录或文件路径 = os.path.join(self.子目录, 子目录或文件)  # 合并为完全 的 访问路径
                    if os.path.isdir(元组目录的子目录或文件路径):  # 判断为 目录 文件夹
                        self.目录路径 = 元组目录的子目录或文件路径

                        self.模具_压缩()
                        self.模具_创建移动文件目录()

                        移动文件名 = str(self.压缩目录名).replace("下载种子目录4", "压缩-下载种子")  # 替换   , 1) 次数 1
                        if not os.path.exists(移动文件名):  # 必有条件选择,否则出错
                            shutil.move(self.压缩目录名, self.删除压缩文件目录名)
                        else:  # 否则
                            os.unlink(移动文件名)
                            shutil.move(self.压缩目录名, self.删除压缩文件目录名)
                        print('移动至目录:', self.删除压缩文件目录名)

                    else:  # 否则 为文件
                        文件路径 = 元组目录的子目录或文件路径
                        self.模具_创建移动文件目录()

                        移动文件名 = str(文件路径).replace("下载种子目录4", "压缩-下载种子")  # 替换   , 1) 次数 1
                        if not os.path.exists(移动文件名):  # 必有条件选择,否则出错
                            shutil.copy(文件路径, self.删除压缩文件目录名)
                            print(文件路径, '复制文件:', self.删除压缩文件目录名)
                        else:  # 否则
                            print('复制文件已存在:跳过当前文件')
                            continue  # 跳过当前循环,继续进行下一轮循环


            else:  # 否则
                if len(文件列表) != 0:
                    self.目录路径 = self.子目录
                    self.模具_压缩()

                移动文件名 = str(self.压缩目录名).replace("下载种子目录4\动漫", "压缩-下载种子\动漫打包")  # 替换   , 1) 次数 1
                if not os.path.exists(移动文件名):  # 必有条件选择,否则出错
                    shutil.move(self.压缩目录名, self.删除压缩文件目录名)
                else:  # 否则
                    os.unlink(移动文件名)
                    shutil.move(self.压缩目录名, self.删除压缩文件目录名)
                print('移动至目录:', 移动文件名)

            break  # 结束循环

类=类_用最新子目录删除压缩的子目录文件()




