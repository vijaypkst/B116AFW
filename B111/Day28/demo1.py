class Emp:
    company='TCS'           #class variable
    def __init__(self,name):
        self.name=name      #instance variable



# Emp.company='IBM'
print(Emp.company)

e1=Emp('Bhanu')
e1.name='Bhanu Prakash'
e1.company="Overwrite" #not recemended
print(e1.name)
print(e1.company)

e2=Emp('Ravi')
print(e2.name)
print(e2.company)