class Square:
    def findArea(self):
        print('to find area use a2')


class Rectangle(Square):
    def findArea(self):
        print('to find area use L x W')




shape1=Square()
shape1.findArea()

shape2=Rectangle()
shape2.findArea()