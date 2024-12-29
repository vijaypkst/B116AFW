import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
driver=Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
login_button=driver.find_element(By.XPATH,"//button[@type='submit']")
font_type=login_button.value_of_css_property("font-family")
print(font_type)

font_size=login_button.value_of_css_property("font-size")
print(font_size)

driver.quit()
