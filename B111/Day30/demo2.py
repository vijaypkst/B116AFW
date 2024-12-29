class A:
    x=5
    __i=10
    @classmethod
    def print_value(cls):
        print(A.x)
        print(A.__i)


class B(A):
    @classmethod
    def print_value(cls):
        print(B.x)


B.print_value()