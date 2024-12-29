class Person:
    def __init__(self,name):
        self.name=name


class Student(Person):
    def __init__(self,name,sub):
        Person.__init__(self,name) #calling parent class constructor from child class contructor
        self.sub = sub


# p1=Person('Ravi')
# print(p1.name)

s1=Student('Kumar','selenium')
print(s1.name,s1.sub)

