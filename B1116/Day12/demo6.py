import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
driver=Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(4)
login_button=driver.find_element(By.XPATH,"//button[@type='submit']")
c=login_button.value_of_css_property("color") #RGB
print(c)
print(Color.from_string(c).hex)

c=login_button.value_of_css_property("background-color")#RGB
print(c)
print(Color.from_string(c).hex)
time.sleep(1)
driver.quit()
