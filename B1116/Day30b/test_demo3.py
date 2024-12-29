import pytest
from selenium.webdriver import Chrome
# example :using selenium in pytest
@pytest.fixture
def browser():
    driver=Chrome()
    yield driver
    driver.quit()

def test_google(browser):
    driver=browser
    driver.get('http://www.google.com')
    print(driver.title)
