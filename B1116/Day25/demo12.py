import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self,driver):
        self.__UN = (By.ID, "input-username")
        self.__PW = (By.ID, "input-password")
        self.__GO = (By.NAME, "login-button")

    def set_user_name(self,un):
        driver.find_element(*self.__UN).send_keys(un)

    def set_password(self,pw):
        driver.find_element(*self.__PW).send_keys(pw)

    def click_go_button(self):
        driver.find_element(*self.__GO).click()


driver=Chrome()
driver.get("https://pos.aksharatraining.in/pos/public/")
login_page=LoginPage(driver)
login_page.set_user_name("admin")
login_page.set_password("pointofsale")
login_page.click_go_button()
time.sleep(2)