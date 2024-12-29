class A:
    __j=100

    @classmethod
    def getvalue(cls):
        return A.__j


v=A.getvalue()
print(v)



