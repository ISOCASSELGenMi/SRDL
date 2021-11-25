#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#用selenium做出實時網頁控制

from selenium import webdriver
print("請輸入網頁連結：")
test_url = input()
options = webdriver.ChromeOptions()
options.add_argument("--headless") # 不要開啟瀏覽器
options.add_argument("window-size=1920,1080") # 設定瀏覽器大小
driver = webdriver.Chrome("/Program Files",options=options)
driver.get(test_url)

#呼叫cmd要用的函式
#計算間隔時間用的時間函式

import os
import datetime
import time
import re

#用xpath找出直播連結

idol = driver.find_element_by_xpath('//*[@id="room-header"]/div[1]/div[1]/h1').text
idol = re.sub(r'[ \\/:*?"<>|\r\n]+',"",idol)
i = 1
T1 = 0
while 1 :
    try:
        element = driver.find_element_by_xpath('//*[@id="choose-stream-variant-dialog"]/ul/li[3]')
        href = element.get_attribute('data-url')
        print("START RECORDING")
    except:
        if T1 == 0:
            if i == 1:
                print("未開始")
            i = i + 1
            continue
        else:
            T2 = datetime.datetime.now()
            if (T2 - T1).seconds >= 200:
                driver.quit()
                print("RECORD COMPLETE")
                break
            else:
                print("未關閉")
                i = i + 1
                continue
    TIME = time.strftime("%Y.%m.%d_%H%M.%S", time.localtime(time.time() + 1*3600))
    ffmpeg = 'ffmpeg -i "' + href + '" -c copy ' + TIME + idol + '.mp4'
    dl = os.popen(ffmpeg)
    print(dl.read())
    T1 = datetime.datetime.now()
    driver.refresh()
    continue


# In[1]:


get_ipython().system('jupyter nbconvert -to script SHOWROOMDL.ipynb')


# In[ ]:




