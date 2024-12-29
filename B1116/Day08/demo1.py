import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("file:///E:/B116_8.30PM_Selenium(Py)/share/page/Sample3.html")
driver.find_element(By.XPATH,"./html/body/a[@id='a1']").click()
time.sleep(1)
driver.back()
time.sleep(1)
driver.find_element(By.XPATH,"//a[@id='a1']").click()
time.sleep(1)
driver.quit()