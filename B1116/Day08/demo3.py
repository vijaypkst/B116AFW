import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("file:///E:/B116_8.30PM_Selenium(Py)/share/page/Sample3.html")
time.sleep(2)
driver.find_element(By.XPATH,"//a[@id='a1' and @name='n1']").click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.find_element(By.XPATH,"//a[text()='Google' or not(@class='c1')]").click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.find_element(By.XPATH,"//a[text()='Google' and not(@class='c2')]").click()
time.sleep(2)
driver.quit()