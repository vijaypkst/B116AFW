class A:
    def m1(self):
     pass

obj1=A()
obj1.m1()

from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def m1(self):
        pass


obj1=A()
obj1.m1()


