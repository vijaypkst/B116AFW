import time
from selenium.webdriver import Chrome

driver=Chrome()
driver.get("https://pos.aksharatraining.in/pos/public/")
time.sleep(1)
driver.set_window_size(500,600)
time.sleep(1)

x=50
y=50
for i in range(10):
    driver.set_window_position(x,y) #move the browser
    x=x+50
    y=y+50
    time.sleep(0.5)

for i in range(10):
    driver.set_window_position(x,y) #move the browser
    x=x+50
    y=y-50
    time.sleep(0.5)

time.sleep(4)
driver.quit()
