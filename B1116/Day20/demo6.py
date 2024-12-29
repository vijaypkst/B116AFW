import time
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

options = Options()
options.set_preference("permissions.default.desktop-notification", 2)  # 1 allow 2 block
driver = Firefox(options=options)

driver.get("https://pushalert.co/demo")
driver.maximize_window()
time.sleep(2)

try:
    driver.find_element(By.XPATH, "//a[text()='Later']").click()
except:
    print('HTML Popup is not displayed')

time.sleep(2)
driver.find_element(By.ID, "send-button").click()
time.sleep(2)

try:
    print(driver.find_element(By.ID, 'pa_class-blocked-info').text)
except:
    print('Blocked Msg Popup is not displayed')

time.sleep(10)

driver.quit()