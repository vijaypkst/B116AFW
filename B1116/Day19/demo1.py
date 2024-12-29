import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver1=Chrome()
time.sleep(3)
driver1.get("http://www.fb.com")
time.sleep(3)
driver2=Chrome()
time.sleep(3)
driver2.get("http://www.google.com")
time.sleep(3)
driver2.quit()
time.sleep(3)
driver1.quit()

