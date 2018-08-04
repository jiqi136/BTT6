import time#导入时间
# -*- coding: UTF-8 -*-

import random# 导入随机

import datetime#导入时间
import pymysql #mysql数据库
import requests  # 导入浏览器
import re
import os
from selenium import webdriver# 浏览的驱动


class 类_注册微软hotmail邮箱:

    def 随机帐号与百家姓(self):
        随机帐号 = []
        for 字符 in range(10):
            字符 = random.choice('qwerrtyyuiiopasdfghjklzxcvbnm')
            随机帐号.append(字符)
        规则 = r"[\[\',\] ]{1}"
        self.随机帐号 = re.sub(规则, "", str(随机帐号))

        self.百家姓 = random.choice("""李王张刘陈杨黄周吴徐孙胡朱高林何郭马罗梁宋郑谢韩唐冯于董萧程曹袁邓许傅沈曾彭吕苏卢蒋蔡贾丁魏薛叶阎余潘杜戴夏钟汪田任姜范方石姚谭廖邹熊金陆郝孔白崔康毛邱秦史顾侯邵孟龙万段漕钱汤尹黎易常武乔贺赖龚文庞樊兰殷施陶洪翟安颜倪严牛温芦季俞章鲁葛伍韦申尤毕聂丛焦向柳邢路岳齐沿梅莫庄辛管祝左涂谷祁时舒耿牟卜
            路詹关苗凌费纪靳盛童欧甄项曲成游阳裴席卫查屈鲍位覃霍翁隋植甘景薄单包司柏宁柯阮桂闵欧阳解强柴华车冉房边辜吉饶刁瞿戚丘古米池滕晋苑邬臧畅宫来嵺苟全褚廉简娄盖符奚木穆燕郎邸冀谈姬屠连郜晏栾郁商蒙计喻揭窦迟宇敖糜鄢冷卓花仇艾蓝都巩稽井练仲乐虞卞封竺冼原官衣楚佟栗匡宗应台巫鞠僧桑荆谌银扬明沙薄伏岑胥保和蔺""")
        if len(self.百家姓) == 0:
            self.百家姓 = random.choice("""李王张刘陈杨黄周吴徐孙胡朱高林何郭马罗梁宋郑谢韩唐冯于董萧程曹袁邓许傅沈曾彭吕苏卢蒋蔡贾丁魏薛叶阎余潘杜戴夏钟汪田任姜范方石姚谭廖邹熊金陆郝孔白崔康毛邱秦史顾侯邵孟龙万段漕钱汤尹黎易常武乔贺赖龚文庞樊兰殷施陶洪翟安颜倪严牛温芦季俞章鲁葛伍韦申尤毕聂丛焦向柳邢路岳齐沿梅莫庄辛管祝左涂谷祁时舒耿牟卜
                    路詹关苗凌费纪靳盛童欧甄项曲成游阳裴席卫查屈鲍位覃霍翁隋植甘景薄单包司柏宁柯阮桂闵欧阳解强柴华车冉房边辜吉饶刁瞿戚丘古米池滕晋苑邬臧畅宫来嵺苟全褚廉简娄盖符奚木穆燕郎邸冀谈姬屠连郜晏栾郁商蒙计喻揭窦迟宇敖糜鄢冷卓花仇艾蓝都巩稽井练仲乐虞卞封竺冼原官衣楚佟栗匡宗应台巫鞠僧桑荆谌银扬明沙薄伏岑胥保和蔺""")

        名1 = random.choice("""李王张刘陈杨黄周吴徐孙胡朱高林何郭马罗梁宋郑谢韩唐冯于董萧程曹袁邓许傅沈曾彭吕苏卢蒋蔡贾丁魏薛叶阎余潘杜戴夏钟汪田任姜范方石姚谭廖邹熊金陆郝孔白崔康毛邱秦史顾侯邵孟龙万段漕钱汤尹黎易常武乔贺赖龚文庞樊兰殷施陶洪翟安颜倪严牛温芦季俞章鲁葛伍韦申尤毕聂丛焦向柳邢路岳齐沿梅莫庄辛管祝左涂谷祁时舒耿牟卜路詹
            关苗凌费纪靳盛童欧甄项曲成游阳裴席卫查屈鲍位覃霍翁隋植甘景薄单包司柏宁柯阮桂闵欧阳解强柴华车冉房边辜吉饶刁瞿戚丘古米池滕晋苑邬臧畅宫来嵺苟全褚廉简娄盖符奚木穆燕郎邸冀谈姬屠连郜晏栾郁商蒙计喻揭窦迟宇敖糜鄢冷卓花仇艾蓝都巩稽井练仲乐虞卞封竺冼原官衣楚佟栗匡宗应台巫鞠僧桑荆谌银扬明沙薄伏岑胥保和蔺""")
        if len(名1) == 0:
            名1 = random.choice("""李王张刘陈杨黄周吴徐孙胡朱高林何郭马罗梁宋郑谢韩唐冯于董萧程曹袁邓许傅沈曾彭吕苏卢蒋蔡贾丁魏薛叶阎余潘杜戴夏钟汪田任姜范方石姚谭廖邹熊金陆郝孔白崔康毛邱秦史顾侯邵孟龙万段漕钱汤尹黎易常武乔贺赖龚文庞樊兰殷施陶洪翟安颜倪严牛温芦季俞章鲁葛伍韦申尤毕聂丛焦向柳邢路岳齐沿梅莫庄辛管祝左涂谷祁时舒耿牟卜路詹
                    关苗凌费纪靳盛童欧甄项曲成游阳裴席卫查屈鲍位覃霍翁隋植甘景薄单包司柏宁柯阮桂闵欧阳解强柴华车冉房边辜吉饶刁瞿戚丘古米池滕晋苑邬臧畅宫来嵺苟全褚廉简娄盖符奚木穆燕郎邸冀谈姬屠连郜晏栾郁商蒙计喻揭窦迟宇敖糜鄢冷卓花仇艾蓝都巩稽井练仲乐虞卞封竺冼原官衣楚佟栗匡宗应台巫鞠僧桑荆谌银扬明沙薄伏岑胥保和蔺""")
        名2 = random.choice("""李王张刘陈杨黄周吴徐孙胡朱高林何郭马罗梁宋郑谢韩唐冯于董萧程曹袁邓许傅沈曾彭吕苏卢蒋蔡贾丁魏薛叶阎余潘杜戴夏钟汪田任姜范方石姚谭廖邹熊金陆郝孔白崔康毛邱秦史顾侯邵孟龙万段漕钱汤尹黎易常武乔贺赖龚文庞樊兰殷施陶洪翟安颜倪严牛温芦季俞章鲁葛伍韦申尤毕聂丛焦向柳邢路岳齐沿梅莫庄辛管祝左涂谷祁时舒耿牟卜路詹
            关苗凌费纪靳盛童欧甄项曲成游阳裴席卫查屈鲍位覃霍翁隋植甘景薄单包司柏宁柯阮桂闵欧阳解强柴华车冉房边辜吉饶刁瞿戚丘古米池滕晋苑邬臧畅宫来嵺苟全褚廉简娄盖符奚木穆燕郎邸冀谈姬屠连郜晏栾郁商蒙计喻揭窦迟宇敖糜鄢冷卓花仇艾蓝都巩稽井练仲乐虞卞封竺冼原官衣楚佟栗匡宗应台巫鞠僧桑荆谌银扬明沙薄伏岑胥保和蔺""")
        if len(名2) == 0:
            名2 = random.choice("""李王张刘陈杨黄周吴徐孙胡朱高林何郭马罗梁宋郑谢韩唐冯于董萧程曹袁邓许傅沈曾彭吕苏卢蒋蔡贾丁魏薛叶阎余潘杜戴夏钟汪田任姜范方石姚谭廖邹熊金陆郝孔白崔康毛邱秦史顾侯邵孟龙万段漕钱汤尹黎易常武乔贺赖龚文庞樊兰殷施陶洪翟安颜倪严牛温芦季俞章鲁葛伍韦申尤毕聂丛焦向柳邢路岳齐沿梅莫庄辛管祝左涂谷祁时舒耿牟卜路詹
                    关苗凌费纪靳盛童欧甄项曲成游阳裴席卫查屈鲍位覃霍翁隋植甘景薄单包司柏宁柯阮桂闵欧阳解强柴华车冉房边辜吉饶刁瞿戚丘古米池滕晋苑邬臧畅宫来嵺苟全褚廉简娄盖符奚木穆燕郎邸冀谈姬屠连郜晏栾郁商蒙计喻揭窦迟宇敖糜鄢冷卓花仇艾蓝都巩稽井练仲乐虞卞封竺冼原官衣楚佟栗匡宗应台巫鞠僧桑荆谌银扬明沙薄伏岑胥保和蔺""")

        self.百家名=名1 + 名2

        self.年 = random.randrange(2, 36)
        self.月 = random.randrange(1, 13)
        self.日 = random.randrange(1, 30)
        self.密码数字= random.randrange(100000,1000000)
    def 模具_换头部信息(self):  # 头部信息 def 函数模具内通行变量
        #nonlocal 头部信息  # def 函数模具内通行变量


        # {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'}  被BT网站墙了
        self.头部信息 = random.choice([{'User-Agent': 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'},
                              {
                                  'User-Agent': 'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},
                              {
                                  'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.9Safari/536.5'},
                              {
                                  'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.9Safari/536.5'},
                              {
                                  'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/535.24(KHTML,likeGecko)Chrome/19.0.1055.1Safari/535.24'},
                              {
                                  'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/535.24(KHTML,likeGecko)Chrome/19.0.1055.1Safari/535.24'},
                              {
                                  'User-Agent': 'Mozilla/5.0(X11;CrOSi6862268.111.0)AppleWebKit/536.11(KHTML,likeGecko)Chrome/20.0.1132.57Safari/536.11'},
                              {
                                  'User-Agent': 'Mozilla/5.0(X11;CrOSi6862268.111.0)AppleWebKit/536.11(KHTML,likeGecko)Chrome/20.0.1132.57Safari/536.11'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2;WOW64)AppleWebKit/537.1(KHTML,likeGecko)Chrome/19.77.34.5Safari/537.1'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2;WOW64)AppleWebKit/537.1(KHTML,likeGecko)Chrome/19.77.34.5Safari/537.1'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2;WOW64)AppleWebKit/535.24(KHTML,likeGecko)Chrome/19.0.1055.1Safari/535.24'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.6(KHTML,likeGecko)Chrome/20.0.1090.0Safari/536.6'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.6(KHTML,likeGecko)Chrome/20.0.1090.0Safari/536.6'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1062.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1062.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.1(KHTML,likeGecko)Chrome/22.0.1207.1Safari/537.1'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.1(KHTML,likeGecko)Chrome/22.0.1207.1Safari/537.1'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.6(KHTML,likeGecko)Chrome/20.0.1092.0Safari/536.6'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.6(KHTML,likeGecko)Chrome/20.0.1092.0Safari/536.6'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1063.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1063.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1062.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1062.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.1)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.0)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.36Safari/536.5'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT6.0)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.36Safari/536.5'},
                              {
                                  'User-Agent': 'Mozilla/5.0(WindowsNT5.1)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1063.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(Macintosh;IntelMacOSX10_8_0)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1063.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0(Macintosh;IntelMacOSX10_8_0)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1063.0Safari/536.3'},
                              {
                                  'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
                              {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
                              {
                                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko'},
                              {
                                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'},
                              {
                                  'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
                              {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'},
                              {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'},
                              {
                                  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},
                              {
                                  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
                              {
                                  'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)'},
                              {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)'},
                              {
                                  'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)'},
                              {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)'},
                              {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)'},
                              {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'},
                              {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'},
                              {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'}])

        self.头部信息 = str(self.头部信息).replace("{", "\"")
        self.头部信息 = str(self.头部信息).replace("}", "\"")
        print(self.头部信息)
    def 模具_插入微软hotmail邮箱数据库(self):
        # 连接数据库
        # 连接数据库
        print('连接数据库....')
        db = pymysql.connect("localhost", "root", "","帐号", charset="utf8")
        cursor = db.cursor()
        # SQL 查询语句   已下载内容网址

        # 获取游标
        sql = """INSERT INTO 微软邮箱帐号(帐号,邮箱帐号,密码,姓名,注册日期)
                   VALUES ('%s','%s','%s','%s','%s')""" % (self.随机帐号,self.邮箱帐号,self.密码,self.姓名,self.今天时间)
        # 执行SQL语句
        cursor.execute(sql)

        # 提交到数据库执行
        db.commit()
        # 关闭数据库连接
        db.close()
    def 模具_换ip连接(self):
        # coding:gbk
        print('宽带连接进行时.....')
        os.system(r"rasphone -h 宽带连接")  # xxx0是你的拨号名称，xp下默认是“宽带连接”。
        os.system(r"rasdial 宽带连接 02007044432@163.gd  77341859")  # xxx0同上，xxx1 拨号用户名 ，xxx2拨号密码。
        time.sleep(3)

    def 模具_浏览器清除缓存(self):
        # 浏览器清除缓存
        self.driver.get("chrome://settings/privacy")

        input("\n按下 确认键enter 键后继续.")

        # self.driver.find_element_by_xpath('//*[@id="iSignupAction"]').click()  # 定位 验证码 的下一步
        print('保存帐号信息')
        self.今天时间 = str(time.strftime("%y-%m-%d", time.localtime()))
        self.邮箱帐号 = self.随机帐号 + '@hotmail.com'
        self.模具_插入微软hotmail邮箱数据库()

        self.driver.implicitly_wait(30)  # 设置  隐式等待（s）


    def 模具_浏览器输入验证码(self):


        var = 1
        while var == 1:  # 表达式永远为 true的无限循环
            self.模具_换头部信息()

            option = webdriver.ChromeOptions()
            # 设置中文
            option.add_argument('lang=zh_CN.UTF-8')
            # 更换头部
            option.add_argument(self.头部信息)
            self.driver = webdriver.Chrome(chrome_options=option)

            # 参数是像素点宽，高
            self.driver.set_window_size(800, 800)
            # self.driver.maximize_window() 浏览器全屏显示，不带参数

            self.随机帐号与百家姓()
            self.driver.get("https://signup.live.com/signup?wa=wsignin1.0&rpsnv=13&ct=1518546784&rver=6.7.6640.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fRpsCsrfState%3dda2d5cac-2e4d-1dbe-0edf-6a43f7c5882c&id=292841&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&contextid=F2F6FA1B0EE66A8B&bk=1518546785&uiflavor=web&uaid=6a16989e858246d8b20565cb1930ba41&mkt=ZH-CN&lc=2052&lic=1")




            self.driver.implicitly_wait(20)  # 设置 隐式等待.单位是秒（s）

            页面标题 = self.driver.title  # 获取title页面标题


            print('页面标题:',页面标题)
            if '帐户' not in 页面标题:
                # 关闭新窗口

                self.driver.close()

            self.driver.find_element_by_xpath('//*[@id="domainLabel"]').click()  # 定位确认 邮箱类型
            time.sleep(1)  # 等待
            self.driver.find_element_by_xpath('//*[@id="domain1"]').click()  # 定位确认 选择 hotmail
            self.密码="qq{}Q%".format(self.密码数字)
            print('密码..........',self.密码)



            self.driver.find_element_by_xpath('//*[@id="MemberName"]').send_keys(self.随机帐号)  # 定位用户名
            self.driver.find_element_by_xpath('//*[@id="Password"]').send_keys(self.密码)  # 定位密码

            self.driver.find_element_by_xpath('//*[@id="iOptinEmail"]').click()  # 定位确认不接收广告邮件
            self.driver.find_element_by_xpath('//*[@id="iSignupAction"]').click()  # 定位确认 下一步
            print('输入姓名......')
            time.sleep(2)  # 等待
            self.driver.implicitly_wait(20)  # 设置 隐式等待.单位是秒（s）

            self.driver.find_element_by_xpath('//*[@id="LastName"]').send_keys(self.百家姓)  # 定位 姓
            self.driver.find_element_by_xpath('//*[@id="FirstName"]').send_keys(self.百家名)  # 定位 姓
            self.driver.find_element_by_xpath('//*[@id="iSignupAction"]').click()  # 定位确认 下一步
            print('邮箱帐号......',self.随机帐号)
            self.姓名=self.百家姓+self.百家名
            print('姓名..........',self.姓名)

            print('选择地区与日期')
            time.sleep(1)  # 等待
            self.driver.implicitly_wait(20)  # 设置  隐式等待（s）,


            self.driver.find_element_by_xpath('//*[@id="BirthYear"]').click()  # 定位 年
            time.sleep(1)  # 等待
            self.driver.find_element_by_xpath('//*[@id="BirthYear"]/option[{}]'.format(self.年)).click()  # 定位 年

            self.driver.find_element_by_xpath('//*[@id="BirthMonth"]').click()  # 定位月
            time.sleep(1)  # 等待
            self.driver.find_element_by_xpath('//*[@id="BirthMonth"]/option[{}]'.format(self.月)).click()  # 定位月

            self.driver.find_element_by_xpath('//*[@id="BirthDay"]').click()  # 定位日
            time.sleep(1)  # 等待
            self.driver.find_element_by_xpath('//*[@id="BirthDay"]/option[{}]'.format(self.日)).click()  # 定位日

            self.driver.find_element_by_xpath('//*[@id="iSignupAction"]').click()  # 定位下一步


            time.sleep(2)  # 等待

            #self.driver.implicitly_wait(20)  # 设置  隐式等待（s）,
            #self.driver.find_element_by_xpath('//*[@id="wlspispSolutionElementcbd03216798445bf9e42f7f41b50cf1f"]').click()  # 定位验证码
            print('输入验证码.')
            time.sleep(5)  # 等待
            input("\n按下 确认键enter 键后继续.")
            #self.driver.find_element_by_xpath('//*[@id="iSignupAction"]').click()  # 定位 验证码 的下一步
            print('保存帐号信息')
            self.今天时间 = str(time.strftime("%y-%m-%d", time.localtime()))
            self.邮箱帐号 = self.随机帐号 + '@hotmail.com'
            self.模具_插入微软hotmail邮箱数据库()



            self.driver.implicitly_wait(30)  # 设置  隐式等待（s）

            print('选择项卡')

            self.driver.find_element_by_xpath('/html/body/section/div/div[2]/section/button/i').click()  # 定位 滑动方向
            self.driver.implicitly_wait(2)  # 设置  隐式等待（s）
            self.driver.find_element_by_xpath('/html/body/section/div/div[2]/section/button[2]/i').click()  # 定位 滑动方向
            self.driver.implicitly_wait(2)  # 设置  隐式等待（s）
            self.driver.find_element_by_xpath('/html/body/section/div/div[2]/section/button[2]/i').click()  # 定位 滑动方向
            self.driver.implicitly_wait(2)  # 设置  隐式等待（s）
            self.driver.find_element_by_xpath('/html/body/section/div/div[2]/section/button[2]/i').click()  # 定位 滑动方向
            self.driver.implicitly_wait(60)  # 设置  隐式等待（s）


            print('全部就绪')
            self.driver.find_element_by_xpath('/html/body/section/div/div[2]/section/section/section/div/button').click()  # 定位 开始吧
            time.sleep(10)  # 等待
            print('登录成功，保存帐号信息')

            input("\n按下 确认键enter 键后继续.")
            print('准备重启')

            self.模具_换ip连接()

            print('退出')
            self.driver.quit()

            time.sleep(3)  # 等待







a = 类_注册微软hotmail邮箱()

#a.模具_浏览器输入验证码()
a.模具_浏览器输入验证码()