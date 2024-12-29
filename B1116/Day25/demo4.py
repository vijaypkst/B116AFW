import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://pos.aksharatraining.in/pos/public/")
locator=[By.ID,"input-username"]
un=driver.find_element(locator[0],locator[1])
un.send_keys("admin")
time.sleep(2)