import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver=Chrome()
driver.get("https://www.globalsqa.com/")
driver.maximize_window()

time.sleep(2)
menu=driver.find_element(By.XPATH,"(//a[text()='Free Ebooks'])[1]")
action=ActionChains(driver)
action.move_to_element(menu).perform() #mouse hover--> we get drop down menu
time.sleep(2)
driver.find_element(By.XPATH,"//span[text()='Free Machine Learning Ebooks']").click()
time.sleep(5)
driver.quit()