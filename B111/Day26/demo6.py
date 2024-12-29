class Emp:
    def __init__(self,n):
        self.name=n


e1=Emp('Mohandas')
e2=e1
e3=e2

e3.name='Ravi'# overwriting

print(e1.name) #M
print(e2.name) #M
print(e3.name) #R