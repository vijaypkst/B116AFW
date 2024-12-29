import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver=Chrome()
driver.get("http://www.dhtmlgoodies.com/submitted-scripts/i-google-like-drag-drop/")
driver.maximize_window()

time.sleep(3)
block1=driver.find_element(By.XPATH,"//h1[text()='Block 1']")
block3=driver.find_element(By.XPATH,"//h1[text()='Block 3']")

action=ActionChains(driver)
action.drag_and_drop(block1,block3).perform()
time.sleep(7)