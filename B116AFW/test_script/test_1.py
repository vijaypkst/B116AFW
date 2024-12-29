from generic.base_class import BaseClass
from generic.utility import Utility
class Test1(BaseClass):
    def test_1(self):
        print('title is',self.driver.title)
        data=Utility.get_xldata(self.xl_path,'Sheet1',1,1)
        print('Data from xl is',data)
