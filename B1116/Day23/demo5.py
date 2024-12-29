import time
from selenium.webdriver import Chrome


#write a script to find out the amount of time taken to load the page
driver=Chrome()
start_time=time.time()
driver.get("https://aksharatraining.com/")
time.sleep(2)
#execute_script method will send JS code to the browser
#browser will execute JS code
#after the execution control wil be transferd back to selenium script
driver.set_script_timeout(0.1)
driver.execute_script("window.scrollBy(0,500)")
print('Done')
time.sleep(5)