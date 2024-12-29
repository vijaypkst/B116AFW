try:
    n=int(input('plz enter a number'))
    if n<=0:
        print('invalid input: it should be >0')
    elif n==1:
        print(n, 'is not a prime number')
    else:
        msg='is a prime number'
        for i in range(2,n):
            if n%i==0:
                msg='is not a prime number'
                break
        print(n, msg)
except:
    print('invalid input: it should be an integer number')