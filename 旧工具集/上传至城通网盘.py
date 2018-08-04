
import webdav.client as wc


# 试,  cert="/path/to/your/certificate.pem" import webdav.client


def rg2():
    webdav = easywebdav.connect('https://pubdav.ctfile.com',
                                username='jiqi1136@163.com',
                                password='q962946',
                                protocol='https')
    # Do some stuff:
    print(webdav.ls())

def wef1():
    options= {
                'webdav_hostname': "https://pubdav.ctfile.com",
                'webdav_login':    "jiqi1136@163.com",
                'webdav_password': "q962946"
                }
    client =wc.Client(options)
    #检查资源的存在
    检查资源a=client.check("dir1/file1")
    检查资源b=client.check("dir1")



    #获取资源列表
    资源列表 = client.list()

    #创建一个目录
    #client.mkdir("d")

    #print('进入列表',client.cd('/'))
    print(检查资源a)
    print('资源列表',资源列表)


wef1()