from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
class HomePage:

    def __init__(self, driver):
        self.__driver = driver
        self.__LOGOUT = (By.XPATH, "//a[text()='Logout']")

    def verify_home_is_displayed(self,wait):
        try:
            wait.until(expected_conditions.visibility_of_element_located( self.__LOGOUT))
            print('Home Page is dispalyed')
            return True
        except:
            print('Home Page is NOT dispalyed')
            return False