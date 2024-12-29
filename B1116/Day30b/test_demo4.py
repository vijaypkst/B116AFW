import pytest
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver import Edge
@pytest.fixture(params=['chrome'])
def browser(request):
    browser_type = request.param
    print('Opening the browser',browser_type)
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
    driver.get('http://www.google.com')
    print(driver.title)
