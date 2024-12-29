import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import os
driver=Chrome()
driver.get("file:///C:/Users/vijay/PycharmProjects/B1116/Page/Sample10.html?")
driver.maximize_window()
time.sleep(3)

relative_path="./../Page/MyCV.docx" #. means current package
absolute_path=os.path.abspath(relative_path)
print(absolute_path)
driver.find_element(By.ID,"A2").send_keys(absolute_path)
time.sleep(3)