class A:
    def __init__(self,n):
        print('UDC-P',n)

class B(A):
    def __init__(self):
        print('UDC')


obj2=B()