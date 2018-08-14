import pyautogui
import time

for i in  '54321':
    print('倒数',i,'分钟')
    time.sleep(60)  # 等待

pyautogui.alert('5分钟时间已到')


print("继续，倒数1分钟")

time.sleep(60)# 等待

pyautogui.alert('1分时间已到')

time.sleep(5)# 等待




