
#create Student class with id and name
class Student:
    def __init__(self,id=0,name='Akshara'):
        self.id=id
        self.name=name


s1=Student() #no id name
print(s1.id,s1.name)

s2=Student(1) #only id no name
print(s2.id,s2.name)

s3=Student(name='Bhanu') #only name , no id
print(s3.id,s3.name)

s4=Student(2,'Ravi')
print(s4.id,s4.name)

# s4=Student(3,'Kumar','Pune','Wakad')

