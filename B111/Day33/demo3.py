from abc import ABC,abstractmethod
class Animal(ABC): #Abstract class--> incomplete class--> we cant create object
    @abstractmethod
    def make_sound(self):       #only header --> only declaration--> abstract method--> incomplete method
        pass


class Dog(Animal): #Concrete class -complete class-normal class--> we can create object
    def make_sound(self): #header + body --> declaration+ implementation--> concrete method-complete method
        print('Bow Bow')


d1=Dog()
d1.make_sound()
