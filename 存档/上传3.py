import easywebdav

webdav = easywebdav.connect(
    host='https://pubdav.ctfile.com',
    username='jiqi1136@163.com',
    port=443,
    protocol="https",
    password='q962946')

_file = "test.py"

#print webdav.cd("/dav/")
# print webdav._get_url("")
print (webdav.ls())
# print webdav.exists("/dav/test.py")
# print webdav.exists("ECS.zip")
# print webdav.download(_file, "./"+_file)
#print webdav.upload("./test.py", "test.py")