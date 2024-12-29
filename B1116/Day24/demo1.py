import time
from selenium.webdriver import Chrome
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as ChromeOptions
# driver=Chrome()
our_grid_url="http://192.168.29.187:4444"
chrome_options=ChromeOptions()

driver=Remote(command_executor=our_grid_url,options=chrome_options)
driver.get("https://aksharatraining.com/")
print(driver.title)
time.sleep(2)
driver.quit()
