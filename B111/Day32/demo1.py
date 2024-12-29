class A:
    def __init__(self,p,q):
        self.i=p
        self.j=q


class B(A):
    def __init__(self,x,y=None):
       A.__init__(self,x,y)


obj=B(10)
print(obj.i,obj.j)

obj2=B(10,20)
print(obj2.i,obj2.j)