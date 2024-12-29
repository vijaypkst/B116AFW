from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
from selenium.webdriver import Chrome
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as ChromeOptions
chrome_options = FirefoxOptions()
chrome_options.browser_version = 'latest'
chrome_options.platform_name = 'Linux'
sauce_options = {}
sauce_options['username'] = 'oauth-vijay.pkst-ee069'
sauce_options['accessKey'] = '2d519378-3a5c-429e-a164-c495245cd7af'
sauce_options['build'] = '<B2024>'
sauce_options['name'] = '<Akshara Login>'
chrome_options.set_capability('sauce:options', sauce_options)

url = "https://oauth-vijay.pkst-ee069:2d519378-3a5c-429e-a164-c495245cd7af@ondemand.eu-central-1.saucelabs.com:443/wd/hub"

driver = Remote(command_executor=url, options=chrome_options)
# run commands and assertions
driver.get("https://www.saucedemo.com")
title = driver.title
titleIsCorrect = "Swag Labs" in title
jobStatus = "passed" if titleIsCorrect else "failed"

# end the session
driver.execute_script("sauce:job-result=" + jobStatus)
driver.quit()