a={"apple":10,"mango":20}
b=a
b['apple']=15

print(a)
print(b)

a={"apple":10,"mango":20}
b=a.copy()
b['apple']=15

print(a)
print(b)