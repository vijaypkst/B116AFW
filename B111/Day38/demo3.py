list1=['Apple','Mango','Grape']
list2=list()
for fruit in list1:
    item=fruit+' juice'
    list2.append(item)

print(list1)
print(list2)


list1=['Apple','Mango','Grape']
list2=[fruit+' juice' for fruit in list1]
print(list1)
print(list2)

def addjuice(fruit):
    return fruit+' juice'

list1=['Apple','Mango','Grape']
list2=list(map(addjuice,list1))
print(list1)
print(list2)

