import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

def go_back(driver):
    time.sleep(0.5)
    driver.back()
    time.sleep(0.5)

#<a id="a1" name="n1" class="c1" title="click me" href="http://www.google.com">Google</a>
driver=Chrome()
driver.get("file:///C:/Users/vijay/PycharmProjects/B1116/Page/Sample3.html")
time.sleep(1)

driver.find_element(By.TAG_NAME,"a").click()
go_back(driver)

driver.find_element(By.ID,"a1").click()
go_back(driver)

driver.find_element(By.NAME,"n1").click()
go_back(driver)

driver.find_element(By.CLASS_NAME,"c1").click()
go_back(driver)

driver.find_element(By.LINK_TEXT,"Google").click()
go_back(driver)

driver.find_element(By.PARTIAL_LINK_TEXT,"Goo").click()
go_back(driver)

driver.quit()