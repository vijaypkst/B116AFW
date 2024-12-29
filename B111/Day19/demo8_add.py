#find sum of n numbers example input 4 ouput : 1+2+3+4 --> 10
n=int(input('plz enter the number:'))
print('Sum of ',n,'is:',end='')
sum=0
while n>=1:
    sum+=n
    n-=1

print(sum)
