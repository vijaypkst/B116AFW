a=10
b=5
try:
    c=a/b
    print(c)
except:
    print('Div by Zero')

print('Thank You-Normal Termination')
print('-'*10)
a=10
b=0
try:
    c=a/b
    print(c)
except:
    print('Div by Zero')

print('Thank You-Grceful Termination')
print('-'*10)

a=10
b=0
c=a/b
print(c)
print('Thank You-Abnormal  Termination')