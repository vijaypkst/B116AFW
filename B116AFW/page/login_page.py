from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.__driver=driver
        self.__UN = (By.NAME, "input-username")
        self.__PW = (By.NAME, "input-password")
        self.__LN = (By.NAME, "login-button")