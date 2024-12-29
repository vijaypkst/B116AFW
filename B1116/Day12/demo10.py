import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://pos.aksharatraining.in/pos/public/")
time.sleep(1)
un_size=driver.find_element(By.ID,"input-username").size
pw_size=driver.find_element(By.ID,"input-password").size

if un_size==pw_size:
    print('size of UN & PW is same')
else:
    print('size of UN & PW is NOT same')

driver.quit()