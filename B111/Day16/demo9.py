fruit_list=['Apple','Banana','Chiku','Mango','Orange','Papaya','Cherry','Grapes','Blueberry']
#print 1st to last elements of the list
for fruit in fruit_list:
    print(fruit)
print('-'*5)
#print last to 1st elements of the list
for fruit in reversed(fruit_list):
    print(fruit)
print('-' * 5)
#print elements of the list in sorted order (A-Z)
for fruit in sorted(fruit_list):
    print(fruit)
print('-' * 5)

#print elements of the list in reverse sorted order (Z-A)
for fruit in sorted(fruit_list,reverse=True):
    print(fruit)
print('-' * 5)

#print alternative elements for the list
for i in range(0,len(fruit_list),2):
    print(fruit_list[i])
print('-' * 5)