import requests #人类的 浏览器
import os #处理电脑系统文件和目录
import re
import random #随机数

from lxml import etree,html #解析与定位网页
import datetime  # 时间
import time #时间


# =====浏览器与IP公用模具==============
def 模具_网络异常等待60秒():
    print('网络异常等待')
    for 倒数 in range(60, 0, -10):
        print('倒数', 倒数, '秒')
        time.sleep(10)


def 模具_换头部信息():  # 头部信息 def 函数模具内通行变量
    # nonlocal 头部信息  # def 函数模具内通行变量
    global 头部信息  # def 函数模具内通行变量

    # {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'}  被BT网站墙了
    头部信息 = random.choice([{'User-Agent': 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'},
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
    print(头部信息)


def 模具_换ip连接():
    # coding:gbk
    print('宽带连接进行时.....')
    os.system(r"rasphone -h 宽带连接")  # xxx0是你的拨号名称，xp下默认是“宽带连接”。
    os.system(r"rasdial 宽带连接 02007044432@163.gd  77341859")  # xxx0同上，xxx1 拨号用户名 ，xxx2拨号密码。
    time.sleep(3)


def 模具_循环测试网页连接():
    循环 = 0
    while 循环 == 0:  # 条件循环
        模具_网络异常等待60秒()
        模具_换ip连接()
        try:
            a = requests.get('http://www.btbtt.net', headers=头部信息, timeout=10)
            time.sleep(1)  # 等待
            return  # 结束模具，返回空值‘nome’
        except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout,
                requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout):
            pass


# ======================================


def 模具_打开的网址请求返回网页内容(打开的网址):
    循环 = 0

    while 循环 == 0:  # 条件循环
        try:
            返回网页内容 = requests.post(打开的网址, headers=头部信息, timeout=10)
            return 返回网页内容
        except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout,
                requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout):
            模具_循环测试网页连接()

print("请输入下载图片的网址:")
网址=str(input())
print("请输入图片的帖子标题:")
图片下载目录=str(input())
模具_换头部信息()
返回网页内容 =模具_打开的网址请求返回网页内容(网址)
#网页 =(返回网页内容.text)
#print("网页:",网页 )
帖子内容html = etree.HTML(返回网页内容.text)
帖子内容html = html.fromstring(返回网页内容.text)
规则='/html/body/ol//text()'
规则 = str(规则).replace("/tbody","")
帖子标题列表 = 帖子内容html.xpath(规则)

图片下载地址列表 = 帖子内容html.xpath('//*[@id="main"]/div[3]/table/tr[1]/th[2]/table/tr/td/div[4]//img/@src')

print("图片下载地址列表:",图片下载地址列表)


规则= ".{1,}\["
图片下载目录 = 图片下载目录.strip('。')
保存目录路径='D:\\桌面\\下载\\目录\\'
图片下载目录 = str(保存目录路径).replace("目录",图片下载目录)
创建图片下载目录 = str(图片下载目录).strip('\\')


if not os.path.exists(创建图片下载目录):  # 必有条件选择，否则出错
    os.makedirs(创建图片下载目录)# makedirs 创建多级目录文件夹，mkdir创建一个文件夹
计数器=1
for 图片下载地址 in 图片下载地址列表:
    返回图片下载内容 =模具_打开的网址请求返回网页内容(图片下载地址)
    图片名=str(计数器)+'.jpg'
    目录与种子名 = str(图片下载目录) + str(图片名)
    with open(目录与种子名, 'wb') as fout:
        fout.write(返回图片下载内容.content)
        fout.close()
        print('完成下载', 图片名)

        计数器+= 1

print('完成下载全部图片，保存目录：',创建图片下载目录)







