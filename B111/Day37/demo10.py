set1={1,2,3,4,5,6,7,8}
list2=[n for n in set1 if n%2==0]
print(list2)

def iseven(n):
    return n%2==0

set1={1,2,3,4,5,6,7,8}
list2=list(filter(iseven,set1))
print(list2)
