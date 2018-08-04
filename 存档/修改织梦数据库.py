import pymysql #mysql数据库


def 修改数据库():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "","试", charset="utf8")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句   已下载内容网址
    sql = "SELECT * FROM dede_archives"#dede_archives表是ID
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    数据列表 = cursor.fetchall()
    计数器=1
    for 数据表 in 数据列表:

        编号id=数据表[0]

        网站副栏目ID=数据表[2]
        网站副栏目ID = str(网站副栏目ID).replace("连载", "124")
        网站副栏目ID = str(网站副栏目ID).replace("犯罪", "40")
        网站副栏目ID = str(网站副栏目ID).replace("灾难", "36")
        网站副栏目ID = str(网站副栏目ID).replace("印度", "31")
        网站副栏目ID = str(网站副栏目ID).replace("多国", "31")
        网站副栏目ID = str(网站副栏目ID).replace(" ", "")
        网站副栏目ID = str(网站副栏目ID).strip(',')
        sql = """UPDATE dede_archives 
                           SET typeid2=('%s')
                          WHERE id=('%d');"""% (网站副栏目ID,编号id)
        print('已修改',计数器)
        计数器+=1
        # 执行SQL语句
        cursor.execute(sql)

        # 提交到数据库执行
        db.commit()
    # 关闭数据库连接
    db.close()

修改数据库()
