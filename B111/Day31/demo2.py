
class Emp:
    company='TCS'

    def __init__(self):
        self.emp_name='Bhanu'

    def print_emp_name(self):
        print( self.emp_name)


obj=Emp()
print(obj.__dir__()) #print all variables and methods from Emp class (its own members + object class memebers)
