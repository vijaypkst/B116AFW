class Emp:
    def __init__(self,id,name):
        self.id=id
        self.name=name


e1=Emp(1,'Akash')
e2=Emp(1,'Akash')
e3=e1
print(e1)
print(e2)
print(e3)
print(e1==e2)
print(e1==e3)