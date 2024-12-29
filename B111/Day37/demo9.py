list1=[0,1,-2,4,-3,7]
list2=[n for n in list1 if n>0] #copy positve numbers from list1 to list2
print(list2)

def ispositive(n):
    return n>0
# print(ispositive(3)) #True
# print(ispositive(-3)) #False


list1=[0,1,-2,4,-3,7]
list2=list(filter(ispositive,list1))
print(list2)
