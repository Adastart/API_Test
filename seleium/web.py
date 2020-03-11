#coding=utf-8
from selenium import webdriver
import unittest
import time

from selenium.webdriver.common.by import By



driver=webdriver.Chrome()
#driver.maximize_window()
driver.get("https://www.weiyangpuhui.com/dist/home")
print(driver.title)
login=driver.find_element_by_xpath('/html/body/div/div/div[1]/div[3]/div/ul/li[1]/span/a')
login.click()


time.sleep(2)
#浏览器关闭
driver.close()
#驱动程序关闭
driver.quit()