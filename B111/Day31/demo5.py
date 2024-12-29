class A:
    pass

class B(A):
    pass


obj1=A()
`obj2=B()
# both A & B has default constructor

class C:        #default constructor
    pass

class D(C):
    def __init__(self): # has no arg UDC
        print('UDC1')

obj3=C()
obj4=D()

class E:
    pass

class F(E):
    def __init__(self,n): # has parameterized UDC
        print('UDC1',n)

obj5=E()
obj6=F(10)