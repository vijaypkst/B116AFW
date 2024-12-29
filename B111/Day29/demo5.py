class A:
    p=10
    _x=40000 #this is still a public class variable
    __i=10

    def __init__(self):
        self.__j=20

    @classmethod
    def print_i(cls):
        print(cls.__i)

    def print_j(self):
        print(self.__j)



A.print_i()
print(A._x)
obj=A()
obj.print_j()
