"""============短信平台================"""

def 模具一一易码短信平台账户信息():
    通信令牌token = '00285014c8a4ce850ee48bcfdd205a14751a49ed'

    令牌网址 = 'http://api.fxhyd.cn/UserInterface.aspx?action=getaccountinfo&token={}'.format(通信令牌token)  # 不换行 end=""

    网址内容 = 模具一一打开的网址请求返回网页内容(令牌网址)
    账户信息 = 网址内容.text.replace("success|", "")  # 替换   , 1) 次数 1
    文本列表 = 账户信息.split("|")
    print('用户名:', 文本列表[0])
    print('账户状态:', 文本列表[1])
    print('账户等级:', 文本列表[2])
    print('账户余额:', 文本列表[3])
    print('冻结金额:', 文本列表[4])
    print('账户折扣:', 文本列表[5])
    print('获取号码最大数量:', 文本列表[6])
    print('=========================')

def 模具一一获取接收的手机号码():
    通信令牌token = '00285014c8a4ce850ee48bcfdd205a14751a49ed'
    项目编号 = "891"
    排除号段 = ''
    获取手机号码接口网址 = "http://api.fxhyd.cn/UserInterface.aspx?action=getmobile&token={}&itemid={}&excludeno={}".format(
        通信令牌token, 项目编号, 排除号段)
    网址内容 = 模具一一打开的网址请求返回网页内容(获取手机号码接口网址)

    手机号码 = 网址内容.text.replace("success|", "")  # 替换   , 1) 次数 1
    print('手机号码:', 手机号码)

def 模具一一获取短信():

    pag.hotkey('altleft', 'tab')  # press()一次完整的击键.hotkey('ctrl','c'):热键函数 .keyDown()按下某个键.keyUp()松开某个键.


    通信令牌token = '00285014c8a4ce850ee48bcfdd205a14751a49ed'
    项目编号 = "891"

    获取短信网址 = "http://api.fxhyd.cn/UserInterface.aspx?action=getsms&token={}&itemid={}&mobile={}".format(
        通信令牌token,
        项目编号, 手机号码)
    """&release=1  自动释放号码标识符 若该参数值为1时,获取到短信的同时系统将自己释放该手机号码.若要继续使用该号码,请勿带入该参数."""


    条件循环 =0
    while 条件循环 < 3:  # 条件循环  break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
        短信内容 = ''

        for i in 'few52676t':
            print('等待 15秒:')
            time.sleep(14)  # 等待
            网址内容 = 模具一一打开的网址请求返回网页内容(获取短信网址)
            if 'success' in 网址内容.text:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
                短信内容 = 网址内容.text.replace("success|", "")  # 替换   , 1) 次数 1
                print('短信内容:', 短信内容)
                条件循环 = 998

                return#返回
            elif '3001' in 网址内容.text:  # 其它条件.
                print('短信尚未到达:3001,应继续调用取短信接口,直到超时为止.')

            else:  # 否则
                print('请求失败:', 网址内容.text)
        条件循环 =条件循环+1
        模具一一重新激活浏览器窗口()
        pag.PAUSE = 5  # 增加延迟
        pag.moveTo(740, 456)  # 鼠标移动X.Y 方位  发送验证码 按钮
        pag.rightClick()  # 右击pag.rightClick()
        开始计时数 = int(time.time())



    释放手机号码接口 = "http://api.fxhyd.cn/UserInterface.aspx?action=release&token={}&itemid={}&mobile={}".format(
        通信令牌token, 项目编号, 手机号码)
    释放手机号码网址内容 = 模具一一打开的网址请求返回网页内容(释放手机号码接口)


"""============旧模具================"""

