#Q:can we write if condition inside another if condition?
#A:yes --> it is called as nested condition
a=int(input('a?'))

if a>10:
    if a>20:
        print('hi1') #30
    else:
        print('bye1') #15
else:
    if a>5:
        print('hi2') #10
    else:
        print('bye2') #3