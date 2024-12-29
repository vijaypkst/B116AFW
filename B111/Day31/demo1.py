

class A:
    i=10

obj=A()
print(obj)
print(obj.__str__())  #print address of the object in string format
print(obj.__dir__()) #print all the members of the class 

