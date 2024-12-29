a=10
print(type(a),a)

b=[10,20]
print(type(b),b)

c=(10,20)
print(type(c),c)

d=10,20 #packing
print(type(d),d)

x=10
y=20
z=30
e=x,y,z #packing  --> storing multiple variable/val into a tuple
print(type(e),e)

p=e[0]
print(type(p),p)

p,q,r=e #unpacking --> storing elements of tuple into mulitple var
print(p,q,r)