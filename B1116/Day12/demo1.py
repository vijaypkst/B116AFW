import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("file:///C:/Users/vijay/PycharmProjects/B1116/Page/Sample9.html")
time.sleep(2)
status=driver.find_element(By.ID,"A5").is_selected() #True -selected
print(status)
status=driver.find_element(By.ID,"A6").is_selected() #False -Not selected
print(status)
time.sleep(2)
driver.quit()
