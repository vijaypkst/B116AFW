def f1(a=0,b=1):
    print(a,b)


f1() #0 1
f1(10) #10 1
f1(None,20) #we cant skip 1st and send value to 2nd one
f1(10,20) #10 20
