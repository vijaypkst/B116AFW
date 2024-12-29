class A:

    def __init__(self):
        self.name="Bhanu"

    def m1(self):
        print('this is m1 method')

    def m2(self):
        return "akshara"

    @property
    def m3(self):
        return "akshara"

#A--> class
#name--> instance variable (attribute)
#m1--> instance method

obj1=A()
print(obj1.name)
obj1.m1()

v=obj1.m2()
print(v)

v=obj1.m3
print(v)
