import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
driver=Chrome()
driver.get("https://pos.aksharatraining.in/pos/public/")
driver.maximize_window()
time.sleep(2)

username=driver.switch_to.active_element
username.send_keys('abc')
time.sleep(2)
#how do u copy paste value from one text box to another
username.send_keys(Keys.CONTROL+ 'a')
time.sleep(2)
username.send_keys(Keys.CONTROL+ 'c')
time.sleep(2)
username.send_keys(Keys.TAB)
time.sleep(2)
password=driver.switch_to.active_element
password.send_keys(Keys.CONTROL+ 'v')
time.sleep(2)
password.send_keys(Keys.TAB)
time.sleep(2)
LoginBtn=driver.switch_to.active_element
time.sleep(2)
