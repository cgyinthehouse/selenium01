from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# 取得當天日期
t = time.localtime()
tt = '/'.join([str(t.tm_mon),str(t.tm_mday)])

# 執行webdriver
sv = Service('G:/python.uch/msedgedriver.exe')
option = webdriver.EdgeOptions()
driver = webdriver.Edge(service=sv,options=option)
driver.get(url := 'https://docs.google.com/forms/d/e/1FAIpQLSdWSRQl1vsAqSE2CEpFZR5ipQVF2DHh_ykNMuv5tSVDVjkb8g/viewform')
# driver.set_window_position(0, 0)
# driver.set_window_size(1200, 1080)
time.sleep(1)

# driver.find_element(by=By.XPATH,value=f"//span[@class='vRMGwf oJeWuf' and contains(text(), '{tt}')]").click()
dropdown = driver.find_element(by=By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]')
dropdown.click()
courses = driver.find_elements(by=By.CLASS_NAME, value='MocG8c')
# fixme :element not interactable
for i in courses:
    if '5/9' in i.accessible_name:
        ActionChains(driver).click(on_element=i).perform()

time.sleep(5)
driver.quit()
