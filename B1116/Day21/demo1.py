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
print('Number of Auto Suggestions:',len(all_AS))

for element in all_AS:
    print(element.text)

driver.quit()

