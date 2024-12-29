class Father:
    def marriage(self):
        print('arranged marriage')
    def property(self):
        print('Car, Home Land.. ')

class Son(Father):
    def marriage(self):
        print('love marriage')


s1=Son()
s1.property()
s1.marriage()



