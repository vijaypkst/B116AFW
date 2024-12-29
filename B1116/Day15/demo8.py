import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver=Chrome()
driver.get("https://www.globalsqa.com/")
driver.maximize_window()

time.sleep(2)

action=ActionChains(driver)

main_menu=driver.find_element(By.XPATH,"(//a[text()='Tester’s Hub'])[1]")
action.move_to_element(main_menu).perform() #mouse hover--> we get drop down menu
time.sleep(1)

sub_menu=driver.find_element(By.XPATH,"//span[text()='Demo Testing Site']")
action.move_to_element(sub_menu).perform() #mouse hover
time.sleep(1)

driver.find_element(By.XPATH,"//span[text()='Tooltip']").click()
time.sleep(5)
driver.quit()