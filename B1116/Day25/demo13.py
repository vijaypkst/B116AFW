import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self,driver):
        self.__UN = (By.NAME, "username")
        self.__PW = (By.NAME, "password")
        self.__LN = (By.XPATH, "//button[@type='submit']")

    def set_user_name(self,un):
        driver.find_element(*self.__UN).send_keys(un)

    def set_password(self,pw):
        driver.find_element(*self.__PW).send_keys(pw)

    def click_login_button(self):
        driver.find_element(*self.__LN).click()


driver=Chrome()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
login_page=LoginPage(driver)
login_page.set_user_name("admin")
login_page.set_password("admin123")
login_page.click_login_button()
time.sleep(7)