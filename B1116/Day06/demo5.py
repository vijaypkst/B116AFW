import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

#selenium script to login to orange hrm app using css Selector as locator

#open the browser
driver=Chrome()
#enter the url
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#maximize the broswer
driver.maximize_window()
time.sleep(1)
#enter user name : admin
driver.find_element(By.CSS_SELECTOR,"input[name='username']").send_keys("admin")
#enter password: admin123
driver.find_element(By.CSS_SELECTOR,"input[name='password']").send_keys("admin123")
time.sleep(1)
#click on login button
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
#verify that home page is displayed
time.sleep(4)

actual_url=driver.current_url
print('Actual URL',actual_url)

expected_url='dashboard'
print('Expected: URL should contain->',expected_url)

if expected_url in actual_url:
    print('PASS:Home Page is displayed')
else:
    print('FAIL:Home Page is NOT displayed')

driver.quit()