def 模具一一手机模式访问并注册知乎():
    头部信息 = "user - agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_5 like Mac OS X) AppleWebKit/612.1.60(KHTML, like Gecko) CriOS/66.0.2524.75 Mobile/15E5239e Safari/612.1'"

    # url = "http://www.sunchateau.com/free/UA.htm"#  浏览器UA头部信息 在线查询
    url = "https://www.zhihu.com/signin?next=https://www.zhihu.com/"
    # 随机手机型号= random.choice(["iPhone 5","iPhone 6","iPhone 6 Plus","iPhone 7","iPhone 7 Plus","iPhone 8","iPhone 8 Plus","iPhone X"])

    随机手机型号 = random.choice(
        ["iPhone 5", "iPhone 6", "iPhone 6 Plus", "iPad Pro", "iPad"])

    随机手机型号 = "iPhone 6"
    print('随机手机型号', 随机手机型号)

    mobile_emulation = {"deviceName": 随机手机型号}  # 设置成手机模式
    options = Options()
    options = webdriver.ChromeOptions()  # 设置中文
    options.add_experimental_option("mobileEmulation", mobile_emulation)  # 更改 浏览头部信息为手机模式
    # options.add_argument(头部信息)

    # options.add_argument('disable-infobars')# 加启动配置 去除正在受到自动软件的控制
    # options.add_argument('headless')  # 静默模式

    # prefs = {"profile.managed_default_content_settings.images": 2}#配置不加载图片
    # options.add_experimental_option("prefs", prefs)#配置不加载图片

    操作 = webdriver.Chrome(chrome_options=options)  # 打开chrome浏览器
    # driver = webdriver.Chrome(chrome_options=options)

    # 模具一一获取接收的手机号码()
    # 手机号码='17131632268'

    操作.get(url)  # 访问网址

    time.sleep(1000)  # 等待

    time.sleep(5)  # 等待
    # 操作.find_element_by_xpath("//*[@id=\"address\"]").send_keys(Keys.CONTROL,'DELETE') # 键盘按击或输入  请空输入框:clear()
    # 操作.find_element_by_xpath("//*[@id=\"address\"]").click()# 光标 点击.click()
    # 操作.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/header/div/div/div/a[2]").click()  # 光标 点击.click()

    # 操作.find_element_by_name("username").send_keys(手机号码)  # 键盘按击或输入  请空输入框:clear()
    操作.find_element_by_xpath("//*[@id=\"root\"]/div/main/div/form/div[1]/div[1]/div[2]/div[1]/input").send_keys(
        手机号码)  # 键盘按击或输入  请空输入框:clear()
    time.sleep(1)  # 等待
    # 操作.find_element_by_class_name("CountingDownButton").click() # 光标 点击.click()

    定位 = 操作.find_element_by_xpath('//*[@id="root"]/div/main/div/form/div[1]/div[2]/button')  # 触摸事件 发送验证码 按扭
    TouchActions(操作).tap(定位).perform()
    time.sleep(1)  # 等待

    模具一一获取短信()
    模具一一知乎短信内容清洗()
    # 短信内容='623516'
    操作.find_element_by_name("digits").send_keys(短信内容)  # 键盘按击或输入  请空输入框:clear()
    time.sleep(1)  # 等待

    定位 = 操作.find_element_by_xpath('//*[@id="root"]/div/main/div/form/button')  # 触摸事件 登录 按扭
    TouchActions(操作).tap(定位).perform()

    time.sleep(5)  # 等待

    保存cookie = [item["name"] + ":" + item["value"] for item in 操作.get_cookies()]
    print('保存cookie:\n', 保存cookie)

    time.sleep(1000)  # 等待

    # 操作.quit()  # 关闭浏览器U

def 模具一一浏览器访问并注册知乎():
    模具一一换头部信息()

    头部信息 = str(头部信息).replace("'User-Agent':", "user-agent=")  # 替换   , 1) 次数 1
    头部信息 = 头部信息.replace("{", "")  # 替换   , 1) 次数 1
    头部信息 = 头部信息.replace("}", "")  # 替换   , 1) 次数 1
    后缀 = 'user-agent=Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'

    options = webdriver.ChromeOptions()  # 设置中文
    # options = Options()
    options.add_argument('disable-infobars')  # 加启动配置 去除正在受到自动软件的控制
    print('头部信息:', 头部信息)
    print('后缀:', 后缀)
    options.add_argument(后缀)

    浏览器操作 = webdriver.Chrome(chrome_options=options)  # 打开chrome浏览器

    url = "https://www.zhihu.com"  # 注册页面  https://www.zhihu.com/signup?next=%2Fexplore
    浏览器操作.get(url)
    time.sleep(500)  # 等待
