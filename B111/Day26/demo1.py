class MyClass:
    pass

obj1=MyClass()

print(id(obj1))

def m1():
    print('displaying out side the class')

class A:
    def m2(self):
        print('Inside the Class and method')


m1()

obj2=A()
obj2.m2()