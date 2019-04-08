from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='/home/bc/桌面/chromedriver')
driver.get('https://www.douban.com/search?q=%E8%80%81%E4%BA%BA%E4%B8%8E%E6%B5%B7')
content = driver.page_source
# with open('gg.html','w') as f:
#     f.write(content)
curren = driver.current_url
cookies = driver.get_cookies()
# print(cookies)
# cookie_dict = {i['name']:i['value'] for i in cookies}
# print(cookie_dict)
