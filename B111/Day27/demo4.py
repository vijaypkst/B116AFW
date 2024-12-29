#create Employee class with id,name &ph
#create a method to print Emp details

class Emp:
    def __init__(self,id:int,name:str,ph:int):
        self.id=id
        self.name=name
        self.ph=ph

    def print_emp_details(self):
        print('id->',self.id,'name->',self.name,'ph->',self.ph)


e1=Emp(1,'Bhanu',9481787493)
e1.print_emp_details()

e2=Emp('a',1,True)
e2.print_emp_details()
