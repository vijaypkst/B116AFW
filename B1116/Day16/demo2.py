import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("file:///E:/B116_8.30PM_Selenium(Py)/share/page/SampleA.html")
driver.maximize_window()
time.sleep(1)
driver.switch_to.frame(0) #go inside the 1st frame-frame index
driver.find_element(By.ID,"t2").send_keys("A")
time.sleep(1)
driver.switch_to.default_content() #exit from the frame --goto main page
driver.find_element(By.ID,"t1").send_keys("A")
time.sleep(2)
driver.quit()