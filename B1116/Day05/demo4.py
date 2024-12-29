import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
driver=Chrome()
driver.get("file:///E:/B116_8.30PM_Selenium(Py)/share/page/Sample4.html")
time.sleep(2)
element=driver.find_element(By.TAG_NAME,'a') #number of match is 3
element.click()
time.sleep(3)
driver.quit()