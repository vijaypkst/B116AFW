import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("file:///C:/Users/vijay/PycharmProjects/B1116/Page/Sample9.html")
time.sleep(2)
status=driver.find_element(By.ID,"A1").is_enabled()#True -enabled
print(status)
status=driver.find_element(By.ID,"A4").is_enabled() #False -disabled
print(status)
time.sleep(2)
driver.quit()
