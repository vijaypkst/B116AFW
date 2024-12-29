print('Start')
a=input('Please enter a number')
b=input('Please enter a number')

try:
    a=int(a)
    b=int(b)        #ValueError: invalid literal for int() with base 10: 'five'
    res=a/b         #ZeroDivisionError: division by zero
    print(res)
except ValueError as e:
    print("'Sorry' is the solution") #recovery code1

except ZeroDivisionError as e:
    print("'Very Sorry' is the solution") #recovery code2

print('End')