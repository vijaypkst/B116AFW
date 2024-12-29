def m1():
    return 'hi' #transfer the controll back to caller with data --> 'hi'

a=m1()

print(a)

def m2():
    print('this is m2')

m2()

def m3():
    print('this is m3')
    return   #empty return statement --> transfer the controll back to caller without any data

m3()