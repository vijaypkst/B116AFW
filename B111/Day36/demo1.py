def f3(n):
    print('f3 starts')
    print(10/n)
    print('f3 ends')

def f2(n):
    print('f2 starts')
    f3(n)
    print('f2 ends')

def f1(n):
    print('f1 starts')
    f2(n)
    print('f1 ends')


f1(0)