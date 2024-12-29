# exception in try- finally block got executed
print('Start')
x=10
try:
    a=int('ten')
    print(a)
except:
    a=5
    print(x/a)
finally:
    print('End')
