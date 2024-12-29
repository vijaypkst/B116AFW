import pytest
from selenium.webdriver import Chrome
from selenium.webdriver import Edge
from selenium.webdriver.support.ui import WebDriverWait
from pyjavaproperties import Properties
class BaseClass:
    @pytest.fixture(autouse=True)
    def precondition(self):

        print('Read data from config.properties')
        pptobj=Properties()
        pptobj.load(open('./../config.properties'))
        browser=pptobj['BROWSER']
        app_url=pptobj['APPURL']
        ito=pptobj['ITO']
        eto=pptobj['ETO']

        if browser.lower() =='chrome':
            print('Open the Chrome Browser')
            self.driver = Chrome()
        else:
            print('Open the Edge Browser')
            self.driver = Edge()

        print('maximize the browser')
        self.driver.maximize_window()
        print('Enter the URL:',app_url)
        self.driver.get(app_url)
        print('Set ITO:',ito)
        self.driver.implicitly_wait(ito)
        print('Set ETO:',eto)
        self.wait=WebDriverWait(self.driver,eto)

    @pytest.fixture(autouse=True)
    def postcondition(self):
        yield
        print('\nClose the browser')
        self.driver.quit()
