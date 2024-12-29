import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

class LoginPage:
    __UN=(By.ID,"input-username")

    def __init__(self,driver):
        self.__unTB = driver.find_element(*self.__UN)

    def set_user_name(self,un):
        self.__unTB.send_keys(un)


driver=Chrome()
driver.get("https://pos.aksharatraining.in/pos/public/")
login_page=LoginPage(driver)
login_page.set_user_name("bhanu")
time.sleep(2)