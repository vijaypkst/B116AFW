import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("file:///C:/Users/vijay/PycharmProjects/B1116/Page/Sample4_same%20link.html")
driver.maximize_window()
time.sleep(1)
element=driver.find_element(By.TAG_NAME,"a")
print(type(element)) #WebElement

elist=driver.find_elements(By.TAG_NAME,"a")
print(type(elist)) #list
print(len(elist)) #3
a=elist[0]
print(type(a))  #WebElement

b=elist[1]
print(type(b))  #WebElement

c=elist[2]
print(type(c))  #WebElement


