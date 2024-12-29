class Student1:
    pass

s1=Student1()
print(s1)
print(s1.__str__())

class Student2:
    def __str__(self):
        return 'ph number'

s2=Student2()
print(s2)
print(s2.__str__())