import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver=Chrome()
# driver.implicitly_wait(10)
# wait=WebDriverWait(driver,10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
# wait.until(expected_conditions.visibility_of_element_located((By.NAME,"username")))
# time.sleep(5)
for i in range(20):
    try:
        driver.find_element(By.NAME,"username").send_keys("Admin")
        print('Element is found and performed the action',i)
        break
    except:
        print('Element is NOT found',i)

print('Done')
time.sleep(10)