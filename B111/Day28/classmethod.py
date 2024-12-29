class A:
    x=10
    y=20

    @classmethod   #decorator
    def print_details(cls):
        print(cls.x)
        print(cls.y)



A.print_details()