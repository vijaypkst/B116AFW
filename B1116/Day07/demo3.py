import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()dAY08
lement(By.XPATH,".//a").click()
time.sleep(1)
driver.back()
time.sleep(1)
driver.find_element(By.XPATH,"//a").click()
time.sleep(1)
driver.quit()