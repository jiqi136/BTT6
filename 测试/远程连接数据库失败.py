import pymysql
import time

def 模具_保存电影与合集过滤帖子网址():

        各帖子链接='1'

        
        条件循环 = 1
        计数器 = 1
        while 条件循环 == 1:  # 条件循环  break # 结束循环 continue # 跳过当前循环，继续进行下一轮循环

            try:
                操作游标 = pymysql.connect(host="123.108.110.122", port=端口, user="ecom_a1",
                                      passwd=密码, db="ecom_a1", charset="utf8")
                # 使用cursor()方法获取操作游标 port =3306,   user =ecom_a1@localhost

            except:
                if 计数器 == 65535:
                    print('遍历完成,大失败', 计数器)
                    条件循环 = 123

                print('错误', 计数器)
                计数器 = 计数器 + 1


            else:  # 否则
                cursor = 操作游标.cursor()
                print('成功进入')
                print('端口port=',计数器)

                条件循环 = 123
            
        操作游标 = pymysql.connect(host ="123.108.110.122",port =3306, user ="ecom_a1@localhost", passwd ="ZGV2KcvqVA8CG8MR", db ="ecom_a1", charset="utf8")
        # 使用cursor()方法获取操作游标 port =3306,   user =ecom_a1@localhost
        cursor = 操作游标.cursor()
        print('成功进入')
        # SQL 插入语句
        sql = """INSERT INTO 过滤网址(过滤网址)
                   VALUES ('%s')""" % (各帖子链接)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            操作游标.commit()
        except:
            # 如果发生错误则回滚
            操作游标.rollback()
        # 关闭数据库连接
        操作游标.close()


def 模具_50m远程数据库():
    print('开始连接')
    远程数据库帐号 = """my55cc密码my55cc

数据库面板及地址： mysql.xrnet.net 或者用IP连接122.114.10.20
set password for my55cc= password('qq856113M%')
    """

    条件循环 = 0
    while 条件循环 == 0:

        try:
            数据库执行 = pymysql.connect(host="122.114.10.20", port=3306, user="my55cc",
                                  passwd='qq856113M%', db="my55cc", charset="utf8")
            # 使用cursor()方法获取操作游标 port =3306,   user =ecom_a1@localhost

        except:

            print('连接错误')
            time.sleep(1)  # 等待



        else:  # 否则
            print('成功进入')

            # 使用cursor()方法获取操作游标
            操作游标 = 数据库执行.cursor()
            条件循环 = 998

    sql语句="""SELECT *
FROM `查询版本号`
WHERE `版本历史` = '最新'"""

    # 执行sql语句
    操作游标.execute(sql语句)




    数据库内容组列表 = 操作游标.fetchall()
    版本内容组=数据库内容组列表[0]
    print('版本内容组:',版本内容组)

    数据库执行.close()  # 关闭数据库连接

      
    def 模具_执行sql语句():

        cursor = 操作游标.cursor()
        print('成功进入')
        # SQL 插入语句
        sql = """INSERT INTO 过滤网址(过滤网址)
                       VALUES ('%s')""" % (各帖子链接)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            操作游标.commit()
        except:
            # 如果发生错误则回滚
            操作游标.rollback()


        # 关闭数据库连接
        数据库执行.close()  # 关闭数据库连接
模具_50m远程数据库()

