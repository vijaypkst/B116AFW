class A:
    @classmethod
    def m1(cls):
        print('this is m1 class method')
        A.__m2()

    @classmethod
    def __m2(cls):
        print('this is m2 class method')



A.m1()
# A.__m2()