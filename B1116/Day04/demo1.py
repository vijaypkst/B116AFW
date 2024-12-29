import time
from selenium.webdriver import Chrome

driver=Chrome()
driver.get("https://pos.aksharatraining.in/pos/public/")
time.sleep(1)
size=driver.get_window_size()
print(size)
print(size['width'])
print(size['height'])

driver.set_window_size(500,600) #resize the browser
time.sleep(1)

position=driver.get_window_position()
print(position)
time.sleep(1)
driver.set_window_position(500,200) #move the browser
time.sleep(4)
driver.quit()
