 a=[10,20,30,40]
print(a) #10 20 30 40

a.remove(20)
print(a) #10 30 40

a=[10,20,30,30,40,30]
print(a)
a.remove(30)
print(a)

a.remove(50)
print(a) #ValueError: list.remove(x): x not in list