#print only upper case names
students=['AKASH','Bhumi','CHANDRA','RAVI','surya']

for name in students:
    if name.isupper()==True:
        print(name)
print('-'*5)

for name in students:
    if name.isupper():
        print(name)
print('-'*5)

for name in students:
    if not(name.isupper()):
        continue
    print(name)