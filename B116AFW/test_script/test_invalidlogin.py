import pytest

from generic.base_class import BaseClass
from generic.utility import Utility
from page.login_page import LoginPage
from page.home_page import HomePage
class Test_InValidLogin(BaseClass):
    @pytest.mark.run(order=2)
    def test_valid_login(self):
        un = Utility.get_xldata(self.xl_path,"Invalid_login",2,1)
        pw = Utility.get_xldata(self.xl_path, "Invalid_login", 2, 2)
    # 1. enter valid un
        login_page=LoginPage(self.driver)
        login_page.set_username(un)

    # 2. enter valid pw
        login_page.set_password(pw)
    # 3. click on go button
        login_page.click_go_button()
    # 4. verify that home page is displayed
        result = login_page.verify_err_is_displayed(self.wait)
        assert result
