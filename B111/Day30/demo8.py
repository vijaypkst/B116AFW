#hybrid inheritance
class A:
    i=10

class B(A):
    pass

class C(A):
   pass

class D(B,C):
    pass


print(A.i)
print(B.i)
print(C.i)
print(D.i)



