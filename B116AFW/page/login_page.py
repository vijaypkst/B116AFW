from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class LoginPage:

    def __init__(self, driver):
        self.__driver = driver
        self.__UN = (By.ID, "input-username")
        self.__PW = (By.ID, "input-password")
        self.__GO = (By.NAME, "login-button")
        self.__errormsg =(By.XPATH,"//div[@class='error']")

    def set_username(self,un):
        self.__driver.find_element(*self.__UN).send_keys(un)

    def set_password(self,pw):
        self.__driver.find_element(*self.__PW).send_keys(pw)

    def click_go_button(self):
        self.__driver.find_element(*self.__GO).click()


    def verify_err_is_displayed(self, wait):
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.__errormsg))
            print('Err msg is dispalyed')
            return True
        except:
            print('Err msg is NOT dispalyed')
            return False