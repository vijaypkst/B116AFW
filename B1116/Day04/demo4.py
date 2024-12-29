import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
driver=Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
time.sleep(2)

username=driver.switch_to.active_element
username.send_keys('Admin')
time.sleep(2)
username.send_keys(Keys.TAB)

password=driver.switch_to.active_element
password.send_keys('admin123')
password.send_keys(Keys.TAB)

login=driver.switch_to.active_element
login.send_keys(Keys.ENTER)

time.sleep(7)

