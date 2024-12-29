class Emp:
    company='TCS'           #class variable
    def __init__(self,name):
        self.name=name      #instance variable

    def m1(self):       #instance method
        print(self.name)
        print(Emp.company)




e1=Emp('Ravi')
e1.m1()

e2=Emp('Asha')
e2.m1()