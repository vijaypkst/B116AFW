import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import  ChromeOptions
options = ChromeOptions()
options.add_experimental_option("detach", True)
driver=Chrome(options)
driver.get("file:///C:/Users/vijay/PycharmProjects/B1116/Page/SampleA.html")
time.sleep(1)
driver.switch_to.frame(0) #go inside the 1st frame-frame index
driver.find_element(By.ID,"t2").send_keys("A")
time.sleep(1)
driver.switch_to.parent_frame()
driver.find_element(By.ID,"t1").send_keys("A")
time.sleep(2)
driver.quit()