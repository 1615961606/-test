from selenium import webdriver
import time
import json
driver = webdriver.Chrome(executable_path='/home/bc/桌面/chromedriver')

driver.get('https://www.zhihu.com/signup?next=%2F')
driver.find_element_by_css_selector('SignContainer-switch')

time.sleep(5)

driver.find_element_by_name('username').send_keys('')
driver.find_element_by_name('password').send_keys('')
driver.find_element_by_css_selector('.Button.SignFlow-submitButton.Button--primary.Button--blue')

cookies = driver.get_cookies()

cookie_dict = {}
for cookie in  cookies:
    cookie_dict[cookie['name']] = cookie['value']