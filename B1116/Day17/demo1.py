import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("file:///C:/Users/vijay/PycharmProjects/B1116/Page/Sample9.html?")
driver.maximize_window()
time.sleep(1)
driver.find_element(By.ID,"A8").click()
time.sleep(2)
alert=driver.switch_to.alert
print(alert.text) #get msg present on alert popup
alert.accept() #click OK
time.sleep(2)