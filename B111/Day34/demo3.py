from abc import ABC,abstractmethod
class A:
    i=10
    def __init__(self):
        self.j=20

    @classmethod
    def m1(cls):
        print('class method of A')

    @staticmethod
    def m2():
        print('static method of A')

    def m3(self):
        print('instance method of A')

print(A.i)
A.m1()
A.m2()
obj=A()
print(obj.j)
obj.m3()

class B(ABC):
    i=10
    def __init__(self):
        self.j=30

    @classmethod
    def m1(cls):
        print('class method of B')

    @staticmethod
    def m2():
        print('static method of B')

    def m3(self):
        print('instance method of B')

print(B.i)
B.m1()
B.m2()
class C(B):
    pass


obj=C()
print(obj.j)
obj.m3()