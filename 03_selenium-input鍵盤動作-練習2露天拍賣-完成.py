"""
資料來源:
https://selenium-python-zh.readthedocs.io/en/latest/getting-started.html

"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by   import By
import time
from bs4 import BeautifulSoup

# driver = webdriver.Firefox()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome('chromedriver.exe',chrome_options=option)
driver.get('https://www.ruten.com.tw/')

time.sleep(5)               # 停個 5 sec

"""
<input id="searchFormSubmit" class="rt-header-search-submit" type="button" value="" title="搜尋">
<input id="searchKeyword" class="rt-header-search-input" name="q" accesskey="4" autocomplete="off" placeholder="搜尋露天拍賣商品">

"""
# element = driver.find_element_by_id("searchFormSubmit")  # id="keyword"
# element = driver.find_element_by_name("k")   # name="k"
# element = find_element(by=By.XPATH, value=xpath)
# element = driver.find_element_by_xpath("//input[@id='searchKeyword']")   # <input id="searchFormSubmit"
element = driver.find_element(by=By.XPATH, value="//input[@id='searchKeyword']")

element.send_keys("android")
element.send_keys(Keys.RETURN)   # 下 ARROW_DOWN)

time.sleep(5)               # 5sec 等待網頁內容全部讀取
html=driver.page_source
print(html)
str1=html.encode('utf-8')

# 把網頁資料放到  BS4 做資料處理
soup=BeautifulSoup(str1, "html.parser")
allItems=soup.select('.product-item')    # class="product-item"
for t1 in allItems:
    t2 = t1.select('.rt-goods-list-item-link')[0].string  # # class="rt-goods-list-item-link"   找 產品名稱
    t3 = t1.select('.rt-text-price')[0].string   # class="rt-text-price"  找價格
    print(" 商品名稱:",t2,"    價格:",t3)

"""
t1=soup.select('.content')  # class="content"
t2=t1[1].select('dd')     #<dd
for dd in t2:
    try:
        prod_name = dd.select('.prod_name')    # class="price"
        print(prod_name[0].contents[1].contents[0])
        price = dd.select('.price')  # class="price"
        print(price[0].contents[0])
    except:
        print("error")
"""



"""
elem = driver.find_element_by_name("q")
elem.clear()                  # 清空
elem.send_keys("powenko")
elem.send_keys(Keys.RETURN)   # 輸入Enter
# assert "No results found." not in driver.page_source
print(driver.page_source)
"""
time.sleep(5)               # 5sec
driver.close()              # 視窗關閉