#factprial of a number 3--> 3 x 2 x 1   1x2x3
n=int(input('plz enter the number:'))
print('Factorial of ',n,'is:',end='')
factorial=1
while n>=1:
    factorial=factorial*n
    n-=1

print(factorial)