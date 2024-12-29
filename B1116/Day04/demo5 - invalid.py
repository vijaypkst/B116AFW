import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
driver=Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
time.sleep(2)

username=driver.switch_to.active_element
username.send_keys('A')
username.send_keys(Keys.TAB)
username.send_keys('B')
time.sleep(5)

