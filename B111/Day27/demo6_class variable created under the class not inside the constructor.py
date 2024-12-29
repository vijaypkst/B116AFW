class A:
    count=0
    def __init__(self):
        A.count=A.count+1


a1=A()
print(A.count) #1

a2=A()
print(A.count) #2

a3=A()
print(A.count) #3