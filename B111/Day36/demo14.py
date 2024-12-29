list1=['Akash','Akshara','Rashmi','Bhumi','Ashwin']

list2=list()

for name in list1:
    if name.startswith('A'):
        list2.append(name)


print(list2)

list3=[name for name in list1  if name.startswith('A') ]
print(list3)