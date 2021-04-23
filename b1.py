from selenium import webdriver

driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')

driver.get('http://practice.automationtesting.in/')
driver.close()