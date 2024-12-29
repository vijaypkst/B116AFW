class A:
    pass

obj1=A() #calling the constructor ,default constructor-no arg constructor

class B:
    def __init__(self): #it is user defined contructor--no arg constructor
        print('UDC')

obj2=B()

class C:
    def __init__(self,n): #it is user defined contructor-parameterized constructor
        print('UDC',n)

obj3=C(10)