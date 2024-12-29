import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import ChromiumOptions

options=ChromiumOptions()
prefs={"profile.default_content_setting_values.notifications":2} #1 allow notificaion; 2 block notificaion
options.add_experimental_option('prefs',prefs)

driver=Chrome(options)
driver.get("https://pushalert.co/demo")
driver.maximize_window()
time.sleep(2)
try:
    driver.find_element(By.XPATH,"//a[text()='Later']").click()
except:
    print('HTML Popup is not displayed')
time.sleep(2)
driver.find_element(By.ID,"send-button").click()
time.sleep(2)
try:
    print(driver.find_element(By.ID,'pa_class-blocked-info').text)
except:
    print('Blocked Msg Popup is not displayed')
time.sleep(4)