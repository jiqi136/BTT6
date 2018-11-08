
# -*- coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  # ActionChains鼠标操作类
from selenium.webdriver.common.keys import Keys  # keys类操作
"""基本用法"""

# 打开浏览器：
browser = webdriver.Chrome()

# # 若未配置环境变量：
# path = r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
# browser = webdriver.Chrome(executable_path = path)

# 在指定时间范围等待：
browser.implicitly_wait(30)

# 设置超时
browser.set_page_load_timeout(30)
browser.set_script_timeout(30)

# 打开url:
browser.get(r"http://www.你的网站.com")

# 前进/后退
browser.forward()
browser.back()

# 刷新
browser.refresh()

# 将浏览器最大化
browser.maximize_window()

# 将设置浏览器为宽480，高800显示'
browser.set_window_size(480, 800)

# 关闭浏览器
browser.quit()

# 关闭标签
browser.close()

'''
获取浏览器窗口相关信息
browser.title # 当前页面标题
browser.name # 浏览器名
browser.current_url # 返回当前页面url
browser.window_handles # 返回当前浏览器的所有窗口
browser.current_window_handle # 返回当前浏览器的窗口句柄
'''

# 跳转到其他标签页
window = browser.window_handles
browser.switch_to_window(window[1])

# 选择窗口
browser.switch_to_window('window_name')

# 截取当前显示的页面并保存
browser.get_screenshot_as_file(r'd:\backup\140591\桌面\首页图片\test.png')


# 定位元素
# 需要先分析源码
text_username = browser.find_element_by_name('username')
text_password = browser.find_element_by_name('password')
form_login = browser.find_element_by_name('formlogin')
# 也可以使用其他方法如xpath，注意转义符
text_username = browser.find_element_by_xpath('//input[@name = \'username\']')
'''
所有相关方法：
find_element(by='id', value=None)
find_element_by_class_name(name)
find_element_by_css_selector(css_selector)
find_element_by_id(id)
find_element_by_link_text(link_text)
find_element_by_name(name)
find_element_by_partial_link_text(link_text)
find_element_by_tag_name(name)
find_element_by_xpath(xpath)
element后加s则返回一组对象
'''

# -----------------------WebElement相关-----------------------

# 输入值
# send_keys也可以用于上传文件：send_keys('d:/abc.txt')
text_username.send_keys("你的用户名_错误")
text_password.send_keys("你的密码")

# 清空输入框，换成正确的用户名
text_username.clear()
text_username.send_keys("你的用户名_正确")

# 提交表单
form_login.submit()

'''
相关方法
clear()  # 清除元素的内容
send_keys()  # 在元素上模拟按键输入
click()  # 单击元素
submit()  # 提交表单
size()  # 返回元素的尺寸
text()  # 获取元素的文本
get_attribute(name)  # 获得属性值
is_displayed()  # 设置该元素是否用户可见
'''

# -------------------alert/confirm/prompt对话框处理-------------------

'''
switch_to_alert()   # 用于获取网页上的警告信息。
text   # 返回 alert/confirm/prompt 中的文字信息。
accept()   # 点击确认按钮。
dismiss()   # 点击取消按钮，如果有的话。
send_keys()   # 输入值，这个alert\confirm没有对话框就不能用了，不然会报错。
'''

# -----------------------下拉框处理-----------------------
# 二次定位
# driver.find_element_by_xx('xx').find_element_by_xx('xx').click()

# 先定位到下拉框 m= driver.find_element_by_id("ShippingMethod")
# 再点击下拉框下的选项
m.find_element_by_xpath("//option[@value='10.69']").click()

# -----------------------cookie处理-----------------------
'''
get_cookies()   # 获得所有cookie信息
get_cookie(name)   # 返回特定name 有cookie信息 
add_cookie(cookie_dict)   # 添加cookie，必须有name 和value 值
delete_cookie(name)   # 删除特定(部分)的cookie信息
delete_all_cookies()   # 删除所有cookie信息
'''

# -----------------------文件上传-----------------------
# 定位上传按钮，添加本地文件
# driver.find_element_by_xx('xx').send_keys('d:/abc.txt')
driver.find_element_by_name("file").send_keys('D:\\selenium_use_case\upload_file.txt')

# -----------------------文件下载-----------------------
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", os.getcwd())
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

browser = webdriver.Firefox(firefox_profile=fp)
browser.get("http://pypi.python.org/pypi/selenium")
browser.find_element_by_partial_link_text("selenium-2").click()

# -----------------------Keys类键盘操作-----------------------
from selenium.webdriver.common.keys import Keys

# element.send_keys(...)，下同
'''
send_keys(Keys.BACK_SPACE) # 返回键
send_keys(Keys.BACK_SPACE) 删除键（BackSpace）
send_keys(Keys.SPACE)  空格键(Space)
send_keys(Keys.TAB)  制表键(Tab)
send_keys(Keys.ESCAPE)  回退键（Esc）
send_keys(Keys.ENTER) 回车键（Enter）
send_keys(Keys.CONTROL,'a') 全选（Ctrl+A）
send_keys(Keys.CONTROL,'c') 复制（Ctrl+C）
send_keys(Keys.CONTROL,'x') 剪切（Ctrl+X）
send_keys(Keys.CONTROL,'v') 粘贴（Ctrl+V）
'''

# ----------------ActionChains类鼠标操作--------------------
from selenium.webdriver.common.action_chains import ActionChains

# 右键单击
ActionChains(browser).context_click(text_username).perform()
# 双击
ActionChains(browser).double_click(text_username).perform()
# 执行元素的移动操作
ActionChains(browser).drag_and_drop(text_username, text_password).perform()

'''
ActionChains 类鼠标操作的常用方法：
context_click()   # 右击
double_click()   # 双击
drag_and_drop()   # 拖动
move_to_element()   # 鼠标悬停在一个元素上
click_and_hold()   # 按下鼠标左键在一个元素上
'''

# -----------执行JavaScript脚本 --------------
js = "var q=document.getElementById(\"user_name\");q.style.border=\"1px solid red\";"
# 调用js
browser.execute_script(js)

# eg:
# 将页面滚动条拖到底部
js = "var q=document.documentElement.scrollTop=10000"
browser.execute_script(js)

# 隐藏文字信息
driver.execute_script('$("#tooltip").fadeOut();')

# 隐藏按钮：
button = driver.find_element_by_class_name('btn')
driver.execute_script('$(arguments[0]).fadeOut()', button)

