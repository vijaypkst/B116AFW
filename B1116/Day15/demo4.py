import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
#homework: print color of the box before and after double click
driver=Chrome()
driver.get("https://www.plus2net.com/javascript_tutorial/ondblclick-demo.php")
driver.maximize_window()

time.sleep(2)
print(driver.find_element(By.ID,"box").text)

button=driver.find_element(By.XPATH,"//input[@value='Double Click']")

action=ActionChains(driver)
action.double_click(button).perform()

time.sleep(2)
print(driver.find_element(By.ID,"box").text)

time.sleep(5)