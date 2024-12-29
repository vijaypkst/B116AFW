import time

from selenium.webdriver import Chrome
print("start")
#creating object of Chrome class
obj=Chrome() #open the chrome browser
time.sleep(3) #wait for 3seconds
#after the execution it deletes the object--> closes the browser
print("done")