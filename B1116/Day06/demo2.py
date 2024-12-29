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

driver.find_element(By.CSS_SELECTOR,"a[id='a1']").click()
go_back(driver)

driver.find_element(By.CSS_SELECTOR,'a[name="n1"]').click()
go_back(driver)

driver.find_element(By.CSS_SELECTOR,"a[class='c1']").click()
go_back(driver)

driver.find_element(By.CSS_SELECTOR,"a[title='click me']").click()
go_back(driver)

driver.find_element(By.CSS_SELECTOR,"a[href='http://www.google.com']").click()
go_back(driver)


driver.quit()