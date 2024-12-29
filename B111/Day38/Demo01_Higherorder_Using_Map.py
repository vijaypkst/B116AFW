list1=[1,2,3,4]
list2=[]
for n in list1:
    list2.append(n*2)

print(list1)
print(list2)

list1=[1,2,3,4]
list2=[n*2 for n in list1]
print(list1)
print(list2)

def double_it(n):
    return n*2

list2=list(map(double_it,list1))
print(list1)
print(list2)