import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://aksharatraining.com/")
driver.maximize_window()
time.sleep(4)
y=driver.find_element(By.XPATH,"//h2[text()='Join the revolution!']").location['y']
y=y-150
y=str(y)
# driver.execute_script("window.scrollBy(0,2692)")

js="window.scrollBy(0,"+y+")"
print(js)
driver.execute_script(js)
time.sleep(6)
