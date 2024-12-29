import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import ChromiumOptions


driver=Chrome()
driver.get("https://pushalert.co/demo")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH,"//a[text()='Later']").click()
time.sleep(2)
driver.find_element(By.ID,"send-button").click()
time.sleep(5)