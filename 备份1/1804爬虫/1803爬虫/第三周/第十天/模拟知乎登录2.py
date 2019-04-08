driver = webdriver.Chrome(executable_path='/home/ljh/桌面/chromedriver')
driver.get('https://www.zhihu.com/')
driver.find_element_by_xpath('//div[@class="HomeSidebar-signBannerActions"]/button[1]').click()
time.sleep(1)
driver.find_element_by_name('username').send_keys('账号')
driver.find_element_by_name('password').send_keys('密码')

#driver.find_element_by_class_name('Button SignFlow-submitButton Button--primary Button--blue').click()
driver.find_element_by_css_selector('Button.SignFlow-submitButton.Button--primary.Button--blue').click()
cookies = driver.get_cookies()
cookie_dict = {}
for cookie in cookies:
print(cookie['name'],cookie['value'])
cookie_dict[cookie['name']] = cookie['value']

#获取cookies值，保存本地
with open('cookie.txt','w') as f:
f.write(json.dumps(cookie_dict,ensure_ascii=False))