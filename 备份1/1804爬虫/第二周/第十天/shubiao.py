from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path='/home/bc/桌面/chromedriver')
driver.get('http:www.baidu.com/')
# action = driver.find_element_by_xpath('//div[@id="u1"]/a[4]')

# ActionChains(driver).move_to_element(action).perform()
# s_element = driver.find_element_by_name('tj_trnews')
# s_hh = driver.find_element_by_id('kw')
# ActionChains(driver).drag_and_drop(s_element,s_hh).perform()
js = 'window.open("http://www.baidu.com")'
#切换窗口
driver.execute_async_script(js)
driver.switch_to_window(driver.window_handles[0])