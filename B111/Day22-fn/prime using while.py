#print only the prime numbers till 10--> 2 3 5 7
#print 10 prime numbers:2 3 5 7 11 13 17 19 23 29

def is_prime(n):
    is_it_prime=False
    if n==1:
        is_it_prime=False
    else:
        is_it_prime=True
        for i in range(2,n):
            if n%i==0:
                is_it_prime = False
                break

    return is_it_prime

uc=int(input("enter the number"))
n=0
count=0
while count<uc:
    n=n+1
    if is_prime(n):
        count+=1
        print(count,'->', n)
