list1=[1,2,3,4,5,6,7,8]
list2=list()

for n in list1:
    if n%2==0:
        list2.append(n)

print(list1)
print(list2)

list3=[n for n in list1 if n%2==0]
print(list3)

list4=[n for n in list1 if n%2==1]
print(list4)