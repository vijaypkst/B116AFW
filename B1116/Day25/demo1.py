#encapsulation
#binding data member with member function
class A:
    __i=None  #1 declaration

    def __init__(self,v):
        self.__i=v #2 initialization

    def get_value(self):
        print(self.__i) #3 utilization


obj=A(10)
obj.get_value()
