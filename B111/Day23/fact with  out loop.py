#find factorial of a number: if input is 3 then o/p 3*2*1--> 6

def factorial(n):
    if n<=1:
        return 1
    else:
        result=n*factorial(n-1)
        return result


print(factorial(4))