import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("file:///C:/Users/vijay/PycharmProjects/B1116/Page/Sample3.html")
time.sleep(2)
driver.find_element(By.XPATH,"//a[starts-with(@href,'http')]").click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.find_element(By.XPATH,"//a[contains(@href,'google')]").click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.find_element(By.XPATH,"//a[ends-with(text(),'ogle')] ").click()
time.sleep(2)
driver.quit()