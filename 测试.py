from selenium import webdriver  # 浏览的驱动
import time  # 时间



option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
driver = webdriver.Chrome(chrome_options=option)
driver.get("http://3e38.com/image/login.php?gotopage=%2Fimage%2Findex.php")
# 参数是像素点宽,高
driver.set_window_size(800, 800)
# driver.maximize_window() 浏览器全屏显示,不带参数
time.sleep(1)
driver.implicitly_wait(20)  # 设置 隐式等待.单位是秒(s),
driver.find_element_by_name("userid").clear()  # 请空输入框
print('请空输入框：')
driver.find_element_by_xpath("//*[@id=\"login-box\"]/div[2]/form/dl/dd[1]/input").send_keys("2")  # 定位用户名  d38min
driver.find_element_by_xpath('//*[@id="login-box"]/div[2]/form/dl/dd[2]/input').send_keys("qq962962")  # 定位密码
print('输入验证码')