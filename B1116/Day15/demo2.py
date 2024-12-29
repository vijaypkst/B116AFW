import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://news.google.com/")
driver.maximize_window()
time.sleep(4)

your_topics=driver.find_element(By.XPATH,"//h2[text()='Sources']")
# y=your_topics.location['y']
#
# js="window.scrollBy(0,"+str(y)+")"
# driver.execute_script(js)
action=ActionChains(driver)
action.scroll_to_element(your_topics).perform()

time.sleep(4)