from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='/home/bc/桌面/chromedriver')

driver.get('https://www.douban.com/')

driver.find_element_by_id('form_email').send_keys('18518753265')
driver.find_element_by_id('form_password').send_keys('ljh123456')
driver.find_element_by_class_name('bn-submit').click()

with open('kk.html','w') as f:
    f.write(driver.page_source)
cookies = driver.get_cookies()
print({i['name']:i['value'] for i in cookies})