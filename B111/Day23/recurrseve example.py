def m1(i):
    if i<=0:
        print('End')
    else:
        print(i)
        i=i-1
        m1(i)

m1(10)

for i in range(10,0,-1):
    print(i)

i=10
while i>=1:
    print(i)
    i=i-1

