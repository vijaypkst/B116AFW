from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def find_area(self):
        pass


class Square(Shape):
    def find_area(self):
        print('Area of Square:L2')


class Rectangle(Shape):
    def find_area(self):
        print('Area of Rectangle:LxB')

class Triangle(Shape):
    def find_area(self):
        print('Area of Triangle:1/2 x H x B')

class Circle(Shape):
    def find_area(self):
        print('Area of Circle:22/7*r*r')

all_shapes=[Square(),Rectangle(),Triangle(),Circle(),Square(),Triangle()]
for shape in all_shapes:
    shape.find_area()