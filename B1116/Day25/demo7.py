import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://pos.aksharatraining.in/pos/public/")
locator=(By.ID,"input-username") #tuple
un=driver.find_element(*locator)
un.send_keys("admin")
time.sleep(2)