import pytest

from generic.base_class import BaseClass
from generic.utility import Utility
from page.login_page import LoginPage
from page.home_page import HomePage
class Test_ValidLogin(BaseClass):
    @pytest.mark.run(order=1)
    def test_valid_login(self):
        un = Utility.get_xldata(self.xl_path,"valid_login",2,1)
        pw = Utility.get_xldata(self.xl_path, "valid_login", 2, 2)
    # 1. enter valid un
        login_page=LoginPage(self.driver)
        login_page.set_username(un)


    # 2. enter valid pw
        login_page.set_password(pw)
    # 3. click on go button
        login_page.click_go_button()
    # 4. verify that home page is displayed
        home_page=HomePage(self.driver)
        result=home_page.verify_home_is_displayed(self.wait)
        assert result
