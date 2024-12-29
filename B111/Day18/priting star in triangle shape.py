#when i is 1, j loop executes 1 time
#when i is 2, j loop executes 2 times
#when i is n, j loop executes n times
for i in range(1,6):
    for j in range(1,i+1):
        print('*',end=' ')

    print()