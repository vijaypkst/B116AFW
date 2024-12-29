import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
#scroll to the specific element
driver=Chrome()
driver.get("https://news.google.com/")
driver.maximize_window()
time.sleep(2)
your_topics=driver.find_element(By.XPATH,"//h2[text()='Your topics']")
y=your_topics.location['y']
y=y-150
print(y)
js="window.scrollBy(0,"+str(y)+")"
driver.execute_script(js)
time.sleep(20)
# driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
#
# time.sleep(5)

driver.quit()