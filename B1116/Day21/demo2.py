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

# all_AS[0].click() #select 1st auto suggestion

# all_AS[3].click()#select 4th auto suggestion

all_AS[-1].click() #select last auto suggestion

time.sleep(3)
driver.quit()

