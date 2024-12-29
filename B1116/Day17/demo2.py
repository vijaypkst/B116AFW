import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver=Chrome()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
time.sleep(2)
xp="//span[text()='right click me']"
button=driver.find_element(By.XPATH,xp)

action=ActionChains(driver)
action.context_click(button).perform()
time.sleep(2)
edit=driver.find_element(By.XPATH,"//span[text()='Edit']")
action.move_to_element(edit).perform()
time.sleep(2)
edit.click()
time.sleep(2)
alert=driver.switch_to.alert
print(alert.text)
alert.accept()
time.sleep(2)
driver.quit()