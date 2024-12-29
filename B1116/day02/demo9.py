import time
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox

#----------------------------
driver=Chrome() #open chrome browser
driver.get('http://www.google.com') #enter the url
time.sleep(2) #wait for 2s
driver.close()

