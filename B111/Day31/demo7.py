class A:
    def __init__(self,n):
        print('UDC of A with param:',n)

class B(A):
    def __init__(self,p):
        print('UDC of B with param:',p)


obj2=B(10)