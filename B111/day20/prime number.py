#check if the given number is prime or not
#it is a natural number which is div exactly by two numbers
#  natural number 1 to infi
#prime number 2 3 5 7--> True
#not a prime: 4 6 8 9 10--.False
n=int(input('plz enter a number'))
flag=True
for i in range(2,n):
    if n%i==0:
        flag=False
        break


# if flag==True:
#     print(n,' is a prime number')
# else:
#     print(n,' is Not a prime number')

if flag:
    print(n,' is a prime number')
else:
    print(n,' is Not a prime number')

