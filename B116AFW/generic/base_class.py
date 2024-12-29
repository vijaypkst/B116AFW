import os.path
import pytest
from selenium import  webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver import Chrome
from selenium.webdriver import Edge
from selenium.webdriver.support.ui import WebDriverWait
from pyjavaproperties import Properties

class BaseClass:
    @pytest.fixture(autouse=True)
    def precondition(self):
        generic_path=os.path.dirname(__file__)
        config_path=generic_path+'/../config.properties'
        print('path of config.properties',config_path)

        self.xl_path=generic_path+'/../data/input.xlsx'
        print('xl path is',self.xl_path)

        print('Read data from config.properties')
        pptobj=Properties()
        pptobj.load(open(config_path))
        grid=pptobj['GRID']
        grid_url=pptobj['GRIDURL']
        browser=pptobj['BROWSER']
        app_url=pptobj['APPURL']
        ito=pptobj['ITO']
        eto=pptobj['ETO']

        if grid.lower()=='no':
            if browser.lower() == 'chrome':
                print('Open the Chrome Browser in Remote System',grid_url)
                chrome_options=ChromeOptions()
                self.driver =webdriver.Remote(command_executor=grid_url,options=chrome_options)
            else:
                print('Open the Edge Browser in Remote System',grid_url)
                edge_options=EdgeOptions()
                self.driver = webdriver.Remote(command_executor=grid_url, options=edge_options)
        else:
            if browser.lower() =='chrome':
                print('Open the Chrome Browser in Local System')
                self.driver = Chrome()
            else:
                print('Open the Edge Browser in Local System')
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
        print('Close the browser')
        self.driver.quit()
