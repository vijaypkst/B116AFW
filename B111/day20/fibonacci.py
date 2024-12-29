#print Fibonacci sequence
n=int(input('How many numbers you want to print in Fibonacci sequence'))
if n>1:
    first=0
    second=1
    print(first,second,end=' ')
    for i in range(n-2):
       next=first+second
       print(next,end=' ')
       first=second
       second=next
else:
    print('invalid input minium should be >=2')
