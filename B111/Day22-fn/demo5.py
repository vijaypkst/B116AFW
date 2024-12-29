#print only the prime numbers till 25

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


for j in range(1,26):
    if is_prime(j):
        print(j)