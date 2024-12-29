a={10,20,30}
b=a
a.add(40)

print(a)
print(b)

a={10,20,30}
b=a.copy()
a.add(40)

print(a)
print(b)