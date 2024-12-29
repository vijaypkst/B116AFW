import time
from logging import exception

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
driver=Chrome()
driver.get("file:///C:/Users/vijay/PycharmProjects/B1116/Page/Sample4_same%20link.html")
time.sleep(2)
try:
    element=driver.find_element(By.TAG_NAME,'a')
    element.click()

except exception as e:
     print("No such element",e)
time.sleep(3)
driver.quit()