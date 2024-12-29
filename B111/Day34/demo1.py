from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def m1(self):
        pass


class B(A):
    def m1(self):
        print('body of m1')


obj=B()
obj.m1()