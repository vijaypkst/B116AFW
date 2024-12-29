import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("http://www.google.com")
driver.maximize_window()
time.sleep(8)
driver.switch_to.frame(0)
time.sleep(1)
driver.find_element(By.XPATH,"//button[text()='Stay signed out']").click()
time.sleep(4)
driver.switch_to.default_content()
driver.find_element(By.ID,"APjFqb").send_keys("selenium")
time.sleep(6)