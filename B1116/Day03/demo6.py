import time

from selenium.webdriver import Chrome
driver=Chrome()
driver.get("https://aksharatraining.com/")
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.fullscreen_window()
time.sleep(2)
driver.minimize_window()
time.sleep(2)
driver.quit()