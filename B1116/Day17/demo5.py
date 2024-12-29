import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("file:///C:/Users/vijay/PycharmProjects/B1116/Page/Sample10.html?")
driver.maximize_window()
time.sleep(1)
relative_path="./../Page/MyCV.docx"
driver.find_element(By.ID,"A2").send_keys(relative_path)

time.sleep(1)