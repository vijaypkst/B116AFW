import time
from selenium.webdriver.firefox.options import Options
from selenium import webdriver

firefox_option=Options()
firefox_option.set_preference("dom.webnotifications.enabled",False)
driver=webdriver.Firefox(options=firefox_option)
driver.get("https://www.irctc.co.in/nget/train-search")
time.sleep(10)
