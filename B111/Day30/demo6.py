class A:
    i=10

class B:
    j=20

class C(A,B):
    pass

print(A.i)
print(B.j)
print(C.i)
print(C.j)