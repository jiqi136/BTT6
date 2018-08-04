import re

import os
import pymysql
import random

import shutil







class 类一一集差:  # 调用 类的模具 self.模具一一数据库()
    def __init__(self):
        self.模具一一递归展开目录提取全部文件名()
        self.模具一一读取内容数据库()
        self.模具一一比较集差()
        self.模具一一删除数据库里无文件空文()


    def 模具一一递归展开目录提取全部文件名(self):
        self.文件名列表=[]
        目标目录 = r"F:\下载种子目录\ftp上传目录链接网页\html网页文件"
        for 根路径, 一层目录列表, 一层文件列表 in os.walk(目标目录, topdown=False):  # "."目录,topdown=False先子文件夹再到全层元组文件夹
            for 文件 in 一层文件列表:  # dirs遍历目录  files遍历文件

                文件 = str(文件).replace(".html", "")  # 替换   , 1) 次数 1
                待机文件 = 文件
                if " " in 文件 or ' ' in 文件 or "[" in 文件 or "]" in 文件 or "(" in 文件 or ")" in 文件 or '`' in 文件:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                    待机文件 = 文件
                    待机文件 = 待机文件.replace(' ', "")  # 替换   , 1) 次数 1
                    待机文件 = 待机文件.replace(' ', "")  # 替换   , 1) 次数 1
                    待机文件 = 待机文件.replace('`', "")  # 替换   , 1) 次数 1
                    待机文件 = 待机文件.replace("[", "【")  # 替换   , 1) 次数 1
                    待机文件 = 待机文件.replace("]", "】")  # 替换   , 1) 次数 1
                    待机文件 = 待机文件.replace("(", "（")  # 替换   , 1) 次数 1
                    待机文件 = 待机文件.replace(")", "）")  # 替换   , 1) 次数 1
                self.文件名列表.append(待机文件)

    def 模具一一读取内容数据库(self):
        # 连接数据库
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "", "电影与合集", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句   已下载内容网址
        sql = "SELECT `短标题` FROM `网站文章内容`"
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        self.短标题组列表 = cursor.fetchall()
        # 关闭数据库连接
        db.close()

    def 模具一一比较集差(self):
        原数据库短标题列表=[]
        清洗后的数据库短标题列表=[]
        for 短标题组 in self.短标题组列表:
            短标题=短标题组[0]
            原数据库短标题列表.append(短标题)

            文件 = 短标题
            待机文件 = 文件
            if " " in 文件 or ' ' in 文件 or "[" in 文件 or "]" in 文件 or "(" in 文件 or ")" in 文件 or '`' in 文件:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环

                待机文件 = 待机文件.replace(' ', "")  # 替换   , 1) 次数 1
                待机文件 = 待机文件.replace(' ', "")  # 替换   , 1) 次数 1
                待机文件 = 待机文件.replace('`', "")  # 替换   , 1) 次数 1
                待机文件 = 待机文件.replace("[", "【")  # 替换   , 1) 次数 1
                待机文件 = 待机文件.replace("]", "】")  # 替换   , 1) 次数 1
                待机文件 = 待机文件.replace("(", "（")  # 替换   , 1) 次数 1
                待机文件 = 待机文件.replace(")", "）")  # 替换   , 1) 次数 1
            清洗后的数据库短标题列表.append(待机文件)

        原数据库短标题列表集 = set(原数据库短标题列表)
        清洗后的数据库短标题列表集 = set(清洗后的数据库短标题列表)
        文件名集 = set(self.文件名列表)
        空文集差=清洗后的数据库短标题列表集-文件名集
        self.不用修改的短标题列表差集 = 空文集差 & 原数据库短标题列表集  # 交集  x & y

        self.要修改的短标题列表差集=空文集差-原数据库短标题列表集 # 差集
        self.模具一一删除数据库里无文件空文二()




    def 模具一一删除数据库里无文件空文(self):
        # 连接数据库
        print('====================================')
        print('连接数据库....')
        db = pymysql.connect("localhost", "root", "", "电影与合集", charset="utf8")
        # 获取游标
        cursor = db.cursor()
        # SQL 查询语句   已下载内容网址
        倒数=len(self.不用修改的短标题列表差集)
        for 短标题 in self.不用修改的短标题列表差集:
            sql = "DELETE FROM `网站文章内容` WHERE`短标题`=('%s')" % (短标题)
            # 执行SQL语句
            cursor.execute(sql)
            print('成功删除数据库短标题', 短标题)
            倒数=倒数-1
            print('成功删除数据库空文,倒数',倒数)
        # 提交到数据库执行
        db.commit()
        # 关闭数据库连接
        db.close()
        print('成功更新全部正文')
    def 模具一一删除数据库里无文件空文二(self):
        # 连接数据库
        print('====================================')
        print('连接数据库....')
        db = pymysql.connect("localhost", "root", "", "电影与合集", charset="utf8")
        # 获取游标
        cursor = db.cursor()
        # SQL 查询语句   已下载内容网址
        倒数=len(self.不用修改的短标题列表差集)
        for 短标题 in self.要修改的短标题列表差集:
            sql = "DELETE FROM `网站文章内容` WHERE`短标题`LIKE '%{}%'".format(短标题)
            # 执行SQL语句
            cursor.execute(sql)
            print('成功删除数据库短标题', 短标题)
            倒数=倒数-1
            print('成功删除数据库空文,倒数',倒数)
        # 提交到数据库执行
        db.commit()
        # 关闭数据库连接
        db.close()
        print('成功更新全部正文')




类=类一一集差()