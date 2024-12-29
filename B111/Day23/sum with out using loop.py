#sum of n numbers: if input is 3 then o/p 3+2+1--> 6

def add(n):
    if n<=0:
        return 0
    else:
        result=n+add(n-1)
        return result


print(add(6))