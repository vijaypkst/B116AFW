def f1(a,b):
    print('f1 starts')
    if b==0:
        print('b cant be ZERO')
    else:
        print(a/b)
    print('f1 ends')


f1(10,0)
print('----------')
def f1(a,b):
    print('f1 starts')
    if b==0:
        raise ZeroDivisionError('Hi Bhanu, b cant be ZERO!!')
    else:
        print(a/b)
    print('f1 ends')

f1(10,0)