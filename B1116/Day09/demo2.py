import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

#selenium script to login to POS app using XPATH as locator

#open the browser
driver=Chrome()
#enter the url
driver.get("https://pos.aksharatraining.in/pos/public/")
#maximize the broswer
driver.maximize_window()
time.sleep(1)
#enter user name : admin
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("admin")
#enter password: pointofsale
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("pointofsale")
time.sleep(1)
#click on go button
driver.find_element(By.XPATH,"//button[@type='submit']").click()
#verify that home page is displayed
time.sleep(4)

actual_url=driver.current_url
print('Actual URL',actual_url)

expected_url='home'
print('Expected: URL should contain->',expected_url)

if expected_url in actual_url:
    print('PASS:Home Page is displayed')
else:
    print('FAIL:Home Page is NOT displayed')

driver.quit()