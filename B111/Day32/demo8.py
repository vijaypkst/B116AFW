class Emp:
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
    def __str__(self):
        msg=str(self.id)+'-'+self.name+'-'+str(self.age)
        return msg

    def __gt__(self, other): #gt -->greater than
        age1=self.age
        age2=other.age
        return age1>age2

e1=Emp(1,'Surya',35)
e2=Emp(2,'Chandra',30)

print(e1>e2)