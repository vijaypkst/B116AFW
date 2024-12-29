# exception in try and also in except - finally block got executed
print('Start')
x=10
try:
    a=int('ten') #risky code
    print(a)
except:
    a=0 #rcovery code
    print(x/a)
finally:
    print('End') #clean up code
