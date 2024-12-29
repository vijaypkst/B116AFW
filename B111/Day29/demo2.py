class A:
    i=10 #public variable, it can be accessed from anywhere
    __j=20  #private variable , it can be accessible only inside the class, we cant access it outside of the class
    s=40
    __x=s

    @classmethod
    def m1(cls):
        print(cls.i)
        print(A.i)
        print(cls.__j)
        print(A.__j)
        print(A.__x)


print(A.i)
# print(A.__j)  Cannot access  private variable


#A.m1()

print(A.s)
A.s=200
A.m1()
