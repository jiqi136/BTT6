import pyautogui as pag
import time
import pymysql

print('打开数据库连接')
# 打开数据库连接, 手机号码
今天时间 = str(time.strftime("%y-%m-%d", time.localtime()))
取女名='取女名'
密码='密码'
手机号码='手机号码'
cookie="""[
{
    "domain": ".zhihu.com",
    "expirationDate": 1611991243.574701,
    "hostOnly": false,
    "httpOnly": false,
    "name": "_xsrf",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "QOuaWlGAt2EGUPlhmMnsWIUiH8PP2xNn",
    "id": 1
},
{
    "domain": ".zhihu.com",
    "expirationDate": 1597303667.508257,
    "hostOnly": false,
    "httpOnly": false,
    "name": "_zap",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "7a60aba6-3437-4f4a-82b1-5d4473dce932",
    "id": 2
},
{
    "domain": ".zhihu.com",
    "expirationDate": 1536823672.910257,
    "hostOnly": false,
    "httpOnly": true,
    "name": "capsion_ticket",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "\"2|1:0|10:1534231722|14:capsion_ticket|44:OWE4Mzg1NzQ1OGM5NDZjYTk4ZGM4YjYzMzY2NzlmMzE=|55eeab68823158d4e7025b16b116dbfa533e7d70dbde0138d657128687c4dc30\"",
    "id": 3
},
{
    "domain": ".zhihu.com",
    "expirationDate": 1628839672.758257,
    "hostOnly": false,
    "httpOnly": false,
    "name": "d_c0",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "\"ACCn1znpDQ6PTn4-SwQ1yEJi2IUUmW3t9zU=|1534231722\"",
    "id": 4
},
{
    "domain": ".zhihu.com",
    "expirationDate": 1628839672.757257,
    "hostOnly": false,
    "httpOnly": false,
    "name": "q_c1",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "1e9475f36ced423ebdda0c449e7df724|1534231722000|1534231722000",
    "id": 5
},
{
    "domain": ".zhihu.com",
    "expirationDate": 1549783814.484146,
    "hostOnly": false,
    "httpOnly": true,
    "name": "z_c0",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "\"2|1:0|10:1534231864|4:z_c0|92:Mi4xdFFhWUN3QUFBQUFBSUtmWE9la05EaVlBQUFCZ0FsVk5PTk5mWEFCbmRjbzJMNTRxOTBYTE91SFltU2NtbGlOcjNn|2c764323cd7ff4455f4b882eba8317ba202f3084f947697f769fe7990a41056e\"",
    "id": 6
},
{
    "domain": "www.zhihu.com",
    "expirationDate": 1534232143.573701,
    "hostOnly": true,
    "httpOnly": false,
    "name": "tgw_l7_route",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "8605c5a961285724a313ad9c1bbbc186",
    "id": 7
}
]
"""


db = pymysql.connect("localhost", "root", "", "影视发帖推广", charset="utf8")
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# SQL 插入语句
sql = """INSERT INTO `知乎帐号`(`帐号`, `密码`, `注册手机号`, `注册日期`, `cookie`) 
VALUES ("{}","{}","{}","{}","{}")""" .format(取女名,密码,手机号码,今天时间,cookie)#不换行 end=""

try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
    print('=保存数据库一知乎用户密码')
except:
    # 如果发生错误则回滚
    print('=====================数据库执行发生错误:===============')
    db.rollback()
# 关闭数据库连接
db.close()