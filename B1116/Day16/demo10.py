import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("file:///E:/B116_8.30PM_Selenium(Py)/share/page/SampleC.html")
driver.maximize_window()
time.sleep(1)
driver.find_element(By.ID,"t0").send_keys("A")
driver.switch_to.frame("f0")
driver.find_element(By.ID,"t1").send_keys("A")
driver.switch_to.frame("f1")
driver.find_element(By.ID,"t2").send_keys("A")
time.sleep(1)
driver.find_element(By.ID,"t2").send_keys("B")
driver.switch_to.parent_frame()
driver.find_element(By.ID,"t1").send_keys("B")
driver.switch_to.default_content()
driver.find_element(By.ID,"t0").send_keys("B")
