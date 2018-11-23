


import os

print('宽带连接进行时.....')
os.system(r"rasphone -h 宽带连接")  # xxx0是你的拨号名称,xp下默认是"宽带连接”.
os.system(r"rasdial 宽带连接 02007044432@163.gd  77341859")  # xxx0同上,xxx1 拨号用户名 ,xxx2拨号密码.

print('换ip再连接完成')


from_=30
to=300
length=400
showvalue=10
tickinterval=20
resolution=10