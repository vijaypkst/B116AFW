import time
from selenium.webdriver import Chrome

#scroll to the bottom of the page
driver=Chrome()
driver.get("https://aksharatraining.com/")
driver.maximize_window()
time.sleep(4)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

time.sleep(5)
driver.quit()