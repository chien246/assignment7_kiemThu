from selenium import webdriver
import time

driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')

driver.get('http://practice.automationtesting.in/')
driver.set_window_size(500,350)
time.sleep(2)
driver.close()