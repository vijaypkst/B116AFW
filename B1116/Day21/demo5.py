import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("file:///C:/Users/vijay/PycharmProjects/B1116/Page/Sample13.html")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID,"A1").click()
time.sleep(1)
driver.find_element(By.XPATH,"//option[text()='Bangalore']").click()
time.sleep(1)
driver.find_element(By.ID,"A1").click()
time.sleep(6)