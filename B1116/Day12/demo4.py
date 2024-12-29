import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("file:///C:/Users/vijay/PycharmProjects/B1116/Page/Sample3.html")
time.sleep(1)
element = driver.find_element(By.ID,"a1")
print(element.tag_name)
print(element.get_attribute("href"))
print(element.get_attribute("title")) #tool tip text
print(element.text)
time.sleep(1)
driver.quit()