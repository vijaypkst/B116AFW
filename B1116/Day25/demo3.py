import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://pos.aksharatraining.in/pos/public/")
un=driver.find_element(By.ID,"input-username")
un.send_keys("admin")
time.sleep(2)