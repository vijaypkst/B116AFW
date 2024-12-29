import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
#<a id="a1" name="n1" class="c1" title="click me" href="http://www.google.com">Google</a>
driver=Chrome()
driver.get("file:///E:/B116_8.30PM_Selenium(Py)/share/page/Sample3.html")
time.sleep(2)
driver.find_element(By.NAME,'n1').click()
time.sleep(2)
driver.quit()