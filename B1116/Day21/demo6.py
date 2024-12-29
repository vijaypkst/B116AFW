import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver=Chrome()
driver.get("file:///E:/B116_8.30PM_Selenium(Py)/share/page/Sample13.html")
driver.maximize_window()
time.sleep(2)
listbox=driver.find_element(By.ID,"A1")
select=Select(listbox)
time.sleep(1)
select.select_by_index(1)
time.sleep(1)
select.select_by_value("c")
time.sleep(2)
select.select_by_visible_text("Delhi")
time.sleep(2)
