a={"apple":10,"mango":20}
print(a)
a['apple']=15   #key is present hence overrite it
print(a)

a['chiku']=30 #key is not present hence add it
print(a)

a={"apple":10,"mango":20}
print(a)
a.setdefault('apple',15) #if key is present dont change
print(a)
a.setdefault('chiku',30) #if key is not present so add it
print(a)
a.setdefault('chiku',0) #if key is not present so add it
print(a)