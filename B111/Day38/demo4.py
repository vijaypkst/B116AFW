list1=['Python','Selenium','API']
list2=list()
for sub in list1:
    list2.append(sub+" class")

print(list1)
print(list2)



list2 = [sub +" -class " for sub in list1]
print(list2)

def AddClass(c):
    return c+"--Class"

list3=list(map(AddClass,list1))
print(list3)