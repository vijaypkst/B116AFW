from abc import ABC,abstractmethod

class MyCar(ABC): #Abstract Class
    @abstractmethod
    def wheels(self):
        pass
    @abstractmethod
    def body(self):
        pass

    @abstractmethod
    def engine(self):
        pass

    @abstractmethod
    def interiors(self):
        pass

class level1(MyCar):#Abstract Class
    def wheels(self):
        print('Car has 4 wheels')

class level2(level1):#Abstract Class
    def body(self):
        print('Car has solid body')

class level3(level2):#Abstract Class
    def engine(self):
        print('Car has solid engine')

class final(level3):#Concrete Class
    def interiors(self):
        print('Car has interiors')

car=final()
car.wheels()
car.body()
car.engine()
car.interiors()
