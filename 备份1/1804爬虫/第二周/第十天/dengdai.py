from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='/home/bc/桌面/chromedriver')

driver.get('http:www.baidu.com/')
#隐士等待
driver.implicitly_wait(10)
driver.find_element_by_id('name')

#显示等待
driver = WebDriverWait(driver,10)
element = driver.until(
    EC.presence_of_element_located(By.CLASS_NAME,'s_ipt')
)
print(element)