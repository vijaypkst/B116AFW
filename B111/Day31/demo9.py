class Animal:
    def __init__(self,color):
        self.color=color

class Cat(Animal):
    def __init__(self,name,color):
        self.name=name
        Animal.__init__(self, color)



c1=Cat('kitty','white')
print(c1.name,c1.color)