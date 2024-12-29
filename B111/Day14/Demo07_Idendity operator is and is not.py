a=[10,20,30]
b=a
c=a.copy()

print(id(a), a)
print(id(b),b)
print(id(c),c)

print( b is a) #True

print( c is a) #False

print( b is not a) #False

print( c is not a) #True