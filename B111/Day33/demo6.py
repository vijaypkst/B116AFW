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
        print('Amba Amba Amba')


all_animal=[Dog(),Cat(),Cow()]

for animal in all_animal:
    animal.makesound()

