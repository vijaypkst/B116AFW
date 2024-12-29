import time
from selenium.webdriver import Chrome

driver=Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(2)
element=driver.switch_to.active_element
element.send_keys('selenium')
time.sleep(5)

