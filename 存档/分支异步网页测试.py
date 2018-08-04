import asyncio
from aiohttp import ClientSession
import requests
import time



class 类_分支异步网页: #调用 类的模具 self.模具_数据库()
    def __init__(self):
        开始时间计数 = int(time.time())
        self.模具_分支异步调度三()



        结束时间计数 = int(time.time())
        用时 = 结束时间计数 - 开始时间计数
        取整除分数 = int(用时) // 60
        除的余数的秒数 = int(用时) % 60
        print('用时计数:', 取整除分数, '分:', 除的余数的秒数, '秒')

    


    async def 模具_分支异步打开网页(self): #定义(def)一个分支异步模具(async)
        async with ClientSession() as 会话:  #aiohttp 的ClientSession 库
            async with 会话.get(self.网址) as 返回网页内容:
                #等待返回网页内容后,再return 返回模具的数据
                返回网页内容=await 返回网页内容.text()
                #self.网页内容列表.append(返回网页内容)
                网页内容网址组=[]
                网页内容网址组.append(返回网页内容)
                网页内容网址组.append(self.网址)

                self.网页内容网址组列表.append(网页内容网址组)

    async def 模具_分支异步打开网页三(self): #定义(def)一个分支异步模具(async)
        async with ClientSession() as 会话:  #aiohttp 的ClientSession 库
            async with 会话.get(self.网址) as 返回网页内容:
                #等待返回网页内容后,再return 返回模具的数据
                目录与种子名 = r'C:\下载中转站\07月新番[MP4].torrent'
                with open(目录与种子名, 'wb') as fd:
                #self.网页内容列表.append(返回网页内容)
                    while True:
                        chunk =await 返回网页内容.content.read()
                        if not chunk:
                            break
                        fd.write(chunk)

    def 模具_分支异步调度三(self):
        网址组 = []


        网址 = "http://91btbtt.com/attach-download-fid-981-aid-4482768.htm"  # {} 初始网址
        网址组.append(网址)

        sem = asyncio.Semaphore(4)  # 设置Semaphore为4,说明在抓取时最多并发发出4个请求
        # 下面三行语句代码完成的功能就是启动事件循环机制,生成待运行的诸协程,然后调度运行
        loop = asyncio.get_event_loop()
        任务列表 = []  # 设置任务为一个列表

        for self.网址 in 网址组:  # 遍历页数

            # 用format替换初始网址产生页数网址,将要代入hello模具,从而包装成一个任务
            任务 = asyncio.ensure_future(self.模具_分支异步打开网页三())
            任务列表.append(任务)  # 每个任务都加入列表

        loop.run_until_complete(asyncio.wait(任务列表))



    def 模具_分支异步调度二(self):

        网址 = "http://91btbtt.com/forum-index-fid-951-page-{}.htm"  #  {} 初始网址
        self.网页内容网址组列表=[]
        sem = asyncio.Semaphore(4)   #设置Semaphore为4,说明在抓取时最多并发发出4个请求
        # 下面三行语句代码完成的功能就是启动事件循环机制,生成待运行的诸协程,然后调度运行
        loop = asyncio.get_event_loop()
        任务列表 = []  # 设置任务为一个列表

        for 数字遍历 in range(5,10,1):  # 遍历页数
            self.网址=网址.format(数字遍历)
            # 用format替换初始网址产生页数网址,将要代入hello模具,从而包装成一个任务
            任务 = asyncio.ensure_future(self.模具_分支异步打开网页())
            任务列表.append(任务)  # 每个任务都加入列表

        loop.run_until_complete(asyncio.wait(任务列表))
        """等待上面的任务列表完成"""
        for 网页内容网址组 in self.网页内容网址组列表:

            返回网页内容=网页内容网址组[0]
            网址=网页内容网址组[1]
            print('返回网页内容:', 返回网页内容)
            print('网址:', 网址)
            print('==================:')

    def 模具_分支异步调度(self):
        async def 模具_分支异步打开网页(网址,网页内容网址组列表):  # 定义(def)一个分支异步模具(async)
            async with ClientSession() as 会话:  # aiohttp 的ClientSession 库
                async with 会话.get(网址) as 返回网页内容:
                    # 等待返回网页内容后,再return 返回模具的数据
                    返回网页内容 = await 返回网页内容.text()
                    # self.网页内容列表.append(返回网页内容)
                    网页内容网址组 = []
                    网页内容网址组.append(返回网页内容)
                    网页内容网址组.append(网址)
                    网页内容网址组列表A=网页内容网址组列表
                    网页内容网址组列表A.append(网页内容网址组)
                    return 网页内容网址组列表A #返回

        网址 = "http://91btbtt.com/forum-index-fid-951-page-{}.htm"  #  {} 初始网址

        sem = asyncio.Semaphore(4)   #设置Semaphore为4,说明在抓取时最多并发发出4个请求
        # 下面三行语句代码完成的功能就是启动事件循环机制,生成待运行的诸协程,然后调度运行
        loop = asyncio.get_event_loop()
        任务列表 = []  # 设置任务为一个列表
        网页内容网址组列表= []
        网页内容网址组列表 = []

        for 数字遍历 in range(5,10,1):  # 遍历页数
            网址=网址.format(数字遍历)
            网页内容网址组列表 = 模具_分支异步打开网页(网址, 网页内容网址组列表)
            # 用format替换初始网址产生页数网址,将要代入hello模具,从而包装成一个任务
            任务 = asyncio.ensure_future(网页内容网址组列表)
            任务列表.append(任务)  # 每个任务都加入列表

        loop.run_until_complete(asyncio.wait(任务列表))
        """等待上面的任务列表完成"""
        for 网页内容网址组 in 网页内容网址组列表:

            返回网页内容=网页内容网址组[0]
            网址=网页内容网址组[1]
            print('返回网页内容:', 返回网页内容)
            print('网址:', 网址)
            print('==================:')



类=类_分支异步网页()