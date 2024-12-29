#create Student class with id and name
class Student:
    def __init__(self, ids, name):
        self.id=ids
        self.name=name



s1=Student(1,'Asha')
print(s1.id,s1.name)

s2=Student(2,'Bhargav')
print(s2.id,s2.name)
