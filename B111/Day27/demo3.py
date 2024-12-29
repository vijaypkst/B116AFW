#create Student class with id and name
class Student:
    def __init__(self,id=0,name='Akshara'):
        self.id=id
        self.name=name


    def print_student_info(self):
        print(self.id, self.name)



s1=Student()
s1.print_student_info()

s2=Student(1)
s2.print_student_info()

s3=Student(name='Bhanu')
s3.print_student_info()

s4=Student(2,'Ravi')
s4.print_student_info()

