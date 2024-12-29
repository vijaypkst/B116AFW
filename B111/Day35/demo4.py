print('Start')
a=input('Please enter a number')
b=input('Please enter a number')

try:
    a=int(a)
    b=int(b)        #ValueError: invalid literal for int() with base 10: 'five'
    res=a/b         #ZeroDivisionError: division by zero
    print(res)
except Exception as e: #e is an objectof type Exception is a class
    print(e)

print('End')