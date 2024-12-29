import time
from selenium.webdriver import Chrome
# open the browser
# enter fb.com
# open another tab
# enter google.com
# close google tab
# close fb tab

driver=Chrome()
time.sleep(3)
driver.get("http://www.fb.com")
time.sleep(3)
driver.switch_to.new_window("tab")
time.sleep(3)
driver.get("http://www.google.com")
time.sleep(3)
driver.close()
time.sleep(3)
driver.quit()