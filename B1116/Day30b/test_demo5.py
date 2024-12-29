import time

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By


@pytest.fixture(params=['chrome','Edge'])
def browser(request):
    browser_type = request.param
    print('Opening the',browser_type,'browser')
    if browser_type=='chrome':
        driver=Chrome()
    elif browser_type=='firefox':
        driver=Firefox()
    else:
        driver=Edge()

    yield driver
    driver.quit()

def test_google(browser):
    driver=browser
    driver.get('https://pos.aksharatraining.in/pos/public/')
    print(driver.title)
    for i in range(10):
        driver.find_element(By.ID,'input-username').send_keys('bhanu')
        time.sleep(1)
        driver.find_element(By.ID, 'input-username').clear()

