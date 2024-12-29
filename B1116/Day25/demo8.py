import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

class A:
    __locator=(By.ID,"input-username")

    def __init__(self,driver):
        self.__un = driver.find_element(*self.__locator)

    def set_user_name(self):
        self.__un.send_keys("admin")


driver=Chrome()
driver.get("https://pos.aksharatraining.in/pos/public/")
obj=A(driver)
obj.set_user_name()
time.sleep(2)