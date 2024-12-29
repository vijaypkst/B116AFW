class A:
    i=10

class B(A):
    j=30

class C(B):
    pass
#multi level inheritance
print(A.i)
print(B.i)
print(C.i,C.j)