a=[10,3,12]
b=a  #both variable pointing to same list
print(id(a))
print(id(b))

print(a)
print(b)

a.sort()
print(a)
print(b)

a=[10,3,12]
b=a.copy()  #list is copied to another variable
print(id(a))
print(id(b))

print(a)
print(b)

a.sort()
print(a)
print(b)
