from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service('G:/python.uch/msedgedriver.exe')
option = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service,options=option)
driver.get(url := 'https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip121/query')

time.sleep(1.2)
# 身份證字號
element = driver.find_element(by=By.ID,value='pid')
element.send_keys('A123456789')
# 出發站
element = driver.find_element(by=By.ID,value='startStation')
element.clear()
element.send_keys('1000-臺北')
# 抵達站
element = driver.find_element(by=By.ID,value='endStation')
element.clear()
element.send_keys('1120-楊梅')
# 去回
element = driver.find_element(by=By.XPATH, value='//*[@id="queryForm"]/div[1]/div[1]/div[5]/div[2]/label[2]')
element.click()
# 一般座票數
element = driver.find_element(by=By.ID,value='normalQty')
element.clear()
element.send_keys('1')
# 日期（去程）
element = driver.find_element(by=By.ID,value='rideDate1')
element.clear()
element.send_keys('20220430')
# 日期（回程）
element = driver.find_element(by=By.ID,value='rideDate2')
element.clear()
element.send_keys('20220502')
# 車次（去程）
element = driver.find_element(by=By.XPATH, value="//input[@id='trainNoList1']")
element.send_keys("2011")
# 車次2（回程）
element = driver.find_element(by=By.XPATH, value='//*[@id="trainNoList4"]')
element.send_keys("1248")
# TODO: search methods for bypass recaptcha
# recaptcha
recaptcha_cookies = '09AG6mx8NkQftj6bR7HGXYmEgOXzY-t8ZkqB-rUZpmui8OY7wUvR-xUaG0YE5hGSCdmBuRyj7W9b_aHVEK8HJvP7g'
driver.add_cookie({'name': '_GRECAPTCHA', 'value': recaptcha_cookies})
frame = driver.find_element(by=By.XPATH,value='/html/body/div[8]/div[4]/iframe')
driver.switch_to.frame(frame)
recaptcha = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'recaptcha-checkbox-checkmark')))

# element = driver.find_element(by=By.XPATH, value='//*[@id="recaptcha-anchor"]')
recaptcha.click()
driver.switch_to.default_content()
# 送出
element = driver.find_element(by=By.XPATH, value='//*[@id="queryForm"]/div[4]/input[2]')
element.click()



# time.sleep(3)
# driver.close()