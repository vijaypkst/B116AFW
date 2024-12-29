import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

def go_back(driver):
    time.sleep(0.5)
    driver.back()
    time.sleep(0.5)

#<a id="a1" name="n1" class="c1" title="click me" href="http://www.google.com">Google</a>
driver=Chrome()
driver.get("file:///E:/B116_8.30PM_Selenium(Py)/share/page/Sample3.html")
time.sleep(1)

driver.find_element(By.CSS_SELECTOR,"a[id='a1']").click()
go_back(driver)

driver.find_element(By.CSS_SELECTOR,'a#a1').click()
go_back(driver)

driver.find_element(By.CSS_SELECTOR,'#a1').click()
go_back(driver)

driver.find_element(By.CSS_SELECTOR,"a[class='c1']").click()
go_back(driver)

driver.find_element(By.CSS_SELECTOR,"a.c1").click()
go_back(driver)

driver.find_element(By.CSS_SELECTOR,".c1").click()
go_back(driver)
driver.quit()