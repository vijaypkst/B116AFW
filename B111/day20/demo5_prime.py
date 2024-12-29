n=int(input('plz enter a number'))
msg='is a prime number'
for i in range(2,n):
    if n%i==0:
        msg='is not a prime number'
        break

print(n,msg)
