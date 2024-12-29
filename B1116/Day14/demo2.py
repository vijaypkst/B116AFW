import time
from a_selenium_screenshot_whole_page import get_screenshot_whole_page_with_scroll
from selenium.webdriver import Chrome

driver=Chrome()
driver.get("https://aksharatraining.com/")
driver.maximize_window()
time.sleep(1)
get_screenshot_whole_page_with_scroll(driver, sleepinterval=(5, 5), save_path='aksharawholepage.png')

time.sleep(1)
driver.quit()