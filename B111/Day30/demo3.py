class A:
    pass
    def m1(self):
        print('instance method m1')

    @classmethod
    def m2(cls):
        print('class method m2')

    @staticmethod
    def m3():
        print('static method m3')

    @staticmethod
    def __m4():
        print('private static method m4')

class B(A):
   pass

obj=B()
obj.m1()
B.m2()
B.m3()
