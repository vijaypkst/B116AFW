import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("http://www.google.com")
driver.maximize_window()
all_links=driver.find_elements(By.XPATH,"//a")
print("Number of links",len(all_links))

for link in all_links:
    print(link.text,link.is_displayed())