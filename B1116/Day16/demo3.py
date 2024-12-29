import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import  ChromeOptions
options = ChromeOptions()
options.add_experimental_option("detach", True)
driver=Chrome(options)
driver.get("file:///C:/Users/vijay/PycharmProjects/B1116/Page/SampleA.html")
driver.maximize_window()
time.sleep(1)
driver.switch_to.frame("f1")#go inside the f1 frame (frame id)
driver.find_element(By.ID,"t2").send_keys("B")
time.sleep(1)
driver.switch_to.default_content() #exit from the frame --goto main page
driver.find_element(By.ID,"t1").send_keys("B")
time.sleep(2)
