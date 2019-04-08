
driver.find_element_by_id('kw').send_keys('野兽与美女')
driver.find_element_by_id('su').click()
time.sleep(5)
driver.find_element_by_link_text('下一页>').click()
time.sleep(2)
# driver.back()
driver.close()
# driver.quit()
html = driver.page_source