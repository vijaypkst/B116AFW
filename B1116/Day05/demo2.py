import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
driver=Chrome()
driver.get("file:///C:/Users/vijay/PycharmProjects/B1116/Page/Sample3.html")
time.sleep(2)
element=driver.find_element(By.TAG_NAME,'a')
element.click()
time.sleep(3)
driver.quit()
