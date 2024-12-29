class A:
    i=10

class B:
    i=20

class C(A,B):
    pass

print(A.i) #10
print(B.i) #20
print(C.i) #10
print(C.i) #10
print(C.i) #10

