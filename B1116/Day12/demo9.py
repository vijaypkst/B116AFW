import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://pos.aksharatraining.in/pos/public/")
time.sleep(1)
un_size=driver.find_element(By.ID,"input-username").size
print(un_size)
print(un_size['height'])
print(un_size['width'])

