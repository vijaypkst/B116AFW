list1=[1,2,3,4]
list2=[n*2 for n in list1]
print(list1)
print(list2)

list2=list(map(lambda n:n*2,list1))
print(list1)
print(list2)

