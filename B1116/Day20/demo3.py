import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import ChromiumOptions

options=ChromiumOptions()
options.add_argument("--disable-notifications")
driver=Chrome(options)
driver.get("https://www.irctc.co.in/nget/train-search")
time.sleep(7)