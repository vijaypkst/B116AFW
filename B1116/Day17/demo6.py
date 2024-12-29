import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("file:///C:/Users/vijay/PycharmProjects/B1116/Page/Sample10.html?")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.ID,"A2").send_keys("MyCV.docx")
time.sleep(3)