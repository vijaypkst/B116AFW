a =  [-1,2,3,4,5,6,7,8,9,13,14]
count=len(a)
for i in range(count):
    for j in range(i+1,count,1):
       f=a[i]
       n=a[j]
       if f+n==15:
           print(f,n)


