print('Start')
a=input('Please enter a number')
b=input('Please enter a number')

try:

    a=int(a)
    b=int(b)

    try:
        res=a/b
        print(res)

    except ZeroDivisionError as e:
        print("'Very Sorry' is the solution")

except ValueError as e:
    print("'Sorry' is the solution")

print('End')