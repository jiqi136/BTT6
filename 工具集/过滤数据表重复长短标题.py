import pymysql #mysql数据库
import asyncio
import aiomysql



class 类_删除重复长短椙数据库: #调用 类的模具 self.模具_数据库()
    def __init__(self):
        #self.新旧剧集 = '电影与合集'
        self.sql句1字段 = ''

        self.新旧剧集 = '最新影视剧'
        影视类型列表 = ['电影', '电视剧', '动漫']
        for self.影视类型 in 影视类型列表:
            print('上传类型:', self.影视类型)
            self.模具_读取内容数据库()
            self.模具_数据表反向过滤短标题()

            self.模具_删除数据库里重复长短标题()

    def 模具_读取内容数据库(self):
        # 连接数据库
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "", self.新旧剧集, charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句   已下载内容网址
        sql = "SELECT `长标题`, `短标题`,`帖子链接` FROM `网站文章内容` WHERE `影视类型`=('%s') " % (self.影视类型)  # 不换行 end=""

        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        self.数据表 = cursor.fetchall()
        # 关闭数据库连接
        db.close()

    def 模具_读取内容数据库3(self):
        # 连接数据库
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "", self.新旧剧集, charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句   已下载内容网址
        sql = "SELECT `长标题`, `短标题`,`帖子链接` FROM `网站文章内容一一测试` WHERE `影视类型`=('%s') " % (self.影视类型)  # 不换行 end=""

        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        self.数据表 = cursor.fetchall()
        # 关闭数据库连接
        db.close()

    def 模具_数据表反向过滤短标题(self):
        # 关闭数据库连接
        数据表 = list(self.数据表)  # 转换为列表
        数据表.reverse()  # 反向排序 列表

        长标题列表 = []
        短标题列表 = []
        self.删除行的链接列表 = []
        for 长短标题链接组 in 数据表:
            长标题 = 长短标题链接组[0]
            短标题 = 长短标题链接组[1]
            帖子链接= 长短标题链接组[2]
            if 短标题 in 短标题列表:
                if len(短标题) == 0:
                    continue  # 跳过当前循环,继续进行下一轮循环
                self.删除行的链接列表.append(帖子链接)
                print('过滤的短标题', 短标题)
                self.sql句1字段 = self.sql句1字段 + "'{}',".format(帖子链接)
                continue  # 跳过当前循环,继续进行下一轮循环
            if 长标题 in 长标题列表:
                if len(长标题) == 0:
                    continue  # 跳过当前循环,继续进行下一轮循环
                self.删除行的链接列表.append(帖子链接)
                print('过滤的长标题........',长标题)
                self.sql句1字段 = self.sql句1字段 + "'{}',".format(帖子链接)
                continue  # 跳过当前循环,继续进行下一轮循环
            if 帖子链接 in 短标题列表:

                print('过滤的长标题........',帖子链接)
                self.sql句1字段 = self.sql句1字段 + "'{}',".format(帖子链接)
                continue  # 跳过当前循环,继续进行下一轮循环

            短标题列表.append(短标题)
            长标题列表.append(长标题)
            短标题列表.append(帖子链接)

    def 模具_删除数据库里重复长短标题(self):
        # ======循环内 拼接========
        # sql句1字段 = sql句1字段 + "WHEN '{}' THEN '正文' ".format(self.网址)
        if len(self.sql句1字段)==0:
            return #返回
        sql句1字段 = str(self.sql句1字段).strip(',')  # 去除最后一个 ，号  默认则是去除空格
        sql语句1字段首 = 'delete from `网站文章内容` where `帖子链接` in ({})'.format(sql句1字段)

        # ======数据库内操作=======
        sql =sql语句1字段首

        # 连接数据库
        print('连接数据库....')
        db = pymysql.connect("localhost", "root", "", self.新旧剧集, charset="utf8")
        # 获取游标
        cursor = db.cursor()
        # SQL 查询语句   已下载内容网址
        # 执行SQL语句
        cursor.execute(sql)

        # 提交到数据库执行
        db.commit()
        # 关闭数据库连接
        db.close()
        print('删除重复长短椙数据库...成功.')



类=类_删除重复长短椙数据库()