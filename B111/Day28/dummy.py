class A:
    class_variable=30

    def __init__(self):
        self.y=40

    def method1(self):
        print(self.y)

    @classmethod
    def bigmethod(cls):
        print(cls.class_variable,A.class_variable)


    @staticmethod
    def m4(p):
        print("Hi",p)

obj1 = A()
print(obj1.y)
print(obj1.class_variable)
print("Using class Name",A.class_variable)
obj1.bigmethod()
obj1.m4("ranga")