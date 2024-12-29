import time
from selenium.webdriver import Remote
from selenium.webdriver.firefox.options import Options as FirefoxOptions

our_grid_url="http://192.168.29.187:4444"
firefox_options=FirefoxOptions()

driver=Remote(command_executor=our_grid_url,options=firefox_options)
driver.get("https://aksharatraining.com/")
print(driver.title)
time.sleep(2)
driver.quit()
