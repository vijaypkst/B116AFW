class Emp:
    def __init__(self,id,name):
        self.id=id
        self.name=name

    def __str__(self):
        msg=str(self.id)+'-'+self.name
        return msg


e1=Emp(1,'Asha')
print(e1)

e2=Emp(2,'Bharath')
print(e2)