class A:
    x=10    #class variable

    def __init__(self):
        self.y=20  #instance variable


    #need a m1 method to access only instance variable
    def m1(self):
        print(self.y)

    #need a m2 method to access only class variable
    @classmethod
    def m2(cls):
        print(cls.x,A.x)

     #need a m3 method to access both    instance & class variable
    def m3(self):
        print(A.x,self.x)
        print(self.y)

    #need a method m4 -but dont want to access any variable
    @staticmethod
    def m4(p):
        print('Hi',p)

#call m1 method
obj1=A()
obj1.m1()

A.m2()

obj1.m3()

A.m4(40)