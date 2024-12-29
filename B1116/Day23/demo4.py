import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

#write a script to find out the amount of time taken to load the page
driver=Chrome()
start_time=time.time()
driver.get("https://www.irctc.co.in/nget/train-search")
end_time=time.time()
time_diff=end_time-start_time
print('Time taken to load the page is',time_diff,'seconds')
time.sleep(5)