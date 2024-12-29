list1=[0,1,-2,4,-3,7]
list2=[n for n in list1 if n>0]
print(list1)
print(list2)

list1=[0,1,-2,4,-3,7]
list2=list(filter(lambda n:n>0,list1))
print(list1)
print(list2)
