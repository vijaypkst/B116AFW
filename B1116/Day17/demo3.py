import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("file:///E:/B116_8.30PM_Selenium(Py)/share/page/Sample10.html")
driver.maximize_window()
time.sleep(1)
driver.find_element(By.ID,"A1").click()
time.sleep(2)
alert=driver.switch_to.alert
print(alert.text) #get msg present on alert popup
alert.dismiss() #click cancel
time.sleep(2)