#No exception- finally block got executed
print('Start')
x=10
try:
    a=int('10')
    print(a)
except:
    a=0
    print(x/a)
finally:
    print('End')
