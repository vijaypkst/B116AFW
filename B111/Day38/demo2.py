#convert list1 element to upper case and add it to list2
list1=['Apple','Mango','Grapes','Tomato']
list2=[]
for fruit in list1:
    list2.append(fruit.upper())

print(list1)
print(list2)

list1=['Apple','Mango','Grapes','Tomato']
list2=[fruit.upper() for fruit in list1]
print(list1)
print(list2)


def to_upper(s):
    return s.upper()

list2=list(map(to_upper,list1))
print(list1)
print(list2)
