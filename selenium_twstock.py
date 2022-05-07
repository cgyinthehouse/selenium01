from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import timedelta, datetime
import os ,glob, shutil, csv
from openpyxl import workbook,load_workbook
service = Service('G:/python.uch/msedgedriver.exe')
option = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service,options=option)
driver.get(url := 'https://www.twse.com.tw/zh/page/trading/exchange/MI_INDEX.html')
time.sleep(1.2)


def download_csv(*date):
    mon1, day1 = date[0].split('/')
    if len(date) > 1:
        mon2, day2 = date[-1].split('/')
    else:
        mon2,day2=mon1+'',day1+''
    d = datetime.strptime(f'2022-{mon1}-{day1}', '%Y-%m-%d')
    d2 = datetime.strptime(f'2022-{mon2}-{day2}', '%Y-%m-%d')
    while d2 >= d:
        if str(d.weekday()) in '01234':  # 只取工作日
            driver.find_element(by=By.XPATH, value=f'//*[@id="d1"]/select[2]/option[{d.month}]').click()  # 選擇月份
            driver.find_element(by=By.XPATH, value=f'//*[@id="d1"]/select[3]/option[{d.day}]').click()  # 選擇日期
            driver.find_element(by=By.XPATH, value='//*[@id="main-form"]/div/div/form/select/option[36]').click()  # 產業
            driver.find_element(by=By.XPATH, value='//*[@id="main-form"]/div/div/form/a').click()  # 點擊查詢
            try:
                download = WebDriverWait(driver, 2).until(    # 等待element出現，不然會unable to locate element
                    EC.presence_of_element_located((By.LINK_TEXT, 'CSV 下載')))
                time.sleep(2.5)  # 每秒請求次數不能大於nginx伺服器rate limiting，不然會被鎖ip
                download.click()
            except TimeoutException:
                pass
            d += timedelta(days=1)
        else:
            d += timedelta(days=1)

# todo: merge downloaded csv files to an excel file
download_csv('4/1', '4/10')    # (開始日期, 結束日期)
if not os.path.exists(mydir := 'H:/下載/csv'):
    os.mkdir(mydir)

for file in csv_files := glob.glob(mydir + '/*.csv'):
    with open (file, 'r', encoding='utf-8', newline='') as f:  # newline 是避免出現兩倍行距
        reader = csv.reader(file)
        for row in reader:


time.sleep(2)
driver.quit()
