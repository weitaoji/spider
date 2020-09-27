import unittest  # unittest提供框架去组织测试用例
from selenium import webdriver  # 提供WebDriver实现
from selenium.webdriver.common.keys import Keys  # 提供键盘操作
driver = webdriver.Chrome()
driver.get('https://www.itjuzi.com/login')
elem = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div/input')
elem.send_keys('j3707821999@163.com')
elem = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/form/div[2]/div/div/input')
elem.send_keys('ji127423')
elem = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/div/button')
elem.send_keys(Keys.ENTER)


