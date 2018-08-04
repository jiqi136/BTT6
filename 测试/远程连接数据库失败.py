import pymysql

def 模具_保存电影与合集过滤帖子网址():

        各帖子链接='1'

        
        条件循环 = 1
        计数器 = 1
        while 条件循环 == 1:  # 条件循环  break # 结束循环 continue # 跳过当前循环，继续进行下一轮循环

            try:
                db3 = pymysql.connect(host="123.108.110.122", port=计数器, user="ecom_a1",
                                      passwd="ZGV2KcvqVA8CG8MR", db="ecom_a1", charset="utf8")
                # 使用cursor()方法获取操作游标 port =3306,   user =ecom_a1@localhost

            except:
                if 计数器 == 65535:
                    print('遍历完成,大失败', 计数器)
                    条件循环 = 123

                print('错误', 计数器)
                计数器 = 计数器 + 1


            else:  # 否则
                cursor = db3.cursor()
                print('成功进入')
                print('端口port=',计数器)

                条件循环 = 123
            
        db3 = pymysql.connect(host ="123.108.110.122",port =3306, user ="ecom_a1@localhost", passwd ="ZGV2KcvqVA8CG8MR", db ="ecom_a1", charset="utf8")
        # 使用cursor()方法获取操作游标 port =3306,   user =ecom_a1@localhost
        cursor = db3.cursor()
        print('成功进入')
        # SQL 插入语句
        sql = """INSERT INTO 过滤网址(过滤网址)
                   VALUES ('%s')""" % (各帖子链接)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db3.commit()
        except:
            # 如果发生错误则回滚
            db3.rollback()
        # 关闭数据库连接
        db3.close()

模具_保存电影与合集过滤帖子网址()

