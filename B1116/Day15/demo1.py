import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
driver=Chrome()
driver.get("https://aksharatraining.com/")
driver.maximize_window()
time.sleep(1)
#scroll down 1000 pixcels 5 times
for i in range(3):
    driver.execute_script("window.scrollBy(0,1000)") #selenium 3 & selenium 4
    time.sleep(1)

action=ActionChains(driver)
for i in range(3):
    action.scroll_by_amount(0,1000).perform() #only selenium 4
    time.sleep(1)

time.sleep(3)
driver.quit()