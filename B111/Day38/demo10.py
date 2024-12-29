set1={1,2,3,4,5,6,7,8}
list2=[n for n in set1 if n%2==0]
print(list2)

set1={1,2,3,4,5,6,7,8}
list2=list(filter(lambda n:n%2==0,set1))
print(list2)