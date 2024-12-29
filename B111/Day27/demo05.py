

class Employee:
    def __init__(self,id,name,ph):
        self.id=id
        self.name=name
        self.ph=ph

    def print_emp_details(self):
        print("id=>",self.id,"name=>",self.name,"ph=>",self.ph)

E1=Employee(123,"vijay","911")
E1.print_emp_details()
