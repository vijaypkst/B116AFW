import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("http://www.google.com")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID,"APjFqb").send_keys("selenium")
time.sleep(2)

all_AS=driver.find_elements(By.XPATH,"//span[contains(text(),'selenium')]")

for element in all_AS:
    if element.text=='selenium dev':
        element.click()
        print('Selected selenium dev')
        break


time.sleep(3)
driver.quit()

