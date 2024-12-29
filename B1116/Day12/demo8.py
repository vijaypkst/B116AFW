import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://pos.aksharatraining.in/pos/public/")
time.sleep(1)
un_location=driver.find_element(By.ID,"input-username").location
print(un_location)
print(un_location['x'])
print(un_location['y'])

pw_loction=driver.find_element(By.ID,"input-password").location
print(pw_loction)
print(pw_loction['x'])
print(pw_loction['y'])

if un_location['y']<pw_loction['y']:
    print('Un is above PWD')
else:
    print('Un is not above PWD')


