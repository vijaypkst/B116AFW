import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("file:///C:/Users/vijay/PycharmProjects/B1116/Page/Sample4_same%20link.html")
driver.maximize_window()
time.sleep(1)

all_links=driver.find_elements(By.XPATH,"//a")
print(len(all_links))

for link in all_links:
    print(link.get_attribute("href"))



