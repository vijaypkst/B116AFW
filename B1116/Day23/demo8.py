from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver import Remote
import time
options = FirefoxOptions()
options.browser_version = 'latest'
options.platform_name = 'Linux'
sauce_options = {}
sauce_options['username'] = ''
sauce_options['accessKey'] = ''
sauce_options['build'] = 'B123'
sauce_options['name'] = 'Akshara Login'
options.set_capability('sauce:options', sauce_options)

url = "https://ondemand.eu-central-1.saucelabs.com:443/wd/hub"
driver = Remote(command_executor=url, options=options)

# run commands and assertions
driver.get("https://aksharatraining.com/")
print(driver.title)
time.sleep(2)
driver.quit()
