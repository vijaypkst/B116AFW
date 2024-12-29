#write a function to check if given number is prime number or not

def is_prime(n):
    msg=''
    if n==1:
        msg='it is not a prime number'
    else:
        msg = 'it is a prime number'
        for i in range(2,n):
            if n%i==0:
                msg = 'it is not a prime number'
                break

    print(n,msg)


for j in range(1,10):
    is_prime(j)



