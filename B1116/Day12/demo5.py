import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
login_button=driver.find_element(By.XPATH,"//button[@type='submit']")
c=login_button.value_of_css_property("color") #RGB
print(c)

c=login_button.value_of_css_property("background-color")#RGB
print(c)

