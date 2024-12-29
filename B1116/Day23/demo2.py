import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver=Chrome()
#enter the url and wait till page is completely loaded
driver.set_page_load_timeout(2)
driver.get("https://www.irctc.co.in/nget/train-search")
print('hi')
time.sleep(5)