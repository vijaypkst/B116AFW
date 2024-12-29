import time

from selenium.webdriver import Chrome
from Screenshot import Screenshot
driver=Chrome()
driver.get("https://aksharatraining.com/")
driver.maximize_window()
time.sleep(1)
ssobj=Screenshot.Screenshot()
ssobj.full_screenshot(driver,"./../my_images","aksharafullpage.png")
time.sleep(1)
driver.quit()
