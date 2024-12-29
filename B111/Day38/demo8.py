def double_it(n):
    return n*2

print(double_it(10))

double_it=lambda n:n*2
print(double_it(10))


def to_upper(s):
    return s.upper()
print(to_upper('bhanu'))

to_upper=lambda s:s.upper()
print(to_upper('bhanu'))


def addjuice(fruit):
    return fruit+' juice'
print(addjuice('Apple'))

addjuice=lambda fruit:fruit+' juice'
print(addjuice('Apple'))

def addclass(sub):
    return sub+' class'

print(addclass('Python'))

addclass=lambda sub:sub+' class'
print(addclass('Python'))
