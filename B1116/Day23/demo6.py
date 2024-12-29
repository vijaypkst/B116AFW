import time
from selenium.webdriver import Chrome
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as ChromeOptions
# driver=Chrome()
saucelab=""
chrome_options=ChromeOptions()

driver=Remote(command_executor=saucelab,options=chrome_options)
driver.get("https://aksharatraining.com/")
print(driver.title)
time.sleep(2)
driver.quit()
