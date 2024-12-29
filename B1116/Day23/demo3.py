import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver=Chrome()
driver.set_page_load_timeout(10)
try:
    driver.get("https://www.irctc.co.in/nget/train-search")
    print('page is loaded within 10s')
except:
    print('page is NOT loaded within 10s')

time.sleep(5)