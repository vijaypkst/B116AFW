import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from selenium.webdriver import  ChromeOptions
options = ChromeOptions()
options.add_experimental_option("detach", True)
driver=Chrome(options)
driver.get("http://www.google.com")
driver.maximize_window()
time.sleep(4)
driver.switch_to.frame(0)
time.sleep(1)
driver.find_element(By.XPATH,"//button[text()='Stay signed out']").click()
time.sleep(4)
