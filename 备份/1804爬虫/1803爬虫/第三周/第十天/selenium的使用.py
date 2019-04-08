from selenium import webdriver
import time
options= webdriver.ChromeOptions()
# options.set_headless()

driver = webdriver.Chrome(executable_path='/home/bc/桌面/chromedriver',
)
driver.get('http://www.baidu.com')

# driver.save_screenshot('baudu.png')
# driver.find_element_by_id('kw').send_keys('帅哥')
# driver.find_element_by_id('su').click()
# driver.find_element_by_name('bg s_btn').click()
time.sleep(2)
# driver.find_element_by_link_text('下一页>').click
# driver.find_element_by_class_name('n').click()
# print(driver.page_source)
# print(driver.get_cookie)
# cookies = driver.get_cookies()
# for cookie in cookies:
#     print(cookie['name']+':'+cookie['value'])
from selenium.webdriver import ActionChains
elelment = driver.find_element_by_xpath('//div[@id="ul"]/a[1]')
ActionChains(driver).move_to_element(elelment).perform()
ActionChains(driver).move_to_element(elelment).click(elelment).perform()
time.sleep(5)
driver.quit()
