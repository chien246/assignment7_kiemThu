from selenium import webdriver
import time

driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')

driver.get('http://practice.automationtesting.in/')
driver.fullscreen_window()
print(driver.title)
time.sleep(2)
driver.close()