a=[10,20]
b=[30,40]
a.append(b)  #append list to list a
print(a)
x=a[0]
print(type(x),x)

x=a[1]
print(type(x),x)

x=a[2]
print(type(x),x)

y=x[0]
print(type(y),y) #int 30

z=x[1]
print(type(z),z) #int 40

# x=a[2]
# z=a[2][1]
print(a[2][1]) #int 40

print(a[2][0])