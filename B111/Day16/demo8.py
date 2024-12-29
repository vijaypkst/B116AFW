fruit_list=['Apple','Banana','Chiku','Mango','Orange','Papaya','Cherry','Grapes','Blueberry']
for fruit in fruit_list:
    print(fruit)

print('-'*5)

for index in range(len(fruit_list)):
    print(fruit_list[index])

print('-'*5)

for index in range(0,len(fruit_list),2):
    print(fruit_list[index])

print('-'*5)

for index in range(len(fruit_list)-1,-1,-1):
    print(fruit_list[index])

print('-'*5)

for fruit in reversed(fruit_list):
    print(fruit)

print('-'*5)