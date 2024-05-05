import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost/BC_24.101.0059.0882_7")
driver.maximize_window()
time.sleep(5)