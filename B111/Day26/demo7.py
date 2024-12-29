class Student:
    def __init__(self,id,name):
        self.id=id
        self.name=name


s1=Student(1,'Akash')
print(s1.id,s1.name)
s2=Student(2,'Vijay')
print(s2.id,s2.name)


class School:
    def __init__(self,i,j):
        self.i=i
        self.j=j

m1=School(5,'rana')
print(m1.i,m1.j)
m1=School(6,'rana')
print(m1.i,m1.j)

class Tester:
    def __init__(self,k,l):
        self.k=k
        self.l=l

s1=Tester(1,"rs")
print(s1.k,s1.l)


