#write a function to print Fibonacci sequence

def generate_fibonacci(n):
    first = 0
    second = 1
    print(first, second, end=' ')
    for i in range(n-2):
        next=first+second
        print(next,end=' ')
        first=second
        second=next



generate_fibonacci(9)
