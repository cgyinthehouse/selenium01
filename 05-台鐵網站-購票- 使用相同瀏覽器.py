#!/usr/bin/env python
# coding: utf-8

# mac 安裝方法
# https://medium.com/@brettlin_78528/%E7%94%A8-python-%E5%8C%AF%E5%85%A5-selenium-%E7%9A%84%E6%96%B9%E5%BC%8F-%E4%BB%A5%E5%8F%8A%E5%A6%82%E4%BD%95%E7%94%A8mac-%E5%AE%89%E8%A3%9D-chromedriver-5d92121c02d7
# In[1]:
import pyautogui

import bs4
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

import os
print(os.name)
if(os.name=="posix"):   # mac 作業系統的處理方法
    chromedriver='/Users/powenko/Desktop/chromedriver'
    chromedriver='chromedriver'
    driver2 =webdriver.Chrome(chromedriver)
else:                   # Windows OS
    option = webdriver.ChromeOptions()
    driver2 = webdriver.Chrome('chromedriver.exe', chrome_options=option)
driver2.get("https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip121/query")
# driver.find_element_by_xpath("//*[@role=\"button\"]").click()




# 取得webdriver 資訊
url = driver2.command_executor._url       #"http://127.0.0.1:60622/hub"
session_id = driver2.session_id            #'4e167f26-dc1d-4f51-a207-f761eaf73c31'
print(url)
print(session_id)
#

driver = webdriver.Remote(command_executor=url,desired_capabilities={})
driver.close()   # this prevents the dummy browser
driver.session_id = session_id

# driver2.get('https://www.yahoo.com.tw/')


time.sleep(1)
driver.switch_to.frame(0)
from selenium.webdriver.common.action_chains import ActionChains


element = driver.find_element_by_xpath("//span[@class='recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox']")


action_chains = ActionChains(driver)
action_chains.move_to_element_with_offset(element, 20, 20).perform()
action_chains.click().perform()

pyautogui.moveTo(100, 100, duration=0.05)
moveTo(100, 100, duration=0.05)


pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
print(pyautogui.size())
width, height = pyautogui.size()
print(width)
print(height)

print(pyautogui.position())  # GET MOUSE
pyautogui.click(587, 790)    # 601,799
pyautogui.scroll(2000)

pyautogui.click(587, 790)    # 601,799



# <input class="idmember pid form-input" maxlength="10" type="text" id="pid" name="pid" value="">
# element = driver.find_element_by_class("idmember")
element = driver.find_element_by_xpath("//input[@id='pid']")
#element = driver.find_element_by_xpath("//input[@class='idmember']")
element.send_keys("Y117083046")

# 出發站
# <input id="startStation" type="text" name="startStation" data-autocomplete="station" class="startStation ui-autocomplete-input" placeholder="出發站" value="" autocomplete="off" aria-required="true" aria-invalid="false">
element = driver.find_element_by_id("startStation")
element.send_keys("1100")

# 抵達站
# <input id="endStation" type="text" name="endStation" data-autocomplete="station" class="endStation ui-autocomplete-input" placeholder="抵達站" value="" autocomplete="off">element = driver.find_element_by_id("startStation")
element = driver.find_element_by_xpath("//input[@id='endStation']")
element.send_keys("1000")



# 日期
# <input   id="rideDate1" pe="text" data-plugin="datepicker" class="rideDate" placeholder="YYYY/MM/DD" id="rideDate1" data-date-start-date="+0d" name="ticketOrderParamList[0].rideDate" value="2021/04/21" aria-required="true">
# <input type="text" data-plugin="datepicker" class="rideDate" placeholder="YYYY/MM/DD" id="rideDate1" data-date-start-date="+0d" name="ticketOrderParamList[0].rideDate" value="2021/04/21" aria-required="true" aria-invalid="false">

element = driver.find_element_by_xpath("//input[@id='rideDate1']")
element.click()
element.clear()
time.sleep(0.1)
element.send_keys("20220430")


# 車次
# <input id="trainNoList1"  ass="form-control input-small trainNoList train1"  placeholder="必填" name="ticketOrderParamList[0].trainNoList[0]" value="" aria-required="true" aria-invalid="false">
# 150
element = driver.find_element_by_xpath("//input[@id='trainNoList1']")
element.send_keys("150")

# 送出
# <input type="submit" class="btn btn-3d" value="訂票">
element = driver.find_element_by_xpath("//input[@type='submit']")
#element.click()
#time.sleep(2)
