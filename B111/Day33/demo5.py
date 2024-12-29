from abc import ABC
from abc import abstractmethod

class Animal(ABC): #Abstract class
    @abstractmethod
    def makesound(self):    #abtract method
        pass


class Dog(Animal):  #Concrte class
    def makesound(self): #concrete method
        print('Bow Bow')


class Cat(Animal):
    def makesound(self):
        print('Meow Meow')

class Cow(Animal):
    def makesound(self):
        print('Amba')


d1=Dog()
d1.makesound()

c1=Cat()
c1.makesound()

t1=Cow()
t1.makesound()


