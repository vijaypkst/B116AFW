import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("file:///E:/B116_8.30PM_Selenium(Py)/share/page/Sample3.html")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/a[text()='Google']").click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.find_element(By.XPATH,"//a[text()='Google']").click()
time.sleep(2)
driver.quit()