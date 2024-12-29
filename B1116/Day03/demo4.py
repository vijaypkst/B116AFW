import time
from selenium.webdriver import Edge

driver=Edge() #open the browser
driver.get('http://www.fb.com') #enter the url
time.sleep(1)
driver.get('http://www.google.com')
time.sleep(1)
driver.back()
time.sleep(1)
driver.forward()
time.sleep(1)
driver.refresh()
time.sleep(4)
driver.close()

