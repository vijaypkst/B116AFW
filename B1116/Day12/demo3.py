import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("file:///C:/Users/vijay/PycharmProjects/B1116/Page/Sample9.html")
time.sleep(1)
status=driver.find_element(By.ID,"A1").is_displayed()#True -Displayed
print(status)
status=driver.find_element(By.ID,"A3").is_displayed() #False -Not displayed
print(status)
time.sleep(1)
driver.quit()
