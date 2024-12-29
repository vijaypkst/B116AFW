import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

def search(driver):
    time.sleep(2)
    driver.find_element(By.ID, "APjFqb").send_keys("selenium")
    time.sleep(2)
    all_AS = driver.find_elements(By.XPATH, "//span[contains(text(),'selenium')]")
    return all_AS


driver=Chrome()
driver.get("http://www.google.com")
driver.maximize_window()
time.sleep(2)
all_AS=search(driver)
all_AS[0].click() #select 1st
time.sleep(2)
driver.back()
time.sleep(2)
all_AS=search(driver)
all_AS[-1].click()#select last
time.sleep(3)
driver.quit()
#home work
#accept option to select from the user
#if it is present select it, if it is not present print 'not present

